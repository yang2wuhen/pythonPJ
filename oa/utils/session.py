import hashlib


class Session:

    def md5Encode(self, s):
        m = hashlib.md5()
        m.update(str(s).encode(encoding="utf-8"))
        return m.hexdigest()


    def createSession(self, name, pwd):
        id = name + pwd
        return self.md5Encode(id)
