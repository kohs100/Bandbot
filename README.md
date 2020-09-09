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
    response = ("chat", "prefix: Hello, World!")
    return [response]

@bot.on_event
def on_chat(usr_i, str_i):
    if "prefix" not in str_i:
        res1 = ("chat", f"prefix: Hi, {usr_i}!")
        res2 = ("chat", f"prefix: You said {str_i}")
        return [res1, res2]
    else:
        return []

bot.run()
```

## Client
```
class bandchat.Client(url, get_rate=0.5, refresh_rate=1800, cli_login=True)
```
Represents a client connection that connects to band chatting. This class is used to interact with abstracted band chatting interfaces.

* url: string. URL of band chatroom
* get_rate: float(second). How often to check for new chats
* refresh_rate: int(second). How often to refresh chatroom
* cli_login: bool. Disable headless option and cli login feature.

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
    if "prefix" not in str_i:
        res1 = ("chat", f"prefix: Hi, {usr_i}!")
        res2 = ("chat", f"prefix: You said {str_i}")
        return [res1, res2]
    else:
        return []
```
* on_chat
  * Parameter: usr_i, str_i
  * Called when client received new chat.

### Return value
Return value of event functions is the list of __Chat tuple__

