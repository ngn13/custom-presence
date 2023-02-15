#!/bin/python
from PyQt5 import QtWidgets, uic
from platform import system
from os.path import expanduser
import sys
import json

class Config:
    def __init__(self):
        self.default = {
            "client_id": 123,
            "details": "Hello World!",
            "state": "Hello from custom presence!",
            "button1": True,
            "button2": False,
            "button1_label": "Get Custom Presence!",
            "button1_url": "https://github.com/ngn13/custom-presence",
            "button2_label": "Click me!",
            "button2_url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
            "large_img": "large",
            "small_img": "leave here empty for none"
        }

        self.config = {}
        
        if system() == "Linux":
            self.savepath = expanduser("~/.local/share/custom-presence/config.json")
        else:
            self.savepath = "./config.json"

    def save(self):
        f = open(self.savepath, "w")
        f.write(json.dumps(self.config))
        f.close()
        return

    def load(self):
        try:
            f = open(self.savepath, "r")
            self.config = json.loads(f.read())
            f.close()
        except:
            self.config = self.default

class UI(QtWidgets.QMainWindow):
    def getUIPath(self):
        if system() == "Linux":
            return expanduser("~/.local/share/custom-presence/config.ui")

        return "./config.ui"

    def savefn(self, btn):
        self.cfg.config["client_id"] = self.cid.text()
        self.cfg.config["details"] = self.details.text()
        self.cfg.config["state"] = self.state.text()

        self.cfg.config["button1"] = self.shwbtn1.isChecked()
        self.cfg.config["button2"] = self.shwbtn2.isChecked()

        self.cfg.config["button1_label"] = self.btn1lbl.text()
        self.cfg.config["button1_url"] = self.btn1url.text()
        self.cfg.config["button2_label"] = self.btn2lbl.text()
        self.cfg.config["button2_url"] = self.btn2url.text()

        self.cfg.config["large_img"] = self.large.text()
        self.cfg.config["small_img"] = self.small.text()

        self.cfg.save()

    def quitfn(self, btn):
        self.close()

    def __init__(self, cfg):
        super(UI, self).__init__()
        uic.loadUi(self.getUIPath(), self)
        self.show()

        self.cfg = cfg

        self.setMinimumWidth(254)
        self.setMinimumHeight(677)
        self.setMaximumWidth(254)
        self.setMaximumHeight(677)

        self.cid.setText(str(self.cfg.config["client_id"]))
        self.details.setText(self.cfg.config["details"])
        self.state.setText(self.cfg.config["state"])

        self.shwbtn1.setCheckState(2 if self.cfg.config["button1"] else 0)
        self.shwbtn2.setCheckState(2 if self.cfg.config["button2"] else 0)

        self.btn1lbl.setText(self.cfg.config["button1_label"])
        self.btn1url.setText(self.cfg.config["button1_url"])
        self.btn2lbl.setText(self.cfg.config["button2_label"])
        self.btn2url.setText(self.cfg.config["button2_url"])

        self.large.setText(self.cfg.config["large_img"])
        self.small.setText(self.cfg.config["small_img"])

        self.save.clicked.connect(self.savefn)
        self.quit.clicked.connect(self.quitfn)

if __name__ == "__main__":
    cfg = Config()
    cfg.load()
    
    app = QtWidgets.QApplication(sys.argv)
    window = UI(cfg)
    app.exec_()
