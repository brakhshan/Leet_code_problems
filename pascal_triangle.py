    def pascal_triangle(self, numRows: int) -> List[List[int]]:
        initial = [[1]]
        for i in range(1,numRows):
            temp = [0] + initial[-1] + [0]
            intermediate = []
            print(len(temp))
            for j in range(len(temp)-1):
                intermediate.append(temp[j] + temp[j+1])
            initial.append(intermediate)
        return initial
