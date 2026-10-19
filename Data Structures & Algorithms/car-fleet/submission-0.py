class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet_num = 0
        prev = 0
        
        # pair up position and speed and sort in decending order (closest to target)
        cars = sorted(zip(position,speed), reverse=True)

        # cannot pass a car ahead of it
        for pos,speed in cars:
            time = (target - pos) / speed
            if time > prev:
                fleet_num += 1
                prev = time

        return fleet_num
