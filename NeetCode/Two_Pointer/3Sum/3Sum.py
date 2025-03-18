class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        pos,neg =[],[]
        res = set()
        zero = 0
        for n in nums:
            if n > 0:
                pos.append(n)
            elif n < 0:
                neg.append(n)
            else:
                zero +=1
        POS,NEG = set(pos),set(neg)
        if zero:
            if zero >= 3:
                res.add(tuple([0,0,0]))
            for p in pos:
                if -p in NEG:
                    res.add(tuple([-p,0,p]))

        for i,p1 in enumerate(pos,0):
            for p2 in pos[i+1:]:
                if -(p1 + p2) in NEG:
                    if p1 > p2:
                        res.add(tuple([-(p1 + p2),p2,p1]))
                    else:
                        res.add(tuple([-(p1 + p2),p1,p2]))

        for i,n1 in enumerate(neg,0):
            for n2 in neg[i+1:]:
                if -(n1+n2) in POS:
                    if n1 > n2:
                        res.add(tuple([n1,n2,-(n1+n2)]))
                    else:
                        res.add(tuple([n2,n1,-(n1+n2)]))
        return list(res)
