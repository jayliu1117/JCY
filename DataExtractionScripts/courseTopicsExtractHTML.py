from lxml import html
import pandas as pd
import requests

df = pd.read_csv(r"ece_courses.csv", delimiter=',')
courseList = df["CourseNum"]

for i in range(1, courseList.size):

    page = requests.get('https://ece.illinois.edu/academics/courses/profile/' + courseList[i])
    tree = html.fromstring(page.content)

    text = tree.xpath('//ul/li/text()')
    newtext = [x for x in text if not (x.startswith("\r") or x.startswith("\t")) ]
    topics = " ".join(newtext)

    df["Topics"][i] = topics
print(df)
#
df.to_csv(r"ece_coursesWtopics.csv")