from flask import Flask, render_template
import json
import scrape_mars

# Import our pymongo library, which lets us connect our Flask app to our Mongo database.
import pymongo

# Create an instance of our Flask app.
app = Flask(__name__)

# Create connection variable
conn = 'mongodb://localhost:27017'

# Pass connection to the pymongo instance.
client = pymongo.MongoClient(conn)

# Connect to a database. Will create one if not already available.
db = client.web_scraping_challenge


@app.route('/')
def index():
  
  scrapeobj=scrape_mars.scrape()
  db.mars.update({},scrapeobj,upsert=True)
 
  finding_mars=db.mars.find_one()
  print (finding_mars)
  return render_template('index.html', finding_mars=finding_mars)
 


@app.route('/scrape')
def scrape():
  scrapeobj=scrape_mars.scrape()
  db.mars.update({},scrapeobj,upsert=True)
  finding_mars=db.mars.find_one()
  return render_template('scrape.html', finding_mars=finding_mars)


if __name__ == '__main__':
  app.run(debug=True)



