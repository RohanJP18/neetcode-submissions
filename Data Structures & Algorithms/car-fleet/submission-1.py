class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        fleets = 0
        prev_time = 0

        for i in range(len(position)):
            cars.append((position[i],speed[i]))
        
        cars.sort(reverse=True)
    
        for p,s in cars: 
            distance_left = target - p
            time_left = distance_left/s

            if time_left > prev_time:
                fleets += 1
                prev_time = time_left
                

        return fleets        
