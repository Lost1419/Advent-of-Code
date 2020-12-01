from utility import Utility

utility = Utility()
answer = utility.find('double', utility.inputs)
solution = utility.result(answer[0], answer[1])

print(solution)
