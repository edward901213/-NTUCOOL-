from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
import time
import threading
options = webdriver.EdgeOptions()
options.add_argument("--user-data-dir=C:\\Users\\edwar\\AppData\\Local\\Microsoft\\Edge\\User Data")
options.add_argument('--profile-directory='+'Default')

driver = webdriver.Edge('msedgedriver', options=options)




driver.get('https://cool.ntu.edu.tw/courses/15573/modules/items/621302')
for i in range(100):
    try:
        time.sleep(5)
        driver.switch_to.frame("tool_content");
        driver.find_element(By.CSS_SELECTOR, '#vjs_video_3 > div.vjs-control-bar > button.vjs-play-control.vjs-control.vjs-button').click()
        driver.find_element(By.CSS_SELECTOR,'#vjs_video_3 > div.vjs-control-bar > div.vjs-volume-panel.vjs-control.vjs-volume-panel-vertical > button').click()
        driver.execute_script("document.getElementById('vjs_video_3_html5_api').play()")
        val = driver.find_element(By.ID, 'vjs_video_3_html5_api').get_attribute("ended")
        while val != 'true':
            val = driver.find_element(By.ID, 'vjs_video_3_html5_api').get_attribute("ended")
            time.sleep(1)
        print('video finished')
        driver.switch_to.default_content()
        driver.execute_script("document.querySelector('#sequence_footer > div.module-sequence-footer > div > span.module-sequence-footer-button--next > a').click()")   
    except Exception as e:
        driver.execute_script("document.querySelector('#sequence_footer > div.module-sequence-footer > div > span.module-sequence-footer-button--next > a').click()")

driver.quit()

