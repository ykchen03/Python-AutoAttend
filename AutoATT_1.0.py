from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import configparser
import tkinter.ttk as ttk
from tkinter import *
from tkinter import messagebox
import tkinter.font as font
from bs4 import BeautifulSoup
from urllib.parse import urlparse, parse_qs
import logging
from threading import Thread

def loop_moodle():
    message.config(text="Moodle自動點名已啟動 待命中...")
    while True:
        if driver.find_elements(By.XPATH,"//a[contains(@href,'sessid')]"):
            driver.get(driver.find_element(By.XPATH, "//a[contains(@href,'sessid')]").get_attribute('href'))
            logging.info(f"CHUMoodle {class_selected.get()} 點名完成")
            message.config(text="點名完成 3秒後自動關閉")
            time.sleep(3)
            driver.quit()
            root.destroy()
            break
     
        time.sleep(config.getint('Config','sleep'))
        driver.refresh()

def start_moodle():
    class_menu.config(state='disable')
    start_button.configure(state='disable')
    driver.get(class_dic[class_selected.get()])
    root.update()
    #<a class="btn btn-primary" href="https://moodle.chu.edu.tw/mod/attendance/attendance.php?sessid=1519146&amp;sesskey=izRvVSgyWw">點名簽到</a>
    Thread(target=loop_moodle).start()

def loop_irs():
    message.config(text="Zuvio IRS自動點名已啟動 待命中...")
    while True:
        if driver.find_elements(By.XPATH,"//div[@class='text' and text()='簽到開放中']"):#目前未開放簽到 #簽到開放中
            driver.find_element(By.ID,"submit-make-rollcall").click()
            message.config(text="點名完成 3秒後自動關閉")
            logging.info(f"Zuvio IRS {class_selected.get()} 點名完成")
            time.sleep(3)
            driver.quit()
            root.destroy()
            break

        time.sleep(config.getint('Config','sleep'))
        driver.execute_script("location.reload()")

def start_irs():
    class_menu.config(state='disable')
    start_button.configure(state='disable')
    driver.execute_script(class_dic[class_selected.get()])
    root.update()
    #<div id="submit-make-rollcall" class="i-r-f-b-make-rollcall-button" onclick="makeRollcall(998257)">我到了</div>
    Thread(target=loop_irs).start()

def login_irs():
    driver.get("https://moodle.chu.edu.tw/chu/irs/")
    driver.find_element(By.ID,"txtAccount").send_keys(config.get('Config', 'studentNumber'))
    driver.find_element(By.ID,"txtPwd").send_keys(config.get('Config', 'password'))
    driver.find_element(By.CSS_SELECTOR,'[style="width:178px; height:50px;"]').click()
    time.sleep(5)
    if(driver.current_url!="https://irs.zuvio.com.tw/student5/irs/index"):
        messagebox.showerror("Error", "帳號或密碼錯誤")
        root.update()
        root.destroy()
        driver.quit()
        return

    soup = BeautifulSoup(driver.page_source,'lxml')
    all_class = soup.find_all('div',{"class":"i-m-p-c-a-c-l-c-b-t-course-name"})
    menu = class_menu['menu']
    menu.delete(0,'end')
    class_selected.set("")
    for i in all_class:
        class_dic[i.text]=f"irs_currentRollcall('{i['data-course-id']}')"
        menu.add_command(label=i.text, command=lambda value=i.text: class_selected.set(value))

    class_selected.set("請選擇課程")
    start_button.configure(state='enable',text='啟動',command=start_irs)

