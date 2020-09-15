from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pandas as pd


def login():
    driver = webdriver.Chrome()
    driver.get('https://www.quora.com/')
    email = driver.find_element_by_xpath(
        "//input[@name='email' and @class='text header_login_text_box ignore_interaction']")
    email.send_keys('*******')
    time.sleep(0.5)
    password = driver.find_element_by_xpath(
        "//input[@name='password' and @class='text header_login_text_box ignore_interaction']")
    password.send_keys('*******')
    time.sleep(0.5)
    login = driver.find_element_by_xpath(
        "//input[@class='submit_button ignore_interaction']")
    login.click()
    time.sleep(0.5)
    return driver


def tweet_scroller(url, driver):
    driver.get(url)
    # define initial page height for 'while' loop
    lastHeight = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        # define how many seconds to wait while dynamic page content loads
        time.sleep(3)
        newHeight = driver.execute_script("return document.body.scrollHeight")
        if newHeight == lastHeight:
            break
        else:
            lastHeight = newHeight
    html = driver.page_source
    return html


def get_QuestionLink():
    driver = login()
    html = tweet_scroller("url", driver)
    driver.close()
    soup2 = BeautifulSoup(html)
    QuestionLink = []
    for i in soup2.findAll(attrs={'class': 'q-text puppeteer_test_question_title',
                                  'style': 'box-sizing: border-box; direction: ltr;'}):
        Link = i.parent.parent.parent.attrs['href']
        QuestionLink.append(Link)
    return QuestionLink


def main():
    QuestionLink = get_QuestionLink()
    QuestionLink_df = pd.DataFrame(QuestionLink)
    QuestionLink_df.to_csv('quora.csv', index=[])


if __name__ == "__main__":
    main()
