import urllib.request

from tensorflow.keras import utils as keras_utils

from train import Train as Ai


def get_output_hash():
    response = urllib.request.urlopen('https://jesus-ai.github.io/scraper/output.txt.md5')
    return response.read().decode('utf-8')


# directory = 'data.txt'
directory = keras_utils.get_file(
    fname='data.txt',
    origin='https://jesus-ai.github.io/scraper/output.txt',
    md5_hash=get_output_hash()
)

print('data.txt location: {}'.format(directory))

ai = Ai()

ai.train(
    file_name=directory
)
