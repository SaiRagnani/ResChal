from selenium import webdriver
from selenium.webdriver import ActionChains


class sample:
    driver= webdriver.Chrome(executable_path="D:\\WebDrivers\\chromedriver.exe")
    driver.get("file:///C:/Users/Nani/Desktop/index.html")
    driver.implicitly_wait(5)
    driver.maximize_window()
    source = driver.find_element_by_xpath("//*[@id='drag1']")
    target = driver.find_element_by_id("div1")
    actions=ActionChains(driver)
    #actions.drag_and_drop(source,target).perform()
    actions.click_and_hold(source).move_to_element(target).pause(2).move_by_offset(20,20).release().perform()

