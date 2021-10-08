class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        count = 0
        for i in '{0:032b}'.format(n):
            if i == '1':
                count+=1
        return(count)    