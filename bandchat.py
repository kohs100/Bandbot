from time import sleep, strftime, time
import os

from bs4 import BeautifulSoup

from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions

class ChatLoadException(Exception):
    def __init__(self):
        super().__init__("Chat loading error")

class Client():
    def __init__(self, url, get_rate = 0.5, refresh_rate = 1800):
        self.chatURL = url
        self.refresh_rate = refresh_rate
        self.get_rate = get_rate

        options = ChromeOptions()
        options.add_argument("--headless")
        options.add_argument('--disable-extensions')
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        
        print("Driver initializing...")
        self.driver = Chrome(options=options)
        print("Driver initialized.")

        self.driver.get(self.chatURL)
        print("Get login page completed.")
        self.driver.implicitly_wait(3)

        self.driver.find_element_by_css_selector(
            ".uBtn.-icoType.-phone").click()
        print("Get PhonenumberPage completed.")
        self.driver.implicitly_wait(3)

        Phonenumber = input("전화번호 입력 :")
        self.driver.find_element_by_id(
            "input_local_phone_number").send_keys(Phonenumber)
        self.driver.find_element_by_css_selector(
            ".uBtn.-tcType.-confirm").click()
        print("Get PasswordPage completed.")
        self.driver.implicitly_wait(3)

        Password = input("비밀번호 입력 :")
        self.driver.find_element_by_id("pw").send_keys(Password)
        self.driver.find_element_by_css_selector(
            ".uBtn.-tcType.-confirm").click()
        print("Get SMSPage completed.")
        self.driver.implicitly_wait(8)
        try:
            print(self.driver.find_element_by_id("hintNumberDiv").text)
            sleep(20)
        except NoSuchElementException:
            pw_band = input("인증번호: ")
            self.driver.find_element_by_id("code").send_keys(str(pw_band))
            self.driver.find_element_by_css_selector(
                "button.uBtn.-tcType.-confirm").click()
            print("Driver get completed.")

        self._get_msgbox()

    def _get_msgbox(self):
        startsec = time()
        while(True):
            try:
                self.msgWrite = self.driver.find_element_by_class_name(
                    "commentWrite")
            except NoSuchElementException:
                if(time() > startsec + 10):
                    raise ChatLoadException
                sleep(1)
                continue
            break
        sleep(1)
        print("boot success")

    def _refresh(self):
        self.last_refresh = time()
        self.next_refresh = self.last_refresh + self.refresh_rate

        self.driver.get(self.chatURL)
        self._get_msgbox()
        self.driver.implicitly_wait(10)

    def _send_image(self, rPath):
        try:
            absPath = os.path.abspath(rPath)
            img_up = self.driver.find_element_by_css_selector(
                "input[data-uiselector='imageUploadButton']")
            img_up.send_keys(absPath)
        except Exception as e:
            print(e)
        return

    def _send_chat(self, str_i):
        lines = str_i.split("\n")

        for chat in lines:
            self.msgWrite.send_keys(chat)
            self.msgWrite.send_keys(Keys.SHIFT, Keys.ENTER)
        self.msgWrite.send_keys(Keys.ENTER)

    def _get_HTML(self):
        soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        chatlist = soup.find_all("span", class_="txt")
        userlist = soup.find_all("button", class_="author")
        return len(chatlist), chatlist, userlist

    def _parse_response(self, res_lst):
        for res in res_lst:
            if res[0] == "chat":
                self._send_chat(res[1])
            elif res[0] == "image":
                self._send_image(res[1])
            elif res[0] == "change":
                self.chatURL = res[1]
                self._refresh()

    def on_chat(self, ifunction):
        self.on_chat_function = ifunction
        return ifunction
    
    def on_ready(self, ifunction):
        self.on_ready_function = ifunction
        return ifunction

    def run(self):
        self._refresh()
        recent_chat, _, _ = self._get_HTML()
        self._parse_response(self.on_ready_function())

        while True:
            if time() >= self.next_refresh:
                self._refresh()
            len_chat, i_chat, i_user = self._get_HTML()

            for i in range(recent_chat - len_chat, 0):
                str_i = i_chat[i].text
                usr_i = i_user[i].text
                print(usr_i + ":" + str_i)

                self._parse_response(self.on_chat_function(usr_i, str_i))
            
            recent_chat = len_chat
            sleep(self.get_rate)