class Solution(object):
    def largestAltitude(self, gain):
        constant=0
        new=[]
        new.append(constant)
        for gains in gain:
            constant=constant+gains
            new.append(constant)
        return (max(new))
     