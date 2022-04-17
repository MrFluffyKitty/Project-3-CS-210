import re
import string


def List(v):
    # opens file and creats a list of the file
    f = open("E:\\repos\\Project Three - Tristin Watson\\Release\\grocerylist.txt", "r")
    list1 = []
    endList = []
    for line in f:
        lineStrip = line.strip()
        lineSplit = lineStrip.split()
        list1.append(lineSplit)
    f.close()
    for i in list1:
        for j in i:
            endList.append(j)
    # prints the items in the list with the count
    for items in endList:
        print(items, endList.count(items))
        for item in endList:
            if items in endList:
                endList.remove(items)
            else:
                break;
    return 1

def Item(v):
    # opens file and creates a list of the items in the file
    f = open("E:\\repos\\Project Three - Tristin Watson\\Release\\grocerylist.txt", "r")
    list1 = []
    endList = []
    for line in f:
        lineStrip = line.strip()
        lineSplit = lineStrip.split()
        list1.append(lineSplit)
    f.close()
    for i in list1:
        for j in i:
            endList.append(j)
    # returns the amount of the specified item v
    counts = endList.count(v)
    return counts

def Histogram(v):
    # opens file and creates a list of the items in the file
    f = open("E:\\repos\\Project Three - Tristin Watson\\Release\\grocerylist.txt", "r")
    list1 = []
    endList = []
    for line in f:
        lineStrip = line.strip()
        lineSplit = lineStrip.split()
        list1.append(lineSplit)
    f.close()
    # writes a file displaying the items with the counts of each item
    w = open("E:\\repos\\Project Three - Tristin Watson\\Release\\frequency.dat" , "w")
    for i in list1:
        for j in i:
            endList.append(j)
    for items in endList:
        w.write(items)
        string = str(endList.count(items))
        w.write(" "), w.write(string), w.write("\n")
        for item in endList:
            if items in endList:
                endList.remove(items)
            else:
                break;
    w.close()
    return 3