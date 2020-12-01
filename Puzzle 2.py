from utility import Utility

utility = Utility()
answer = utility.find('triple', utility.inputs)
solution = utility.result(answer[0], answer[1], answer[2])

print(solution)
