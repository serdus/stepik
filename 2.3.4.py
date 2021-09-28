from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math
import os
try: 
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
        #нажимаем на кнопку в магическое...
    button = browser.find_element_by_css_selector("button.btn.btn-primary")
    button.click()
    #принимаем конфирм
    confirm = browser.switch_to.alert
    confirm.accept()
    #вычисляем значение
    elem1 = browser.find_element_by_id("input_value")
    fordef1 = elem1.text    
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    resux=calc(fordef1)
    #выбираем и заполняем поля
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(resux)
    button = browser.find_element_by_css_selector("button.btn.btn-primary")
    button.click()
    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
