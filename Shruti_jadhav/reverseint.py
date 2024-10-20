class Num:
    def __init__(self,a): #constructor
        self.input_int=a
    def reverse(self):  # class is called by which object is denoted by self
        int_to_str=str(self.input_int)
        reverse_str=int_to_str[::-1]
        return int(reverse_str)
a1=Num(1000)   #object
print(a1.reverse())

a2=Num(34435435)
print(a2.reverse())
