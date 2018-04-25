#coding: utf-8

class id_calc:
    def __init__(self):
        self.id_list = []
        with open("./id.txt", "r") as f:
            a = f.readlines()
	    self.id_list = list(map(lambda num:int(num), a))

    def calclist(self):
        sumoflist = 0
        for i in self.id_list:
	    sumoflist += i

	return sumoflist


if __name__ == "__main__":
    Calc = id_calc()
    ans = Calc.calclist()
    print(ans)
