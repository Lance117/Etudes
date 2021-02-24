class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        res = []
        fileMap = {}
        for path in paths:
            pSplit = path.split(' ')
            dPath = pSplit[0]
            for f in pSplit[1:]:
                oParen, cParen = f.index('('), f.index(')')
                fName, fContents = f[:oParen], f[oParen+1:cParen]
                fileMap[fContents] = fileMap.get(fContents, [])
                fullPath = dPath + '/' + fName
                fileMap[fContents].append(fullPath)
        for p, c in fileMap.items():
            if len(c) > 1:
                res.append(c[:])
        return res
