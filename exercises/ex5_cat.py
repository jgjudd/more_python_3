import argparse

parser = argparse.ArgumentParser()

parser.add_argument('files', metavar='F', type=str, nargs='+')
parser.add_argument('-n', '--numbers' action='store_true', help='Print line numbers')

args = parser.parse_args()

print(">>> parsed args: ", args)

line_number = 1
for in_file_name in args.files:
  in_file = open(in_file_name)
  if args.numbers:
    for line in in_file.readlines():
      print(f"{i} {line}", end="")
      line_number += 1
    print(in_file.read())