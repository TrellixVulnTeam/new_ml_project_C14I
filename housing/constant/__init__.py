
import os
from datetime import datetime

ROOT_DIR = os.getcwd()

config_path = "Config"
config_file = "config.yaml"

CONFIG_FILE_PATH = os.path.join(ROOT_DIR, config_path, config_file)

CURRENT_TIME_STAMP = f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"

# training pipeline variable

TRAINING_PIPELINE_CONFIG_KEY = 'training_pipeline_config'
TRAINING_PIPELINE_NAME = 'pipeline_name'
TRAINING_PIPELINE_ARTIFACT_DIR = 'artifact_dir'

# data ingestion variables

DATA_INGESTION_CONFIG = 'data_ingestion_config'
DATA_INGESTION_ARTIFACT_DIR = 'data_ingestion'
DATA_INGESTION_DATASET_DOWNLOAD_URL_KEY = 'dataset_download_url'
DATA_INGESTION_RAW_DATA_DIR_KEY = 'raw_data_dir'
DATA_INGESTION_TGZ_DOWNLOAD_DIR_KEY = 'tgz_download_dir'
DATA_INGESTION_INGESTED_DIR_KEY = 'ingested_dir'
DATA_INDESTION_INGESTED_TRAIN_DIR_KEY = 'ingested_train_dir'
DATA_INGESTION_INGESTED_TEST_DIR_KEY = 'ingested_test_dir'

# data validation variables

DATA_VALIDATION_CONFIG = 'data_validation_config'
DATA_VALIDATION_SCHEMA_FILE_NAME = 'schema_file_name'