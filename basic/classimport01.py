import random
class RandomItem:
    def __init__(self,start,end,number):
        self.start=start
        self.end=end
        self.number=number
        self.numbers=[]
        self.get_randoms()
    def get_randoms(self):
        while True:
            temp=random.randint(self.start,self.end)
            if temp not in self.numbers:
                self.numbers.append(temp)
            if len(self.numbers)==self.number:
                break
