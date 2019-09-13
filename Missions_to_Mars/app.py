from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import mission_to_mars_output

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/NASA_db"
mongo = PyMongo(app)

@app.route("/")
def index():
    mars_output = mongo.db.mars_output.find_one()
    return render_template('index.html', mars_output = mars_output,table = mars_output['mars_facts'])

@app.route("/scrape")
def scrape():
    mars_output = mongo.db.mars_output
    mars_data = mission_to_mars_output.scrape_info()
    mars_output.update({}, mars_data, upsert=True)
    return redirect("/", code = 302)

if __name__ == "__main__":
    app.run(debug=True)
