import csv
import requests
import os
import json
import re
from urllib.request import urlopen
from bs4 import BeautifulSoup
from itertools import cycle

import time

def parse_webpage_info(soup2) :

    # Get Job Position Title and Location
    job_detail = soup2.find('script')
    job_des_soup = soup2.find('div', {'class': "jobDescriptionContent desc module pad noMargBot"})
    job_loc_soup = soup2.find('script', {'type': "application/ld+json"})

    if job_des_soup :
        job_des = job_des_soup.text
        job_des = job_des.replace("\"", "")
        job_des = job_des.encode("ascii", "ignore").decode("ascii")
    else :
        job_des = ""

    if job_loc_soup :
        job_loc = job_loc_soup.text
    else :
        job_loc = ""


    # Parsing through relevant attributes
    reg_exp_addrloc = r"(?<=\"addressLocality\": \").+?(?=\",)"
    job_addr = re.search(reg_exp_addrloc, job_loc)
    if job_addr :
        job_addr = job_addr.group()
        job_addr = job_addr.encode("ascii", "ignore").decode("ascii")

    reg_exp_addrreg = "(?<=\"addressRegion\": \").+?(?=\",)"
    job_reg = re.search(reg_exp_addrreg, job_loc )
    if job_reg :
        job_reg = job_reg.group()
        job_reg = job_reg.encode("ascii", "ignore").decode("ascii")

    if job_detail :
        reg_exp_job = r"(?<='jobTitle' : \").+?(?=\",)"
        job_position = re.search(reg_exp_job, job_detail.text)
        if job_position :
            job_position = job_position.group()
            job_position = job_position.encode("ascii", "ignore").decode("ascii")

        reg_exp_company = r"(?<='name':\").+?(?=\",)"
        company = re.search(reg_exp_company, job_detail.text)
        if company :
            company = company.group()
            company = company.encode("ascii", "ignore").decode("ascii")
    else :
        job_position = ""
        company = ""

    if job_addr and job_reg :
        citystate = job_addr + " " + job_reg
    elif job_addr and not job_reg :
        citystate = job_addr
    elif not job_addr and job_reg :
        citystate = job_reg
    else :
        citystate = ""

    if citystate :
        citystate = citystate.encode("ascii", "ignore").decode("ascii")



    return company, job_position, citystate, job_des
    # reg_exp_city = r"(?<='city' : \").+?(?=\",)"
    # city = re.search(reg_exp_city, job_detail.text)
    # if city :
    #     city = city.group()
    #
    # reg_exp_state = r"(?<='state' : \").+?(?=\",)"
    # state = re.search(reg_exp_state, job_detail.text)
    # if state :
    #     state = state.group()
    # print(company)
    # print(job_position)
    # print(job_reg)
    # print(job_addr)


research_area = "Bioelectronics and bioinformatics"
research_keyword = []

with open("Research_Area.csv") as r :
    csv_reader = csv.reader(r, delimiter=',')
    first_row = 1
    for row in csv_reader :

        if first_row :
            first_row = 0
            continue

        elif row[1] == research_area :
            row[2] = row[2].encode('ascii', 'ignore').decode('ascii', 'ignore')
            row[2] = row[2].replace(" ", "+")
            research_keyword.append( row[2] )
        else :
            break

print(research_keyword)
start_time = time.time()

# Setting up System Info
#'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
#'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
headers = { 'user-agent' : 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0)'}
count = 0
#proxies = ["96.118.254.95:8080", "1.2.169.101:47477", "62.205.169.74:53281", "203.77.239.18:37002", "103.70.205.241:44424", "178.182.228.69:36657"]
#proxy_pool = cycle(proxies)
# no single ISA, ultraviolet spectro

