import hashlib
import os.path

from tensorflow.keras import utils as keras_utils

from train import Train as Ai


def md5(fname):
    if not os.path.isfile(fname):
        return hashlib.md5(b'No file found.').hexdigest()

    with open(fname, "rb") as f:
        return hashlib.md5(f.read()).hexdigest()


# directory = 'data.txt'
directory = keras_utils.get_file(
    fname='data.txt',
    origin='https://jesus-ai.github.io/scraper/output.txt',
    # keep a hash of the file so it downloads the new one when changed
    md5_hash=md5('data.txt')
)

ai = Ai()

ai.train(
    file_name=directory
)
