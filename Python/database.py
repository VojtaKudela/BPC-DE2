
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


#raw = raw_data()
#raw.add(36)
#raw.add(145)
#raw.add(19)
#raw.add(3)
#raw.add(9)
#raw.add(89)
#raw.add(0)
#raw.add(80)
#raw.add(1)
#raw.add(37)
#raw.add(2)
#raw.add(64)
#raw.add(65)
#raw.add(255)

#raw.show_bin()
#raw.show_hex()
#raw.show_dec()

#data = data_file(raw)
#data.create_database()
#data.save_data()
#data.show_data()

#raw1 = raw_data()
#raw1.add(36)
#raw1.add(145)
#raw1.add(19)
#raw1.add(3)
#raw1.add(9)
#raw1.add(89)
#raw1.add(33)
#raw1.add(80)
#raw1.add(4)
#raw1.add(37)
#raw1.add(3)
#raw1.add(64)
#raw1.add(65)
#raw1.add(255)

#data.upgrade_data(raw1)
#data.save_data()
#data.show_data()

#data.upgrade_data(raw)
#data.save_data()
#data.show_data()

#data.upgrade_data(raw1)
#data.save_data()
#data.show_data()

#db = database()
#db.load_data()