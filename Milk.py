class Milk:
    total_value = 0

    def __init__(self, type='Coconut Milk', data='28', color='white', manufacturer='Milky Way', value=255.55):
        self.type = type
        self.__data = data
        self.color = color
        self.manufacturer = manufacturer
        self.value = value
        Milk.total_value += value

    def to_string(self):
        print('Type: %s \nColor: %s \nManufacturer: %s \nValue: %s' % (
            self.type, self.color, self.manufacturer, self.value))

    def print_sum(self):
        print("Total value of " + self.manufacturer + "'s milks: ", self.value, "$")

    @staticmethod
    def print_static_sum():
        print('Total value: {0} $'.format(Milk.total_value))


if __name__ == '__main__':
    milk0 = Milk()
    milk1 = Milk('Cows Milk', 'White', 'Milk Rabbit', 20.25)
    milk2 = Milk('Goats Milk', 'White', 'Halynka ', 31.55)
    milk3 = Milk('Almond Milk', 'Yellow', 'Kyharochka ', 100.00)
    milk4 = Milk('Coconut Milk ', 'White', 'Milky Way', 255.55)

milk0.to_string
print("\n")
milk1.to_string()
print("\n")
milk2.to_string()
print("\n")
milk3.to_string()
print("\n")
milk4.to_string()
print("\n\n")
milk1.print_sum()
milk2.print_sum()
milk3.print_sum()
milk4.print_sum()
Milk.print_static_sum()


 d ={(1,2,3):1,2:(1,2,3)}

d= {1: (1,2,3),2: (1,2,3)}