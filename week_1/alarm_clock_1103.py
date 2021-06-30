def alarm_clock():
    
    h1, m1, h2, m2 = map(int, list(input().split()))

    while True:
        if h1 == m1 == h2 == m2 == 0:
            break   

        if h1 == 0:
            h1 = 24

        if h2 == 0:
            h2 = 24
        
        if h2 < h1:
            sleep_minutes = (24 - (h1 - h2)) * 60
            if m2 < m1:
                sleep_minutes -= m1 - m2
            elif m2 > m1:
                sleep_minutes += m2 - m1

        elif h2 == h1:
            if m2 < m1:
                sleep_minutes = 24 * 60
                sleep_minutes -= m1 - m2
            else:
                sleep_minutes = m2 - m1

        else:
            sleep_minutes = (h2 - h1) * 60
            if m2 >= m1:
                sleep_minutes += m2 - m1
            else:
                sleep_minutes -= m1 - m2
                

        print(sleep_minutes)

        h1, m1, h2, m2 = map(int, list(input().split()))

if __name__ == "__main__":
    alarm_clock()
