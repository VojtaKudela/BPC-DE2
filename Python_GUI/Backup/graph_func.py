
def set_xlabel(self):
    match (self.time_scale.get()):
        case 'Last minute':
            self.ax.set_xlabel('Time [sec]')
        case 'Last hour':
            self.ax.set_xlabel('Time [min]')
        case 'Last day':
            self.ax.set_xlabel('Time [hour]')
        case 'Last week':
            self.ax.set_xlabel('Time [day]')
        case 'Last month':
            self.ax.set_xlabel('Time [day]')
        case 'Last year':
            self.ax.set_xlabel('Time [month]')
        case _:
            self.ax.set_xlabel('Time [year]')

def set_ylabel(self):
    match (self.radio_var.get()):
        case 1:
            self.ax.set_ylabel('Temperature [°C]')
        case 2:
            self.ax.set_ylabel('Humidity [%]')
        case 3:
            self.ax.set_ylabel('Soil moisure [%]')
        case _:
            self.ax.set_ylabel('Illumination [lx]')

def n_of_days(month,year):
    # April, June, September and November have 30 days
    if ((month == "4") | (month == "6") | (month == "9") | (month == "11")):
        return 30
    # February 28 or 29 days
    elif ((month == "2")):
        if ((int(year) % 4) == 0):
            # leap year
            return 29
        else:
            # normal year
            return 28
    # Other months have 31 days
    else:
        return 31
    
def n_of_days_year(year):
    if (int(year) % 4 == 0):
        return 365
    else:
        return 366
    
# Number of day bofore tihs month
def n_of_days_cum(month,year):
    match(month):
        case "1":
            return 0
        case "2":
            return n_of_days("1",year)
        case "3":
            return n_of_days("1",year) + n_of_days("2",year)
        case "4":
            return n_of_days("1",year) + n_of_days("2",year) + n_of_days("3",year)
        case "5":
            return n_of_days("1",year) + n_of_days("2",year) + n_of_days("3",year) + n_of_days("4",year)
        case "6":
            return n_of_days("1",year) + n_of_days("2",year) + n_of_days("3",year) + n_of_days("4",year) + n_of_days("5",year)
        case "7":
            return n_of_days("1",year) + n_of_days("2",year) + n_of_days("3",year) + n_of_days("4",year) + n_of_days("5",year) + n_of_days("6",year)
        case "8":
            return n_of_days("1",year) + n_of_days("2",year) + n_of_days("3",year) + n_of_days("4",year) + n_of_days("5",year) + n_of_days("6",year) + n_of_days("7",year)
        case "9":
            return n_of_days("1",year) + n_of_days("2",year) + n_of_days("3",year) + n_of_days("4",year) + n_of_days("5",year) + n_of_days("6",year) + n_of_days("7",year) + n_of_days("8",year)
        case "10":
            return n_of_days("1",year) + n_of_days("2",year) + n_of_days("3",year) + n_of_days("4",year) + n_of_days("5",year) + n_of_days("6",year) + n_of_days("7",year) + n_of_days("8",year) + n_of_days("9",year) 
        case "11":
            return n_of_days("1",year) + n_of_days("2",year) + n_of_days("3",year) + n_of_days("4",year) + n_of_days("5",year) + n_of_days("6",year) + n_of_days("7",year) + n_of_days("8",year) + n_of_days("9",year) + n_of_days("10",year)
        case "12":
            return n_of_days("1",year) + n_of_days("2",year) + n_of_days("3",year) + n_of_days("4",year) + n_of_days("5",year) + n_of_days("6",year) + n_of_days("7",year) + n_of_days("8",year) + n_of_days("9",year) + n_of_days("10",year) + n_of_days("11",year)
