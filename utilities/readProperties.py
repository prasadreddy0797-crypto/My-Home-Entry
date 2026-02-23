import configparser

config = configparser.ConfigParser()
config.read("Configurations/config.ini")


class ReadConfig:

    @staticmethod
    def getApplicationURL():
        url = config.get('common info', 'baseURL')
        return url

    @staticmethod
    def getUseremail():
        email = config.get('common info', 'useremail')
        return email

    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password
