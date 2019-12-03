import schedule
import time

from textgenrnn import textgenrnn

from configs import model_cfg
from configs import model_name
from configs import train_cfg
from configs import paths
from configs import temperature
import pytumblr

client = pytumblr.TumblrRestClient(
    '',
    '',
    '',
    ''
)

textgen = textgenrnn(
    name=model_name,
    config_path=paths['config_path'],
    vocab_path=paths['vocab_path'],
    weights_path=paths['weights_path'],
)

# temperature = [1.0, 0.5, 0.2, 0.8]
prefix = None  # if you want each generated text to start with a given seed text

if train_cfg['line_delimited']:
    n = 1000
    max_gen_length = 60 if model_cfg['word_level'] else 300
else:
    n = 1
    max_gen_length = 2000 if model_cfg['word_level'] else 10000


def create_post():
    print("Generating\n")

    generated = textgen.generate(
        n=n,
        temperature=temperature,
        max_gen_length=max_gen_length,
        prefix=prefix,
        return_as_list=True
    )

    output = "\n".join(generated)

    print(output + "\n")

    print("Posing\n")

    client.create_text(
        "lexobotus",
        state="published",
        # slug="testing-text-posts",
        # title="Testing",
        body=output,
        tags=[
            "lexobotus",
            "phandom",
            "lexxpocalypse",
        ]
    )

    print("Posted\n")


schedule.every().hour.do(create_post)

create_post()

while True:
    schedule.run_pending()
    time.sleep(1)
