#aattempt1:
class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        steps = 0
        while(target != startValue and target>startValue):
            if target%2:
                target += 1
            else:
                target //= 2
            steps += 1
        return steps + (startValue-target)
