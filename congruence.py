class Solution:
    def dayoftheweek (day: int, month: int, year: int) -> str:

        week = {
            0 : "Saturday",
            1 : "Sunday",
            2 : "Monday",
            3 : "Tuesday",
            4 : "Wednesday",
            5 : "Thursday",
            6 : "Friday"
        }

        d = day
        m = month
        j = year // 100
        k = year % 100

        h = d + 13 * (m + 1) // 5 + k + k // 4 + j // 4 + 5 * j
        h = h % 7

        weekday = week[h]

        return weekday

print(Solution.dayoftheweek(21,9,2022))