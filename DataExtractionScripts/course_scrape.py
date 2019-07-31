# import requests
# from urllib.request import urlopen
# from bs4 import BeautifulSoup
#
#
# resp = urlopen("https://feheroes.gamepedia.com/Nino:_Pale_Flower/Quotes")
# soup = BeautifulSoup( resp.read(), features = "html5lib" )
#
# links = soup.find_all('a')
#
# for link in links: # Processing each link and getting the url value
#     url = link.get( 'href' )
#     print(url)

import csv
import requests
import os
from urllib.request import urlopen
from bs4 import BeautifulSoup


# Setting up System Info
headers = { 'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}

# Scraping Text
with requests.Session() as s :
    url = "http://catalog.illinois.edu/courses-of-instruction/ece/"
    r = s.get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'html5lib')
    data_scraped = soup.find_all(['a','p'], ['schedlink','courseblockdesc'])

# Organizing Text
# test = data_scraped[4].text
# new_test = test.replace("  ", ",")
# new_test = new_test[:-2] + ','
# print(new_test)

total_string_block = len(data_scraped)
delete_string_list = [" credit: ", " Hours. ", " Hour. "]

with open("ece_courses.csv", 'w', newline = '' ) as f :
    fieldnames = ['CourseNum', 'CourseName', 'Credits', 'Description']
    writerobject = csv.DictWriter(f, fieldnames = fieldnames )
    writerobject.writeheader()

    for i in range (0,total_string_block,2) :
        course_properties = (data_scraped[i].text).split("  ")
        course_properties[0] = course_properties[0].encode('utf8', 'ignore').decode('ascii', 'ignore')  #Killing some unknown characters

        course_properties[1] = course_properties[1][1:]

        for remove in delete_string_list :
            course_properties[2] = course_properties[2].replace(remove, "")

        course_properties[2] = course_properties[2].encode('utf8', 'ignore')

        #print(course_properties)
        course_description = data_scraped[i+1].text
        writerobject.writerow({'CourseNum' : course_properties[0], 'CourseName' : course_properties[1], 'Credits' : course_properties[2], "Description" : course_description })




# links = soup.find_all('a')
#
# for link in links: # Processing each link and getting the url value
#     url = link.get( 'href' )
#     print(url)
