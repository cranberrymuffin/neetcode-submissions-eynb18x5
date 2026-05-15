class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        times = []
        for (pos, speed) in sorted(zip(position, speed), reverse = True):
            toAppend = ((target - pos) / speed)
            if(len(times) > 0):
                if(times[-1] < toAppend):
                    times.append(toAppend)
            else:
                times.append(toAppend)
        
        return len(times)

        