
# GOAL: sign into blackboard

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time


service = Service(executable_path="/usr/bin/chromedriver")

chrome_options = Options()
chrome_options.add_argument(r"--user-data-dir=/home/matt/.config/google-chrome/")
chrome_options.add_argument(r"--profile-directory=Default")

driver = webdriver.Chrome(service=service, options=chrome_options)


try:

    # driver.get("https://google.com")
    # driver.get("https://webcourses.niu.edu/ultra/course")

    domain = "webcourses.niu.edu"
    # j_session = "13754D0B346D8CA27572423B120F8D62"
    # bb_router = "expires:1733630345,id:1DB7B3F6C206CBE09812B15690338B75,sessionId:2706945838,signature:8c72aaa1a832ba6ee7d9404724082c1654acf033d42bbd3f50579e528ee537c9,site:a16720d8-33d0-413f-9412-dd9606e3f2d4,timeout:10800,user:1163c297653f4afcb849c3d0f28c5bb6,v:2,xsrf:f53d1758-a3bb-403a-92ff-6b4c7b67ed60"
    # auth_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJBTExZIiwic3ViIjoiQUxMWV9UT0tFTiIsImZpbGVJZHMiOltdLCJjb3Vyc2VSb2xlIjoidW5wcml2aWxlZ2VkIiwiaXNzIjoiMDJpSnh4eWJlcWo1U2RBaEM1MlJycE14aUxhcTRSNkUiLCJyaWNoQ29udGVudElkcyI6W10sImV4cCI6MTczMzY0MzQwMSwiaWF0IjoxNzMzNjQzMTAxLCJjb3Vyc2VJZCI6Il8zNTA2NzNfMSIsInVzZXJJZCI6Il85ODc1NTJfMSJ9.H8x6X963bzz_kzNbtwCFeMxqpq_p0A9oLbk0CoUdX4w"
    #
    # cookies = [
    #         {"name": "authToken", "value": auth_token, "domain": domain, "path": '/'}
    #     ]
    #
    # for cookie in cookies:
    #     driver.add_cookie(cookie)


    driver.get("https://webcourses.niu.edu/ultra/course")

#
    time.sleep(3)

    print(driver.title)

except Exception as e:
    print(f"an error occured: {e}")

finally:
    driver.quit()
