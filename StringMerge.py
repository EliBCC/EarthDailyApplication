from collections import Counter                              # To check if lists of strings are equal
import pandas as pd

# Solution
def mergeLists(originalList, addList, rmList):
    # Create dataframes from lists
    originalDF = pd.DataFrame(originalList, columns = ["strings"])
    addDF = pd.DataFrame(addList, columns = ["strings"])

    # Create dataframe with correct values
    ans = originalDF                                                            # Create original list as Pandas dataframe
    if len(originalList) == 0:
        ans = addDF                                                             # If the original list was blank, use the add list instead
    elif len(addList) > 0:
        ans = ans.merge(addDF, how='outer')                                     # If both the original list and the add list contain items, merge them
    ans = ans[~ans.isin(rmList)].dropna()                                       # Drop strings from rmList
        
    # Sort dataframe correctly
    ans["charCount"] = ans["strings"].apply(lambda string: len(string))         # Create column with the length of each string
    ans = ans.sort_values(["charCount", "strings"], ascending=False)            # Sort in reverse order, first by character count, then alphabetically
    
    return ans["strings"].tolist()

# Tests
tests = [\
    {
        "original": ['one', 'two', 'three'],
        "add": ['one', 'two', 'five', 'six'],
        "delete": ['two', 'five'],
        "answer": ['three', 'six', 'one']
    },
    {
        "original": ['two', 'three'],
        "add": [],
        "delete": [],
        "answer": ['three', 'two']
    },
    {
        "original": ['three', 'two'],
        "add": [],
        "delete": [],
        "answer": ['three', 'two']
    },
    {
        "original": [],
        "add": ['two', 'three'],
        "delete": [],
        "answer": ['three', 'two']
    },
    {
        "original": ['two', 'three'],
        "add": [],
        "delete": ['four'],
        "answer": ['three', 'two']
    },
    {
        "original": [],
        "add": [],
        "delete": [],
        "answer": []
    },
]

def runTests():
    for test in tests:
        result = mergeLists(test["original"], test["add"], test["delete"])
        if Counter(result) == Counter(test["answer"]):
            print("Test passed")
        else:
            print("Test failed.\nCase: {}\nResult: {}".format(test, result))

# runTests()

# Run
originalStrings = input("Please enter the original list of strings, separated by commas: ")
addStrings = input("Please enter a list of strings to add, separated by commas: ")
rmStrings = input("Please enter a list of strings to remove, separated by commas: ")

originalStrings = [str.strip() for str in originalStrings.split(',')]
addStrings = [str.strip() for str in addStrings.split(',')]
rmStrings = [str.strip() for str in rmStrings.split(',')]

result = mergeLists(originalStrings, addStrings, rmStrings)
print("The resulting list is:\n{}".format(result))