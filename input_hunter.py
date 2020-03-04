import os
import schedule
import time

DATASET = []
ALREADY_READ_FILE_LIST = []

def READ_EXECUTE(DATASET):

    FILE_LIST = os.listdir(".\Data")
    BASE_PATH = ".\\Data\\"
    LOG_PATH = ".\\DataLogs"

    for FILE_NAME in FILE_LIST:
        if FILE_NAME in ALREADY_READ_FILE_LIST:
            continue
        else:
            try:
                with open(BASE_PATH + FILE_NAME, 'r') as NEW_FILE:
                    DATA = NEW_FILE.readline()
                    DATA_COLUMNS = DATA.split(',')
                    for i in range(len(DATA_COLUMNS)):
                        DATA_COLUMNS[i] = DATA_COLUMNS[i].strip()
                # Model predict and train
                DATASET.append(DATA_COLUMNS)
                ALREADY_READ_FILE_LIST.append(FILE_NAME)
                os.system("move " + BASE_PATH + FILE_NAME + " " + LOG_PATH)
            except Exception as e:
                print(str(e))

schedule.every(1).seconds.do(READ_EXECUTE, DATASET)

while True:
    schedule.run_pending()
    time.sleep(1)
    print(DATASET)