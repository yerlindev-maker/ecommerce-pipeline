import requests
from requests.adapters import HTTPAdapter
from urllib3.util import Retry
import logging

logger = logging.getLogger(__name__)

def fetch_products():
    URL = "https://fakestoreapi.com/products"
    
    # Configure retry strategy for transient errors (rate limit, gateway timeout, etc.)
    retry_strategy = Retry(
        total=3,
        backoff_factor=1,
        status_forcelist=[429, 500, 502, 503, 504],
        allowed_methods=["GET"]
    )
    adapter = HTTPAdapter(max_retries=retry_strategy)
    
    session = requests.Session()
    session.mount("https://", adapter)
    session.mount("http://", adapter)
    
    logger.info("Iniciando extracción de datos desde FakeStoreAPI")
    try:
        # Added 10 seconds timeout to prevent indefinite hangs
        response = session.get(URL, timeout=10)
        response.raise_for_status()
        products = response.json()
        logger.info(f"Extracción exitosa: {len(products)} productos obtenidos")
        return products
    except requests.exceptions.RequestException as e:
        logger.error(f"Error durante la extracción de datos: {e}")
        raise

