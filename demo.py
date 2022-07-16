from housing.config.configuration import Configuration
from housing.pipeline.pipeline import Pipeline
from housing.exception import HousingException
from housing.logger import logging


def main():
    try:
        #pipeline = Pipeline()
        #pipeline.run_pipeline()
        Configuration().get_model_trainer_config()
        
    except Exception as e:
        logging.error(f"{e}")
        print(e)


if __name__=="__main__":
    main()