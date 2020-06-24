from selenium import webdriver
import time
import selenium


chromedriver = r"C:\Users\Arjun\Desktop\chromedriver.exe"

driver = webdriver.Chrome(chromedriver)
driver.get("https://www.medicines.org.uk/emc/browse-companies")
driver.find_element_by_xpath("/html/body/section[2]/div[2]/div[2]/div/main/div[1]/ul/li[1]/a").click()
driver.find_elements_by_class_name("row")
#driver.save_screenshot("C:\Screenshot\First_Company.png")#
Company_Details = driver.find_element_by_class_name("gfdCompanyDetailsCol").text
Contact_Details = driver.find_element_by_class_name("col-md-4").text

Company_information = Company_Details + Contact_Details

print(Company_information
