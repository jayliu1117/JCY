import pandas as pd
import numpy as np

research_areas = pd.read_csv('research_areas.csv')
ece_courses = pd.read_csv('ece_courses.csv')
course_related = pd.read_csv('course_related.csv')

area = research_areas["ResearchArea"]
keywords = research_areas["ResearchKeyword"]
desp = ece_courses["Description"]
topics = ece_courses["Topics"]

# Finding the distinct area names and their starting row
st_pts = []
areaList = []
areaName = 0
count = 0
for i in area:
    if i != areaName:
        areaName = i
        areaList.append(i)
        st_pts.append(count)
    count += 1


# Iterate and count matches to each of the keyword on the keyword list
# This is done to both Description and Topics in the courses csv file
for course in range(len(desp)):

    matchCt = np.zeros((len(keywords),))
    for i in range(len(keywords)):
        keyword = keywords[i]
        match = 0

        # To avoid nan values
        if desp[course] == desp[course]:
            for k in range(len(desp[course]) - len(keyword)):
                if(desp[course][k:k+len(keyword)]==keyword):
                    match += 1

        if topics[course] == topics[course]:

            for k in range(len(topics[course]) - len(keyword)):
                if(topics[course][k:k+len(keyword)]==keyword):
                    match += 1

        matchCt[i] = match

    countTotalList = []
    # sum up and decide on the area
    for i in range(len(st_pts) - 1):
        count = np.sum(matchCt[st_pts[i]:st_pts[i+1]])
        countTotalList.append(count)

    if np.sum(countTotalList) < 1:
        finalArea = ""
    else:
        finalArea = areaList[np.argmax(countTotalList)]
    course_related["ResearchArea"][course] = finalArea
    print(countTotalList, finalArea)


print(course_related)

course_related.to_csv("course_related.csv")
