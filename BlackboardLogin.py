"""time module is used to put pauses between each selenium action
   as the website sometimes take a second to load"""
import time
from selenium import webdriver

class BlackboardLogin:
    """this class opens up firefox and logs into Blackboard Admin site"""
    def __init__(self, username, password, site):
        """init method intializes all variables to be used in this class"""
        self._username = username
        self._password = password
        self._urls = {'prod': 'https://learnadmin.liberty.edu',
                      'test': 'https://bbtestadmin.liberty.edu'}
        self._site = self._urls[site]
        self._browser = webdriver.Firefox()
        self._cookies = None

    def bblogin(self):
        """this is the actual method that performs the log in process"""
        self._browser.get(self._site)
        time.sleep(1)
        self._browser.find_element_by_id("agree_button").click()
        self._browser.find_element_by_id("user_id").send_keys(self._username)
        self._browser.find_element_by_id("password").send_keys(self._password)
        time.sleep(1)
        self._browser.find_element_by_id("entry-login").click()
        time.sleep(1)

    def cookie_sesh(self):
        """this method stores cookie session in property for future usage"""
        self._cookies = self._browser.get_cookies()

    @property
    def site(self):
        """this property is used to store the site url"""
        return self._site

    @property
    def cookies(self):
        """this property is intended to be used to keep cookie
           session open for other methods to implement"""
        return self._cookies
    