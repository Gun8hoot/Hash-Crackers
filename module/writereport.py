import time, os 

def writerep(pipe):
    path = "report/"
    try:
        os.makedirs(path)
    except FileExistsError:
        pass
    cr_report = open(path + time.strftime('%d-%m-%Y') + "_report-crackers.txt", "w")
    report = cr_report.writelines(H4sh)

    writerep(H4sh)