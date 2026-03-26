class HistoryDict:
    def __init__(self):
        self.data = {}
        self.history = {}
    
    def __setitem__(self, key, value):
        self.data[key] = value
        if key not in self.history:
            self.history[key] = []
        self.history[key].append(value)
    
    def __getitem__(self, key):
        return self.data.get(key, 0)
    
    def __call__(self, key):
        return self.history.get(key, [])


hd = HistoryDict()
hd['x'] = 10
hd['x'] = 20
print(hd['x'])
print(hd('x'))
print(hd['y'])