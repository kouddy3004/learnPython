
class GenericSet():

    def fibonacciSeries(self, maxNumber):
        cRow = 0
        nRow = 1
        list = []
        list.append(cRow)
        for i in range(maxNumber):
            cRow = cRow + nRow
            nRow = cRow - nRow
            list.append(cRow)
        print(list)