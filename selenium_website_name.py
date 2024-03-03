from selenium import webdriver

driver = webdriver.Chrome()
driver.get('./example.html')

title = driver.title
print("Title of the website:", title)

driver.quit()
