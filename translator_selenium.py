from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

class SeleniumTranslator:
    site = "https://translate.google.com/"
    driverPath = "drivers/chromedriver.exe"
    driver = None

    def __init__(self):
        self.driver = webdriver.Chrome(self.driverPath)
        self.driver.get(self.site)

    def setLang(self,dest,src="auto"):
        time.sleep(2)
        self.driver.get(self.site + f"?hl=tr&tab=TT&sl={src}&tl={dest}&op=translate")

    def translate(self,sentence):
        wait = WebDriverWait(self.driver,5)

        textIn = self.driver.find_element_by_class_name("er8xn")
        textIn.send_keys(sentence)
        time.sleep(2)
        element = wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "J0lOec"))
        )
        res = element.text
        textIn.clear()
        return res

    def exit(self):
        self.driver.quit()