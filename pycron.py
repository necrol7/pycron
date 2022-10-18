import configparser
import logging

app_settings = {}    

def readConf(path,app_settings):
    config = configparser.ConfigParser()
    config.read(path)
    app_settings["log_file"] = config.get("Settings", "log_file")
    app_settings["log_level"] = config.get("Settings", "log_level")
    app_settings["crontab_file"] = config.get("Settings", "crontab_file")
   
if __name__ == "__main__":
    path = "pycron.conf"
    readConf(path,app_settings)
    logging.basicConfig(filename=app_settings["log_file"], filemode='w', format='%(name)s - %(levelname)s - %(message)s') #, level=logging.{app_settings["log_level"]})
    logging.debug('settings read done')
    
    