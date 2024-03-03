from selenium import webdriver

driver = webdriver.Chrome('path_to_chromedriver')
driver.get('./example.html')

title = driver.title
print("Title of the website:", title)

driver.quit()
