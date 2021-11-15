import time
from datetime import datetime as dt
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

sites_to_block = [
    'www.facebook.com',  'facebook.com'
]

Window_host = r"C:\Windows\System32\drivers\etc\hosts"
default_hoster = Window_host
redirect = "127.0.0.1"


def block_websites(start_hour , end_hour):

    while True:
        if dt(dt.now().year, dt.now().month, dt.now().day,start_hour)< dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,end_hour):
            print("Do the work ....")
            check_web_site()

            with open(default_hoster, 'r+') as hostfile:
                hosts = hostfile.read()
                for site in sites_to_block:
                    if site not in hosts:
                       hostfile.write(redirect+' '+site+'\n')
                       hostfile.write('http://127.0.0.1:5000/'+ '\n')

        else:
            with open(default_hoster, 'r+') as hostfile:
                hosts = hostfile.readlines()
                hostfile.seek(0)
                for host in hosts:
                    if not any(site in host for site in sites_to_block):
                        hostfile.write(host)
                hostfile.truncate()
            print('Good Time')
        time.sleep(3)


def check_web_site():
    opt = Options()
    opt.add_experimental_option("debuggerAddress", "localhost:8989")
    driver = webdriver.Chrome(executable_path=".\\SaveData\\chromedriver.exe", chrome_options=opt)
    if driver.title == "www.facebook.com":
        driver.get("http://127.0.0.1:5000/saveyourmoney")
        print("Switch to saveYourMoney API")
    else:
        print("This is not facebook")


if __name__ == '__main__':
    block_websites(8, 23)
