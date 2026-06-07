import os
import sys
import yaml

from dotenv import load_dotenv
from logger import logger

load_dotenv()

def load_config():
    try:
        with open('config.yml', 'r') as f:
            config = yaml.safe_load(f)
                
            return config

    except FileNotFoundError:
        logger.critical("config.yml was not found or is missing from root directory.")
        sys.exit(1)
        
    except yaml.YAMLError as e:
        logger.critical(f"Failed to parse config.yml, please check your syntax \nError: {e}")
        sys.exit(1)

def get_required_env(name: str):
    variable = os.getenv(name)
    
    if not variable:
        logger.critical(f"{name} is not set in the environment variables.")
        sys.exit(1)
    
    return variable

def get_optional_env(name: str):
    variable = os.getenv(name)
    
    if not variable:
        logger.warning(f"{name} is not set in the environment variables, some functionality may not worked as expected.")
    
    return variable
        
class Environment:
    def __init__(self):
        self.config = load_config()
        
        self.token = get_required_env("DISCORD_TOKEN")
        self.kat_api_url = get_optional_env("KAT_API_URL")

environment = Environment()