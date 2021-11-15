from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def run():
    opt = Options()
    opt.add_experimental_option("debuggerAddress", "localhost:8989")
    driver = webdriver.Chrome(executable_path=".\\SaveData\\chromedriver.exe",chrome_options=opt)
    result = driver.get("http://www.ynet.co.il")
    print(result)

if __name__ == '__main__':
    run()