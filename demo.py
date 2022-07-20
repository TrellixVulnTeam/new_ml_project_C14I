from housing.config.configuration import Configuration
from housing.pipeline.pipeline import Pipeline
from housing.exception import HousingException
from housing.logger import logging
import os,sys


def main():
    try:
        config_path = os.path.join("Config", "config.yaml")
        pipeline = Pipeline(Configuration(config_file_path=config_path))

        pipeline.start()
        logging.info("main function execution completed.")
        
        
    except Exception as e:
        logging.error(f"{e}")
        print(e)


if __name__=="__main__":
    main()