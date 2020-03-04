import csv
import time
import random

FILE_PATH = "D:\\Users\\VB85788\\PycharmProjects\\creme_deneme\\dataset.csv"
LOG_PATH = ".\\Data\\"
LOG_COUNTER = 1

with open(FILE_PATH, 'r') as FILE:
    csvreader = csv.reader(FILE)
    for row in csvreader:
        TEXT = ""
        time.sleep(random.randint(1, 10))
        FILE = open(LOG_PATH+str(LOG_COUNTER)+".txt", 'w')
        for column in row:
            TEXT += column + " "
        TEXT = TEXT[:-1]
        FILE.write(TEXT)
        FILE.close()
        print("File Write Done")
        LOG_COUNTER += 1
