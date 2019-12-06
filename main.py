import hashlib
import os.path

from tensorflow.keras import utils as keras_utils

from train import Train as Ai

# directory = 'data.txt'
directory = keras_utils.get_file(
    fname='data.txt',
    origin='https://jesus-ai.github.io/scraper/output.txt'
)

ai = Ai()

ai.train(
    file_name=directory
)
