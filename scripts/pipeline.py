import logging
from dotenv import load_dotenv  
from extract import fetch_products
from load import load_to_staging

# Configure logging format
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Load env variables from .env file (for local execution)
load_dotenv()

def run_pipeline():
    logger.info("Iniciando Pipeline ELT")
    try:
        data = fetch_products()
        load_to_staging(data)
        logger.info("Pipeline finalizado con éxito")
    except Exception as e:
        logger.critical(f'El pipeline falló: {e}')

if __name__ == "__main__":
    run_pipeline()
