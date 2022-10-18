import argparse

parser = argparse.ArgumentParser()
parser.add_argument('blog1', nargs='?', default="Guido van rossum", help="Enter name here.", type=str)
parser.add_argument('blog2', nargs='?', default="Python", help="Enter lang here.", type=str)
parser.add_argument('blog3', nargs='?', help="Enter version here.", type=int)
args = parser.parse_args()

if args.blog1 == "Guido van rossum" and args.blog2 == "Python":
    print('You made it!')

else:
    print("Didn't make it!")

print(args.blog3)

