class Solution(object):
    def isAnagram(self, s, t):
        if (len(s) != len(t)):
            return False
        else:
            s_sort = sorted(s)
            t_sort = sorted(t)
            return s_sort == t_sort

        