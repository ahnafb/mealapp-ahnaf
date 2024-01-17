from flask import Flask, render_template, jsonify, request, redirect, url_for

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