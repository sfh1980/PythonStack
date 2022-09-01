#OOP
#Objects-things, items, have properties and attributes
    #emphasizes grouping data and functionality in entities known as Objects

cat1_data = {
    'name': 'Scar',
    'color': 'dark brown',
    'age': 3,
    'breed': 'lion'
}
cat2_data = {
    'name': 'Garfield',
    'color': 'orange/striped',
    'age': 30,
    'breed': 'lasagna'
}

class Cat():   #Cat() is a class. Creation of an instsance of a class - Instantination
    all_cats = []
    def __init__(self, cat_data):    #special function. when called designates space in memory to store data
        self.name = cat_data['name']
        self.color = cat_data['color']
        self.age = cat_data['age']
        self.breed = cat_data['breed']
        Cat.all_cats.append(self)

    def print_info(self):
        print(f"name:{self.name} color:{self.color} age:{self.age} breed:{self.breed}")
        return self
    def meow(self):
        print(f"{self.name} lets out a cry: MEOOWWW")
        return self

cat1 = Cat(cat1_data)
cat2 = Cat(cat2_data) 

#Constructor -funtion that contains instructions for making new instance (individual object of a certain class) of a Class. An object that belongs to a class is an instace of the class.


cat1.print_info().meow()
for one_cat in Cat.all_cats:
    one_cat.print_info()