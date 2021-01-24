


class crypto :
    def __init__(self,phrase):
        self.phrase = phrase

    def __str__(self):
        return str(self)
    
    def decalage(self,phrase):
        dec = 5
        code = []
        for i in phrase:
            code.append(ord(i))
        return code

crypto.decalage("SAlut")


