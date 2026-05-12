class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        
        # 00:00
        # 23:59
        # [2,0,5,9]

        # []: x = 0 - 2
        # []: x = 0 - 9
        # []: x = 0 - 5
        # []: x = 0 - 9

        self.time = 0
        self.best_time = 0
        self.res = ""

        def dfs(idx:int) -> None:
            
            if idx == 4:
                print(f"new time found: {self.time}")
                if self.time > self.best_time:
                    self.best_time = self.time

                    self.time = str(self.time)
                    if len(self.time) == 3:
                        self.time = "0" + self.time

                    self.res = str(self.time[:2]) + ":" + str(self.time[2:])
                elif self.time == 0:
                    self.res = "00:00"
                return

            for i in range(len(arr)):
                original_num = arr[i]

                if original_num != "#":
                    original_time = self.time

                    if idx == 0:
                        if original_num <= 2:
                            self.time = original_num
                            print(f"idx = {idx}, time = {self.time}")

                            arr[i] = "#"
                            dfs(idx + 1)

                    elif idx == 1:
                        if self.time < 2:
                            self.time *= 10
                            self.time += original_num
                            print(f"idx = {idx}, time = {self.time}")

                            arr[i] = "#"
                            dfs(idx + 1)
                        elif self.time == 2:
                            if original_num >= 0 and original_num <= 3:
                                self.time *= 10
                                self.time += original_num
                                print(f"idx = {idx}, time = {self.time}")

                                arr[i] = "#"
                                dfs(idx + 1)

                    elif idx == 2:
                        if original_num >= 0 and original_num <= 5:
                            self.time *= 10
                            self.time += original_num
                            print(f"idx = {idx}, time = {self.time}")

                            arr[i] = "#"
                            dfs(idx + 1)
                    elif idx == 3:
                        self.time *= 10
                        self.time += original_num
                        print(f"idx = {idx}, time = {self.time}")

                        arr[i] = "#"
                        dfs(idx + 1)

                    # reset
                    print("")
                    arr[i] = original_num
                    self.time = original_time

        dfs(0)
        

        return self.res
        