import csv
from collections import Counter

class FastUI():

    def render(self, board):
        pass

    def tick(self):
        pass

    def get_move(self):
        raise NotImplementedError

    def add_score(self, winnaar):
        pass

    def initiate_csv(self):
        with open('test.csv', mode='a', newline='') as myfile:
            fieldnames = [1, 2, 3]
            mywriter = csv.DictWriter(myfile, fieldnames=fieldnames)
            mywriter.writeheader()

    def add_csv(self, winnaars):
        with open('test.csv', mode='a', newline='') as myfile:
            fieldnames = [1, 2, 3]
            mywriter = csv.DictWriter(myfile, fieldnames=fieldnames)
            mywriter.writerow(Counter(winnaars[-101:-1]))
