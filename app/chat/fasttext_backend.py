import numpy as np
from torchtext.transforms import VocabTransform  # torchtext should be 0.12+
import os
import torch
from torch import nn
from torch.nn import functional as F
from torchtext.data.utils import ngrams_iterator
import re


remove_chars = '[·’!"\#$%&\'()＃！（）*+,-./:;<=>?\@，：?￥★、…．＞【】［］《》？“”‘’\[\\]^_`{|}~]+'


def pad_or_cut(value: np.ndarray, target_length: int):
    """pad or cut text to constant length"""
    data_row = None
    if len(value) < target_length:  # padding
        data_row = np.pad(value, [(0, target_length - len(value))])
    elif len(value) > target_length:  # cut
        data_row = value[:target_length]
    return data_row


class FastText(nn.Module):
    def __init__(self, vocab_size, embedding_dim=100, output_dim=2):
        """
        FastText

        :param vocab_size: size of vocab
        :param embedding_dim: dimension of vector
        :param output_dim: number of classes
        """
        super().__init__()
        self.embedding = nn.Embedding(vocab_size, embedding_dim)
        self.linear = nn.Linear(embedding_dim, output_dim)

    def forward(self, text_token):
        embedded = self.embedding(text_token)  # shape:[batch_size, word-length, embedding_dim]
        pooled = F.avg_pool2d(embedded, (embedded.shape[1], 1)).squeeze(1)  # [batch size, embedding_dim]
        out_put = self.linear(pooled)
        return out_put

    def get_embedding(self, token_list: list):
        return self.embedding(torch.Tensor(token_list).long())


def remove_punc(string: str):
    return re.sub(remove_chars, " ", string)


def get_classes(path):
    lines = open(path, 'r').readlines()
    return [line.strip("\n") for line in lines]


def prepare_models():
    cfgs = {
        'brands': {
            'n_classes': 25,
            'model-ckpt': 'app/chat/ckpts/fasttext-model-cars_brands.pth',
            'vocab-ckpt': 'app/chat/ckpts/fasttext-vocab-cars_brands.pth',
            'classes-path': 'app/chat/data/brands/classes.txt'
        },
        'products': {
            'n_classes': 172,
            'model-ckpt': 'app/chat/ckpts/fasttext-model-cars_products.pth',
            'vocab-ckpt': 'app/chat/ckpts/fasttext-vocab-cars_products.pth',
            'classes-path': 'app/chat/data/products/classes.txt'
        },
        'intents': {
            'n_classes': 4,
            'model-ckpt': 'app/chat/ckpts/fasttext-model-cars_intents.pth',
            'vocab-ckpt': 'app/chat/ckpts/fasttext-vocab-cars_intents.pth',
            'classes-path': 'app/chat/data/intents/classes.txt'
        }
    }
    
    models = dict()

    for key, val in cfgs.items():
        state_dict = torch.load(val['model-ckpt'], map_location=torch.device('cpu'))
        vocab = torch.load(val['vocab-ckpt'], map_location=torch.device('cpu'))
        classes = get_classes(val['classes-path'])

        model = FastText(len(vocab), output_dim=val['n_classes'])
        model.load_state_dict(state_dict)
        model.eval()

        vocab_transform = VocabTransform(vocab)

        models[key] = {
            'model': model,
            'vocab-transform': vocab_transform,
            'classes':classes
        }

    return models


def predict_text(text, model, vocab_transform, classes, max_length=50):
    all_sentence_words = list(ngrams_iterator(remove_punc(text).split(' '), 2))
    sentence_id_list = pad_or_cut(
        np.array(vocab_transform(all_sentence_words)), 
        target_length=max_length)
    text_tensor = torch.Tensor(sentence_id_list).long()
    model_out = model(text_tensor.unsqueeze(0))
    pred_id = int(torch.argmax(F.softmax(model_out, dim=1), dim=1).numpy())
    return classes[pred_id]

def predict_text_all(text, models, max_length):
    preds = dict()
    for key, val in models.items():
        preds[key] = predict_text(
            text, 
            val['model'], val['vocab-transform'], val['classes'], 
            max_length)
    return preds


