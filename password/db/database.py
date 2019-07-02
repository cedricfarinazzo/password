from .config import Config
from .entry import Entry


class Database:

    def __init__(self, conf):
        self.conf = conf
        self.__data = []

    def register(self, account, master_key):
        pass

    def retrieve(self, account_id, master_key):
        pass

    def delete(self, account_id, master_key):
        pass

    def update(self, account_id, data, master_key):
        pass

    def list(self):
        pass

    def load(self, master_key):
        pass

    def save(self):
        pass
