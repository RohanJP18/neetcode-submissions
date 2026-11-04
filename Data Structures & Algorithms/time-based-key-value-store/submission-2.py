class TimeMap:
        
    def __init__(self):
        self.key_val_ds = {} # key : [(value,time)]

    def set(self, key: str, value: str, timestamp: int) -> None: # O(1)
        if key not in self.key_val_ds:
            self.key_val_ds[key] = []
        self.key_val_ds[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str: # O(logn)
        # if its the only tuple with the key
        # if the provided time stamp not there you take the largest previous one
        l = 0
        res = ""
        if key not in self.key_val_ds:
            return ""
            
        val_timestamp_list = self.key_val_ds[key]
        r = len(val_timestamp_list) - 1
        while l <= r:
            m = l + (r-l)//2
            if val_timestamp_list[m][1] <= timestamp:
                res = val_timestamp_list[m][0]
                l = m + 1
            else:
                r = m - 1
        return res