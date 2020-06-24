from selenium import webdriver
import time

class AutoMate():

    chromedriver = r"C:\Users\Arjun\Desktop\chromedriver.exe"

    def test1(self,driver):

     self.driver = webdriver.Chrome(chromedriver)
     self.driver.get("https://www.medicines.org.uk/emc/browse-companies")
     self.driver.find_element_by_xpath("/html/body/section[2]/div[2]/div[2]/div/main/div[1]/ul/li[1]/a").click()
     self.driver.find_elements_by_class_name("row")


First_Test=AutoMate()

#driver.save_screenshot("C:\Screenshot\First_Company.png")#
''''
    def CompanyDetails():

     Company_Details = driver.find_element_by_class_name("gfdCompanyDetailsCol").text
     Contact_Details = driver.find_element_by_class_name("col-md-4").text

     Company_information = Company_Details + Contact_Details
