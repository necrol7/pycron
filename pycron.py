import configparser
import os

app_settings = {}


def readConfig(path,app_settings):
    config = configparser.ConfigParser()
    config.read(path)
    app_settings["log_file"] = config.get("Settings", "log_file")
    app_settings["log_level"] = config.get("Settings", "log_level")
    print(app_settings["log_level"])
    print(app_settings["log_file"])
    
if __name__ == "__main__":
    path = "pycron.conf"
    readConfig(path,app_settings)
    print(app_settings["log_level"])
    print(app_settings["log_file"])
    