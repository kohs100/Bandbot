import argparse

parser = argparse.ArgumentParser(description='Argparse Tutorial')
# argument는 원하는 만큼 추가한다.
parser.add_argument('--prints-number', type=int, 
                    help='an integer for printing repeatably')

args = parser.parse_args()

for i in range(args.prints_number):
    print('print number {}'.format(i+1))