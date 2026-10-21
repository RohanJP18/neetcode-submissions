class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for current_index, current_temp in enumerate(temperatures):
            # if the current temp is greater than the top of the stack and stack exists
            while stack and current_temp > temperatures[stack[-1]]:
                prev_index = stack.pop()
                res[prev_index] = current_index - prev_index
                # pop, store prev_index
                # res[prev_index] = current_index - prev_index 
            # if the current temp is greater than the top of the stack, append
            stack.append(current_index)
            
        return res
    
