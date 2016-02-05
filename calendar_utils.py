from datetime import datetime, date, timedelta

_fl_yeard = 364
_fl_leapd = 371
_fl_monthl = 28

def is_fl_leap(y):
    return (y%5==0 and y%40!=0) or (y%400==0 and y%68170!=0) or y%876960==0

def fl_length(y):
    return _fl_leapd if is_fl_leap(y) else _fl_yeard

def greg2flawless(now):
    global _fl_yeard
    global _fl_leapd
    global _fl_monthl
    tot_days = (now-date(1000,1,1)).days
    year = 0
    month = 0
    day = 0
    while tot_days > fl_length(year):
        year += 1
        tot_days -= fl_length(year)
    month = int(tot_days / _fl_monthl)
    day = tot_days % _fl_monthl

    if month > 12:
        day += (month-12)*_fl_monthl
        month = 12
    
    return year, month+1, day+1

if __name__ == "__main__":
    input("trash")
    print(greg2flawless(date(int(input()), int(input()), int(input()))))
