import os
from time import sleep

import chromedriver_binary
import pandas
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

height=1000
px=2000
def scroll():
    global height, px
    while height<px:
        driver.execute_script('window.scrollTo(0,{});'.format(height))
        height += 100

        sleep(1)
    
    box = driver.find_element_by_class_name('sw-MoreButton__button')
    box.click()
    px += 3000

login_url = 'https://login.yahoo.co.jp/'
img_url = 'https://search.yahoo.co.jp/image'
serch_config ='https://search.yahoo.co.jp/search/preferences?pref_done=https%3A%2F%2Fsearch.yahoo.co.jp%2Fimage'

IMAGE_DIR = './images/'

x = 1

print('セーフティーサーチを「低」にする。\n0:いいえ\n1:はい\n')
choice = int(input())
while not 0<=x<=1:
    print('正しく入力してください。\n')
    print('セーフティーサーチを「低」にする。\n0:いいえ\n1:はい\n')
    choice = int(input())


options=Options()
options.add_argument('--incognito')
#options.add_argument('--headless')

driver = webdriver.Chrome(options=options)
driver.maximize_window()

if choice == 1:
    print('IDを入力してください。\n')
    ID = str(input())
    print('パスワードを入力してください。\n')
    PATH = str(input())

    driver.get(login_url)

    sleep(3)

    box = driver.find_element_by_id('username')
    box.send_keys(ID)
    box = driver.find_element_by_id('btnNext')
    box.click()

    sleep(1)

    box = driver.find_element_by_id('passwd')
    box.send_keys(PATH)
    box = driver.find_element_by_id('btnSubmit')
    box.click()

    sleep(1)

    driver.get(serch_config)

    sleep(3)

    box = driver.find_element_by_id('WOmm3')
    box.click()
    box.send_keys(Keys.ENTER)

while x:
    driver.get(img_url)

    sleep(2)

    print('検索ワードを入力してください。\n')
    serch_word = input()

    box = driver.find_element_by_tag_name('input')
    box.clear()
    box.send_keys(serch_word)
    box.submit()

    sleep(1)

    print('取得枚数を入力してください。\n')
    n = int(input())
    while n<=0:
        print('正しく入力してください。\n')
        print('取得枚数を入力してください。\n')
        n = int(input())

    scroll()

    img = []
    while len(img) < n:
        img = driver.find_elements_by_tag_name('img')
        scroll()
    
    
    img_list = []
    for i in range(n):
        img_list.append(img[i].get_attribute('src'))

    if not os.path.isdir(IMAGE_DIR):
        os.makedirs(IMAGE_DIR)
        print(f'created {IMAGE_DIR}.')

    for i, image_url in enumerate(img_list):
        image = requests.get(image_url)
        with open(IMAGE_DIR + str(i+1) + '.jpg', 'wb') as f:
            f.write(image.content)
        sleep(1)
    
    print('完了しました。\n')
    print('0:終了\n1:再実行\n')
    x = int(input())
    while not 0<=x<=1:
        print('正しく入力してください。\n')
        print('0:終了\n1:再実行\n')
        x = int(input())

driver.quit()
