# Q.2 Using the Pandas library create a one dimensional array.
# Check its default index value and change its index value according to your choice.
# Output should be:
# A	1
# B	2
# C	3
# D	4
# Help : pandas.series

import pandas as pd
a = [1,2,3,4]
s1 = pd.Series(a)
print(s1)
s = pd.Series(a, index=["A","B","C","D"])
print(s)