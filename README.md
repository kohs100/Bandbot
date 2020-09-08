# bandchat API

```
import bandchat

bot = bandchat.Client("https://band.us/band/55800178/chat/CP2C7U")

@bot.on_ready
def onready():
    response = ("chat", f"Hello, World!")
    return [response]

@bot.on_chat
def onchat(usr_i, str_i):
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
class bandchat.Client(url, url, get_rate = 0.5, refresh_rate = 1800)
```
Represents a client connection that connects to band chatting. This class is used to interact with abstracted band chatting interfaces.
