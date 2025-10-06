import os
import pandas 
from src.logger import get_logger
from src.custom_exception import CustomException
import yaml
import pandas as pd 

logger = get_logger(__name__)

def read_yaml(file_path):
    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File is not in the given path")
        
        with open(file_path,"r") as yaml_file:
            config = yaml.safe_load(yaml_file)
            logger.info("Succesfully read the YAML File")
            return config
        
    except Exception as e:
        logger.error("Error while reading YAML File")
        raise CustomException("Failed to read YAML File",e)
    

def load_data(path):
    try:
        logger.info("Loading Data")
        return pd.read_csv(path)
    except Exception as e:
        logger.error(f"Error Loading the data {e}")
        raise CustomException("Failed to load the data",e)
    

    