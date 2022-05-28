class Student:
    # [assignment] Skeleton class. Add your code here
    
    
    def __init__(self, name, age, tracks, score):
        self.name=name
        self.age=age
        self.tracks=tracks
        self.score=score
        
    def change_name(self,name):
        self.name = name

    def change_age(self, age):
        try:
            new_age = int(age)
            self.age = new_age
        except:
            print('Please enter a valid age ')
        else:
            print('Age sucessfully changed')

    def add_track(self, track):
        try:
            self.tracks.append(track)
             
        except:
            print('error')                                   
        else:
            print('Track sucessfully added')
            
    def get_score(self):
        print('Your score is ', self.score)
    


Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)


# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()