class Solution:
    def mincostTickets(self, days, costs):
        day_size = days[len(days) - 1]
        days = set(days)
        dp = [0 for i in range(day_size + 1)]
        for i in range(1, day_size + 1):
            if i in days:
                dp[i] = min(dp[i - 1] + costs[0], dp[max(0, i - 7)] +
                            costs[1], dp[max(0, i - 30)] + costs[2])
            else:
                dp[i] = dp[i - 1]
        return dp[day_size]

    def mincostTickets2(self, days, costs):
        dp = [0 for _ in range(396)]
        days = set(days)
        for i in reversed(range(1, 366)):
            if i in days:
                dp[i] = min(dp[i + 1] + costs[0], dp[i + 7] +
                            costs[1], dp[i+30] + costs[2])
            else:
                dp[i] = dp[i+1]
        return dp[1]
