import pandas 
from time import sleep

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager

excel_data = pandas.read_excel("data\database.xlsx", sheet_name='database')

count = 1

driver = webdriver.Firefox()

driver.get("https://web.whatsapp.com" )
input("Scan QR Code Also Press Enter")
for colum in excel_data['Number'].tolist() :
    url = "https://web.whatsapp.com/send?phone=" + str(excel_data["Number"][count]) + '&text=' + excel_data['Pesan'][0]
    sent = False
    driver.get(url)
    xpath_val = '/html/body/div[1]/div/div/div[2]/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]'
    wbw = WebDriverWait(driver, 10)
    wbw.until(EC.presence_of_element_located((By.XPATH, xpath_val))).send_keys(Keys.ENTER)
    sent = True
    sleep(5)
    print("Pesan Terkirim :" + str(excel_data["Number"][count]))
    count = count + 1
    
        
        

driver.quit()
