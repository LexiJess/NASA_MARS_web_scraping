# Dependencies
from bs4 import BeautifulSoup as bs
import requests
from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

#Finding the full-image for the astrogeology site
url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url)

soup=bs(browser.html, 'html.parser')

title=soup.find_all(name='div', class_="description")
title[0].find("h3")
find_h3=title[0].find("h3")

title_stripped=find_h3.text.strip("<h3>")
title_stripped
find_h3

title_names = []
urls=[]

#this looks at each item in "title", which scrapes the div/description from the url
for i in range (len(title)):
    
    #this makes a variable that pins the front of the basic url to the returned portion of the a/href coming back from each iteration through the title
    newstr='https://astrogeology.usgs.gov'+title[i].find('a').get('href')
    
    #this tells splinter to navigate to the url returned above ^
    browser.visit(newstr)
    
    #this creates a soup object from the new splinter/browser from above
    soup=bs(browser.html, 'html.parser')
    
    #this uses the soup object to scrape the url from the img/class on the page that splinter just navigated to
    found_url=soup.find(name='img', class_="wide-image").get('src')
    
    #this redefines found_url as the the front part of the main page PLUS the returned scraping from above
    found_url='https://astrogeology.usgs.gov'+found_url
    
    #this adds the above to the list of urls.
    urls.append(found_url)
    
    #this find the h3 item (title) for each iteration through the page, sets it as a viariable, and captures it in the list
    title[i].find("h3")
    find_h3=title[i].find("h3")
    title_names.append(find_h3.text.strip("<h3>"))
    
    #add to dict
    
print (title_names)
print(urls)

hemisphere_image_urls = []


for name, url in zip(title_names, urls):
    savannah={"title": name, "img_url": url}
    hemisphere_image_urls.append(savannah)
    
print (hemisphere_image_urls)


#Mars_facts

#Finding planet facts
url2 = 'https://space-facts.com/mars/'
browser.visit(url2)

#making a soup object
soup2 = bs(browser.html, 'html.parser')
type(soup2)

tables = pd.read_html(url2)
tables

#this has to use [0] becuase it's a list and we need to step inside the [] in order to get to the values
df = tables[0]
df.head(9)

#turn the dataframe into an html
html_table = df.to_html()
html_table

#Finding the full-image for the astrogeology site
url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url)

#set the variable for the links to follow for each image
image_nav=browser.find_by_id("h3")
type(image_nav)

#following the link to the image
click_image=browser.find_by_tag("h3").first.click()

#Use bs to parse the code (why am I doing this? what, exactly, does it do?)
soup=bs(browser.html, 'html.parser')
#print(soup.prettify())

#finding the code that indicates the download-the-pic link
pic_url=soup.find(name='div', class_="downloads")

#Setting the featured image for the image url
featured_image_url=pic_url.find(name='a').get('href')
featured_image_url

#Use soup to capture the headline of the page that the full-resolution image is on.
title=soup.find_all(name='h2', class_="title")
title[0]

#strip the header junk off the title
page_title=title[0].text.strip("<")
page_title


#Mission_to_mars
url = 'https://mars.nasa.gov/news'
browser.visit(url)

# Create a Beautiful Soup object
soup = bs(browser.html, 'html.parser')
type(soup)

titles=soup.find_all(name='div', class_="content_title")

#finding the first-listed title
titles[0].text

#storing the first title as a variable
latest_title=titles[0].text.strip("\n")
latest_title

#This is the list of titles
titles_list=[]
for t in titles:
    titles_list.append(t.text.strip("\n"))
titles_list

paragraph_text=soup.find_all(name='div', class_="rollover_description_inner")
#paragraph_text

#Storing the first paragraph as a variable
paragraph_text[0].text
latest_paragraph_text=paragraph_text[0].text
latest_paragraph_text

# Setup splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url)

#finding the image box, set as variable
image_nav=browser.find_by_id("full_image")

#following the link to the image
click_image=browser.find_by_id("full_image").first.click()

#navigate through the "more info" box to get to the final destination
click_more_info=browser.links.find_by_partial_text("more info").first.click()

#each time we write code with the browser, we change the identity of the browser, so when we use it in this variable,
#it calls to the latest iteration. 
soup=bs(browser.html, 'html.parser')
#print(soup.prettify())

#finding the code that indicates the download-the-pic link
pic_url=soup.find(name='div', class_="download_tiff")

#Setting the featured image for the image url
featured_image_url=pic_url.find(name='a').get('href')
featured_image_url

