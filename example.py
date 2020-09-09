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