from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import random
import json
import zipfile
import os
import requests
import sys
import string
from datetime import datetime, timedelta

username = "karolelnore"
password = '123123'
print('file đang chạy là' + os.path.basename(sys.argv[0]).split('.')[0])
filechay = os.path.basename(sys.argv[0]).split('.')[0]

def getPlugin(proxy_host, proxy_port, proxy_user, proxy_pass):
    manifest_json = """
    {
        "version": "1.0.0",
        "manifest_version": 2,
        "name": "Chrome Proxy",
        "permissions": [
            "proxy",
            "tabs",
            "unlimitedStorage",
            "storage",
            "<all_urls>",
            "webRequest",
            "webRequestBlocking"
        ],
        "background": {
            "scripts": ["background.js"]
        },
        "minimum_chrome_version":"22.0.0"
    }
    """

    background_js = """
    var config = {
            mode: "fixed_servers",
            rules: {
            singleProxy: {
                scheme: "http",
                host: "%s",
                port: parseInt(%s)
            },
            bypassList: ["localhost"]
            }
        };

    chrome.proxy.settings.set({value: config, scope: "regular"}, function() {});

    function callbackFn(details) {
        return {
            authCredentials: {
                username: "%s",
                password: "%s"
            }
        };
    }

    chrome.webRequest.onAuthRequired.addListener(
                callbackFn,
                {urls: ["<all_urls>"]},
                ['blocking']
    );
    """ % (proxy_host, proxy_port, proxy_user, proxy_pass)
    pluginfile = 'proxy_auth_plugin.zip'

    with zipfile.ZipFile(pluginfile, 'w') as zp:
        zp.writestr("manifest.json", manifest_json)
        zp.writestr("background.js", background_js)
    
    return pluginfile

def telegram_bot_sendtext(bot_message):

   bot_token = '6132854382:AAG4a4L9ndMuYMiTVulYQOlGH9uklhb8B-Q'
   bot_chatID = '-1001884739111'
   send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

   response = requests.get(send_text)

   return response.json()

# driver = webdriver.Chrome('./chromedriver')
options = Options()
service = Service(executable_path=r'C:\Users\Hai\Desktop\Meteex\chromedriver-win32\chromedriver.exe')
#chromeOptions.add_argument("--headless")
# driver = webdriver.Chrome(executable_path="chromedriver.exe", chrome_options=chromeOptions)
#options.add_extension(getPlugin('38.153.139.105','9781','gcgtgfjm','xuzqwpo8yu87'))
# driver = webdriver.Chrome(executable_path="chromedriver.exe", chrome_options=chromeOptions)
#options.add_argument("--disable-extensions")





#options.add_argument("--headless=new")
# options.add_argument("--no-sandbox")
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument('--log-level=1')
options.add_argument("--disable-renderer-backgrounding");
options.add_argument("--disable-background-timer-throttling");
options.add_argument("--disable-backgrounding-occluded-windows");
options.add_argument("--disable-client-side-phishing-detection");
options.add_argument("--disable-crash-reporter");
options.add_argument("--disable-oopr-debug-crash-dump");
options.add_argument("--no-crash-upload");
options.add_argument("--disable-low-res-tiling");
options.add_argument("--incognito");

options.add_argument('--ignore-gpu-blacklist')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-gpu')
# options.add_argument('--blink-settings=imagesEnabled=false')
#options.add_argument("--start-maximized")

prefs = {'profile.default_content_setting_values': {'images': 2, 
                            'plugins': 2, 'popups': 2, 'geolocation': 2, 
                            'notifications': 2, 'auto_select_certificate': 2, 'fullscreen': 2, 
                            'mouselock': 2, 'mixed_script': 2, 'media_stream': 2, 
                            'media_stream_mic': 2, 'media_stream_camera': 2, 'protocol_handlers': 2, 
                            'ppapi_broker': 2, 'automatic_downloads': 2, 'midi_sysex': 2, 
                            'push_messaging': 2, 'ssl_cert_decisions': 2, 'metro_switch_to_desktop': 2, 
                            'protected_media_identifier': 2, 'app_banner': 2, 'site_engagement': 2, 
                            'durable_storage': 2}}
options.add_experimental_option('prefs', prefs)


