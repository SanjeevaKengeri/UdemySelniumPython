from selenium import webdriver
from selenium.webdriver import ActionChains


class MouseActions():
		
		def test_hover():
			ff_driver_path = 'C:\\Users\\Administrator\\Downloads\\geckodriver-v0.22.0-win64\\geckodriver.exe'
			driver = webdriver.Firefox(executable_path = ff_driver_path)
			driver.get("https://w3schools.com")
			driver.implicitly_wait(3)
			
			
			
			