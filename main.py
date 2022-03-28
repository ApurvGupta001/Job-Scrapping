# Basic Scrap
# from bs4 import BeautifulSoup
# with open('home.html', 'r') as html_file:
#     content = html_file.read();
#     # print(content)
#     soup = BeautifulSoup(content, 'lxml') #lxml format
#     #print(soup.prettify()) #pretties the code
#     # This was my way
#     course_content = soup.find_all('h5')  #scarps data of h5 tag
#     course_price = soup.find_all('a')   #scraps data of a tag
#     for (course, price) in zip(course_content, course_price): #filter out the required data
#         print(course.text, price.text)


#     #Course way of doing the same
#     course = soup.find_all('div', class_="card") #filtering div by card
#     for content in course: #iterating through each card
#         course_name = content.h5.text; 
#         course_price = content.a.text.split()[-1];
#         print(f'{course_name} costs {course_price}')




#Scrap Using Requests from Website
# from bs4 import BeautifulSoup
# import requests
# html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
# soup = BeautifulSoup(html_text, 'lxml')
# # print (soup)
# jobs = soup.find_all('li', class_="clearfix job-bx wht-shd-bx")
# for job_det in jobs:
#     post_time = job_det.find('span', class_="sim-posted").text
#     company_name = job_det.find('h3', class_="joblist-comp-name").text.replace(' ','')
#     skill_req = job_det.find('span', class_="srp-skills").text.replace(' ','')
#     # if post_time == "Posted few days ago":s
#     post_time.lstrip();
#     post_time.rstrip();
#     if 'few'in post_time:
#         print(company_name)
#         print(skill_req)
#         print(post_time)


#more scrapping on previous website scrapping periodically and writing in a file
from bs4 import BeautifulSoup
import requests
import time
print('Enter the skill you are unfamiliar with');   
s = input('>')
print(f'Filtering out {s}')
def find_jobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    soup = BeautifulSoup(html_text, 'lxml') 
    # print (soup)
    jobs = soup.find_all('li', class_="clearfix job-bx wht-shd-bx")
    for i, job_det in enumerate(jobs):
        post_time = job_det.find('span', class_="sim-posted").text
        company_name = job_det.find('h3', class_="joblist-comp-name").text.replace(' ','')
        skill_req = job_det.find('span', class_="srp-skills").text.replace(' ','')
        more_info = job_det.header.h2.a['href']
        # if post_time == "Posted few days ago":
        if 'few' in post_time and s not in skill_req:
            with open(f'posts/{i}.txt', 'w') as f:
                f.write(f'Company Name: {company_name.strip()}\n')
                f.write(f'Required Skill: {skill_req.strip()}\n')
                f.write(f'More info: {more_info}\n')
                print(f'Saved in {i}.txt')
if __name__ == '__main__':
    while(1):
        find_jobs()
        time_wait = 10
        print(f'Waiting for {time_wait} seconds')
        time.sleep(10)