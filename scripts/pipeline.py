from dotenv import load_dotenv  
from extract import fetch_products
from load import load_to_staging

load_dotenv()

def run_pipeline():
    print("Iniciando Pipeline ELT")
    try:
        data = fetch_products()
        load = load_to_staging(data)
        print("Pipeline finalizado con éxito")
    except Exception as e:
        print(f'El pipeline falló: {e}')

if __name__ == "__main__":
    run_pipeline()
