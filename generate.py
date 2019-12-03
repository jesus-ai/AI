import itertools
import os
from time import sleep

from textgenrnn import textgenrnn

from configs import model_cfg
from configs import model_name
from configs import paths
from configs import temperature
from configs import train_cfg

# items is loop_times * 1000
loop_times = 100

print("Generating {} items for the database".format(loop_times * 1000))
# exit(0)

textgen = textgenrnn(
    name=model_name,
    config_path=paths['config_path'],
    vocab_path=paths['vocab_path'],
    weights_path=paths['weights_path'],
)

prefix = None  # if you want each generated text to start with a given seed text

if train_cfg['line_delimited']:
    n = 1000
    max_gen_length = 60 if model_cfg['word_level'] else 300
else:
    n = 1
    max_gen_length = 2000 if model_cfg['word_level'] else 10000


def generate_from_model():
    return textgen.generate(
        n=n,
        temperature=temperature,
        max_gen_length=max_gen_length,
        prefix=prefix,
        return_as_list=True
    )


def write_to_database(saying):
    print(saying)
    os.system("php insert_db.php {}".format(saying))
    return None


# Loop a few times so we have a lot of data
# every generation is 1000 items
for _ in itertools.repeat(None, loop_times):
    generated = generate_from_model()

    for say in generated:
        write_to_database(saying=say)
        # sleep for 0.5 seconds to not spam the database
        sleep(0.5)
