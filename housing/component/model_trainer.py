from housing.exception import HousingException
from housing.logger import logging
from housing.entity.artifact_entity import DataTransformationArtifact, ModelTrainerArtifact
from housing.constant import *
import os, sys
from housing.entity.model_factory import ModelFactory
from housing.util.util import load_numpy_array_data
from housing.entity.config_entity import ModelTrainerConfig







class ModelTrainer:

    def __init__(self, data_transformation_artifact:DataTransformationArtifact,
                model_trainer_config:ModelTrainerConfig) -> None:
        try:
            self.data_transformation_artifact = data_transformation_artifact
            self.model_trainer_config = model_trainer_config
        except Exception as e:
            raise HousingException(e, sys) from e
    





    def initiate_model_trainer(self)-> ModelTrainerArtifact:
        try:
            transformed_train_file_path = self.data_transformation_artifact.transformed_train_file_path
            train_array = load_numpy_array_data(file_path=transformed_train_file_path)

            transformed_test_file_path = self.data_transformation_artifact.transformed_test_file_path
            test_array = load_numpy_array_data(file_path=transformed_test_file_path)

            x_train, y_train, x_test, y_test = train_array[:,:-1], train_array[:,-1], test_array[:,:-1], test_array[:,-1]

            model_config_file_path = self.model_trainer_config.model_config_file_path

            model_factory = ModelFactory(model_config_path=model_config_file_path)

            base_accuracy = self.model_trainer_config.base_accuracy

            best_model = model_factory.get_best_model(X=x_train, y=y_train, base_accuracy=base_accuracy)

        except Exception as e:
            raise HousingException(e, sys) from e