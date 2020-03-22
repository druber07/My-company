class date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def show(self):
        print(self.year,",",self.month,",",self.day)


class person:
    def __init__(self, Fname, Sname, tp, Id, birthday, Fday, FuSalary,
                 BaSalary, BoSalary):
        self.Fname = Fname
        self.Sname = Sname
        self.tp = tp
        self.Id = Id
        self.birthday = birthday
        self.Fday = Fday
        self.FuSalary = FuSalary
        self.BaSalary = BaSalary
        self.BoSalary = BoSalary

    def show(self):
        return ("Name:", self.Fname, self.Sname + "\nType: ",
                self.tp + "\nId: ", self.Id + "\nBirthday: ",
                self.birthday + "\nSalary:", self.FuSalary + "(Bonus:",
                BoSalary + ")")


class manager(person):
    def __init__(self, Fname, Sname, tp, Id, birthday, Fday, FuSalary,
                 BaSalary, BoSalary, buyers, Npr, Nds):
        super().__init__(Fname, Sname, tp, Id, birthday, Fday, FuSalary,
                         BaSalary, BoSalary)
        self.buyers = buyers
        self.Npr = Npr
        self.Nds = Nds

    def show(self):
        return (self.show() + "\nNumber of buyers:",
                self.buyers + "\nNumber of programers:",
                self.Npr + "\nNumber of designers", self.Nds)


class worker(person):
    def __init__(self, Fname, Sname, tp, Id, birthday, Fday, FuSalary,
                 BaSalary, BoSalary, managerN, hours, bonus):
        super().__init__(Fname, Sname, tp, Id, birthday, Fday, FuSalary,
                         BaSalary, BoSalary)
        self.managerN = managerN
        self.hours = hours
        self.bonus = bonus

    def show(self):
        return (self.show() + "\nManager's name:",
                self.managerN + "\nHours worked day:",
                self.hours + "\nBonus per hour in a day", self.bonus)