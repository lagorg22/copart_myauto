import csv
import requests
import threading

proxies_all = []

with open('proxies.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        proxies_all.append(row[1])

# url = 'http://httpbin.org/ip'
# proxies = {
#     'http': proxy,
#     'https': proxy,
# }
#
# for proxy in proxies_all:
#     try:
