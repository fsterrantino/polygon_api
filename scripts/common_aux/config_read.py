import configparser

def config_read():
    config = configparser.ConfigParser()
    config.sections()
    config.read('/opt/config.ini')

    return config