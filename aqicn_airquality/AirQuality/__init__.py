# -*- coding: utf-8 -*-
import os
import sys

# root_path = /path/to/scrapyPrj
root_path = os.path.dirname(
    os.path.dirname(
        os.path.dirname(__file__)
    )
)
sys.path.append(root_path)

# GLOBAL VARIABLES
from utils.configreader import configreader

# "/root/scrapyPrj/configs/.env"
CONFIG = configreader(os.path.join(root_path, 'configs', '.env'))
MONGO_URI = CONFIG['TV_NEWS']['MongoUri']
MONGO_DB = CONFIG['TV_NEWS']['MongoCollection']