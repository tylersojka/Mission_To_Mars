from flask import Flask, render_template
from flask_pymongo import PyMongo
import scraping

#set up flask
app = Flask(__name__)

#use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

@app.route("/")
def index():
   mars = mongo.db.mars.find_one()
   return render_template("index.html", mars=mars)

# function will set up our scraping route. This route will be the 
# "button" of the web application, the one that will scrape updated
# data when we tell it to from the homepage of our web app 
@app.route("/scrape")   # defines the route that Flask will be using.
def scrape():
   mars = mongo.db.mars  # assign a new variable that points to our Mongo database
   mars_data = scraping.scrape_all()   #In this line, we're referencing the scrape_all function in the scraping.py
   mars.update({}, mars_data, upsert=True) # update the database
   return render_template("return.html")

if __name__ == "__main__":
   app.run(debug=True)
