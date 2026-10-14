class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        string = []

        def backtrack(nOpen, nClose):

            if n == nOpen == nClose:
                res.append("".join(string))
                return

            if nOpen < n:
                string.append("(")
                backtrack(nOpen+1, nClose)
                string.pop()
            
            if nClose < nOpen:
                string.append(")")
                backtrack(nOpen, nClose + 1)
                string.pop()
        
        backtrack(0,0)
        return res
