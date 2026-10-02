class TimeMap:

    def __init__(self):
        self.timeMap = {} # key: [value, timestamp]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timeMap:
            self.timeMap[key] = []
        self.timeMap[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res, values = "", self.timeMap.get(key, [])
        l, r = 0, len(values) - 1

        while l <= r:
            m = (l+r) // 2

            if values[m][1] <= timestamp:
                res = values[m][0] # string vals associated with m num timestamp
                l = m + 1 # check if theres a timestamp thats bigger
            else:
                r = m - 1
        
        return res
