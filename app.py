def timer(time):
    """Timer"""
    day, hour, mnt, sec = time // 86400, time % 86400 // 3600, time % 86400 % 3600 // 60, time % 60
    sub1, sub2  = 'day'+'s'*(day > 1), 'hour'+'s'*(hour > 1)
    sub3, sub4 = 'minute'+'s'*(mnt > 1), 'second' + 's'*(sec > 1) + '.'
    print("%d %s %d %s %d %s %d %s"%(day, sub1, hour, sub2, mnt, sub3, sec, sub4))
timer(int(input()))
