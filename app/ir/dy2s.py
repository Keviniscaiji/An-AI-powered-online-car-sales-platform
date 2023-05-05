import paddle
import argparse
from paddle.static import InputSpec

from models.ir_resnet_encoder import ResNet50Encoder
 
 
def main(args):
    if args.m == 'encoder':
        model = ResNet50Encoder(n_feat=args.n_feat)
    model.set_state_dict(paddle.load(args.ckpt_path))
    model.eval()
	
    x_spec = InputSpec(shape=[1, 3, args.size, args.size], dtype=args.dtype, name='x')
    model = paddle.jit.save(model, path=args.save_dir+"/"+args.tag, input_spec=[x_spec])
 

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('--m', type=str, default="encoder")
    parser.add_argument('--tag', type=str, default="encoder_d20_ckpt_300")
    parser.add_argument('--n_feat', type=int, default=128)
    parser.add_argument('--size', type=int, default=256)
    parser.add_argument('--dtype', type=str, default="float32")
    parser.add_argument(
        '--ckpt_path', type=str, default="./ckpts/encoder_d20_ckpt_300.pdparam")
    parser.add_argument(
        '--save_dir', type=str, default="./ckpts/static")

    args = parser.parse_args()
    main(args)


