class DisjSet:
    def __init__(self, n):
        self.rank = [1] * n
        self.parent = [i for i in range(n)]

    def find(self, x):

        if (self.parent[x] != x):

            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    def Union(self, x, y):
        xset = self.find(x)
        yset = self.find(y)

        if xset == yset:
            return

        if self.rank[xset] < self.rank[yset]:
            self.parent[xset] = yset

        elif self.rank[xset] > self.rank[yset]:
            self.parent[yset] = xset

        else:
            self.parent[yset] = xset
            self.rank[xset] = self.rank[xset] + 1


obj = DisjSet(10)
obj.Union(0, 1)
obj.Union(1, 2)
obj.Union(3, 2)
obj.Union(4, 3)
obj.Union(5, 6)
obj.Union(6, 7)
obj.Union(7, 8)
obj.Union(8, 9)
obj.Union(9, 2)

if obj.find(4) == obj.find(0):
    print('Yes')
else:
    print('No')
if obj.find(1) == obj.find(0):
    print('Yes')
else:
    print('No')
