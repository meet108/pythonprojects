class Parent:
    def walk(self):
        print('walking')


class Child(Parent):
    def crawl(self):
        print('crawling')
        self.walk()


d = Child()

d.crawl()

d.walk()
