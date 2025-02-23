from flask import Flask, jsonify
import os
from dotenv import load_dotenv

load_dotenv()

APP_PORT = os.getenv('APP_PORT')

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
    return "Selamat datang di Toko Sihir Ajaib! Pesan ramuan di /order/<nama_ramuan>"


@app.route('/order/<potion>')
def order_potion(potion):
    if potion in potions:
        return jsonify({"message": f"Ramuan '{potions[potion]}' telah disiapkan!"})
    else:
        return jsonify({"error": "Ramuan tidak tersedia"}), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000 if APP_PORT is None else APP_PORT)
