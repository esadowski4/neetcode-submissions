class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res= []
        combo = []
        digitToLetter = { "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        
        def backtrack(i):
            if i >= len(digits):
                res.append("".join(combo))
                return
            
            # add letter
            for c in digitToLetter[digits[i]]:
                combo.append(c)
                backtrack(i + 1)
                combo.pop()
        if not digits:
            return []    
        backtrack(0)
        return res