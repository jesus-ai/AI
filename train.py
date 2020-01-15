from datetime import datetime

from textgenrnn import textgenrnn

from configs import model_cfg
from configs import model_name
from configs import train_cfg
from configs import paths
from configs import temperature


class Train:

    def train(self, file_name):
        textgen = textgenrnn(
            name=model_name,
            config_path=paths['config_path'],
            vocab_path=paths['vocab_path'],
            weights_path=paths['weights_path'],
        )

        train_function = textgen.train_from_file if train_cfg['line_delimited'] else textgen.train_from_largetext_file

        train_function(
            file_path=file_name,
            new_model=model_cfg['create_new'],
            num_epochs=train_cfg['num_epochs'],
            gen_epochs=train_cfg['gen_epochs'],
            batch_size=train_cfg['batch_size'],
            train_size=train_cfg['train_size'],
            dropout=train_cfg['dropout'],
            validation=train_cfg['validation'],
            is_csv=train_cfg['is_csv'],
            rnn_layers=model_cfg['rnn_layers'],
            rnn_size=model_cfg['rnn_size'],
            rnn_bidirectional=model_cfg['rnn_bidirectional'],
            max_length=model_cfg['max_length'],
            dim_embeddings=100,
            word_level=model_cfg['word_level'])

        prefix = None  # if you want each generated text to start with a given seed text

        if train_cfg['line_delimited']:
            n = 20
            max_gen_length = 60 if model_cfg['word_level'] else 300
        else:
            n = 1
            max_gen_length = 2000 if model_cfg['word_level'] else 10000

        timestring = datetime.now().strftime('%Y%m%d_%H%M%S')
        gen_file = 'items/{}_gentext_{}.txt'.format(model_name, timestring)

        textgen.generate_to_file(gen_file,
                                 temperature=temperature,
                                 prefix=prefix,
                                 n=n,
                                 max_gen_length=max_gen_length)
