import configparser

config = configparser.RawConfigParser()

config.read("C:/Users/sh.makhmudov/PycharmProjects/web_ui_playground/Configurations/config.ini")


class read_Config:
    @staticmethod
    def get_url():
        url = config.get('common info', 'codes')
        return url
