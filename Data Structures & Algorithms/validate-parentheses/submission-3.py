from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        pth = deque([])
        
        close = {')':'(', ']':'[', '}':'{'}
        for ch in s:
            if ch not in close:
                pth.append(ch)
            else:
                if not pth or pth[-1] != close[ch]:
                    return False
                pth.pop()
                        
        return not pth