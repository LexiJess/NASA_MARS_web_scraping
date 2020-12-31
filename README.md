The pertinent files are in folders titled "Flask_HTML code", "Flask_HTML Images", and "Jupyter Scraping Files". 


Whew! Webscraping is not for the faint of heart. It will make a hard man humble. 

This project was set up to capture information and images from nifty stuff in space. I used Splinter to navigate through the target websites (the JPL and NASA sites) and Beautiful Soup to capture the desired information. I wrote the code (using Splinter and Beautiful Soup) in Jupyter Notebook and then used VSCode to consolidate the multiple scraping programs into one large function, write the file out to MongoDB, and then connect the MongoDB to Flask and HTML documents. The HTML documents were assisted by using the Boostrap library. Flask/HTML pulled the information back out of storage in MongoDB and rendered the scraping programs into a tiny website that displays the information and images. 

Getting all the connections to establish and function was complicated. Getting the website to render appropriately is also difficult--Bootstrap formatting is enormously useful, but still tricky to get all of the code organized such that the images rendered correctly and displayed all the required information. 

The opening page displays the site concept and a button that calls the scraping function by bringing the user to the 
"/scrape" page that contains said function and also the HTML to display it. 