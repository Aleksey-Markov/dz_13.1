class MixinShow:
    def __init__(self, *args, **kwargs):
        print(repr(self))

    def __repr__(self):
        return f'{self.__class__.__name__}{str([a for a in self.__dict__.values()]).replace("[", "(").replace("]", ")")}'


