# -*- coding: utf-8 -*-
import pandas as pd
import re

csv_df = pd.read_csv("D:/SKYWART/Title_cleaning/Titles - Sheet1.csv", sep='\t')
csv_df.fillna("", inplace=True)

def clean(string):
    class_, subject, chapter_number, chapter_name = "", "", "", ""
#     string = re.sub("\s+", " ", string, flags=re.I)
#     string = re.sub("\sncert solutions$", " ", string, flags=re.I).strip(" ").strip("-").strip(" ")
#     string = re.sub("\sncert mcq$", " ", string, flags=re.I).strip(" ").strip(" –").strip(" ")
#     string = re.sub("\swith answers$", " ", string, flags=re.I).strip(" ").strip("-").strip(" ")
#     print(string)
    
#     if(re.search(r"^mcq questions for class\s", string, flags=re.I)):
#         string = re.sub("^mcq questions for\s", " ", string, flags=re.I).strip(" -")
#         match_object = re.search(r"^class\s(\d+)\s(.*?)\schapter\s(\d+)\s(.*?)$", string, flags=re.I)
#         if(match_object):
#             class_ = match_object.group(1)
#             subject = match_object.group(2)
#             chapter_number = match_object.group(3)
#             chapter_name = match_object.group(4)
#             return [string, class_, subject, chapter_number, chapter_name]
    
#     match_object = re.search(r"^(.*?)\sclass\s(\d+)\smcq\squestions\swith\sanswers\s(.*?)\s(?:chapter|poem)\s(\d+)$", string, flags=re.I)
#     if(match_object):
#         print("pattern 1")
#         class_ = match_object.group(2)
#         subject = match_object.group(3)
#         chapter_number = match_object.group(4)
#         chapter_name = match_object.group(1)
#         return [string, class_, subject, chapter_number, chapter_name]

    match_object = re.search(r"(Class\s\d+)\s(.*?)\s(Chapter\s\d+)\s(.*)", string, flags=re.I)
    if(match_object):
        class_ = match_object.group(1)
        subject = match_object.group(2)
        chapter_number = match_object.group(3)
        chapter_name = match_object.group(4)
        return [string, class_, subject, chapter_number, chapter_name]
        

        
#     match_object = re.search(r"^reading\scomprehension\smcq\squestions\swith\sanswers\sclass\s(\d+)\s(.*?)$", string, flags=re.I)
#     if(match_object):
#         print("pattern 3")
#         class_ = match_object.group(1)
#         subject = match_object.group(2)
#         chapter_number = ""
#         chapter_name = "Reading Comprehension"
#         return [string, class_, subject, chapter_number, chapter_name]
            
#     return [string, class_, subject, chapter_number, chapter_name]

csv_df["temp_title"], csv_df["class"], csv_df["subject"], csv_df["chapter_number"], csv_df["chapter_name"] = zip(*csv_df.apply(lambda row: clean(row["title"]), axis=1))
csv_df.to_csv("D:/SKYWART/Title_cleaning/testing.csv", index=False, sep="\t", encoding="utf-8")
csv_df.head()
