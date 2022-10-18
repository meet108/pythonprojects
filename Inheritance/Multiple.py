class CLanguage:
    def pop(self):
        print('procedure oriented...')


class CPlusPlus():
    def oop(self):
        print('object oriented...')


class Python(CLanguage, CPlusPlus):
    def interpreted(self):
        self.pop()
        self.oop()
        print('interpreted...')


d = Python()

d.pop()

d.oop()

d.interpreted()
