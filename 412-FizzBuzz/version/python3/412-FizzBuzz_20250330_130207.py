# Last updated: 3/30/2025, 1:02:07 PM
# This solution starts employing malbda functions
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        '''
        answer = []
        for i in range(1,n+1):
            if i % 15 == 0:
                answer.append("FizzBuzz") 
                continue
            if i % 5 == 0:
                answer.append("Buzz")
                continue
            if i % 3 == 0:
                answer.append('Fizz')
                continue
            answer.append(f"{i}")

        return answer
        '''
        return [ "Fizz"*(i % 3 == 0) + "Buzz" * (i % 5 == 0) or f"{i}" for i in range(1,n+1)]
        