def login_moodle():
    driver.get('https://elearn.chu.edu.tw/')
    driver.find_element(By.ID,"txtAccount").send_keys(config.get('Config', 'studentNumber'))
    driver.find_element(By.ID,"txtPwd").send_keys(config.get('Config', 'password'))
    driver.find_element(By.CSS_SELECTOR,'[style="width:178px; height:50px;"]').click()
    time.sleep(5)
    if(driver.current_url!="https://moodle.chu.edu.tw/my/"):
        messagebox.showerror("Error", "帳號或密碼錯誤")
        root.update()
        root.destroy()
        driver.quit()
        return

    soup = BeautifulSoup(driver.page_source,'lxml')
    all_class = soup.find('div', {'class': 'dropdown-menu', 'id': lambda x: x and x.endswith('8') and x.startswith('drop-down-menu-')}).find_all('a', {'class': 'dropdown-item', 'role': 'menuitem'})
    menu = class_menu['menu']
    menu.delete(0,'end')
    class_selected.set("")
    for i in all_class:
        class_dic[i.text]="https://moodle.chu.edu.tw/local/chucourseview/attendance.php?id="+parse_qs(urlparse(i['href']).query).get('id', [None])[0]
        menu.add_command(label=i.text, command=lambda value=i.text: class_selected.set(value))

    class_selected.set("請選擇課程")
    start_button.configure(state='enable',text='啟動',command=start_moodle)

def login_trigger():
    config.set('Config', 'studentNumber', stu_num_input_area.get())
    config.set('Config', 'password', stu_password_entry_area.get())
    file = open('config.ini','w',encoding='utf-8')
    config.write(file)
    file.close()
    
    stu_num_input_area.config(state='readonly')
    stu_password_entry_area.config(state='readonly')
    platform_menu.config(state='disable')
    start_button.configure(state='disable')
    debug_box.configure(state='disabled')
    message.config(text="登入中...")
    root.update()

    chrome_option = Options()
    if(debug_value.get()==0):
        chrome_option.add_argument("--headless")

    global driver
    driver = webdriver.Chrome(options=chrome_option)
    if(platform_selected.get()=="CHUMoodle"):
        login_moodle()
    else:
        login_irs()

    message.config(text="登入中成功!")

config = configparser.ConfigParser()
config.read('config.ini',encoding='utf-8')
logging.basicConfig(filename='app.log',filemode='w',level=logging.INFO,format='%(asctime)s - %(levelname)s - %(message)s',encoding='utf-8')
class_dic = {}
root = Tk()  
root.geometry("450x300") 
default_font = font.Font(family="Microsoft JhengHei")
default_font.configure(size=12)
root.option_add("*Font", default_font)
root.title("Moodle IRS 無人自動點名")

platform_label = Label(root,text="平台")
platform_label.place(x = 80,y = 20)

stu_num = Label(root,text = "學號")
stu_num.place(x = 80,y = 60) 
   
stu_password = Label(root,text = "密碼")
stu_password.place(x = 80,y = 100)

class_label = Label(root,text = "課程")
class_label.place(x = 80,y = 140) 
   
stu_num_input_area = Entry(root,width = 15)
stu_num_input_area.place(x = 140,y = 60)
stu_num_input_area.insert(0,f"{config.get('Config','studentNumber')}")
   
stu_password_entry_area = Entry(root,width = 15,show="●")
stu_password_entry_area.place(x = 140,y = 100)
stu_password_entry_area.insert(0,f"{config.get('Config','password')}")

custom_style = ttk.Style()
custom_style.configure('Custom.TMenubutton', font=("Microsoft JhengHei", 12))
custom_style.configure('Custom.TButton', font=("Microsoft JhengHei", 12))

platform_selected = StringVar()
platform_selected.set("CHUMoodle")
platform_menu = ttk.OptionMenu(root,platform_selected,platform_selected.get(),*["CHUMoodle","Zuvio IRS"],style='Custom.TMenubutton')
platform_menu["menu"].configure(tearoff=0)
platform_menu.place(x = 140,y = 20)

debug_value = IntVar()
debug_box = Checkbutton(root,text="Debug",variable=debug_value)
debug_box.place(x = 280,y = 20)

class_selected = StringVar(root)
class_selected.set("登入後選課程")
class_menu = ttk.OptionMenu(root,class_selected,class_selected.get(),"登入後選課程",style='Custom.TMenubutton')
class_menu["menu"].configure(tearoff=0)
class_menu.place(x = 140,y = 140)
     
start_button = ttk.Button(root,text = "登入",width=15,command=login_trigger,style='Custom.TButton')
start_button.place(x = 80,y = 170)

message = Label(root,text="",foreground="green")
message.place(x=80,y=200)

root.mainloop()
driver.quit()
