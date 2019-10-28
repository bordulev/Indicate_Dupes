# Indicate_Dupes
Find duplicates of electronics in .txt file and update this file with information about dupes

Input filename list.txt
Output filename new_list.txt

Change the path to input and output file in the main.py

Input contains info about VMM3a chips in the CERN ATLAS Database. The task is to indicates duplicates of chips (by the name Correct_OTHER_ID). If so, this dupes should be counted (for every chip) and marked (remove or keep in the database). The rule is simple: if this chip is the first in file - it should be kept, if not - removed.

The output should be the same as input, but with two additional columns: Dupes (number of dupes for every chip) and Flag(Remove or Keep)

Run the code main.py.

Code was written for the Python 2.7.5
