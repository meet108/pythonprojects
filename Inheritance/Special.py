class CLanguage:
    def array(self):
        print('array feature...')


class CPlusPlus():
    def array(self):
        print('array feature...')


class Python(CLanguage, CPlusPlus):
    def array(self):
        print('array feature...')


d = Python()

d.array()
