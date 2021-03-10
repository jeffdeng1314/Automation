# https://www.youtube.com/watch?v=cnPlKLEGR7E
# Thanks Tim!


# This is to insert the job application link with parsed data into my Google Sheet so I can keep track of my applied jobs

import requests
from bs4 import BeautifulSoup
from datetime import datetime

import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope =["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json")

client = gspread.authorize(creds)

# make sure we are getting the first sheet
sheet = client.open("Companies").sheet1



def recording():
    while True:
        try:
            # Ideally from LinkedIn
            url = str(input("Please enter the Job URL: "))
        except:
            print("Invalid URL! Bye!!!")
            break    

        soup = BeautifulSoup(requests.get(url).content, "html.parser")
        company = str(soup.find("a", {"class" : "topcard__org-name-link"})).split('>')[1].split('<')[0]

        position = str(soup.find("h1", {"class" : "topcard__title"})).split('>')[1].split('<')[0]

        location = str(soup.find("span", {"class" : "topcard__flavor topcard__flavor--bullet"})).split('>')[1].split('<')[0]

        today = datetime.now().strftime('%m/%d/%Y')
        
        now = "{}".format(today)



        data = sheet.get_all_records()

        insertRow = [company,position,url,"",location]

        # print(len(data)+1)
        sheet.insert_row(insertRow,len(data)+2)

        # the date somehow showed up with an apostrophe in front, so I gotta update it to correct it back to actual date type
        sheet.update_cell(len(data)+2,4,now)





if __name__ == "__main__":
    recording()