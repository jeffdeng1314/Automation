# I am too lazy to go through applying hundreds of jobs with (almost) the same procedures, so Imma let this bot applies it for me

# Please have your resume in the same directory and named it Resume.pdf

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time
from urllib import request
import os
import json
from sys import exit

# Change this to your json file
class myFiles:
    jsonFile = "myInfo.json"
    resume = "Resume.pdf"

def lever(dr):
    WebDriverWait(dr,5).until(lambda d: d.find_element_by_class_name('"application-file-input invisible-resume-upload'))
    
    resumeButton = dr.find_element_by_id_name("resume-upload-input")
    resumeButton.click()


    print('this is lever')


def smartRecruiters(dr):
    print("This is smart")


def workday(dr):
    print("workday")


def recruitingParser(url):

    for key,val in recruitingList.items():
        if key in url:
            return val
    
    exit("The recruitment company is currently not supported or the link you've entered is not a valid job app")



def main():
    
    jobURL = str(input("Enter your job application url: "))

    site = recruitingParser(jobURL)

    dr = webdriver.Chrome(executable_path="../chromedriver.exe")
    dr.get(jobURL)

    # Calling the function to the corresponding recruiting company
    site(dr)


if __name__ == "__main__":
    
    # switch statement function call idiom
    recruitingList = {
        "lever.co": lever,
        "smartrecruiters.com": smartRecruiters,
        "myworkdayjobs.com": workday
    }

    with open(myFiles.jsonFile) as f:
        myself = json.load(f)
    f.close()

    main()    
