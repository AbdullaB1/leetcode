class Solution:
    def simplifyPath(self, path: str) -> str:
        dirs = path.split('/')
        result = []
        for d in dirs:
            if d == "..":
                if result:
                    result.pop()
            # elif d - против путей вида "//home/"
            elif d and d != '.':
                result.append(d)
        return '/' + '/'.join(result)
