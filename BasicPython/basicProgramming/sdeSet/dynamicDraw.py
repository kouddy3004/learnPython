

class DynamicDraw():
    def catDraw(self,number):
        for rep in range(1,number):
            endn=((number+2)-rep)
            for i in range(1,endn):
                if((i<rep)):
                    i=" "
                print(i,end ="")
            print()

    def halfPyramid(self,number):
        for rep in range(1,number):
            print(rep*"*")

    def inHalfPyramid(self,number):
        for rep in range(number,0,-1):
            print(rep*"*")

    def fullPyramid(self,number):
        for i in range(number):
            print(number*("*"))