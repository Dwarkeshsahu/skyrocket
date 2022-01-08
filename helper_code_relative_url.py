# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import re, requests, time, random

parent_url = "https://www.studiestoday.com/multiple-choice-questions/67/cbse.html"
headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}
request_object = requests.get(parent_url, headers=headers)
html_content = request_object.text 
soup = BeautifulSoup(html_content, "lxml")


if soup.select('div[class="item-list"] > ul > li > div > span > a[href*="multiple-choice-questions"],  div > div.view-footer div > table tbody > tr > td > a[href*="mcq"]'):
	elements = soup.select('div[class="item-list"] > ul > li > div > span > a[href*="multiple-choice-questions"],  div > div.view-footer div > table tbody > tr > td > a[href*="mcq"]')
	for element in elements:
		current_link = element.get('href')
		print("https://www.studiestoday.com" + current_link)
    
   
