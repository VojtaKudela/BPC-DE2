
from data_file import data_file
from raw_data import raw_data

class database:
    def __init__(self):
        self.data = []

    def load_data(self):
        self.data = []
        f = open("database.txt","r")
        lines = f.readlines()

        for i in range(1,len(lines),1):
            line = lines[i].split("\t")
            self.data.append({"year":line[0],"month":line[1],"date":line[2],
                              "day":line[3],"hour":line[4],"min":line[5],
                              "sec":line[6],"temp":line[7],"hum":line[8],
                              "lig":line[9],"soil":line[10]})
        f.close()
