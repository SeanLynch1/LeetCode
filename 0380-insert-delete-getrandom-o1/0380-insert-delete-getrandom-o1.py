class RandomizedSet:

    def __init__(self):
        self.dict_tracker = {}
        self.list_tracker = []
        

    def insert(self, val: int) -> bool:
        if val not in self.dict_tracker:
            self.dict_tracker[val] = len(self.list_tracker)
            self.list_tracker.append(val)

            return True
        else:
            return False

    def remove(self, val: int) -> bool:

        if val in self.dict_tracker:
            if val == self.list_tracker[-1]:
                self.list_tracker.pop()
                del self.dict_tracker[val]
                return True

            last_val = self.list_tracker.pop()
            self.list_tracker[self.dict_tracker[val]] = last_val

            self.dict_tracker[last_val] = self.dict_tracker[val]
            del self.dict_tracker[val]

            return True
        else:
            return False
        

    def getRandom(self) -> int:

        return random.choice(self.list_tracker)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()