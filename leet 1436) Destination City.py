import sys

class Solution(object):
    def destCity(self, paths):
        start = set()
        end = set()

        for city in paths:
            start.add(city[0])
            end.add(city[1])

        return (end - start).pop()

paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]

Solution.destCity(paths)