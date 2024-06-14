from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time 

#salva o script de comunicação entre o código em Python e o navegador em uma variavel 
chrome_driver_path = "chromedriver.exe"

#abre o script
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)

#abre o site do jogo cookiecliker
driver.get("https://orteil.dashnet.org/cookieclicker/")

#pega o id do cookie
coockie_id = "bigCookie"

#espera carregamento da escolha de linguagem
WebDriverWait(driver,5).until(
   EC.presence_of_element_located((By.ID,"langSelect-PT-BR"))
)
#click na linguem desejada
botao = driver.find_element(By.ID,"langSelect-PT-BR")
botao.click()

#espera aparecer o cookie
WebDriverWait(driver,10).until(
   EC.presence_of_element_located((By.ID,coockie_id))
)
#salva o local do cookie em uma variavel 
cookie = driver.find_element(By.ID,coockie_id)
cookie_1 = "cookies"
prod_id = "productPrice0"

#esse while faz o click e salve a quantidade de cookies, esse while é infinito 
while True:
   cookie.click()
   cookies_count = driver.find_element(By.ID,cookie_1).text.split(" ")[0]
   cookies_count = int(cookies_count.replace(",",""))
   print(cookies_count)
   
