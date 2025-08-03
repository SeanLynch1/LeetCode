import random

class RandomizedSet:

    def __init__(self):
        # dictionary, used to keep track of number's index
        self.my_dict = {}
        # array, used to select random number in O(1)
        self.my_array = []

    def insert(self, val: int) -> bool:
        if val in self.my_dict:
            return False
        
        self.my_dict[val] = len(self.my_array)
        self.my_array.append(val)

        return True

    def remove(self, val: int) -> bool:
        if val not in self.my_dict:
            return False

        # find index position
        index_pos = self.my_dict[val]
        last_val = self.my_array[-1]

        # update number in array at index_position with last value added
        self.my_array[index_pos] = last_val
        self.my_dict[last_val] = index_pos

        # remove last value added
        self.my_array.pop()

        # update last val in dict to equal array position
        del self.my_dict[val]

        return True

    def getRandom(self) -> int:
        return random.choice(self.my_array)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()