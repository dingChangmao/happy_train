import time
import re
from selenium import webdriver
import urllib.request
"""
爬妹子图片，资源重在分享，欢迎广大基友给我分享资源！！！！
请直接告诉我地址，我就喜欢直接点！！！！！

"""
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.zhihu.com/question/29134042")

i = 0
while i < 10:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    try:
        driver.find_element_by_css_selector('button.QuestionMainAction').click()
        print("page"+str(i))
        time.sleep(1)
    except:
        break

result_raw = driver.page_source
content_list = re.findall("img src=\"(.+?)\" ", str(result_raw))
n = 0

while n<len(content_list):
    i = time.time()
    local = (r"%s.jpg" % (i))
    urllib.request.urlretrieve(content_list[n], local)
    print("编号：" + str(i))
    n = n + 1
