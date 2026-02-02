import kaggle

kaggle.api.authenticate()

kaggle.api.dataset_download_files('mysarahmadbhat/airbnb-listings-reviews',path='./dataset', unzip=True)