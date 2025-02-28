from flask import Flask, jsonify
import os
import time
from dotenv import load_dotenv
import psycopg2
from psycopg2.extras import RealDictCursor

load_dotenv()

APP_PORT = 5000 if os.getenv('APP_PORT') is None else os.getenv('APP_PORT')
APP_NAME = 'Toko Sihir Ajaib' if os.getenv(
    'APP_NAME') is None else os.getenv('APP_NAME')


class DBPostgre:
    PG_HOST = None if os.getenv(
        'POSTGRES_HOST') is None else os.getenv('POSTGRES_HOST')
    PG_PORT = None if os.getenv(
        'POSTGRES_PORT') is None else os.getenv('POSTGRES_PORT')
    PG_DATABASE = None if os.getenv(
        'POSTGRES_DATABASE') is None else os.getenv('POSTGRES_DATABASE')
    PG_USERNAME = None if os.getenv(
        'POSTGRES_USERNAME') is None else os.getenv('POSTGRES_USERNAME')
    PG_PASSWORD = None if os.getenv(
        'POSTGRES_PASSWORD') is None else os.getenv('POSTGRES_PASSWORD')


app = Flask(__name__)

conn = None if DBPostgre.PG_HOST is None else psycopg2.connect(
    database=DBPostgre.PG_DATABASE,
    host=DBPostgre.PG_HOST,
    user=DBPostgre.PG_USERNAME,
    password=DBPostgre.PG_PASSWORD,
    port=DBPostgre.PG_PORT
)

# Daftar ramuan yang tersedia
potions = {
    "healing": "Potion of Healing",
    "mana": "Mana Elixir",
    "strength": "Elixir of Strength",
    "invisibility": "Cloak of Invisibility Potion"
}


@app.route('/')
def welcome():
    return f"Selamat datang di {APP_NAME}! Pesan ramuan di /order/<nama_ramuan>"


@app.route('/order/<potion>')
def order_potion(potion):
    if potion in potions:
        return jsonify({"message": f"Ramuan '{potions[potion]}' telah disiapkan!"})
    else:
        return jsonify({"error": "Ramuan tidak tersedia"}), 404


@app.route('/gudang')
def gudang_barang():
    if conn is None:
        return jsonify({"message": f"Ubur ubur ikan lele, gudangnya belum ada le...", "data": None})
    else:
        try:
            cur = conn.cursor(cursor_factory=RealDictCursor)
            cur.execute("select * from potions")
            return jsonify({"message": "gudang barang", "data": cur.fetchall()})
        except:
            return jsonify({"message": f"terjadi gangguan pada gudang", "data": None}), 500
        finally:
            cur.close()


if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', port=APP_PORT)
    finally:
        print("shuting down app...")
        if conn is not None:
            print("shuting down db...")
            conn.close()
            if conn.closed == 1:
                print("\tdb connection successfully closed")
            time.sleep(5)
        print("exiting")
