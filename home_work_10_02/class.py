class My_refrigerator():
    def __init__(self, colour, brand, no_of_doors):
        self.colour = colour
        self.brand = brand
        self.no_of_doors = no_of_doors

    def ref_temperature(self, temp):
        str1 = "temperature of refrigerator is {}".format(temp)
        return str1


# mrt = My_refrigerator("BLACK", "WHIRLPOOL", '2')
print(type(mrt))
print(mrt.colour)
print(mrt.brand)
print(mrt.no_of_doors)
result1 = mrt.ref_temperature(40)
print(result1)


class My_mobile():
    def __init__(self, colour, brand):
        self.colour = colour
        self.brand = brand

    def contact_number(self, contact_number):
        str1 = "my contact {}".format(contact_number)
        return str1

    def price(self, price):
        str2 = "price of mobile {}".format(price)
        return str2

    def memory(self, memory):
        str3 = "memory of the mobile {}".format(memory)
        return str3


mmb = My_mobile("pink", "samsung")
print(type(mmb))
print(mmb.colour)
print(mmb.brand)
result1 = mmb.contact_number(925678120)
print(result1)
result2 = mmb.price("13k")
print(result2)
result3 = mmb.memory("126gb")
print(result3)


class My_house():
    def __init__(self, colour, doors, bed_rooms):
        self.colour = colour
        self.doors = doors
        self.bed_rooms = bed_rooms

    def no_of_pepeple(self, no_of_people):
        str1 = "people in the house {}".format(no_of_people)
        return str1

    def builder(self, builder):
        str2 = "construction builder:{}".format(builder)
        return str2


mmh = My_house("white", "4", "4")
print(type(mmh))
print(mmh.colour)
print(mmh.doors)
print(mmh.bed_rooms)
result1 = mmh.no_of_pepeple(9)
print(result1)
result2 = mmh.builder("edge homes")
print(result2)


class My_bakery():
    def __init__(self, cakes, biscuits, chocolates):
        self.cakes = cakes
        self.biscuits = biscuits
        self.chocolates = chocolates

    def no_of_staff(self, no_of_staff):
        str1 = "staff in the bakery {}".format(no_of_staff)
        return str1

    def open_time(self, open_time):
        str2 = "opening time of bakery:{}".format(open_time)
        return str2

    def close_time(self, close_time):
        str3 = "opening time of bakery:{}".format(close_time)
        return str3


mbk = My_bakery("all flavours,customization available for cakes ", "all type of biscuits", "all varieties")
print(type(mbk))
print(mbk.cakes)
print(mbk.biscuits)
print(mbk.chocolates)
print(mbk.no_of_staff(10))
result1 = mbk.open_time("9am")
print(result1)
result2 = mbk.close_time("9pm")
print(result2)


class My_bank():
    def __init__(self, staff, cash, customers, lockers):
        self.staff = staff
        self.cash = cash
        self.customers = customers
        self.lockers = lockers

    def branch(self, branch):
        str1 = "name of the branch {}".format(branch)
        return str1

    def home_loans(self, home_loan):
        str2 = "number of home loans:{}".format(home_loan)
        return str2

    def gold_loan(self, gold_loan):
        str3 = "number of gold_loans:{}".format(gold_loan)
        return str3


mbb = My_bank("15", "10lakhs", "10", "10")
print(type(mbb))
print(mbb.staff)
print(mbb.cash)
print(mbb.customers)
print(mbb.lockers)
result1 = mbb.branch("eluru")
print(result1)
result2 = mbb.home_loans("10")
print(result2)
result2 = mbb.home_loans("10")
print(result2)
result3 = mbb.gold_loan("10")
print(result3)
