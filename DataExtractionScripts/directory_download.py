import csv
import requests
import os
import numpy as np
from urllib.request import urlopen
from bs4 import BeautifulSoup

# ECE Faculty: https://directory.illinois.edu/detail?departmentId=illinois.eduKP933
# Issues: Can only do 30 directory search at a time.
# Setting up System Info
headers = { 'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}

# Scraping NetId/Available Professors First
# with requests.Session() as s :
#     url = "https://directory.illinois.edu/detail?departmentId=illinois.eduKP434"
#     r = s.get(url, headers=headers)
#     soup = BeautifulSoup(r.content, 'html5lib')
#
#     faculty_netId = []
#     start_add = 0
#     delete_string_list = ['javascript:goToDetail', '(', ')', "'"]
#
#     for a in soup.find_all('a', href = True ) :
#         if a.text :
#             current_text = a['href']
#
#             for curr in delete_string_list :
#                 current_text = current_text.replace(curr, "")
#
#             # First Faculty is haitham here.
#             if current_text == "zaher" :
#                 start_add = 1
#
#             if start_add :
#                 faculty_netId.append(current_text)
#
#             # Last Faculty is wjzhu here.
#             if current_text == "zilles" :
#                 start_add = 0
# print(faculty_netId)

# Scraping Remaining Information
faculty_netId = ['torrella', 'twidale', 'nhv', 'shobhav', 'p-violas', 'vmahesh', 'winslett', 'mdfwong', 'mwoodley', 'czhai', 'zilles']
full_faculty_info = []
count = 0
for netID in faculty_netId :
    current_link = "https://directory.illinois.edu/detail?search_type=&search=&from_result_list=true&skinId=0&userId=%s&sub=" %(netID)

    with requests.Session() as s :
        #url = "https://directory.illinois.edu/detail?search_type=&search=&from_result_list=true&skinId=0&userId=minhdo&sub="
        r = s.get(current_link, headers=headers)
        soup = BeautifulSoup(r.content, 'html5lib')

        # Getting Professor Name
        prof_name_soup = soup.find_all('h2', 'name flex-col-6')
        if prof_name_soup != [] :
            prof_name = prof_name_soup[0].text
        else :
            prof_name = ""


        # Scraping Professor's Description
        prof_description = soup.find_all('p')
        full_description = ""

        for i in range( 4,len(prof_description) ) :
            full_description = full_description + prof_description[i].text + " "

        # Scraping Research Related Text
        prof_research = soup.find_all('h3')
        research_keyword = ["Research Interests", "Research Areas", "Research Topics"]
        research_interest = ""
        research_areas = ""
        research_topics = ""

        col = 0

        for i in range( len(prof_research) ) :
            # print(i)
            # print(prof_research[i].text)

            if prof_research[i].text in research_keyword :
                research_desc = prof_research[i].next_sibling.next_sibling.text

                if prof_research[i].text == "Research Interests" :
                    research_interest = research_desc

                elif prof_research[i].text == "Research Areas" :
                    research_areas = research_desc

                else :
                    research_topics = research_desc

                #print(testing.upper())
    # unknnown_variable = ["\u2265"]
    # test_netID = netID.replace("\u015f", "")
    # prof_name = prof_name.replace("\u015f", "")
    # full_description = full_description.replace("\u015f", "")
    # research_interest = research_interest.replace("\u015f", "")
    # research_areas = research_areas.replace("\u015f", "")
    # research_topics = research_topics.replace("\u015f", "")

    test_netID = netID.encode('ascii', 'ignore').decode('ascii', 'ignore')
    prof_name = prof_name.encode('ascii', 'ignore').decode('ascii', 'ignore')
    full_description = full_description.encode('ascii', 'ignore').decode('ascii', 'ignore')
    research_interest = research_interest.encode('ascii', 'ignore').decode('ascii', 'ignore')
    research_areas = research_areas.encode('ascii', 'ignore').decode('ascii', 'ignore')
    research_topics = research_topics.encode('ascii', 'ignore').decode('ascii', 'ignore')

    faculty = (test_netID, prof_name, full_description.rstrip(), research_interest.rstrip(), research_areas.rstrip(), research_topics.rstrip())
    full_faculty_info.append(faculty)

    # print(full_faculty_info[count][1] )
    # count += 1
        #div class="categories"

print("Success! %d" %(len(full_faculty_info)) )

with open("cs_faculty4.csv", 'w', newline = '' ) as f :
    fieldnames = ['NetID', 'Professor Name', 'Professor Description', 'Research Interest', 'Research Area', 'Research Topic']
    writerobject = csv.DictWriter(f, fieldnames = fieldnames )
    writerobject.writeheader()

    for faculty in full_faculty_info :
        writerobject.writerow({'NetID' : faculty[0], 'Professor Name' : faculty[1], 'Professor Description' : faculty[2], 'Research Interest' : faculty[3], 'Research Area' : faculty[4], 'Research Topic' : faculty[5] })

print("Successful Write")

# for netID in faculty_netId :
#     current_link = "https://directory.illinois.edu/detail?search_type=&search=&from_result_list=true&skinId=0&userId=%s&sub=" %(netID)
#
#     with requests.Session() as s :
#         url = "https://directory.illinois.edu/detail?search_type=&search=&from_result_list=true&skinId=0&userId=minhdo&sub="
#         r = s.get(url, headers=headers)
#         soup = BeautifulSoup(r.content, 'html5lib')
#
#         faculty_netId = []
#         start_add = 0
#         delete_string_list = ['javascript:goToDetail', '(', ')', "'"]
#
#         for a in soup.find_all('a', href = True ) :
#             if a.text :
#                 current_text = a['href']
#
#                 for curr in delete_string_list :
#                     current_text = current_text.replace(curr, "")
#
#                 if current_text == "haitham" :
#                     start_add = 1
#
#                 elif current_text == "wjzhu" :
#                     start_add = 0
#
#                 if start_add :
#                     faculty_netId.append(current_text)
#
#         print(faculty_netId)

    #data_scraped = soup.find_all(['a','p'], ['schedlink','courseblockdesc'])
    # <a href="javascript:goToDetail('erhan')">
