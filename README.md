# bandchat API
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
class bandchat.Client(url, get_rate = 0.5, refresh_rate = 1800)
```
Represents a client connection that connects to band chatting. This class is used to interact with abstracted band chatting interfaces.

* url: string. URL of band chatroom
* get_rate: float(second). How often to check for new chats
* refresh_rate: int(second). How often to refresh chatroom

## Methods
* Client.run(): Start event loop

## Event
### on_ready
```
@bot.on_event
def on_ready():
    response = ("chat", "prefix: Hello, World!")
    return [response]
```
* Parameter: None
* Called when bandchat client is ready to listen.

### on_chat
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
* Parameter: usr_i, str_i
* Called when client received new chat.

### Return value
Return value of event functions is the list of __Chat tuple__


# Dependencies
## Google Chrome
* https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
```
$ wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
$ sudo dpkg -i google-chrome*.deb
```

## chromedriver
* https://chromedriver.chromium.org/

## BAND Account
* Should be able to login with phone number