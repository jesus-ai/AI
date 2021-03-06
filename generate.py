import itertools

from textgenrnn import textgenrnn

from config.model import name as model_name, model_cfg, train_cfg, paths, temperature
from sql import insert_sayings

# items is loop_times * line_split_count
loop_times = 1
# line_split_count = 1
# line_split_count = 1000
# line_split_count = 500
# line_split_count = 5
line_split_count = 20

print("Generating {} items for the database".format(loop_times * line_split_count))
# exit(0)

textgen = textgenrnn(
    name=model_name,
    config_path=paths['config_path'],
    vocab_path=paths['vocab_path'],
    weights_path=paths['weights_path'],
)

if train_cfg['line_delimited']:
    n = line_split_count
    max_gen_length = 60 if model_cfg['word_level'] else 300
else:
    n = 1
    max_gen_length = 2000 if model_cfg['word_level'] else 10000


def generate_from_model():
    return textgen.generate(
        n=n,
        temperature=temperature,
        max_gen_length=max_gen_length,
        prefix=None,
        return_as_list=True
    )


# Loop a few times so we have a lot of data
# every generation is 1000 items
for _ in itertools.repeat(None, loop_times):
    generated = generate_from_model()

    # insert_sayings(generated)
    insert_sayings(generated, 'sayings_bible')

    for saying in generated:
        print()
        print(saying)
        print()
        # sleep for 0.5 seconds to not spam the database
        # sleep(0.5)
