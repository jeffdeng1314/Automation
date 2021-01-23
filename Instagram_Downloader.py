# Need to use Selenium to simulate the browsing action

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# import time
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

def instaBot(link):
    srcName = link.split('/')[4]

    login = "https://www.instagram.com/"
    dr = webdriver.Chrome()


    # Loggin into Instagram
    dr.get(login)

    # will wait for the dom to load and when we can see the 'loginform' id element
    WebDriverWait(dr,5).until(lambda d: d.find_element_by_id('loginForm'))

    dr.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(user.username)
    dr.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(user.password)
    dr.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button').click()

    # time.sleep(3)

    # WebDriverWait(dr).until(document_initialised)
    WebDriverWait(dr,5).until(lambda d: d.find_element_by_id('react-root'))
    dr.get(link)


    # img = dr.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/div[2]/div/div/div[1]/img')

    vid_links = []
    img_links = []


    counter = 0
    n = 0
    while True:
        
        try:
            buttons = dr.find_elements_by_class_name('_6CZji')
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
            img = dr.find_elements_by_class_name('KL4Bh')[n-1].find_element_by_tag_name('img').get_attribute('src')
            img_links.append(img)
        except:
            vid = dr.find_elements_by_class_name('_5wCQW')[n-1].find_element_by_tag_name('video').get_attribute('src')
            vid_links.append(vid)

        print('n: ', n)
    
    for each in range(len(img_links)):
        # This downloads the image
        fullPathName = os.path.join(user.downloadPath, f"{srcName}_img_{each+1}.png")
        request.urlretrieve(img_links[each],fullPathName)


    for each in range(len(vid_links)):
        # This downloads the videos
        fullPathName = os.path.join(user.downloadPath, f"{srcName}_vid_{each+1}.mp4")
        request.urlretrieve(vid_links[each],fullPathName)


    return dr


if __name__ == '__main__':
    link = input(str("Enter your Instagram link: "))
    driver = instaBot(link)
    driver.close()

    # Kill the chrome drive in the background
    os.system("taskkill /f /im chromedriver.exe /T")