
def solution(numbers, hand):
    answerList = []

    left = [1, 4, 7, "*"]
    right = [3, 6, 9, "#"]
    middle = [2, 5, 8, 0]
    leftIdx = 3
    rightIdx = 3

    leftMiddle = 0
    rightMiddle = 0
    for n in numbers:
        if n in [1, 4, 7]:
            leftIdx = left.index(n)
            leftMiddle = 0
            answerList.append("L")
        elif n in [3, 6, 9]:
            rightIdx = right.index(n)
            rightMiddle = 0
            answerList.append("R")
        else:
            middleIdx = middle.index(n)
            if abs(middleIdx - leftIdx) - leftMiddle < abs(middleIdx - rightIdx) - rightMiddle:
                leftIdx = middleIdx
                answerList.append("L")
                leftMiddle = 1
            elif abs(middleIdx - leftIdx) - leftMiddle > abs(middleIdx - rightIdx) - rightMiddle:
                rightIdx = middleIdx
                answerList.append("R")
                rightMiddle = 1
            else:
                if hand == "left":
                    leftIdx = middleIdx
                    answerList.append("L")
                    leftMiddle = 1
                else:
                    rightIdx = middleIdx
                    answerList.append("R")
                    rightMiddle = 1
    
    answer = ''.join(answerList)
    
    return answer

numbers2 = [7, 0, 8, 2, 8]	

hand2 = "left"	

print(solution(numbers2, hand2))


'''
 LRLLR
 LRLLL

'''