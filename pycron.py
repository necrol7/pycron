import configparser
import os

def readConfig(path):   # Читаем конфиг файл
    config = configparser.ConfigParser()
    config.read(path)
    log-level = config.get("Settings", "log-level")
    log-file = config.get("Settings", "log-file")
    
 
if __name__ == "__main__":
    path = "pycron.conf"
    readConfig(path)