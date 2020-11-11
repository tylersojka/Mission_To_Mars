# Mission_To_Mars

![mars](Resources/vectorstock_19656662.png)
*****
*****

* By: Tyler Sojka
* November 2020
* Data scraping with Python, PyMongo, MongoDB, Splinter, Flask, HTML, bootstrap, BeautifulSoup, and a dash of pandas

*****
*****

## T-43 hours and counting

T-43 hours and counting is standard, old school, shuttle launch countdown lingo. It denotes the beginning of the countdown clock, and the start of the final preparations for launch.

Our client, Robin, is an avid space enthusiast and freelance astronomer, whose dream is to land a job with NASA. She wants to build a web app showcasing current Mars information, including:

* A featured Mars image
* A table holding various facts about mars
* Some information on the current weather on Mars
* The title and a snippet of the latest story about Mars missions
* Images of the different hemispheres of mars
  
## T-27 hours and counting

This milestone of the countdown denotes the beginning of operations to load cryogenic reactants into the orbiters fuel cell storage tanks

Robin wants us to help her with her web app. To carry out her requests, we will be automating the data gathering process with web scraping. We will be scraping information and images from multiple sites and storing it with MongoDB. MongoDB, being a NoSQL document-oriented database, is perfect for this because of its is ability to store a variety of different values. We will then be using Flask to build a web app to render all of our scraped data.

* ### Scraping the data
  
  Using BeautifulSoup and Splinter, along with chromes developer tools, we will inspect various websites html, and scrape the required information.
  * The latest Mars mission title and snippet will be scraped from <https://mars.nasa.gov/news/>
  * The featured image will be scraped from <https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars>
  * The table of facts will be scraped from <http://space-facts.com/mars/>
  * The Mars weather will be imbedded web content from <https://mars.nasa.gov/insight/weather/>
  * The Mars hemisphere images will be scraped from <https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars>

## T-6 hours and counting

This countdown milestone denotes the finishing of filling the external tank with its load of liquid hydrogen and liquid oxygen propellants.

Once we have created the scripts to perform the web scraping, it’s time to build the Flask web app to preform and render the results. We will be using one of the flask routes to initiate the scrape. All of the scraped information will then be stored in MongoDB, and rendered via our web app.

* ### Storing the data
  
  We will be starting a MongoDB database called mars_app and connecting to it via PyMongo. PyMongo will allows us to access our Mongo database via Flask.
  * Start a new MongoDb database
  * Use PyMongo to create a connection to our MongoDB database
  * Using HTML and bootstrap we will create an index.html template to be rendered with flask. This will allow us to present the data in a visually appealing fashion.
  * Use the first flask route to render all new scraped data inside of a HTML index template
  * Use the second flask route to perform the scrape and update the MongoDB database with all new information

## T-5, 4, 3, 2, 1...BLASTOFF

This countdown milestone is arguably one of the most exciting. It denotes the final countdown to the solid rocket booster ignition and liftoff.

Now that we have all of the pieces in place it’s time to initiate the web app!

* Initiation
  * We will first run MongoDB in our terminal. This enables us to use MongoDB
    * <code>$ brew services start mongodb-community@4.4</code>
  * We will then run our Flask App from our terminal.
    * <code>$ python app.py</code>
  * Opening up a web browser and navigating to <localhost:500> will show us our final product! upon the first visit, however, there will be no data. We must first navigate to the second flask route to perform the first scrape, and once we return to the home route all of the latest Mars information will be rendered!

![renderedpage](Resources/image%20(2).png)

