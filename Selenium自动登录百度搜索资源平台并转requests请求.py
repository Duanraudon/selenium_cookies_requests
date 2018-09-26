from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time,requests


def login(url,driver,username,password):

    driver.maximize_window()
    driver.get("https://www.baidu.com/index.php")
    time.sleep(5)
    driver.find_element_by_id("u1").find_element_by_name("tj_login").click()
    time.sleep(5)
    driver.find_element_by_css_selector('#TANGRAM__PSP_10__footerULoginBtn').click()
    driver.find_element_by_css_selector("#TANGRAM__PSP_10__userName").clear()
    driver.find_element_by_css_selector("#TANGRAM__PSP_10__userName").send_keys(username)
    driver.find_element_by_css_selector("#TANGRAM__PSP_10__password").clear()
    driver.find_element_by_css_selector("#TANGRAM__PSP_10__password").send_keys(password)
    driver.find_element_by_css_selector("#TANGRAM__PSP_10__submit").click()
    time.sleep(10)  # 留充足的时间手动输入验证码
    driver.find_element_by_id("kw").clear()
    driver.find_element_by_id("kw").send_keys("百度搜索资源平台")
    driver.find_element_by_id("su").click()
    time.sleep(5)
    driver.find_element_by_xpath('//div[@id="1"]/h3/a').click()
    time.sleep(10)
    cookies = driver.get_cookies()
    cookies1 = {}
    for cookie in cookies:
        cookies1[cookie['name']] = cookie['value']

    r= requests.get(url,cookies=cookies1)
    print(r.content.decode('utf-8'))
    return r.text
if __name__ == "__main__":
    username = str(input('请输入账号：'))
    password = str(input('请输入密码: '))
    url = 'https://ziyuan.baidu.com/'
    #浏览器页面可隐藏
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')

    driver = webdriver.Chrome(executable_path='E:\京兆人\Python\chromedriver.exe',chrome_options=chrome_options)
    login(url,driver,username,password)
