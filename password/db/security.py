from Crypto.Hash import SHA512


class Hash:

    @staticmethod
    def hash(s):
        hash = SHA512.new()
        hash.update(s.encode())
        return hash.digest()

    @staticmethod
    def verify_hash(s, hash):
        return Hash.hash(s) == hash
