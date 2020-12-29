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
  
  #These two lines (24,25) entered to see if it will update Mongo
  # scrapeobj=scrape_mars.scrape()
  # db.mars.update({},scrapeobj,upsert=True)
 
  finding_mars=db.mars.find_one()
  print (finding_mars)
  return render_template('index.html', finding_mars=finding_mars)
  #this section of code populates the "Mars Now" right after "My Website" (line 17 of index.html)
  #the rest of the mongo collection/json will have to be added in similarly. 
  #<h1>My Website {{ finding_mars.news_title }}</h1> This is the line that needs to be emulated (17 in index.html)
# def index():
#   finding_mars_2=db.mars.find_two() 
#   return render_template('index.html', finding_mars_2=finding_mars_2)
# def index():
#   finding_mars_3=db.mars.find_three() 
#   return render_template('index.html', finding_mars_3=finding_mars_3)

# @app.route('/scrape')
# def scrape():
#   scrapeobj=scrape_mars.scrape()
#   db.mars.update({},scrapeobj,upsert=True)
#   finding_mars=db.mars.find_one()
#   return render_template('scrape.html', finding_mars=finding_mars)


if __name__ == '__main__':
  app.run(debug=True)



