class Browser:
    def __init__(self):
        self.bs = []
        self.fs = []

    def go(self, url):
        self.bs.append(url)
        self.fs.clear()

    def back(self):
        if len(self.bs) > 1:
            self.fs.append(self.bs.pop())
            return self.bs[-1]

    def forward(self):
        if self.fs:
            self.bs.append(self.fs.pop())
            return self.bs[-1]

    def printAll(self):
        print(*self.bs)


brwsr = Browser()
brwsr.go("https://google.com")
brwsr.go("https://ukdw.ac.id")
brwsr.go("https://facebook.com")

print(brwsr.back()) #output: https://ukdw.ac.id
print(brwsr.back()) #output: https://google.com
print(brwsr.forward()) #output: https://ukdw.ac.id

brwsr.go("https://twitter.com") 
brwsr.printAll() #output: https://google.com https://ukdw.ac.id https://twitter.com