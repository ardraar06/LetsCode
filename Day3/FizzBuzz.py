from typing import List

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:

        answer = []   # empty list to store results

        for i in range(1, n + 1):   # loop from 1 to n

            if i % 3 == 0 and i % 5 == 0:
                answer.append("FizzBuzz")

            elif i % 3 == 0:
                answer.append("Fizz")

            elif i % 5 == 0:
                answer.append("Buzz")

            else:
                answer.append(str(i))

        return answer
