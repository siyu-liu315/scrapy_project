from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common import keys
import time

email = 'xzkp117@163.com'
password = "sy13110617031l"

def connection():
    PATH = r"C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    return driver

def search(key_words):
    encoding = key_words.replace(" ", "%20")
    search_link = f"https://www.linkedin.com/search/results/content/?facetSortBy=date_posted&?keywords={encoding}&origin=GLOBAL_SEARCH_HEADER"
    linkedin_login()
    driver.get(search_link)

    # need to search agian dont know why.
    search = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Search']")))
    search.send_keys('data analyst hiring')
    search.send_keys(Keys.ENTER)
    # driver.find_element_by_xpath("//button[contains(@class,'search-global')]").click()

def linkedin_login(driver):
    driver.get("https://www.linkedin.com/login")
    username = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID,"username")))
    username.send_keys(email)
    username.send_keys(Keys.ENTER)
    driver.find_element_by_id('password').send_keys(password)
    driver.find_element_by_xpath("//button[contains(text(),'Sign in')]").click()

# def find_element():
#     content = driver.find_element_by_xpath("//span[contains(@class,'break-words')]")
#     title = driver.find_element_by_xpath("//span[contains(@class,'feed-shared-actor__name')]")
#     link = driver.find_element_by_xpath("//a[contains(@class,'container-link')]/@href")
#     description = driver.find_element_by_xpath("//span[contains(@class, feed-shared-actor__description')]")
#     print(content,title,link,description)
#


# driver = connection()
# search("data analyst hiring")
# find_element()




# class linkedin():
#     PATH = r"C:\Program Files (x86)\chromedriver.exe"
#     url = "https://www.linkedin.com/login"
#
#     def __int__(self):
#         driver = webdriver.Chrome(self.PATH)
#         driver.get(self.url)
#
#     def linkedin_login(self):
#         WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.Id, "email-address")).send_keys("xzkp117@163.com")
#         self.driver.find_element_by_id("")
#
#
#
#     # https://www.linkedin.com/voyager/api/search/blended?count=6&filters=List(resultType-%3ECONTENT)&keywords=data%20analyst%20hiring&origin=SWITCH_SEARCH_VERTICAL&q=all&queryContext=List()&start=12
#     # CSRF check failed.
#
#     def linkedin_search(self):
#         key_words = 'data analyst hiring'
#         encoding = key_words.replace(" ", "%20")
#         url = f"https://www.linkedin.com/search/results/content/?keywords={encoding}&origin=GLOBAL_SEARCH_HEADER"
#



