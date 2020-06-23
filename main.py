import urllib.request
import random
import math

from tensorflow.keras import utils as keras_utils

from train import Train as Ai
from config.model import dataset as url

query = '?r={}'.format(math.floor(random.random() * 10000))


def get_output_hash():
    response = urllib.request.urlopen('{}.md5{}'.format(url, query))
    return response.read().decode('utf-8')


# directory = 'data.txt'
directory = keras_utils.get_file(
    fname='data.txt',
    origin=url + query,
    md5_hash=get_output_hash()
)

print('data.txt location: {}'.format(directory))

ai = Ai()

ai.train(
    file_name=directory
)
