import logging
import logging.config
import yaml
import os

def setup_logging(config_path="config/logging_config.yaml"):
    if os.path.exists(config_path):
        with open(config_path, "r") as f:
            config = yaml.safe_load(f)
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=logging.INFO)
        logging.warning("Archivo logging_config.yaml no encontrado. Usando configuración básica.")

# Activar logger al importar
setup_logging()
logger = logging.getLogger(__name__)
