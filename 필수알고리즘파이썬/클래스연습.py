class myclass:
    def __init__(self, num, a=0):
        self.stnum = num
        self.d = a


me = myclass(2)
print(me.stnum, me.d)
