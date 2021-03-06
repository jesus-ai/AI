import os

import config.models.masterpiece as model

name = model.model_name

dataset = model.dataset

temperature = model.temperature

ai_dir = os.getcwd()

paths = {
    # 'weights_path': f"{ai_dir}/model_files/{name}_weights.hdf5",
    'weights_path': os.path.join(ai_dir, 'model_files', f"{name}_weights.hdf5"),
    # 'vocab_path': f"{ai_dir}/model_files/{name}_vocab.json",
    'vocab_path': os.path.join(ai_dir, 'model_files', f"{name}_vocab.json"),
    # 'config_path': f"{ai_dir}/model_files/{name}_config.json",
    'config_path': os.path.join(ai_dir, 'model_files', f"{name}_config.json"),
}

model_cfg = model.model_cfg
train_cfg = model.train_cfg
