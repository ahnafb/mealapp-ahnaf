import os
from os.path import join, dirname
from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

MONGODB_URI = os.environ.get("MONGODB_URI")
DB_NAME = os.environ.get("DB_NAME")

client = MongoClient(MONGODB_URI)
db = client[DB_NAME]

app = Flask(__name__)

@app.route("/", methods=['GET'])
def home():
    return render_template("index.html")

@app.route("/category-detail", methods=['GET'])
def category_detail():
    category_name = request.args.get('category-name')
    
    return render_template("detail.html", category_name=category_name)

@app.route("/meal_detail", methods=['GET'])
def meal_detail():
    meal_id = request.args.get('meal-id')
    return render_template("meal_detail.html", meal_id=meal_id)

if __name__ == "__main__":
    app.run("0.0.0.0", port=5000, debug=True)