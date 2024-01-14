class Human:
    def __init__(self, name, age, height, sex):
        if not name: raise ValueError(" Missing name ") 
        if not age: raise ValueError(" Missing age ")
        if not height: raise ValueError(" Misssing height ")
        if not sex: raise ValueError(" Missing sex ")
        self.name = name
        self.age = age
        self.height = height
        self.sex = sex
    # def __str__(self):
    #     return f" My name is {self.name} and age is {self.age}, height is {self.height}, sex is {self.sex}. "
 




def get_human():
    name = input(" What is your name? ")
    age = float(input(" What is your age? "))
    height = float(input(" What is your height? "))
    sex = input(" What is you sex? ")
    human = Human(name, age, height, sex)
    return human

def main():
    human = get_human()
    print(f" My name is {human.name}, age is {human.age}, height is {human.height} and sex is {human.sex}. ")

if __name__ == "__main__":
    main()