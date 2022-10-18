import argparse

parser = argparse.ArgumentParser()
parser.add_argument("blog")
args = parser.parse_args()

print(args)
print(args.blog)
