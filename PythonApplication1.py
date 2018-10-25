import os
import selenium.webdriver.support.ui as ui
# Подключаем selenium (сперва установить через pip install selenium)
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from time import sleep  
includes_path = "C:/Users/BRAXXMAN/source/repos/includes/"
os.environ["webdriver.chrome.driver"] = includes_path+"chromedriver.exe"

chrome_options = Options()
chrome_options.add_extension(includes_path+'Ghostery-–-Privacy-Ad-Blocker_v8.2.4.crx')
# Перед инициализацией драйвера браузера удалим куки-файл, если он существует
cookiesfile = "./DIRECTORYTOPROFILEFOLDERWITHINAPPDATA\Default\Cookies"
if os.path.isfile(cookiesfile):
    os.remove(cookiesfile)
else:    ## Show an error ##
    print("Error: %s cookiesfile not found" % cookiesfile)
# Сохраняет настройки расширений и браузера
chrome_options.add_argument("user-data-dir=DIRECTORYTOPROFILEFOLDERWITHINAPPDATA")
driver = webdriver.Chrome(executable_path=includes_path+'chromedriver.exe', chrome_options=chrome_options)
#driver=webdriver.Firefox()

# Переходим на страницу, на которой нужно что-то сделать
driver.get('https://vk.com/')

# Получаем указатель на поле ввода текста в форме постинга
textarea=driver.find_element_by_css_selector('#index_email')
# Печатаем в поле ввода какой-либо текст
textarea.send_keys('shustov_egor@mail.ru')

# Получаем указатель на поле ввода пароля
textarea=driver.find_element_by_css_selector('#index_pass')
# Печатаем в поле ввода пароль
textarea.send_keys('WrongPassword')

#Получаем указатель на кнопку "Войти"
submit=driver.find_element_by_css_selector('#index_login_button')
submit.click()
#Ждём пока загрузится кнопка "диалоги"
messages_button = ui.WebDriverWait(driver, 15).until(lambda driver: driver.find_element_by_id('l_msg'))
#Нажимаем эту кнопку через Ctrl (в новой вкладке)
ActionChains(driver) \
    .key_down(Keys.CONTROL) \
    .click(messages_button) \
    .key_up(Keys.CONTROL) \
    .perform()
#driver.close()
#sleep(10)