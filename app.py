from flask import Flask, jsonify
import os
from dotenv import load_dotenv

load_dotenv()

APP_PORT = 5000 if os.getenv('APP_PORT') is None else os.getenv('APP_PORT')
APP_NAME = 'Toko Sihir Ajaib' if os.getenv(
    'APP_NAME') is None else os.getenv('APP_NAME')

app = Flask(__name__)

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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=APP_PORT)