options.add_argument( '--disable-blink-features=AutomationControlled' )
options.add_argument(r"--user-data-dir=D:\DULIEU" + '\\' +filechay)
#driver=webdriver.Chrome(executable_path=r'C:\Users\ACER\Desktop\meteex\chromedriver-win32\chromedriver.exe', options=options)
driver = webdriver.Chrome(executable_path=r'C:\Users\ACER\Desktop\meteex\chromedriver-win32\chromedriver.exe',options=options)
#drivers = [webdriver.Chrome(executable_path=r'C:\Development\chromedriver.exe', options=options[0]), webdriver.Chrome(executable_path=r'C:\Development\chromedriver.exe', options=options[1])]
# driver.implicitly_wait(5)
driver.set_window_size(200, 650)
 
driver.get("https://meteex.com/login")


time.sleep(6)
driver.find_element("xpath","/html/body/table/tbody/tr[2]/td[2]/div/div[1]/form/table/tbody/tr[2]/td/label/input").send_keys(username)
time.sleep(3)
driver.find_element("xpath","/html/body/table/tbody/tr[2]/td[2]/div/div[1]/form/table/tbody/tr[3]/td/label/input").send_keys(password)
dangnhap3=driver.find_element('xpath', '/html/body/table/tbody/tr[2]/td[2]/div/div[1]/form/center/button')
dangnhap3.click()
time.sleep(8)
try:
    driver.find_element('xpath', '/html/body/table/tbody/tr[2]/td[3]/div/div[1]/div[1]/div[3]/span[2]').click()
    time.sleep(3)
    driver.find_element('xpath', '/html/body/div[13]/div[2]/form/table/tbody/tr/td/button/span').click()
    time.sleep(3)
except:
    driver.get('https://meteex.com/reytbirj_new')
    time.sleep(5)
try:
    so_sao = driver.find_element('xpath', '/html/body/table/tbody/tr[2]/td[3]/div/div[1]/div[1]/div[1]/div[1]').text
    if (float(so_sao) >= 50):
        time.sleep(1)
        print('số sao có trong tài khoản là', so_sao)
        telegram_bot_sendtext(filechay+" co so sao la: " + so_sao)
        driver.find_element('xpath', '/html/body/table/tbody/tr[2]/td[3]/div/div[3]/div/div[1]/a[2]').click()
        time.sleep(3)
        driver.find_element('xpath', '/html/body/table/tbody/tr[2]/td[3]/div/div[5]/div[1]/table/tbody/tr[2]/td[4]/span').click()
        time.sleep(3)
        sell_sao3 = driver.find_element("xpath","/html/body/div[13]/div[2]/form/table[1]/tbody/tr[4]/td[2]/input").send_keys(so_sao)
        time.sleep(3)
        driver.find_element('xpath', '/html/body/div[13]/div[2]/form/table[2]/tbody/tr/td/button/span').click()
        time.sleep(3) 
except:
    driver.reload()
try: 
    click_star = driver.find_element('xpath', '/html/body/table/tbody/tr[2]/td[1]/div[1]/div/div[1]/div[2]/a[1]')
    click_star.click()
except:
        pass


time.sleep(6)


