from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from send import send_mail


path = './chromedriver'
browser = webdriver.Chrome(executable_path=path)
browser.get('https://mp.weixin.qq.com/')

# 设置显式等待时间
wait = WebDriverWait(browser, 10)
wait.until(EC.presence_of_all_elements_located)

# 登录
browser.find_element_by_css_selector(
    '#header > div.banner > div > div > form > div.login_input_panel > div:nth-child(1) > div > span > input').send_keys(
    'fl1584s@163.com')
browser.find_element_by_css_selector(
    '#header > div.banner > div > div > form > div.login_input_panel > div:nth-child(2) > div > span > input').send_keys(
    'liin87654322')
browser.find_element_by_css_selector('#header > div.banner > div > div > form > div.login_btn_panel > a').click()

wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'weui-desktop-qrcheck__img-area')))
# 定位当前页面
browser.current_window_handle

wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'weui-desktop-qrcheck__img-area')))
src = browser.find_element_by_css_selector('#app > div.weui-desktop-layout__main__bd > div > div.js_scan.weui-desktop-qrcheck > div.weui-desktop-qrcheck__qrcode-area > div > img').get_property('src')
print(src)
for i in range(1):  # 发送1封，上面的列表是几个人，这个就填几
    if send_mail("你好", src):  # 邮件主题和邮件内容
        # 这是最好写点中文，如果随便写，可能会被网易当做垃圾邮件退信
        print("done!")
    else:
        print("failed!")

# 检测登录成功
wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'top_user_switch')))


