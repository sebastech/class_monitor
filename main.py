import re
import smtplib
import time
from email.mime.text import MIMEText
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0

driver = webdriver.Chrome("C:\\watcher\\chromedriver.exe")
driver.get("https://smccis.smc.edu/smcweb/f?p=118:1")
driver.implicitly_wait(10)
select = Select(driver.find_element_by_id('P1_SEMNAME'))
select.select_by_visible_text('Summer 2018')
time.sleep(5)
driver.implicitly_wait(100)
select = Select(driver.find_element_by_id('P1_SUBJECTS'))
select.select_by_visible_text('Computer Science')
driver.implicitly_wait(100)
link = driver.find_element_by_id('B7997204475679174987')
link.click()
time.sleep(5)
try:
    # we have to wait for the page to refresh, the last thing that seems to be updated is the title
    WebDriverWait(driver, 10).until(EC.title_contains("Online Class List"))

    # You should see "cheese! - Google Search"
    print driver.title
    val = driver.page_source
    val = val.encode('ascii', 'ignore').decode('ascii')
    #print val
    with open("out.txt", "w") as text_file:
        text_file.write(val)

finally:
    driver.quit()

#isclosed = re.search(r'Status.*CLOSED', val)
isopen = re.search(r'C Programming.*123[4|5].*OPEN', val)
#isopen = re.search(r'1697.*OPEN', val)
#print isclosed
if isopen:
    s = smtplib.SMTP("smtp.gmail.com", 587)
    s.ehlo()
    s.starttls()
    s.login( 'randomaccount@gmail.com', '****' )
    s.sendmail('randomaccount@gmail.com', 'randomaccount@gmail.com', 'sup' )
    s.quit()
    print "open"
else:
    print "closed"
#driver.close()
