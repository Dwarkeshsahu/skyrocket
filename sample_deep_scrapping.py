# -*- coding: utf-8 -*-
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import re, requests, time, random
import pandas as pd

def get_data(url,soup):
	questions = soup.select('.category-mcq-questions .entry-content > p')
  
	for question in questions:
		data_dict = {}
		data_dict["crawl_url"] = url
		data_dict["title"] = soup.title.get_text()
		temp_question_list = question.get_text(separator=" ").split('\n')
    
		if len(temp_question_list) > 4:
			data_dict["question"] = temp_question_list[1]
		else:
			continue

		for idx, option in enumerate(temp_question_list[2:]):
			option = re.sub(r"^\([a-z]\)", " ", option, flags = re.I)
			data_dict["option_"+str(idx+1)] = option

		if question.find_next("details"):
			if question.find_next("details").find("p"):
				data_dict["correct_option"] = question.find_next("details").find("p").get_text()
				data_dict["correct_option"] = re.sub(r"^answer\s*:", " ", data_dict["correct_option"], flags = re.I)

		for temp in data_dict.keys():
			if type(data_dict[temp])==str:
				data_dict[temp] = re.sub(r"\s+", " ", data_dict[temp])
				data_dict[temp] = data_dict[temp].strip()

		pd.DataFrame([data_dict], columns = col_names).to_csv(result, sep="\t", index=False, header=False, encoding='utf-8', mode='a')




def bfs(visited, current_link, headers):
	visited.append(current_link)
	queue.append(current_link)
	domain = urlparse(current_link).netloc

	while queue:
		url = queue.pop(0) 
		request_object = requests.get(url, headers=headers)
		html_content = request_object.text 
		soup = BeautifulSoup(html_content, "lxml")

		time.sleep(random.randint(1,4))
		if soup.select('h2 ~ ul > li > a[href*="mcq-questions"], h2 ~ ol > li > a[href*="mcq-questions"]'):
			elements = soup.select('h2 ~ ul > li > a[href*="mcq-questions"], h2 ~ ol > li > a[href*="mcq-questions"]')

			for element in elements:
				current_link = element.get('href')
				if urlparse(current_link).netloc == domain and current_link not in visited:
					print(current_link)
					visited.append(current_link)
					queue.append(current_link)

		if soup.select('.category-mcq-questions .entry-content > p'):
			print("Processing:", url)
			time.sleep(random.randint(1,3))
			get_data(url,soup)




# parent_url = "https://www.ncertbooks.guru/mcq-questions/"
parent_url = "https://ncertsolutions.guru/mcq-questions-with-answers/"
# parent_url = "https://www.learninsta.com/mcq-questions-for-class-12-biology-chapter-16/"

headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}

col_names = ["crawl_url", "title", "question", "option_1", "option_2", "option_3", "option_4", "option_5", "option_6", "correct_option", "Board", "Class", "Subject", "Chapter", "Topic", "Sub-topic"]
result = "result_ncertsolutions.guru.csv"
pd.DataFrame(columns = col_names).to_csv(result, sep="\t", index=False, encoding='utf-8')

visited = [] # List for visited nodes.
queue = []     #Initialize a queue
request_object = requests.get(parent_url, headers=headers)
html_content = request_object.text 
soup = BeautifulSoup(html_content, "lxml")
if(str(request_object.status_code).startswith("2")):
	bfs(visited,parent_url,headers)
	print(len(visited))
	print("Done")
else:
	print("No Response from website")
