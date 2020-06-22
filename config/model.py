import config.models.sayai as model

name = model.model_name

temperature = model.temperature

paths = {
    'weights_path': f"{name}_weights.hdf5",
    'vocab_path': f"{name}_vocab.json",
    'config_path': f"{name}_config.json",
}

model_cfg = model.model_cfg
train_cfg = model.train_cfg
