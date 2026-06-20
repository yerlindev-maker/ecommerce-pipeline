import psycopg2
from psycopg2.extras import execute_values
import json
import os
import logging

logger = logging.getLogger(__name__)

def load_to_staging(products):
    conn = None
    try:
        conn = psycopg2.connect(
            host=os.getenv('DB_HOST'),
            database=os.getenv('DB_NAME'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            port=os.getenv('DB_PORT')
        )
        cur = conn.cursor()

        logger.info("Limpiando tabla staging.products") 
        cur.execute("TRUNCATE TABLE staging.products")

        # Template for psycopg2 extras execute_values must end with VALUES %s
        insert_query = """
            INSERT INTO staging.products(id, title, price, description, category, image, rating)
            VALUES %s
        """

        logger.info(f"Insertando masivamente {len(products)} productos a staging.products")
        
        # Prepare list of tuples
        args_list = [
            (
                p['id'], 
                p['title'], 
                p['price'], 
                p['description'], 
                p['category'], 
                p['image'], 
                json.dumps(p['rating'])
            )
            for p in products
        ]
        
        # Perform bulk insert
        execute_values(cur, insert_query, args_list)
        conn.commit()
        logger.info('Carga masiva exitosa en staging')

    except Exception as e:
        if conn:
            conn.rollback()
        logger.error(f'Error en la carga: {e}')
        raise
    finally:
        if conn:
            cur.close()
            conn.close()
