
#Run this file after you can run "amazon.py"
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
from selenium import webdriver
driver = webdriver.Firefox()
driver.set_window_size(900,700)
driver.get('https://www.amazon.com/gp/sign-in.html')
driver.save_screenshot('screen.png')


inputElement = driver.find_element_by_id("ap_email")
inputElement.send_keys("YOUR EMAIL")
inputElement = driver.find_element_by_id("ap_password")
inputElement.send_keys("YOUR PASSWORD")
inputElement.send_keys(Keys.ENTER)
#driver.find_element_by_id("signInSubmit").click()

_file = open("AmazonName.txt",'a')
_file2 = open("Errorlist.txt",'a')


pro = []
with open("profiles2.txt") as f:
    for a in f:
       pro.append(a)

print 'Rank' + '        ' + 'Name' + '      ' +  'Email Address' + '        ' + 'Helpful Review'
for t in pro:
        i = 1
        while(i >  0):
             time.sleep(1)
             i = i - 1
        driver.get(t)
        try:
            driver.find_element_by_link_text('Send an Email').click()
        except:
            pass
        time.sleep(5)
        page = BeautifulSoup(driver.page_source)
        a = page.find_all('h1')
        name = a[0].text
        b = page.find_all('span',{"class":"a-size-large a-text-bold"})
        rank = (b[0].text)[1:]
        review = b[1].text
        data = []
        try:
            e = page.find_all('a',{"class":'a-link-normal pr-email'})
            email = e[0].text
            data.append(rank)
            data.append(name)
            data.append(email)
            data.append(review)
            print data[0] + '       ' + data[1] + '         '+ data[2] + '          '+ data[3]
            _file.write(t)
            _file.write('\n')
            _file.write(str(data))
            _file.write('\n')
        except:
            pass

