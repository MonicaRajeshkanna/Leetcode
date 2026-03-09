class Solution:
    def compareVersion(self, version1, version2):
        rev1 = version1.split(".")
        rev2 = version2.split(".")
        
        n = max(len(rev1), len(rev2))
        
        for i in range(n):
            v1 = int(rev1[i]) if i < len(rev1) else 0
            v2 = int(rev2[i]) if i < len(rev2) else 0
            
            if v1 > v2:
                return 1
            elif v1 < v2:
                return -1
        
        return 0