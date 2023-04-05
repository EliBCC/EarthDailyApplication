from collections import Counter                              # To check if lists of strings are equal

# Solution
def mergeLists(originalList, addList, rmList):
    pass

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
        