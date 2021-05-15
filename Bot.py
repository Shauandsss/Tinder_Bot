from selenium import webdriver
from time import sleep
from User import usuario, senha

class Tinder():

    def open(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://tinder.com/pt')

    def login(self):
        self.driver.find_element_by_xpath('//*[@id="t1197069193"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a').click()

        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="t-531311883"]/div/div/div[1]/div/div[3]/span/div[2]/button').click()

        janela_principal = self.driver.window_handles[0]

        popup = self.driver.switch_to.window(self.driver.window_handles[1])

        self.driver.find_element_by_xpath('//*[@id="email"]').send_keys(usuario)

        self.driver.find_element_by_xpath('//*[@id="pass"]').send_keys(senha)

        self.driver.find_element_by_xpath('//*[@id="loginbutton"]').click()

        self.driver.switch_to.window(janela_principal)  

        self.driver.find_element_by_xpath('//*[@id="t1197069193"]/div/div[2]/div/div/div[1]/button').click()

        sleep(5)
        self.driver.find_element_by_xpath('//*[@id="t-531311883"]/div/div/div/div/div[3]/button[1]').click()

        self.driver.find_element_by_xpath('//*[@id="t-531311883"]/div/div/div/div/div[3]/button[2]').click()


        
    def LikeButton(self):
        while(True):
            try:
                self.driver.find_element_by_xpath('//*[@id="t1197069193"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button').click()
            except:
                try:
                    self.driver.find_element_by_xpath('//*[@id="t-531311883"]/div/div/button[2]').click()
                except:
                    try:
                        self.driver.find_element_by_xpath('//*[@id="t-531311883"]/div/div/div[2]/button[2]').click()
                    except:
                        continue

bot = Tinder()
bot.open()
bot.login()
bot.LikeButton()