class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ps = sorted(dict(zip(position, speed)).items(), reverse=True)
        time = [None]*len(speed)
        stack = []
        for i,a  in enumerate(ps) :
            time[i] = (target - a[0])/a[1]
        for t in time:
            if stack and stack[-1] >= t:
                continue
            stack.append(t)
        return len(stack)