band.py
=======
An ancient, hard to use, feature-less, and async unready pseudo-API for Band chatting written in Python.


Dependencies
------------
* Google Chrome
  * https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
```
$ wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
$ sudo dpkg -i google-chrome*.deb
```

* Chromedriver
  * https://chromedriver.chromium.org/
```
$ CD_VERSION=$(wget -qO- https://chromedriver.storage.googleapis.com/LATEST_RELEASE) && \
  echo "Using chromedriver version: "$CD_VERSION && \
  wget --no-verbose -O /tmp/chromedriver_linux64.zip https://chromedriver.storage.googleapis.com/$CD_VERSION/chromedriver_linux64.zip && \
  unzip /tmp/chromedriver_linux64.zip -d /tmp/ && \
  rm /tmp/chromedriver_linux64.zip
$ sudo mv /tmp/chromedriver /usr/bin/chromedriver
$ sudo chmod 755 /usr/bin/chromedriver
```

* BAND Account
  * Should be able to login with phone number.


Quick example
-------------
```
import bandchat

bot = bandchat.Client("https://band.us/band/55800178/chat/CP2C7U")

@bot.on_event
def on_ready():
    response = ("chat", "Hello, World!")
    return [response]

@bot.on_event
def on_chat(usr_i, str_i):
    if str_i.startswith('!bot'):
        res1 = ("chat", f"Hi, {usr_i}!")
        res2 = ("chat", f"You said {str_i}")
        return [res1, res2]
    else:
        return []

bot.run()
```

## Client
```
class bandchat.Client(url, get_rate=0.5, refresh_rate=1800, cli_login=True, user_data=None)
```
Represents a client connection that connects to band chatting. This class is used to interact with abstracted band chatting interfaces.

* url: string. URL of band chatroom
* get_rate: float(second). How often to check for new chats
* refresh_rate: int(second). How often to refresh chatroom
* cli_login: bool. Disable headless option and cli login feature. You should login manually from chrome then press enter to continue
* user_data: string. Absolute path to chrome profile directory. e.g. "%localappdata%\\Google\\Chrome\\User Data"

### Methods
* Client.run(): Start event loop

### Event
```
@bot.on_event
def on_ready():
    response = ("chat", "prefix: Hello, World!")
    return [response]
```
* on_ready
  * Parameter: None
  * Called when bandchat client is ready to listen.

```
@bot.on_event
def on_chat(usr_i, str_i):
    if str_i.startswith('!bot'):
        res1 = ("chat", f"Hi, {usr_i}!")
        res2 = ("chat", f"You said {str_i}")
        return [res1, res2]
    else:
        return []
```
* on_chat
  * Parameter: usr_i, str_i
  * Called when client received new chat.

### Return value
Return value of event functions is the list of tuples of response type and content.

#### Response type
* chat
  * content: string
```
res1 = ("chat", f"Hi, {usr_i}!")
return [res1]
```
* image
  * content: string. relative path to image
```
res1 = ("chat", "this is your image")
res2 = ("image", "path/to/image.jpg")
return [res1, res2]
```
* change
  * content: string. URL of new chatroom
```
res1 = ("change", "https://band.us/band/77955502/chat/ABCDEF")
res2 = ("chat", "hello, world!")
res3 = ("change", "https://band.us/band/77955502/chat/ASDFGH")
return [res1, res2, res3]
```
* delay
  * content: string. delay time in second(float)
```
res1 = ("chat", "How do turtles communicate?")
res2 = ("delay", "3.2")
res3 = ("chat", "With shell phones")
return [res1, res2, res3]
```