# Scraping Text
with requests.Session() as s :
    with open("C:/Users/chris/Downloads/Scripts/job_csv/bio_elec_info_2.csv", 'w', newline = '' ) as f :
        fieldnames = ['Company', 'JobTitle', 'CityState', 'Description', "JobUrl", "ResearchArea", "ResearchKeyWord"]
        writerobject = csv.DictWriter(f, fieldnames = fieldnames )
        writerobject.writeheader()

        # Obtain all job links shown on the first page
        for keyword in research_keyword :
            #proxy = next(proxy_pool)
            #print("Requesting %s" %(proxy) )
            url = "https://www.glassdoor.com/Job/jobs.htm?suggestCount=0&suggestChosen=false&clickSource=searchBtn&typedKeyword=%s+engineer&sc.keyword=%s+engineer&locT=&locId=&jobType=" %(keyword, keyword)
            # try:
            r = s.get(url, headers=headers )
            # except :
            #     print("Not good")
            #     continue

            soup = BeautifulSoup(r.content, 'html5lib')

            job_links = soup.find_all('a', {'class': 'jobLink'}, href = True )
            full_job_links_page = []
            jobID_full = []

            for i in range(len(job_links) ) :
                jobID = job_links[i]['href']
                jobID = jobID[jobID.find("jobListingId"):]

                if jobID not in jobID_full :
                    full_job_links_page.append(job_links[i]['href'])
                    jobID_full.append(jobID)

            print(url)
            # url = "https://www.glassdoor.com/partner/jobListing.htm?pos=101&ao=298419&s=149&guid=0000016c15a260c7a41a9f3ed7f8c27f&src=GD_JOB_AD&t=SRFJ&extid=4&exst=O&ist=L&ast=OL&vt=w&slr=true&cs=1_d169f4d8&cb=1563731059511&jobListingId=3226504305"
            # r = s.get(url, headers=headers)
            # soup = BeautifulSoup(r.content, 'html5lib')

            #job_des = soup.find_all('div', {'class': "jobDescriptionContent desc module pad noMargBot"})
            #job_detail = soup.find_all('script')
            #print(job_detail[0].text)



            for i in range( len(full_job_links_page) ) :
                # Navigating to Job Info Link
                test_job_link = full_job_links_page[i].encode("utf-8", "ignore").decode("utf-8")
                #print(test_job_link)
                job_info_url = "https://www.glassdoor.com" + test_job_link
                #job_info_url = job_info_url.encode("utf-8", "ignore").decode("ascii")
                print(job_info_url)
                try :
                    r2 = s.get(job_info_url, headers=headers )
                except :
                    print("Unknown Reason")
                    continue 
                soup2 = BeautifulSoup(r2.content, 'html5lib')


                if not soup2 :
                    print("Skip")
                    continue
                company, job_position, citystate, job_des = parse_webpage_info(soup2)
                adjusted_keyword = keyword.replace("+", " ")
                adjusted_keyword = adjusted_keyword.encode("ascii", "ignore").decode("ascii")

                writerobject.writerow({'Company' : company, 'JobTitle' : job_position, 'CityState' : citystate, "Description" : job_des, "JobUrl" : job_info_url, "ResearchArea" : research_area, "ResearchKeyWord" : adjusted_keyword })

            count += 1
            print("Successful Write %d" %(count) )


print("--- %s seconds ---" % (time.time() - start_time))
print("Completed")





# print(job_detail)
# Testing stuff with glassdoor.txt
# with open("glassdoor_text.txt", 'w', newline = '' ) as f :
#     for i in range(len(full_job_links_page) ) :
#         f.write(full_job_links_page[i] )
        #f.write("\n")
    #f.write(full_job_links_page)
    #f.write(soup.prettify().encode('ascii', 'ignore').decode('ascii', 'ignore') )

    # count = 0
    # for i in range ( len(job_des) ) :
    #     count += 1
    #     print(count)
    #     f.write( job_des[i].prettify() + "\n")

    # for i in range( len(job_detail)) :
    #     f.write(job_detail[i].prettify().encode('ascii', 'ignore').decode('ascii', 'ignore') )

    #f.write(job_detail[0].text.encode('ascii', 'ignore').decode('ascii', 'ignore') )


# Get rid of amp; from initial reading


# 1) Figure out Search Term for glassdoor
# 2) Retrieve all HTML Links on the search page
# 3) Traverse through all the links and obtain info based on respective page



