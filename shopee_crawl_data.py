from lib2to3.pgen2 import driver
from fileinput import filename
from selenium.webdriver.common.by import By
from selenium import webdriver
import datetime
import os,time

if __name__ == "__main__":
    data_save_file_csv = []
    url_file_driver = os.path.join('etc','chromedriver.exe')
    driver = webdriver.Chrome(executable_path=url_file_driver)
    driver.get('https://shopee.vn/M%C3%A1y-%E1%BA%A2nh-M%C3%A1y-Quay-Phim-cat.11036101')
    
    target = driver.find_elements(By.XPATH, "/html/body/div[1]/div/div[3]/div/div[4]/div[2]/div/div[2]")
    for data in target:
        names = data.find_elements(By.CLASS_NAME, "ZG__4J")
        # prices = data.find_elements(By.CLASS_NAME,"zp9xm9 kNGSLn l-u0xK")
        quantities = data.find_elements(By.CLASS_NAME,"_1uq9fs")

    names_list = [name.text for name in names]
    # prices_list = [price.text for price in prices]
    quantity_list = [quantity.text for quantity in quantities]

    for i in range(len(names_list)):
        row = "{},{}\n".format(names_list[i],quantity_list[i])
        data_save_file_csv.append(row)

    today = (datetime.datetime.now()).strftime("%Y%m%d")
    filename = f"Shopee_MayAnh&QuayPhim_{today}.csv"

    with open(os.path.join("data",filename), 'w+', encoding="UTF-8") as f:
        f.writelines(data_save_file_csv)
    
    time.sleep(10)
    driver.close()

