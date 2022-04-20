# import selenium để crawl dữ liệu
from fileinput import filename
from lib2to3.pgen2 import driver
from random import randint, random
from selenium import webdriver
import datetime     # datetime dùng để lấy thời gian tự động crawl
import os, time     # os dùng để nối path, time.sleep()



if __name__ == "__main__":
    data_save_file_csv = []     # Biến chứa data lưu vào file
    url_file_driver = os.path.join('etc','chromedriver.exe')    # Nối path đến etc để lấy chromedrvier
    driver = webdriver.Chrome(executable_path=url_file_driver)
    driver.get("https://covid19.gov.vn/")
    # Di chuyển đến chỗ cần crawl dữ liệu
    driver.switch_to.frame(1)   # Frame được đánh theo thứ tự 0 => frame cần crawl là 1
    # Dùng Xpath
    target = driver.find_elements_by_xpath("/html/body/div[2]/div[1]/div")
    # Data lấy về dạng list hoặc string
    for data in target:     # Vì là list nên dùng for để filter
        cities = data.find_elements_by_class_name("city")
        totals = data.find_elements_by_class_name("total")
        daynows = data.find_elements_by_class_name("daynow")
        dies = data.find_elements_by_class_name("die")
    
    list_cities = [city.text for city in cities]
    list_totals = [total.text for total in totals]
    list_daynows = [daynow.text for daynow in daynows]
    list_dies = [die.text for die in dies]
    # Đã có data, giờ thì cần lưu vào 1 file

    for i in range(len(list_cities)):
        row = "{},{},{},{}.".format(list_cities[i],list_totals[i],list_daynows[i],list_dies[i])
        data_save_file_csv.append(row)

    # Tạo ngày giờ lấy file 1 cách tự động, chỉ cần mở lên là chạy
    today = (datetime.datetime.now()).strftime("%Y%m%d")
    filename = f"Covid_Web_{today}.csv"

    # w+ là ghi đè lên file cũ luôn
    with open(os.path.join("data",filename), 'w+', encoding="UTF-8") as f:
        f.writelines(data_save_file_csv)
    #time.sleep(randint(4,8))    # Dừng chương trình random 4s -> 8s để máy ko nhận ra mình auto
    driver.close()  # Đóng driver để khỏi tốn tài nguyên