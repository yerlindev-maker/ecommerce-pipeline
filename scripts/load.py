import psycopg2
import json
import os

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

        print("Limpiando tabla staging.products") 
        cur.execute("TRUNCATE TABLE staging.products")

        insert_query = """
            INSERT INTO staging.products(id, title, price, description, category, image, rating)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """

        print(f"Insertando datos {len(products)} productos")
        for p in products:
            cur.execute(insert_query, (
                p['id'], p['title'], p['price'], p['description'], 
                p['category'], p['image'], json.dumps(p['rating'])
            ))
        conn.commit()
        print('Carga exitosa en staging')

    except Exception as e:
        if conn:
            conn.rollback()
        print(f'Error en la carga: {e}')
        raise
    finally:
        if conn:
            cur.close()
            conn.close()
