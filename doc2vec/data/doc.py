import logging
import os
import re

import nltk
from nltk.tokenize import word_tokenize


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


def _read(path):
    with open(path, 'r') as f:
        return f.read()


def _doc_id(path):
    doc_id, = re.search(r'(\d+)', path).groups()
    return doc_id


def _full_paths(directory):
    return [os.path.join(directory, path) for path in os.listdir(directory)]


def docs_by_id(directory):
    logger.info('Loading documents from {}'.format(directory))
    return {_doc_id(path): _read(path) for path in _full_paths(directory)}


def tokens(doc):
    return word_tokenize(doc)


def tokens_by_doc_id(directory):
    nltk.download('punkt')
    return {doc_id: tokens(doc) for doc_id, doc in docs_by_id(directory).items()}
