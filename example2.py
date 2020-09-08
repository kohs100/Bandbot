import argparse
import glob
import hashlib
import json

import requests as r

import bandchat

def sha256(path, blocksize=1024):
    file_hash = hashlib.sha256()
    with open(path, 'rb') as f:
        fb = f.read(blocksize)
        while len(fb) > 0:
            file_hash.update(fb)
            fb = f.read(blocksize)
    return file_hash.hexdigest()

def getFile(content):
    def dlFile(uri, name):
        with open(name, "wb") as f:
            res = r.get(uri)
            f.write(res.content)

    f_name = content["filename"]
    f_hash = content["filehash"]
    f_uri = content["fileuri"]

    if glob.glob(f_name):
        if sha256(f_name) == f_hash:
            pass
        else:
            dlFile(f_uri, f_name)
    else:
        dlFile(f_uri, f_name)


parser = argparse.ArgumentParser(
    description='Example to use bandchat pseudoAPI')
parser.add_argument('url')

api_endpoint = parser.parse_args().url

bot = bandchat.Client("https://band.us/band/55800178/chat/CP2C7U")

@bot.on_chat
def bot_onchat(usr_i, str_i):
    req = {
        "type": "chat",
        "content": {
                "user": usr_i,
                "chat": str_i
        }
    }
    headers = {'Content-Type': 'application/json'}
    try:
        res = r.get(api_endpoint, data=json.dumps(req), headers=headers)
    except:
        print("Connection to bandbot backend endpoint failed.")
        return []
        
    if 200 <= res.status_code and res.status_code < 300:
        res = res.json()
        response = []
        for resp in res:
            if resp["type"] == "chat":
                response.append("chat", resp["content"])
            elif resp["type"] == "image":
                getFile(resp["content"])
                response.append("image", resp["content"]["filename"])
            elif resp["type"] == "file":
                getFile(resp["content"])
            elif resp["type"] == "change":
                response.append("change", resp["content"]["uri"])
            else:
                print("Unknown response type: ", resp["type"])
                return []
        return response
    else:
        print("status code not 200")
        return []