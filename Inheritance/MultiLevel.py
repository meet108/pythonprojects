class CLanguage:
    def array(self):
        print('array feature...')


class CPlusPlus(CLanguage):
    def inheritance(self):
        self.array()
        print('inheritance feature...')


class Python(CPlusPlus):
    def variable_length(self):
        self.array()
        self.inheritance()
        print('variable length arguments...')


d = Python()

d.array()

d.inheritance()

d.variable_length()
