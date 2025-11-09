import kaggle
import os

kaggle.api.authenticate()

kaggle.api.dataset_download_files(
    'tomigelo/spotify-audio-features',
    path='.', 
    unzip=True
)

