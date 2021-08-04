def deposit(start, deposits, percent, years):
    i = 0
    end_deposit = int(start)
    perc = float(percent) / 100 * end_deposit
    _years = float(years) * 12
    while i < _years:
        i += 1
        end_deposit += int(deposits)
        if i in range(0, int(_years) + 1, 12):
            end_deposit = end_deposit + perc
    print(end_deposit)


x = input('Enter start deposit:')
y = input('Enter monthly deposit:')
z = input('Enter percent:')
a = input('Enter for what years deposit:')

deposit(start=x, deposits=y, percent=z, years=a)