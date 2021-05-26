from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
browser  = webdriver.Chrome(ChromeDriverManager().install())

#REPLACE LINK BELOW WITH QUILL LINK ANONYMOUS!
browser.get('')
time.sleep(3)


browser.find_element_by_xpath('//*[@id="main-content"]/div/section/div/section/div/div/button').click()
browser.find_element_by_xpath('//*[@id="main-content"]/div/section/div/section/div/button').click()
# =============================
dict={1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[]}
print(dict)
for y in range(8):
    for i in range(5):
        x = browser.find_element_by_xpath('//*[@id="main-content"]/div/section/div[2]/div/div/div[2]/div[3]/div/div/div')
        keys=1
        time.sleep(1)
        x.send_keys(keys)
        keys+=1
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="main-content"]/div/section/div[2]/div/div/div[2]/div[4]/button').click()
    browser.find_element_by_xpath('//*[@id="main-content"]/div/section/div[2]/div/div/div[2]/div[4]/button').click()
    time.sleep(1)
    dict_num=1
    browser.find_element_by_xpath('//*[@id="main-content"]/div/section/div[2]/div/section/div/div[3]/button[1]').click()
    answer_text = browser.find_element_by_xpath('//*[@id="main-content"]/div/section/div[2]/div/div/div[2]/div[2]/div[2]/ul/li[1]/div[2]')
    texxt=(answer_text.text)
    dict[dict_num].append(texxt)
    dict_num=dict_num+1
    time.sleep(1)
    xx=1
    browser.find_element_by_xpath('//*[@id="main-content"]/div/section/div[2]/div/div/div[2]/div[4]/button').click()
    print(dict[xx][xx-1])
    xx+=1
print(dict[1][1])
time.sleep(2)

#REPLACE LINK BELOW WITH STUDENT LINK
browser.get('')


time.sleep(2)
browser.find_element_by_xpath('//*[@id="main-content"]/div/section/div/section/div/div/button').click()
time.sleep(1)
browser.find_element_by_xpath('//*[@id="main-content"]/div/section/div/section/div/button').click()


xx = browser.find_element_by_xpath('//*[@id="main-content"]/div/section/div[2]/div/div/div[2]/div[3]/div/div/div')

key1=(dict[1][0])
xx.send_keys(key1)
time.sleep(1)
browser.find_element_by_xpath('//*[@id="main-content"]/div/section/div[2]/div/div/div[2]/div[4]/button').click()
time.sleep(1)
browser.find_element_by_xpath('//*[@id="main-content"]/div/section/div[2]/div/div/div[2]/div[4]/button').click()
time.sleep(1)
browser.find_element_by_xpath('//*[@id="main-content"]/div/section/div[2]/div/div/div[2]/div[4]/button').click()
time.sleep(3)




x = browser.find_element_by_xpath('//*[@id="main-content"]/div/section/div[2]/div/div/div[2]/div[3]/div/div/div')

key1=(dict[1][1])
x.send_keys(key1)
time.sleep(1)
browser.find_element_by_xpath('//*[@id="main-content"]/div/section/div[2]/div/div/div[2]/div[4]/button').click()
time.sleep(1)
browser.find_element_by_xpath('//*[@id="main-content"]/div/section/div[2]/div/div/div[2]/div[4]/button').click()
time.sleep(1)
browser.find_element_by_xpath('//*[@id="main-content"]/div/section/div[2]/div/div/div[2]/div[4]/button').click()
time.sleep(3)

e=browser.find_element_by_xpath('//*[@id="main-content"]/div/section/div[2]/div/div/div[2]/div[3]/div/div/div')
key1=(dict[1][2])
e.send_keys(key1)
time.sleep(1)
browser.find_element_by_xpath('//*[@id="main-content"]/div/section/div[2]/div/div/div[2]/div[4]/button').click()
time.sleep(1)
browser.find_element_by_xpath('//*[@id="main-content"]/div/section/div[2]/div/div/div[2]/div[4]/button').click()
time.sleep(1)
browser.find_element_by_xpath('//*[@id="main-content"]/div/section/div[2]/div/div/div[2]/div[4]/button').click()

time.sleep(3)

a=browser.find_element_by_xpath('//*[@id="main-content"]/div/section/div[2]/div/div/div[2]/div[3]/div/div/div')

key1=(dict[1][3])
a.send_keys(key1)
time.sleep(1)
browser.find_element_by_xpath('//*[@id="main-content"]/div/section/div[2]/div/div/div[2]/div[4]/button').click()
time.sleep(1)
browser.find_element_by_xpath('//*[@id="main-content"]/div/section/div[2]/div/div/div[2]/div[4]/button').click()
time.sleep(1)
browser.find_element_by_xpath('//*[@id="main-content"]/div/section/div[2]/div/div/div[2]/div[4]/button').click()

time.sleep(3)

b=browser.find_element_by_xpath('//*[@id="main-content"]/div/section/div[2]/div/div/div[2]/div[3]/div/div/div')

key1=(dict[1][4])
b.send_keys(key1)
time.sleep(1)
browser.find_element_by_xpath('//*[@id="main-content"]/div/section/div[2]/div/div/div[2]/div[4]/button').click()
time.sleep(1)
browser.find_element_by_xpath('//*[@id="main-content"]/div/section/div[2]/div/div/div[2]/div[4]/button').click()
browser.find_element_by_xpath('//*[@id="main-content"]/div/section/div[2]/div/div/div[2]/div[4]/button').click()
time.sleep(3)

g=browser.find_element_by_xpath('//*[@id="main-content"]/div/section/div[2]/div/div/div[2]/div[3]/div/div/div')

key1=(dict[1][5])
g.send_keys(key1)
time.sleep(1)
browser.find_element_by_xpath('//*[@id="main-content"]/div/section/div[2]/div/div/div[2]/div[4]/button').click()
time.sleep(1)
browser.find_element_by_xpath('//*[@id="main-content"]/div/section/div[2]/div/div/div[2]/div[4]/button').click()
time.sleep(1)
browser.find_element_by_xpath('//*[@id="main-content"]/div/section/div[2]/div/div/div[2]/div[4]/button').click()
time.sleep(3)

mm=browser.find_element_by_xpath('//*[@id="main-content"]/div/section/div[2]/div/div/div[2]/div[3]/div/div/div')

key1=(dict[1][6])
mm.send_keys(key1)
time.sleep(1)
browser.find_element_by_xpath('//*[@id="main-content"]/div/section/div[2]/div/div/div[2]/div[4]/button').click()
time.sleep(1)
browser.find_element_by_xpath('//*[@id="main-content"]/div/section/div[2]/div/div/div[2]/div[4]/button').click()
time.sleep(1)
browser.find_element_by_xpath('//*[@id="main-content"]/div/section/div[2]/div/div/div[2]/div[4]/button').click()
time.sleep(3)


mmx=browser.find_element_by_xpath('//*[@id="main-content"]/div/section/div[2]/div/div/div[2]/div[3]/div/div/div')

key1=(dict[1][7])
mmx.send_keys(key1)
time.sleep(1)
browser.find_element_by_xpath('//*[@id="main-content"]/div/section/div[2]/div/div/div[2]/div[4]/button').click()
time.sleep(1)
browser.find_element_by_xpath('//*[@id="main-content"]/div/section/div[2]/div/div/div[2]/div[4]/button').click()
time.sleep(1)
browser.find_element_by_xpath('//*[@id="main-content"]/div/section/div[2]/div/div/div[2]/div[4]/button').click()
time.sleep(3)




