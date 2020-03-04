import os

LOG_PATH = ".\DataLogs"
FILE_LIST = os.listdir(LOG_PATH)

os.system("del /S " + LOG_PATH)

print("Clean Done!")
