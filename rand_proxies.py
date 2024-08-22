import csv
import random
# import threading

class RandomProxy:
    def __init__(self):
        self.proxies = []
        with open('proxies.csv', 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                self.proxies.append(row[1])


    def get_random_proxy(self):
        return random.choice(self.proxies)
