from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

user_name = "Github User Name"
class Github:
    
    def __init__(self,username):
        self.browser = webdriver.Chrome(executable_path="your chrome driver path")
        self.url = "https://github.com/"
        self.username = username
        self.followers = []

    def loadFollowers(self):
        items = self.browser.find_elements_by_css_selector('.d-table.table-fixed')

        for item in items:
            name = item.find_elements_by_tag_name('div')[1].find_elements_by_tag_name('span')[0].text
            username = item.find_elements_by_tag_name('div')[1].find_elements_by_tag_name('span')[1].text
            user = {
                "name": name,
                "username": username
            }
            self.followers.append(user)

    def getFollowers(self):
        self.browser.get(f"{self.url}{self.username}?tab=followers")
        self.loadFollowers()        

        
        for follower in self.followers:
            print(follower['username']) 

    def __del__(self):
        time.sleep(2)
        self.browser.close()


app = Github(user_name)
app.getFollowers() 