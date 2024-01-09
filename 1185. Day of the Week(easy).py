class Solution(object):
    def dayOfTheWeek(self, day, month, year):
        time = [ 0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4 ]
        week = {
            1:'Monday', 2:'Tuesday', 3:'Wednesday',
            4:'Thursday', 5:'Friday', 6:'Saturday',
            7:'Sunday'
        }
        if month < 3:
            year -= 1

        res = (year + year // 4 - year // 100 + year // 400 + time[month - 1] + day) % 7
        if res < 7 and res > 0:
            return week[res]
        else:
            return week[7]