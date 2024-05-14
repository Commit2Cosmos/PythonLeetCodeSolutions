from collections import defaultdict

class TimeMap:

    def __init__(self):

        def def_val():
            return []
        self.time_map = defaultdict(def_val)


    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append((timestamp, value))

        
    def get(self, key: str, timestamp: int) -> str:
        arr = self.time_map[key]

        #* arr == [(1,'foo'), (2,'foo2')]

        if len(arr) == 0:
            return ''
        
        low = 0
        high = len(arr)-1

        if timestamp < arr[low][0]:
            return ''
        
        res = ''

        while low <= high:

            mid = (high + low) // 2
            
            if arr[mid][0] <= timestamp:
                res = arr[mid][1]
                low = mid+1

            else:
                high = mid-1

        return res




obj = TimeMap()
obj.set("foo", "bar", 1)
print(obj.get("foo", 1))
print(obj.get("foo", 3))
obj.set("foo", "bar2", 4)
print(obj.get("foo", 4))
print(obj.get("foo", 5))