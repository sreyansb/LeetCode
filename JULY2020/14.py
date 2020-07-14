#for every hour->30 degrees used.
#for every minute->6 degrees used.
#for every 12 minutes->hour hand moves by 12 degrees
class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        if hour==12:
            hour=0
        k=abs(hour*30+minutes/2-minutes*6)
        return min(360-k,k)
