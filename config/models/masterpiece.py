model_name = 'masterpiece'

dataset = 'https://jesus-ai.github.io/scraper/output2.txt'

# more info on all of this:
# https://minimaxir.com/2018/05/text-neural-networks/

# this temperature schedule cycles between 1 very unexpected token, 1 unexpected token, 2 expected tokens, repeat.
# changing the temperature schedule can result in wildly different output!
temperature = [1.0, 0.8, 0.5, 0.2]

model_cfg = {
    'create_new': False,  # set to True if you want to make a new model
    'word_level': True,  # set to True if want to train a word-level model (requires more data and smaller max_length)
    'rnn_size': 128,  # number of LSTM cells of each layer (128/256 recommended)
    'rnn_layers': 8,  # number of LSTM layers (>=2 recommended)
    'rnn_bidirectional': False,  # consider text both forwards and backward, can give a training boost
    'max_length': 5,
    # number of tokens to consider before predicting the next (20-40 for characters, 5-10 for words recommended)
    'max_words': 10000,  # maximum number of words to model; the rest will be ignored (word-level model only)
}

train_cfg = {
    'line_delimited': True,  # set to True if each text has its own line in the source file
    'num_epochs': 10,  # set higher to train the model for longer (was 20)
    'gen_epochs': 5,  # generates sample text from model after given number of epochs
    'train_size': 0.8,  # proportion of input data to train on: setting < 1.0 limits model from learning perfectly
    'dropout': 0.6,  # ignore a random proportion of source tokens each epoch, allowing model to generalize better
    'validation': False,  # If train__size < 1.0, test on holdout dataset; will make overall training slower
    'is_csv': False,  # set to True if file is a CSV exported from Excel/BigQuery/pandas
    'batch_size': 2048,  # 128, 1024, 2048 (bigger size is slower training but more at the same time)
}
