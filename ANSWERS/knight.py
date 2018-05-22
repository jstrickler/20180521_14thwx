import os

DATA_FOLDER = os.getenv("DATADIR", "DATA")
DATA_FILE = os.path.join(DATA_FOLDER, 'knights.txt')

class UnknownKnightError(Exception):
    pass

class Knight(object):

    def __init__(self,name):
        self._name = name
        with open(DATA_FILE) as knights_in:
            for line in knights_in:
                (name,title,color,quest,cmt) = line.rstrip('\n\r').split(":")
                if name == self._name:
                    self._title = title
                    self._color = color
                    self._quest = quest
                    self._comment = cmt
                    break
            else:
                raise UnknownKnightError("No such knight as '" + self._name + "'")

    @classmethod
    def get_knight_names(cls):
        with open(DATA_FILE) as knights_in:
            return [ line.split(':')[0] for line in knights_in]

    @property
    def name(self):
        return self._name
            
    @property
    def title(self):
        return self._title
            
    @property
    def color(self):
        return self._color
            
    @property
    def quest(self):
        return self._quest
            
    @property
    def comment(self):
        return self._comment
            

if __name__== "__main__":
    k = Knight("Arthur")
    print k.title, k.name,k.color,k.comment
    try:
        k2 = Knight("Bob")
    except UnknownKnightError,e:
        print e
