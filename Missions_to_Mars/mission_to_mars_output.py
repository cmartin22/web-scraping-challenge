#!/usr/bin/env python
# coding: utf-8

# In[59]:


# Dependencies
from bs4 import BeautifulSoup
import requests
from splinter import Browser
from splinter.exceptions import ElementDoesNotExist
import pandas as pd


# In[60]:


def scrape_info():


    # In[61]:




    # In[62]:


    # URL of page to be scraped
    url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'

    # Retrieve page with the requests module
    response = requests.get(url)
    # Create BeautifulSoup object; parse with 'lxml'
    soup = BeautifulSoup(response.text, 'lxml')


    # In[63]:


    #news title
    news_titles = soup.find_all('div', class_='content_title')
    news_title=news_titles[0].text.lstrip()
    length1=len(news_title)
    news_title=news_title[:length1-2]
    #news paragraph
    news_ps = soup.find_all('div', class_='rollover_description_inner')
    news_p=news_ps[0].text.lstrip()
    length2=len(news_p)
    news_p=news_p[:length2-1]


    # In[64]:


    # URL of page to be scraped
    twitter = 'https://twitter.com/marswxreport?lang=en'

    # Retrieve page with the requests module
    response_twitter = requests.get(twitter)
    # Create BeautifulSoup object; parse with 'lxml'
    soup_twitter = BeautifulSoup(response_twitter.text, 'lxml')


    # In[65]:


    #twitter
    mars_weathers = soup_twitter.find_all('div', class_='js-tweet-text-container')
    mars_weather=mars_weathers[3].text.strip()
    length3=len(mars_weather)
    mars_weather=mars_weather[:length3-31]


    # In[66]:


    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)

    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)

    try:
        browser.click_link_by_partial_text('FULL IMAGE')
        
        img_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
        img_url_request = requests.get(img_url)
        soup_img_url = BeautifulSoup(img_url_request.text, 'lxml')
        img = soup_img_url.find_all('a', class_='button fancybox')
        img_url_2=img[0].get('data-fancybox-href')
        featured_image_url= 'https://www.jpl.nasa.gov' +img_url_2
        
    except ElementDoesNotExist:
        print("Scraping Complete")


    # In[71]:


    mars_facts_url = 'https://space-facts.com/mars/'

    mars_facts = pd.read_html(mars_facts_url)[1]
    mars_facts.columns = ['Description','Value']
    mars_facts = mars_facts.to_html(index=False)


    # In[72]:


    executable_path = {'executable_path': 'chromedriver.exe'}
    browser2 = Browser('chrome', **executable_path, headless=False)

    url2 = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser2.visit(url2)

    try:
        browser2.click_link_by_partial_text('Cerberus Hemisphere Enhanced')
        
        hemisphere_1 = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced'

        # Retrieve page with the requests module
        response_hemisphere_1 = requests.get(hemisphere_1)
        # Create BeautifulSoup object; parse with 'lxml'
        soup_hemisphere_1 = BeautifulSoup(response_hemisphere_1.text, 'lxml')
        img_hemisphere_1 = soup_hemisphere_1.find_all('a',href=True)

        cerberus_hemisphere_url =img_hemisphere_1[4].get('href')
        cerberus_hemisphere_url
        
    except ElementDoesNotExist:
        print("Scraping Complete")


    # In[73]:


    executable_path = {'executable_path': 'chromedriver.exe'}
    browser2 = Browser('chrome', **executable_path, headless=False)

    url2 = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser2.visit(url2)

    try:
        browser2.click_link_by_partial_text('Schiaparelli Hemisphere Enhanced')
        
        hemisphere_2 = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced'

        # Retrieve page with the requests module
        response_hemisphere_2 = requests.get(hemisphere_2)
        # Create BeautifulSoup object; parse with 'lxml'
        soup_hemisphere_2 = BeautifulSoup(response_hemisphere_2.text, 'lxml')
        img_hemisphere_2 = soup_hemisphere_2.find_all('a',href=True)

        schiaparelli_hemisphere_url =img_hemisphere_2[4].get('href')
        schiaparelli_hemisphere_url
        
    except ElementDoesNotExist:
        print("Scraping Complete")


    # In[74]:


    executable_path = {'executable_path': 'chromedriver.exe'}
    browser2 = Browser('chrome', **executable_path, headless=False)

    url2 = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser2.visit(url2)

    try:
        browser2.click_link_by_partial_text('Syrtis Major Hemisphere Enhanced')
        
        hemisphere_3 = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced'

        # Retrieve page with the requests module
        response_hemisphere_3 = requests.get(hemisphere_3)
        # Create BeautifulSoup object; parse with 'lxml'
        soup_hemisphere_3 = BeautifulSoup(response_hemisphere_3.text, 'lxml')
        img_hemisphere_3 = soup_hemisphere_3.find_all('a',href=True)

        syrtis_major_hemisphere_url =img_hemisphere_3[4].get('href')
        syrtis_major_hemisphere_url
        
    except ElementDoesNotExist:
        print("Scraping Complete")


    # In[75]:


    executable_path = {'executable_path': 'chromedriver.exe'}
    browser2 = Browser('chrome', **executable_path, headless=False)

    url2 = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser2.visit(url2)

    try:
        browser2.click_link_by_partial_text('Valles Marineris Hemisphere Enhanced')
        
        hemisphere_4 = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced'

        # Retrieve page with the requests module
        response_hemisphere_4 = requests.get(hemisphere_4)
        # Create BeautifulSoup object; parse with 'lxml'
        soup_hemisphere_4 = BeautifulSoup(response_hemisphere_4.text, 'lxml')
        img_hemisphere_4 = soup_hemisphere_4.find_all('a',href=True)

        valles_marineris_hemisphere_url =img_hemisphere_4[4].get('href')
        valles_marineris_hemisphere_url
        
    except ElementDoesNotExist:
        print("Scraping Complete")

    hemisphere_image_urls = [{"title": "Valles Marineris Hemisphere", "img_url": valles_marineris_hemisphere_url},
        {"title": "Cerberus Hemisphere", "img_url": cerberus_hemisphere_url},
        {"title": "Schiaparelli Hemisphere", "img_url": schiaparelli_hemisphere_url},
        {"title": "Syrtis Major Hemisphere", "img_url": syrtis_major_hemisphere_url}]
    #unfortunately I could not figure out how to call from the dictionary. I apologize for that.
    mars_scrape = {"news_title": news_title,
                "news_p": news_p,
                "featured_image_url": featured_image_url,
                "mars_weather": mars_weather,
                "mars_facts": mars_facts,
                "hemisphere_image_urls": hemisphere_image_urls,
                "valles_marineris_hemisphere_url":valles_marineris_hemisphere_url,
                "syrtis_major_hemisphere_url":syrtis_major_hemisphere_url,
                "schiaparelli_hemisphere_url":schiaparelli_hemisphere_url,
                "cerberus_hemisphere_url":cerberus_hemisphere_url}

    return mars_scrape