# Unused research keyword
# 210,Networking and distributed computing,internet of things,
# 211,Networking and distributed computing,IoT,
# 212,Networking and distributed computing,scheduling,
# 213,Networking and distributed computing,queueing,
# 214,Networking and distributed computing,wearable computing,
# 215,Networking and distributed computing,internet security,
# 216,Networking and distributed computing,IoT security,
# 217,Networking and distributed computing,wireless sensing,
# 218,Networking and distributed computing,wireless imaging,
# 219,Networking and distributed computing,network tomography,
# 220,Networking and distributed computing,mobile health,
# 228,Power and energy systems,electric transportation,
# 229,Power and energy systems,efficient device,
# 230,Power and energy systems,efficient building,
# 231,Power and energy systems,utility system,
# 232,Power and energy systems,microgrid,
# 233,Power and energy systems,energy-harvesting,
# 234,Power and energy systems,solar energy,
# 235,Power and energy systems,wind energy,
# 236,Power and energy systems,electric vehicle,
# 237,Power and energy systems,hybrid vehicle,
# 238,Power and energy systems,energy management,
# 239,Power and energy systems,energy conversion,
# 240,Power and energy systems,energy storage,
# 241,Power and energy systems,energy control,
# 242,Power and energy systems,power converter,
# 243,Power and energy systems,electricity grid,
# 244,Power and energy systems,power network,
# 245,Power and energy systems,power electronics,
# 251,Reliable and secure computing systems,malicious attack,
# 252,Reliable and secure computing systems,resiliency ,
# 253,Reliable and secure computing systems,reliability ,
# 254,Reliable and secure computing systems,privacy,
# 255,Reliable and secure computing systems,computer security,
# 256,Reliable and secure computing systems,information trust,
# 257,Reliable and secure computing systems,cryptographic system,
# 258,Reliable and secure computing systems,protocol,
# 259,Reliable and secure computing systems,fault tolerance,
# 260,Reliable and secure computing systems,formal method,
# 261,Reliable and secure computing systems,software verification,
# 268,Data/Information science and systems,information storage ,
# 269,Data/Information science and systems,information transmission,
# 270,Data/Information science and systems,information processing,
# 271,Data/Information science and systems,information learning,
# 272,Data/Information science and systems,learning,
# 273,Data/Information science and systems,data utilization ,
# 274,Data/Information science and systems,data representation,
# 275,Data/Information science and systems,data storage ,
# 276,Data/Information science and systems,data transmission,
# 277,Data/Information science and systems,data processing,
# 278,Data/Information science and systems,data learning,
# 279,Data/Information science and systems,cognitive computing,
# 280,Data/Information science and systems,computational science,
# 281,Data/Information science and systems,computational engineering,
# 282,Data/Information science and systems,cybersecurity,
# 283,Data/Information science and systems,privacy,
# 284,Data/Information science and systems,data analytics,
# 285,Data/Information science and systems,decision science,
# 286,Data/Information science and systems,distributed computing,
# 287,Data/Information science and systems,distibuted storage,
# 288,Data/Information science and systems,game theory,
# 289,Data/Information science and systems,imaging ,
# 290,Data/Information science and systems,machine learning,
# 291,Data/Information science and systems,network science,
# 292,Data/Information science and systems,network engineering,
# 293,Data/Information science and systems,scio-technical,
# 294,Data/Information science and systems,wearable computing,
# 295,Data/Information science and systems,mobile computing,
# 302,"Electronics, plasmonics, and photonics",plasmons,
# 303,"Electronics, plasmonics, and photonics",NEMS,
# 304,"Electronics, plasmonics, and photonics",quantum mechanics,
# 305,"Electronics, plasmonics, and photonics",qubit,
# 306,"Electronics, plasmonics, and photonics",electromagnetic,
# 307,"Electronics, plasmonics, and photonics",beyond CMOS,
# 308,"Electronics, plasmonics, and photonics",CMOS,
# 309,"Electronics, plasmonics, and photonics",charge particle,
# 310,"Electronics, plasmonics, and photonics",microelectromechanical,
# 311,"Electronics, plasmonics, and photonics",nanoelectromechanical,
# 312,"Electronics, plasmonics, and photonics",optical engineering,
# 313,"Electronics, plasmonics, and photonics",optical system,
# 314,"Electronics, plasmonics, and photonics",quantum optics,
# 315,"Electronics, plasmonics, and photonics",cryptography,
# 316,"Electronics, plasmonics, and photonics",RF engineering,
# 317,"Electronics, plasmonics, and photonics",microwave engineering,
# 318,"Electronics, plasmonics, and photonics",semiconductor manufacturing,
# 319,"Electronics, plasmonics, and photonics",RF,
# 320,"Electronics, plasmonics, and photonics",microwave,
# 327,Artificial intelligence and autonomous systems,UAV,
# 328,Artificial intelligence and autonomous systems,autonomous vehicular technology,
# 329,Artificial intelligence and autonomous systems,cyberphysical system,
# 330,Artificial intelligence and autonomous systems,internet of things,
# 331,Artificial intelligence and autonomous systems,IoT,
# 332,Artificial intelligence and autonomous systems,human computer interaction,
# 333,Artificial intelligence and autonomous systems,machine vision,
# 334,Artificial intelligence and autonomous systems,computer vision,
# 335,Artificial intelligence and autonomous systems,robotics,
# 336,Artificial intelligence and autonomous systems,sensing system,
# 337,Artificial intelligence and autonomous systems,smart infrastructure,
# 338,Artificial intelligence and autonomous systems,speech processing,
# 339,Artificial intelligence and autonomous systems,language processing,
# 340,Artificial intelligence and autonomous systems,audio processing,
# 347,Bioelectronics and bioinformatics,disease diagnostics,
# 348,Bioelectronics and bioinformatics,clinical test,
# 349,Bioelectronics and bioinformatics,medical imaging,
# 350,Bioelectronics and bioinformatics,neural synapse,
# 351,Bioelectronics and bioinformatics,genetic,
# 352,Bioelectronics and bioinformatics,proteomic,
# 353,Bioelectronics and bioinformatics,genomics,
# 354,Bioelectronics and bioinformatics,healthcare,
# 355,Bioelectronics and bioinformatics,nanomedicine,
# 356,Bioelectronics and bioinformatics,bio-nanotechnology,
# 357,Bioelectronics and bioinformatics,bionanotechnology,
# 358,Bioelectronics and bioinformatics,neuro-engineering,
# 359,Bioelectronics and bioinformatics,neuroengineering,
# 360,Bioelectronics and bioinformatics,diagnostics,
