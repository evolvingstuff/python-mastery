import sys


def portfolio_cost(path):
    with open(f'../../{path}') as f:
        lines = f.readlines()
    total = 0
    for line in lines:
        line = line.replace('\n', '')
        ticker, shares, cost = line.split(' ')
        shares, cost = int(shares), float(cost)
        total += shares * cost
    return total


if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise SystemExit("Usage: pcost.py path")
    print(portfolio_cost(sys.argv[1]))