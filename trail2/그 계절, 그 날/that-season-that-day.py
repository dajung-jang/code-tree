y, m, d = map(int, input().split())

# 윤년인지 아닌지 확인
def is_yoou(y):
    return (y % 4 == 0 and y % 100 != 0) or y % 400 == 0

# 해당 달의 마지막 날 반환 함수
def last_day_check(y, m):
    if m == 2:
        if is_yoou(y): return 29
        return 28
    elif m in (4, 6, 9, 11): return 30
    return 31

# 해당 월의 일이 존재하는지 확인 함수
def posi_day(y, m, d):
    return m <= 12 and d <= last_day_check(y, m)


# 계절 출력
def season(y, m, d):
    if posi_day(y, m, d):
        if m in (3, 4, 5): return 'Spring'
        if m in (6, 7, 8): return 'Summer'
        if m in (9, 10, 11): return 'Fall'
        return 'Winter'
    return -1
print(season(y, m, d))