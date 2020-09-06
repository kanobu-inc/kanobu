class User:
    def __init__(self, name):
        self.name = name

        enter = input(f"{self.name} enter choice... ")

        if enter == "1" or enter == "2" or enter == "3":
            self.choice = enter - 1
        else:
            print("Введите число от 1 до 3")
            exit()
