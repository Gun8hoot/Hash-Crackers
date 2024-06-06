import time, os 

def writerep(given_hash, word):
    path_linux = "report/"
    path_win = 'report\\'
    try:
        if os.name == 'nt':
            os.makedirs(path_win)
        else:
            os.makedirs(path_linux)
    except FileExistsError:
        pass

    if os.name == 'nt':
        create_report = open(path_win + time.strftime('%S-%M-%H|%d-%m-%Y') + "_report-crackers.txt", "w")
        write_report = create_report.writelines(f"{given_hash} : {word}")
    else:
        create_report = open(path_linux + time.strftime('%S-%M-%H|%d-%m-%Y') + "_report-crackers.txt", "w")
        write_report = create_report.writelines(f"{given_hash} : {word}")