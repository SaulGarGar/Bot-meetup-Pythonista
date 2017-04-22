from selenium import webdriver
import time

def meetup():
	driver = webdriver.Chrome()
	driver.get('https://es.wikipedia.org/wiki/Wikipedia:Portada')
	barra = driver.find_element_by_name('search')
	barra.send_keys('gatitos') 
	
	boton = driver.find_element_by_class_name('searchButton')
	boton.click()

	time.sleep(5)


meetup()