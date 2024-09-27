def timeConversion(s:str):
    if 'AM' in s:
        s = s.replace('AM', '')
        hour = int(s[:2])
        if hour == 12:
            s = '00' + s[2:]
    else:
        s = s.replace('PM', '')
        hour = int(s[:2])
        if hour != 12:
            hour = hour + 12
            s = str(hour).zfill(2) + s[2:]
    return s

