import argparse

parser = argparse.ArgumentParser()
parser.add_argument('blog', nargs='?', default="Asit")
args = parser.parse_args()

print("Type=", type(args.blog), "Value=", args.blog)

if args.blog == 'Asit':
    print('You made it!')
else:
    print("Didn't make it!")
