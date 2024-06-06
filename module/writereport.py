import time, os 

def writerep(given_hash, word):
    path = "report/"
    try:
        os.makedirs(path)
    except FileExistsError:
        pass
    
    create_report = open(path + time.strftime('%S-%M-%H|%d-%m-%Y') + "_report-crackers.txt", "w")
    write_report = create_report.writelines(f"{given_hash} : {word}")
