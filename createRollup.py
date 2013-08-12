#!/usr/bin/env python

import os
import fileinput

pathToYui = "../yui3.10.3/"
blackList = ["yui-nodejs-min.js", "get-nodejs-min.js", "yui-min.js", "yui-core-min.js", "simpleyui-min.js"]
scriptNote = "/* generated by createRollup.py from ...*/\n"

def concatFiles(filePaths, fileName):
    with open(fileName, 'w') as fout:
        fout.write(scriptNote)
        for line in fileinput.input(filePaths):
            fout.write(line)
    print "[" + fileName + "] written"


def findFilesEndingTo(fileEnding, startPath):
    filePaths = []
    for r,d,f in os.walk(startPath):
        for fileName in f:
            if fileName.endswith(fileEnding):
                if fileName not in blackList:
                    filePath = os.path.join(r,fileName)
                    filePaths.append(filePath)
                    print "[" + fileName + "] added"
                else:
                    print "[" + fileName + "] blacklisted"
    print "[" + str(len(filePaths)) + "] files found"
                
    return filePaths


def sortToFirstPosition(filePaths, name):
    position = -1
    for filePath in filePaths:
        if filePath.endswith(name):
            position = filePaths.index(filePath)

    if position > -1:
        firstContent = filePaths[0]
        tempContent = filePaths[position]
        filePaths[position] = firstContent
        filePaths[0] = tempContent
        print "[" + name + "] sorted entry up"
    else:
        print "could not found [" + name + "] to sort up"

    return filePaths


#main
filePaths = findFilesEndingTo("-min.js", pathToYui)
filePaths = sortToFirstPosition(filePaths, "yui-base-min.js")
concatFiles(filePaths, "yuiCompleteRollup.js")