ramdomso = random.randint(600, 1800)
loi=0
print("Nhan phim ban ky de bat dau chay")
# xyz= input()
for x in range(30):
    try:
        try:
            driver.get('https://meteex.com/reytbirj_new')
            time.sleep(3)
            so_tien = driver.find_element('xpath', '/html/body/table/tbody/tr[2]/td[1]/div[1]/div/div[3]/a/span[1]/span[1]').text
            print('số tiền có trong tài khoản là', so_tien)
            if (float(so_tien) >= 10):
                telegram_bot_sendtext(filechay+": " + so_tien)
                clic_nut_tien = driver.find_element('xpath', '/html/body/table/tbody/tr[2]/td[1]/div[1]/div/div[3]/a/span[1]/span[1]')
                clic_nut_tien.click()
                time.sleep(5)

                click_payeer = driver.find_element('xpath', '/html/body/table/tbody/tr[2]/td[3]/div/div[2]/div[2]/form/center/div[2]/div[1]/div/div/div')
                click_payeer.click()
                time.sleep(5)
                print('chua sua slider duoi xuong')
                slider = driver.find_element('xpath', '/html/body/table/tbody/tr[3]/td[3]/div[2]/div[2]/form/div[2]/input')

                # Adjust the offset value according to your requirement
                offset = 50
                print('a2')
                # Move the slider to the right using ActionChains
                actions = ActionChains(driver)
                actions.click_and_hold(slider).move_by_offset(offset, 0).release().perform()
                time.sleep(5)
                print('click rút tiền nào')
                rut_tien_napo = driver.find_element('xpath', '/html/body/table/tbody/tr[3]/td[3]/div[2]/div[2]/form/center[2]/input')
                rut_tien_napo.click()
                time.sleep(5)
                telegram_bot_sendtext(filechay+": " + so_tien)

            time.sleep(2)
        except:
            pass
            print('lỗi rút tiền')
        #start click xem video
        print('xem video')
        time.sleep(3)
        try:
            print('xem video2')
            surf2=driver.find_element('xpath', '/html/body/table/tbody/tr[2]/td[1]/div[2]/div/div/center/div[1]/a[5]')
            surf2.click()
        except:
            print('xem video1')
            surf1=driver.find_element('xpath', '/html/body/table/tbody/tr[2]/td[1]/div[2]/div/div/center/span[1]')
            surf1.click()
            surf2=driver.find_element('xpath', '/html/body/table/tbody/tr[2]/td[1]/div[2]/div/div/center/div[1]/a[5]')
            surf2.click()
        
        # clickVideo = driver.find_element('xpath', '/html/body/table/tbody/tr[3]/td[1]/div[2]/div/div/center/div[1]/a[5]')
        # clickVideo.click()
        print('xem video12')
        # try:
            # print('aaaaaaaaaaaaaaaaaaaaaaaaaaa')
            # time.sleep(5)
            # kkkkkkkk = driver.find_element('xpath', '/html/body/table/tbody/tr[2]/td[3]/div/div[2]/div[5]/table/tbody/tr/td[2]/div[1]/div/span[1]').text
            # print('kkkkk', kkkkkkkk)
            # if kkkkkkkk == 'Feeling Good Mix - Emma Péters, Carla Morrison':
                # xoavideoloi = driver.find_element('xpath', '/html/body/table/tbody/tr[2]/td[3]/div/div[2]/div[4]/table/tbody/tr/td[3]/div/a')
                # xoavideoloi.click()
            # print("xoa video loi khong xem duoc")
            # # xoavideoloi = driver.find_element('xpath', '/html/body/table/tbody/tr[3]/td[3]/div[2]/div[3]/table/tbody/tr/td[3]/div/a')
            # # xoavideoloi.click()
        # except:
            # pass
        try:
            time.sleep(5)
            
            # try: 
                # print('xxxx') 
            xemthoigian123 = driver.find_element('xpath', '/html/body/table/tbody/tr[2]/td[3]/div/div[2]/div[4]/table/tbody/tr/td[3]/div/span[1]').text
            if(xemthoigian123 != ''):
                print('thời gian chạy task là xxxx:', xemthoigian123.split(" ")[0])    
            
                try:
                    xemvideoxxx = driver.find_element('xpath', '/html/body/table/tbody/tr[2]/td[3]/div/div[2]/div[4]/table/tbody/tr/td[2]/div[1]/div/span[1]')
                    xemvideoxxx.click()
                except:
                    xemvideoxxx = driver.find_element('xpath', '/html/body/table/tbody/tr[2]/td[3]/div/div[2]/div[4]/table/tbody/tr/td[2]/div[1]/div')
                    xemvideoxxx.click()
                 
               
                time.sleep(3)
                print('click tab để xem video rồi')
                try:
                    xemvideo111 = driver.find_element('xpath', '/html/body/table/tbody/tr[2]/td[3]/div/div[2]/div[4]/table/tbody/tr/td[2]/div[1]/div/span')
                    xemvideo111.click()
                    time.sleep(3)
                    try:
                        driver.switch_to.window(driver.window_handles[-1])
                        time.sleep(1)
                        driver.switch_to.frame(driver.find_element('xpath', '/html/body/table/tbody/tr[2]/td/iframe'))
                        time.sleep(1)
                        
                        gettitle = driver.find_element('xpath', '/html/body/div/div/div[3]/div[2]/div/a')
                        print(gettitle.text+'1')
                        if(gettitle.text != ""):
                            print(gettitle.text)
                            xemvideodi = driver.find_element('xpath', '/html/body/div/div/div[4]/button')
                            xemvideodi.click()
                            time.sleep(float(xemthoigian123.split(" ")[0]) + 4)
                        else:
                            time.sleep(1)
                            driver.switch_to.window(driver.window_handles[0])
                            time.sleep(1)
                            print("xoa video loi khong xem duoc")
                            xoavideoloi = driver.find_element('xpath', '/html/body/table/tbody/tr[2]/td[3]/div/div[2]/div[5]/table/tbody/tr/td[3]/div/a')
                            xoavideoloi.click()
                            time.sleep(3)
                            driver.switch_to.window(driver.window_handles[-1])
                            time.sleep(1)
                         
                    except:
                        print("lỗi youtube không chạy")
                        pass
                except:
                    print("Button click red color")
                    
                
            else:
                
            # except:  
                # print('xxxx33333333333') 
                xemthoigian123 = driver.find_element('xpath', '/html/body/table/tbody/tr[2]/td[3]/div/div[2]/div[5]/table/tbody/tr/td[3]/div/span[1]').text
                print('thời gian chạy task là xxxx:', xemthoigian123.split(" ")[0])    
            
                try: 
                    xemvideoxxx = driver.find_element('xpath', '/html/body/table/tbody/tr[2]/td[3]/div/div[2]/div[5]/table/tbody/tr/td[2]/div[1]/div/span[1]')
                    xemvideoxxx.click()
                except:
                    xemvideoxxx = driver.find_element('xpath', '/html/body/table/tbody/tr[2]/td[3]/div/div[2]/div[5]/table/tbody/tr/td[2]/div[1]/div')
                    xemvideoxxx.click()
                
               
                time.sleep(3)
                print('click tab để xem video rồi')
                try:
                    
                    xemvideo111 = driver.find_element('xpath', '/html/body/table/tbody/tr[2]/td[3]/div/div[2]/div[5]/table/tbody/tr/td[2]/div[1]/div/span')
                    xemvideo111.click()
                    time.sleep(3)
                    try:
                        driver.switch_to.window(driver.window_handles[-1])
                        time.sleep(1)
                        driver.switch_to.frame(driver.find_element('xpath', '/html/body/table/tbody/tr[2]/td/iframe'))
                        time.sleep(1)
                        gettitle = driver.find_element('xpath', '/html/body/div/div/div[3]/div[2]/div/a')
                        print(gettitle.text+'1')
                        if(gettitle.text != ""):
                            print(gettitle.text)
                            xemvideodi = driver.find_element('xpath', '/html/body/div/div/div[4]/button')
                            xemvideodi.click()
                            time.sleep(float(xemthoigian123.split(" ")[0]) + 4)
                        else:
                            time.sleep(1)
                            driver.switch_to.window(driver.window_handles[0])
                            time.sleep(1)
                            print("xoa video loi khong xem duoc") 
                            xoavideoloi = driver.find_element('xpath', '/html/body/table/tbody/tr[2]/td[3]/div/div[2]/div[5]/table/tbody/tr/td[3]/div/a')
                            xoavideoloi.click()
                            time.sleep(3)
                            driver.switch_to.window(driver.window_handles[-1])
                            time.sleep(1)
                    except:
                        print("lỗi youtube không chạy")
                        pass
                except:
                    print("Button click red color")
                
        except:
            time.sleep(3)
           
            # driver.quit()
                # # hết video thì lướt sóng
            # time.sleep(3)
            try:
                surf2=driver.find_element('xpath', '/html/body/table/tbody/tr[2]/td[1]/div[2]/div/div/center/div[1]/a[1]')
                surf2.click()
            except:
                surf1=driver.find_element('xpath', '/html/body/table/tbody/tr[2]/td[1]/div[2]/div/div/center/span[1]')
                surf1.click()
                surf2=driver.find_element('xpath', '/html/body/table/tbody/tr[2]/td[1]/div[2]/div/div/center/div[1]/a[1]')
                surf2.click()
            
            time.sleep(5)
            # try:
            print('yyy') 
            xemthoigian111 = driver.find_element('xpath', '/html/body/table/tbody/tr[2]/td[3]/div/div[2]/div[1]/div/div[3]/div/span[2]').text
            if(xemthoigian111 != ''):
                print('thời gian chạy task là yyy:', xemthoigian111) 
                time.sleep(3)
                
                try:  
                    xemvideo = driver.find_element('xpath', '/html/body/table/tbody/tr[2]/td[3]/div/div[2]/div[1]/div/div[2]/div')
                    xemvideo.click()
                except:  
                    xemvideo = driver.find_element('xpath', '/html/body/table/tbody/tr[2]/td[3]/div/div[2]/div[2]/div/div[2]/div')
                    xemvideo.click()
                
                time.sleep(3)
                print('click tab để xem video rồi')
            
                try:
                    xemvideo1 = driver.find_element('xpath', '/html/body/table/tbody/tr[2]/td[3]/div/div[2]/div[1]/div/div[2]/a')
                    xemvideo1.click() 
                except:
                    xemvideo1 = driver.find_element('xpath', '/html/body/table/tbody/tr[2]/td[3]/div/div[2]/div[2]/div/div[2]/a')
                    xemvideo1.click() 
                time.sleep(3)
                driver.switch_to.window(driver.window_handles[-1])
                time.sleep(float(xemthoigian111.split(" ")[0]) + 2)
                try:
                    curr=driver.current_window_handle
                    for handle in driver.window_handles:
                        driver.switch_to.window(handle)
                        if handle != curr:
                            driver.close()
                except:
                    pass
                 
            xemthoigian111 = driver.find_element('xpath', '/html/body/table/tbody/tr[2]/td[3]/div/div[2]/div[1]/div/div[3]/div/span[1]').text    
            if (xemthoigian111 != ''):
                print('thời gian chạy task là yyy:', xemthoigian111) 
                time.sleep(3)
                
                try:  
                    xemvideo = driver.find_element('xpath', '/html/body/table/tbody/tr[2]/td[3]/div/div[2]/div[1]/div/div[2]/div')
                    xemvideo.click()
                except:  
                    xemvideo = driver.find_element('xpath', '/html/body/table/tbody/tr[2]/td[3]/div/div[2]/div[2]/div/div[2]/div')
                    xemvideo.click()
                
                time.sleep(3)
                print('click tab để xem video rồi')
            
                try:
                    xemvideo1 = driver.find_element('xpath', '/html/body/table/tbody/tr[2]/td[3]/div/div[2]/div[1]/div/div[2]/a')
                    xemvideo1.click() 
                except:
                    xemvideo1 = driver.find_element('xpath', '/html/body/table/tbody/tr[2]/td[3]/div/div[2]/div[2]/div/div[2]/a')
                    xemvideo1.click() 
                time.sleep(3)
                driver.switch_to.window(driver.window_handles[-1])
                time.sleep(float(xemthoigian111.split(" ")[0]) + 2)
                try:
                    curr=driver.current_window_handle
                    for handle in driver.window_handles:
                        driver.switch_to.window(handle)
                        if handle != curr:
                            driver.close()
                except:
                    pass
            # except:  
            else:
                try:
                    print('yyyy33333333333')                        
                    xemthoigian111 = driver.find_element('xpath', '/html/body/table/tbody/tr[2]/td[3]/div/div[2]/div[2]/div/div[3]/div/span[1]').text
                    xemthoigian111 != ''
                    print('thời gian chạy task là yyy:', xemthoigian111) 
                except:    
                    print('yyyy44444') 
                    xemthoigian111 = driver.find_element('xpath', '/html/body/table/tbody/tr[2]/td[3]/div[2]/div[2]/div/div[3]/div/span[2]').text
                    print('thời gian chạy task là yyy:', xemthoigian111) 
                time.sleep(3)
                
                try:  
                    xemvideo = driver.find_element('xpath', '/html/body/table/tbody/tr[2]/td[3]/div/div[2]/div[1]/div/div[2]/div')
                    xemvideo.click()
                except:  
                    xemvideo = driver.find_element('xpath', '/html/body/table/tbody/tr[2]/td[3]/div/div[2]/div[2]/div/div[2]/div')
                    xemvideo.click()
                
                time.sleep(3)
                print('click tab để xem video rồi')
            
                try:
                    xemvideo1 = driver.find_element('xpath', '/html/body/table/tbody/tr[2]/td[3]/div/div[2]/div[1]/div/div[2]/a')
                    xemvideo1.click() 
                except:
                    xemvideo1 = driver.find_element('xpath', '/html/body/table/tbody/tr[2]/td[3]/div/div[2]/div[2]/div/div[2]/a')
                    xemvideo1.click() 
                time.sleep(3)
                driver.switch_to.window(driver.window_handles[-1])
                time.sleep(float(xemthoigian111.split(" ")[0]) + 2)
                try:
                    curr=driver.current_window_handle
                    for handle in driver.window_handles:
                        driver.switch_to.window(handle)
                        if handle != curr:
                            driver.close()
                except:
                    pass
        else:
           time.sleep(1)
                
        # end lướt

       
        try:
            curr=driver.current_window_handle
            for handle in driver.window_handles:
                driver.switch_to.window(handle)
                if handle != curr:
                    driver.close()
        except:
            pass
        
        # end click xem video
        
        
    except:
        print('Bên lướt hết nhiệm vụ rồi')
        loi = loi + 1
        if loi >= 3:
            driver.quit()
        #driver.close()
        
        driver.get('https://meteex.com/reytbirj_new')
        
        pass
driver.quit()