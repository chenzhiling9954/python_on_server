from selenium import webdriver

brower = webdriver.Firefox(executable_path=r"D:\develop\python\geckodriver\geckodriver.exe",
        firefox_binary=r"C:\Program Files\Mozilla Firefox\firefox.exe")
brower.get('http://localhost:8000')

assert 'Django' in brower.title