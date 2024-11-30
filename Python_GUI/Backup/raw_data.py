class raw_data:

    def __init__(self):
        self.list = []
        self.full = 0

    def add(self,data):
        if (data < 255):
            self.list.append(data)
        else:
            self.full = 1

    def show_bin(self):
        string = 'Binary values: '
        for i in range(0,len(self.list),1):
            string += f'{self.list[i]:b} '
        print(string)

    def show_hex(self):
        string = 'Hexadecimal values: '
        for i in range(0,len(self.list),1):
            string += f'{self.list[i]:x} '
        print(string)

    def show_dec(self):
        string = 'Decimal values: '
        for i in range(0,len(self.list),1):
            string += f'{self.list[i]} '
        print(string)
