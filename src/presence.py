#!/bin/python
import json
from platform import system
from os.path import expanduser
from pypresence import Presence
import time

class Config:
    def __init__(self):
        self.config = {}
        
        if system() == "Linux":
            self.savepath = expanduser("~/.local/share/custom-presence/config.json")
        else:
            self.savepath = "./config.json"
        
        self.load()
        

    def load(self):
        try:
            f = open(self.savepath, "r")
            self.config = json.loads(f.read())
            f.close()
        except:
            print("Config not found, please make sure to edit the config with the editor.")
            exit()

def loop(rpc, buttons):
    try:
        if cfg.config["large_img"] != "" and cfg.config["small_img"] != "":
            rpc.update(
                buttons=buttons,
                details=cfg.config["details"],
                state=cfg.config["state"],
                large_image=cfg.config["large_img"],
                small_image=cfg.config["small_img"]  
            )
    
        elif cfg.config["large_img"] != "" and cfg.config["small_img"] == "":
            rpc.update(
                buttons=buttons,
                details=cfg.config["details"],
                state=cfg.config["state"],
                large_image=cfg.config["large_img"]   
            )

        elif cfg.config["large_img"] == "" and cfg.config["small_img"] != "":
            rpc.update(
                buttons=buttons,
                details=cfg.config["details"],
                state=cfg.config["state"],
                small_image=cfg.config["small_img"]   
            )

        else:
            rpc.update(
                buttons=buttons,
                details=cfg.config["details"],
                state=cfg.config["state"],
            )
    except Exception as e:
        print(f"Presence update failed: {e}")
        exit()


if __name__ == "__main__":
    cfg = Config()
    try:
        rpc = Presence(cfg.config["client_id"])
        rpc.connect()
    except:
        print("Invalid client ID")
        exit()

    buttons = []
    for i in range(2):
        if cfg.config[f"button{i+1}"]:
            buttons.append({
                "label": cfg.config[f"button{i+1}_label"],
                "url": cfg.config[f"button{i+1}_url"]
            }) 

    while True:
        loop(rpc, buttons)
        time.sleep(60)
