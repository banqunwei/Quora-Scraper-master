from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pandas as pd


def login():
    driver = webdriver.Chrome()
    driver.get('https://www.quora.com/')
    email = driver.find_element_by_xpath(
        "//input[@name='email' and @class='text header_login_text_box ignore_interaction']")
    email.send_keys('2214654333@qq.com')
    time.sleep(0.5)
    password = driver.find_element_by_xpath(
        "//input[@name='password' and @class='text header_login_text_box ignore_interaction']")
    password.send_keys('Ban123456')
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


def get_AnswerDetail(html, Qi):
    soup2 = BeautifulSoup(html)
    AnswerList = []
    i = 1
    for hit in soup2.find_all(
            attrs={'class': 'q-box qu-pt--medium qu-pb--tiny'}):
        try:
            a = {
                'QuestionNo': 'Q'+str(Qi)+'-A'+str(i),
                'QuestionAuthor': hit.find(attrs={'class': 'q-box qu-display--inline'}).get_text(),
                'QuestionDate': hit.find(attrs={'class': 'q-box qu-cursor--pointer qu-hover--textDecoration--underline'}).get_text().replace('Answered ', ''),
                'QuestionText': hit.find(attrs={'class': 'q-text qu-display--block'}).get_text(),
            }
            i += 1
            AnswerList.append(a)
        except BaseException:
            print('NoneType')
    return AnswerList


def get_Answer(QuestionLink):
    driver = login()
    Answer = []
    for i in QuestionLink:
        url = 'https://www.quora.com/Hypertension-1'+str(i)
        html = tweet_scroller(url, driver)
        Answer.append(get_AnswerDetail(html, QuestionLink.index(i)+1))
    driver.close()
    return Answer


def main():
    QuestionLink = pd.read_csv('QuoraLink.csv')['url'].tolist()
    Answer = get_Answer(QuestionLink)
    Answer_df = pd.DataFrame(Answer[0])
    Answer_df.to_csv('QuoraAnswer.csv', index=[])


if __name__ == "__main__":
    main()
