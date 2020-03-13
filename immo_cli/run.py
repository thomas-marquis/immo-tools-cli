import argparse
from immo_tools import calculator


display = print
BASE_DURATION_UNIT = 'year'


def get_loan(amount, duration, year_rate, insurance_rate):
    loan = calculator.build_loan(
        duration,
        amount,
        year_rate,
        insurance_rate,
        duration_unit=BASE_DURATION_UNIT,
        build_summary=True)
    return loan


def handle_cost(args):
    loan = get_loan(args.amount, args.duration, args.rate, args.insurance_rate)
    cost = loan.get_cost(args.duration if not args.years else args.years, to_string=True)
    display(cost)


def route(info, args):
    if info == 'cost':
        handle_cost(args)
    elif info == '':
        pass
    else:
        display(f'{info} is not a valid argument')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('info', help='specify info to return', type=str)
    parser.add_argument('years', help='years before sale', type=int, default=None)
    parser.add_argument('-a', '--amount', type=int, help='main capital amount. example: 300000', required=True)
    parser.add_argument('-r', '--rate', type=float, help='year rate. example: 1.5', default=.0)
    parser.add_argument('-i', '--insurance-rate', type=float, help='example: 0.5', default=.0)
    parser.add_argument('-d', '--duration', type=int, help=f'duration in {BASE_DURATION_UNIT}', default=25)

    args = parser.parse_args()
    route(args.info, args)


if __name__ == '__main__':
    main()
