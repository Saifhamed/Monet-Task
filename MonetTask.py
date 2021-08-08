#Selenium Webdriver wird implementiert
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import time

#Benutzereingabe
userInput = input("Bitte Suchbegriff eingeben ")

#Suche nach dem "chromedriver" Pfad
browser = webdriver.Chrome(r'C:\Users\PC\Downloads\chromedriver_win32\chromedriver')
browser.implicitly_wait(1)

#www.Google.de öffnen
browser.get("https://google.de")

#Cookies automatisch akzeptieren
browser.find_element_by_id("L2AGLb").click()
time.sleep(1)

#Gibt die Suchleiste von "Google" zurück
search_box = browser.find_element_by_name('q')

#Suchbegriff des Users wird verarbeitet
search_box.send_keys(userInput)
search_box.submit()
time.sleep(1)

#Rückgabe der Website und des URL-Codes
results = browser.find_elements_by_css_selector('div.g')
link = results[0].find_element_by_tag_name("a")
href = link.get_attribute("href")
browser.get(href)

#URL-Code
get_title = browser.title

#Ausgabe URL-Code
print(get_title)
print(href)

#Browser schließen
browser.quit()
