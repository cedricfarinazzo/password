import os
import pickle


class Config:

    def __init__(self, config_dic={}):
        self.__config = config_dic

    def __getitem__(self, item):
        return self.__config[item]

    def __setitem__(self, key, value):
        self.__config[key] = value

    def __delitem__(self, key):
        self.__config.__delitem__(key)

    def __contains__(self, item):
        return self.__config.__contains__(item)

    def __iter__(self):
        for key, value in self.__config.items():
            yield key, value

    def __len__(self):
        return len(self.__config)

    def __str__(self):
        return str(self.__config)

    def clean(self):
        self.__config = {}

    @staticmethod
    def load_config(path):
        if not os.path.exists(path):
            raise FileNotFoundError(path)
        try:
            with open(path, 'rb') as f:
                config = pickle.load(f)
            return Config(config_dic=config)
        except:
            return None

    def save_config(self, path):
        with open(path, 'wb+') as f:
            pickle.dump(self.__config, f)
