from datetime import datetime

from textgenrnn import textgenrnn

from configs import model_cfg
from configs import model_name
from configs import train_cfg
from configs import paths
from configs import temperature
import pytumblr

textgen = textgenrnn(
    name=model_name,
    config_path=paths['config_path'],
    vocab_path=paths['vocab_path'],
    weights_path=paths['weights_path'],
)

# temperature = [1.0, 0.5, 0.2, 0.2]
prefix = None  # if you want each generated text to start with a given seed text

if train_cfg['line_delimited']:
    n = 1000
    max_gen_length = 60 if model_cfg['word_level'] else 300
else:
    n = 1
    max_gen_length = 2000 if model_cfg['word_level'] else 10000

timestring = datetime.now().strftime('%Y%m%d_%H%M%S')
gen_file = 'items/{}_gentext_{}.txt'.format(model_name, timestring)

generated = textgen.generate(
    n=n,
    temperature=temperature,
    max_gen_length=max_gen_length,
    prefix=prefix,
    return_as_list=True
)

output = "\n".join(generated)

print(output)

# with open(gen_file, "w") as text_file:
#     text_file.write(output)

client = pytumblr.TumblrRestClient(
  '',
  '',
  '',
  ''
)

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
        "dev tests",
    ]
)
