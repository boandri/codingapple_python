class I:
    def __init__(self, name):
        self.name = name

class My(I):
    Degree, Skills, Languages, Strength = {}, [], (), []

my_instance = I('Seo Woo Jang')
My.Degree = {'Centennial College': 'Software Engineering Technician', 'Ewha Womans University': 'Music Composition'}
My.Skills = ['Programming', 'Web design', 'Data analysis', 'Computer networking', 'Operating system', 'SCM']
My.Languages = ('Python', 'C#', 'Java', 'JavaScript', 'Node', 'MongoDB', 'Angular', 'React', 'Swift', 'Dart')
My.Strength = ['Curiosity', 'Creativity', 'Detail-oriented', 'Positive attitude', 'Adaptability']

print(my_instance.name)
print(My.Degree)
print(My.Skills)
print(My.Languages)
print(My.Strength)