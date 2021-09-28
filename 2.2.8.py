from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math
import os
try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
        #выбираем поле и вводим информацию
    input1 = browser.find_element_by_css_selector("div.form-group :nth-child(2)")
    input1.send_keys("Михаил")
    input2 = browser.find_element_by_css_selector("div.form-group :nth-child(4)")
    input2.send_keys("Тимошенко")
    input1 = browser.find_element_by_css_selector("div.form-group :nth-child(6)")
    input1.send_keys("pop@ruko.ru")
    #Создаем файл
    with open("test.txt","w") as file:
        content = file.write("автопитон")
    #Ищем путь и заполняем поле
    dira = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(dira,"test.txt")
    choose=browser.find_element_by_css_selector("[type=file]")
    choose.send_keys(file_path)
    button = browser.find_element_by_css_selector("button.btn.btn-primary")
    button.click()
    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
