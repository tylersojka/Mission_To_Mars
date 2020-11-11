# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
import datetime as dt

def scrape_all():

    # Set the executable path and initilize the chrome browser in splinter
    #ex_path = {'executable_path' : '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', executable_path="chromedriver", headless=True)

    # Next, we're going to set our news title and paragraph variables
    news_title, news_paragraph = mars_news(browser)

    # Run all scraping functions and store results in dictionary
    data = {
        "news_title": news_title,
        "news_paragraph": news_paragraph,
        "featured_image": featured_image(browser),
        "facts": mars_facts(),
        "last_modified": dt.datetime.now(),
        "mars_hemi": mars_hemis(browser),
        #"weather": mars_weather(browser)
    }

    # Stop webdriver and return data
    browser.quit()
    return data


def mars_news(browser):

    # Visit the mars nasa news site
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    # Optional delay for loading the page
    browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)

    # set up html parser
    html = browser.html
    news_soup = soup(html, 'html.parser')
    
    # add try/except for error handeling
    try:
        slide_elem = news_soup.select_one('ul.item_list li.slide')

        #find the parent class
        slide_elem.find("div", class_='content_title')

        # Use the parent element to find the first `a` tag and save it as `news_title`
        news_title = slide_elem.find("div", class_='content_title').get_text()
        
        # Use the parent element to find the paragraph text
        news_p = slide_elem.find('div', class_="article_teaser_body").get_text()
    except AttributeError:
        return None, None

    return news_title, news_p

# # Featured Images
def featured_image(browser):

    # Visit URL
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)

    # Find and click the full image button
    full_image_elem = browser.find_by_id('full_image')
    full_image_elem.click()

    # Find the more info button and click that
    browser.is_element_present_by_text('more info', wait_time=1)
    more_info_elem = browser.links.find_by_partial_text('more info')
    more_info_elem.click()

    # Parse the resulting html with soup
    html = browser.html
    img_soup = soup(html, 'html.parser')

    try:
        # Find the relative image url
        img_url_rel = img_soup.select_one('figure.lede a img').get("src")

        # Use the base URL to create an absolute URL
        img_url = f'https://www.jpl.nasa.gov{img_url_rel}'
    except AttributeError:
        return None

    return img_url
# # Mars Facts

def mars_facts():
    try:
        # use 'read_html" to scrape the facts table into a dataframe
        df = pd.read_html('http://space-facts.com/mars/')[0]
    except BaseException:
        return None

    df.columns=['description', 'value']
    df.set_index('description', inplace=True)

    # turn the df back into html code, add bootstrap
    return df.to_html()

def mars_hemis(browser):
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)

    # 2 make a list to hold the urls
    hemisphere_image_urls = []

    # 3. Write code to retrieve the image urls and titles for each hemisphere.
    # parse the page html
    html = browser.html
    hemi_soup = soup(html, 'html.parser')
    # find the container that holds all the links
    hemi_parent = hemi_soup.find('div', class_='collapsible results')
    # find the container that holds each individual link
    hemi_child = hemi_parent.find_all('a')
    #loop through all the results and do a bunch of stuff:
    for item in hemi_child[::2]:
        #grab the relative link to the fullsize image
        link = item.get('href')
        # make the full url 
        hemi_item_url = f'https://astrogeology.usgs.gov{link}'
        #send the browser to that link
        browser.visit(hemi_item_url)
        #parse the page html
        html = browser.html
        hemi_soup = soup(html, 'html.parser')
        # get the relative image url
        hemi_img_url_rel = hemi_soup.select_one('img.wide-image').get("src")
        # get the title
        img_title = hemi_soup.select_one('h2.title').text
        # Use the base URL to create an absolute URL
        hemi_img_url = f'https://astrogeology.usgs.gov{hemi_img_url_rel}'
        # append the url list with a dictionary containing the title and image url
        hemisphere_image_urls.append({"img_title" : img_title, "img_url" : hemi_img_url})
    # each child container had 2 identicle links, drop the dupes
    #hemisphere_image_urls = [i for n, i in enumerate(hemisphere_image_urls) if i not in hemisphere_image_urls[n + 1:]] 
    # 4. return the list that holds the dictionary of each image url and title.
    return hemisphere_image_urls

# def mars_weather(browser):
#     # Visit the weather website
#     url = 'https://mars.nasa.gov/insight/weather/'
#     browser.visit(url)

#     # Parse the data
#     html = browser.html
#     weather_soup = soup(html, 'html.parser')

#     # Scrape the Daily Weather Report table
#     weather_table = weather_soup.find('pre', class_='embed_code').text
#     return weather_table

if __name__ == "__main__":
    # If running as script, print scraped data
    print(scrape_all())
