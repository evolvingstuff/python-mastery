with open('../../Data/portfolio.dat') as f:
    lines = f.readlines()
total = 0
for line in lines:
    line = line.replace('\n', '')
    ticker, shares, cost = line.split(' ')
    shares, cost = int(shares), float(cost)
    total += shares * cost
print(f'total = ${total:,.2f}')