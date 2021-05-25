from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import selenium

class HomePage:
    frame=(By.CSS_SELECTOR,"div#test-1-div")
    modal=(By.CSS_SELECTOR,"button[class*=btn-lg]")
    name=(By.ID,"name")
    city=(By.ID,"city")
    namevalue=(By.ID,"nameVal")
    cityvalue=(By.ID,"cityVal")
    submit=(By.ID,"enter")
    close = (By.CSS_SELECTOR, "button[class*=btn-default]")

    clickme=(By.CSS_SELECTOR,"button[class*=dropdown-toggle]")
    allsubs=(By.XPATH,"//div[@id='test-2-div']/div/div/ul/li")
    filterTB=(By.ID,"myInput")

    searchTB=(By.ID,"searchMe")
    allrows=(By.XPATH,"//div[@id='test-3-div']/div/table/tbody/tr")
    namerows=(By.XPATH,"//td[text() = 'USA']")

    source =("drag1")
    target =("div1")
    frame1=(By.ID,"test-4-div")


    def __init__(self, driver):
        self.driver = driver


    #testone
    def getframe(self):
        self.driver.find_element(*HomePage.frame)

    def modalclick(self):
        self.driver.find_element(*HomePage.modal).click()

    def entername(self,name):
        self.driver.find_element(*HomePage.name).send_keys(name)

    def entercity(self,city):
        self.driver.find_element(*HomePage.city).send_keys(city)

    def save(self):
        self.driver.find_element(*HomePage.submit).click()

    def closebutton(self):
        return self.driver.find_element(*HomePage.close).click()

    def getnamevalue(self):
        return self.driver.find_element(*HomePage.namevalue).text

    def getcityvalue(self):
        return self.driver.find_element(*HomePage.cityvalue).text

    # testtwo
    def clickmebutton(self):
        self.driver.find_element(*HomePage.clickme).click()

    def enterfiltertext(self,Sub):
        alllist=[]
        self.driver.find_element(*HomePage.filterTB).send_keys(Sub)
        lists = self.driver.find_elements(*HomePage.allsubs)
        print(lists)
        for list in lists:
            if Sub in list.text:
                alllist.append(list.text)
        print(alllist)
        return alllist

    def filterclear(self):
        self.driver.find_element(*HomePage.filterTB).clear()

    # testtwhree
    def entersearchtext(self,value):
        self.driver.find_element(*HomePage.searchTB).send_keys(value)

    def getallrows(self):
        return self.driver.find_elements(*HomePage.allrows)

    def getnamerows(self):
        return self.driver.find_elements(*HomePage.namerows)

    def searchclear(self):
        self.driver.find_element(*HomePage.searchTB).clear()

    # testfour
    def draganddrop(self):
        self.driver.find_element(*HomePage.frame1)
        actions = ActionChains(self.driver)
        source = self.driver.find_element_by_id(self.source)
        target = self.driver.find_element_by_id(self.target)
        actions.click_and_hold(source).move_to_element(target).pause(2).move_by_offset(20,20).release().perform()