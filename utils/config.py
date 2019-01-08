#coding:utf-8
import os
import yaml

class Config:

    BASE_PATH = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
    CONFIG_FILE = os.path.join(BASE_PATH, "config", "config.yml")
    REPORT_FILE = os.path.join(BASE_PATH, "report", "result.html")
    LOG_FILE = os.path.join(BASE_PATH, "log", "log.txt")
    IMG = os.path.join(BASE_PATH, "data", "logo.png")
    DRIVER_PATH = os.path.join(BASE_PATH, "drivers", "chromedriver.exe")

    def __init__(self, config=CONFIG_FILE):
        f = open(config,'rb')
        self.config = yaml.load(f)
    def getInfo(self, type, parm):
        return self.config[type][parm]