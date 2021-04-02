import configparser
import os


path = os.path.dirname(os.path.dirname(__file__))
new_path = path +"\\config\\config.ini"
conf=configparser.ConfigParser()
conf.read(new_path,encoding="utf-8")
sections = conf.sections()
options = conf.options("host")
value = conf.items("host")
gets = conf.get("host","uu")
print(gets)