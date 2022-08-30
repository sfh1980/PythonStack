#empty_list = []
#ninjas = ['Rozen', 'KB', 'Oliver']
#print(ninjas[2])
#ninjas[0] = 'Francis'
#ninjas.append('Michael')
#print(ninjas)
#ninjas.pop()
#print(ninjas)
#ninjas.pop(1)
#print(ninjas)


#empty_dict = {}
#new_person = {'name': 'John', 'age': 38, 'weight': 160.2, #'has_glasses': False}
#new_person['name'] = 'Jack'
#new_person['hobbies'] = ['climbing', 'coding']
#print(new_person)
#w = new_person.pop('weight')
#print(w)
#print(new_person)


#name = "Zen"
#print("my name is" + name)

#first_name = 'Zen'
#last_name = 'Coder'
#age = 27
#print(f'My name is {first_name} {last_name} and I am {age} years old.#')

#first_name = "Alana"
#last_name = "Da Silva"
#age = 36
#profession = "Software Developer"
#years_experience = 5

#greeting = "Hello my name is", first_name, last_name

#print('Hello my name is ' + first_name + last_name)

#print(f'I am {age} years old')

#print("I work as a {}.".format(profession))

#exp_string = "I have worked in the field for {} years."
#print(exp_string.format(years_experience))

#output = age - years_experience

#print("I started in the field when I was", output, "years old.")

#fruits = ['apple', 'banana', 'orange', 'strawberry']
#vegetables = ['lettuce', 'cucumber', 'carrots']
#fruits_and_vegetables = fruits + vegetables
#print(fruits_and_vegetables)
#salad = 3 * vegetables
#print(salad)


def flex_countdown(low, high, mult):
    for i in range (low, high):
        if i % mult == 0:
            print (i)
            
flex_countdown(2, 9, 3)


