from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

navegador = webdriver.Firefox()

navegador.get("https://suportesindico.com.br")
navegador.maximize_window()
navegador.find_element()