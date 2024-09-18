class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        # prices.sort()

        # if prices[0] + prices[1] <= money:
        #     return money - prices[0] - prices[1]

        # return money

        first_min, second_min = float("inf"), float("inf")

        for price in prices:
            if price < first_min:
                second_min = first_min
                first_min = price
            elif price < second_min:
                second_min = price

        if first_min + second_min <= money:
            return money - first_min - second_min

        return money
