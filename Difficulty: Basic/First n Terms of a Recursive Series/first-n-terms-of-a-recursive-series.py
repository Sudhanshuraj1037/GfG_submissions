class Solution:
    def gfSeries(self, n):
        # code here
        if n <= 0:
            return []
        if n == 1:
            return 1
        series = [0,1]
        for i in range(2,n):
            next_term = (series[i - 2] ** 2) - series[i - 1]
            series.append(next_term)
        return series