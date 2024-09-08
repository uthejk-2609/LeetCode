class Solution:
    def convertDateToBinary(self, date: str) -> str:
        year, month, day = date.split('-')

        binary_year = bin(int(year))[2:]
        binary_month = bin(int(month))[2:]
        binary_day = bin(int(day))[2:]

        return f"{binary_year}-{binary_month}-{binary_day}"
