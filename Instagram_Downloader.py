# Need to use Selenium to simulate the browsing action

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from urllib import request
import os


# https://www.selenium.dev/documentation/en/webdriver/waits/
# https://stackoverflow.com/questions/63977746/selenium-python-instagram-scraping-all-images-in-a-post-not-working
from selenium.webdriver.support.ui import WebDriverWait

class user:
    username = "NooooooooooU_BallsDeep"
    password = "123456789BallsDeep420"

    
    name = os.environ['USERNAME']
    downloadPath = f"C:\\Users\\{name}\\Downloads"

class classNames:
    nextButton = '_6CZji'
    img = 'KL4Bh'
    vid = '_5wCQW'

    stories_click = "_42FBe"


def loggingIn(dr):
    dr.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(user.username)
    dr.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(user.password)
    dr.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button').click() 


def instaBot(link):
    srcName = link.split('/')[4]
    storeMode = False

    if link.split('/')[3] == 'stories':
        storeMode = True
        classNames.nextButton = 'FhutL'

    login = "https://www.instagram.com/"
    dr = webdriver.Chrome(executable_path="chromedriver.exe")


    # Loggin into Instagram
    dr.get(login)

    # will wait for the dom to load and when we can see the 'loginform' id element
    WebDriverWait(dr,5).until(lambda d: d.find_element_by_id('loginForm'))

    loggingIn(dr)

    # WebDriverWait(dr,5).until(lambda d: d.find_element_by_tag_name('main'))
    time.sleep(4)

    dr.get(link)
    if storeMode:
        WebDriverWait(dr,5).until(lambda d: d.find_element_by_class_name('Cd8X1'))
        elements = dr.find_elements_by_class_name(classNames.stories_click)
        elements[0].click()

    vid_links = []
    img_links = []


    counter = 0
    n = 0

    # In story mode
    if storeMode:
        while True:
            s = dr.current_url
            if s == login:
                break
            try:
                vid = dr.find_elements_by_tag_name('source')
                vid_detail = vid[0].get_attribute('src')
                print('vid: ',vid_detail)
                vid_links.append(vid_detail)

            except:
                img = dr.find_elements_by_tag_name('img')
                img_detail = img[0].get_attribute('src')
                print('img: ',img_detail)
                img_links.append(img_detail)
            
            try:
                buttons = dr.find_elements_by_class_name(classNames.nextButton)
                buttons[0].click()
                WebDriverWait(dr,5).until(lambda d: d.find_element_by_id('react-root'))
            except:
                WebDriverWait(dr,5).until(lambda d: d.find_element_by_id('react-root'))
                print("End of stories")
                break


    # Not in story mode
    else:
        while True:
            
            try:
                buttons = dr.find_elements_by_class_name(classNames.nextButton)
                buttons[0].click()
                WebDriverWait(dr,5).until(lambda d: d.find_element_by_id('react-root'))
                n+=1
            except:
                counter+=1
                n+=1
                WebDriverWait(dr,5).until(lambda d: d.find_element_by_id('react-root'))
                if counter==2:
                    break
                    
            
            try:
                vid = dr.find_elements_by_class_name(classNames.vid)[n-1].find_element_by_tag_name('video').get_attribute('src')
                vid_links.append(vid)

            except:
                img = dr.find_elements_by_class_name(classNames.img)[n-1].find_element_by_tag_name('img').get_attribute('src')
                img_links.append(img)

            print('n: ', n)

    try:   
        for each in range(len(img_links)):
            # This downloads the image
            fullPathName = os.path.join(user.downloadPath, f"{srcName}_img_{each+1}.png")
            request.urlretrieve(img_links[each],fullPathName)


        for each in range(len(vid_links)):
            # This downloads the videos
            fullPathName = os.path.join(user.downloadPath, f"{srcName}_vid_{each+1}.mp4")
            request.urlretrieve(vid_links[each],fullPathName)
    except:
        print("Unable to download the URLs, maybe the lists are empty")

    return dr


if __name__ == '__main__':
    link = input(str("Enter your Instagram link: "))
    driver = instaBot(link)
    driver.close()

    # Kill the chrome drive in the background
    os.system("taskkill /f /im chromedriver.exe /T")