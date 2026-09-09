class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        class Counter():
            def __init__(self, my_str):
                self.my_str = my_str

            def count_map(self):
                x = {}
                for i in self.my_str:
                    if i in x:
                        x[i] += 1
                    else:
                        x[i] = 1
                return x

        s_count = Counter(s).count_map()
        t_count = Counter(t).count_map()
        if s_count == t_count:
            return True
        else:
            return False