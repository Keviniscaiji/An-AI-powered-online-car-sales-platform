# MetaPluser

## 1. Introduction

Video Introduction: https://www.dropbox.com/scl/fi/cwmpzyuclz1jubf2xmsi6/Group-Project.mp4?rlkey=z1xco65xqi65dxhbr06s5hh9j&dl=0

An online car booking website with python and flask

## 2. Development Usage

### 2.1 Basic Usage

```
# run server
bash run.sh
```

### 2.2 Database Tools

We provide `predifined data` under app/dev/_dev_data.py for development and testing
```
# Clear database
$ python dev_tools.py -reset

# Create and insert data
$ python dev_tools.py -reset -insert -a

# ...
...
```

### 2.3 MultiLanguage Support
We provide English and Chinese support for our website by using `python_bible` replacing all the English terms.

To build a new language support:
```
# 0. Add new language abbreviation (e.g. 'zh') in Config.py
# 1. Extract terms from specified .py and html files into messages.pot
$ pybabel extract -F babel.cfg -k _l -o messages.pot --input-dirs=.

# 2. Initiate language dictionary
$ pybabel init -i messages.pot -d app/translations -l <language-abbrivation>

# 3. Add translations in new created 'app/translations/<language-abbrivation>/LC_MESSAGE/messages.po'

# 4. compile message.po
$ pybabel compile -d app/translations
```

To update existed translation
```
# 1. Extract terms from specified .py and html files into messages.pot
$ pybabel extract -F babel.cfg -k _l -o messages.pot --input-dirs=.

# 2. Update dictionary
$ pybabel update -i messages.pot -d app/translations

# 3. Change dictionary in 'app/translations/<language-abbrivation>/LC_MESSAGE/messages.po'

# 4. compile message.po
$ pybabel compile -d app/translations
```

