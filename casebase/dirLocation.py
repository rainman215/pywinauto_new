import os
import sys

def searchDir(dirName):
    dir =r'E:\chenglong\Auto_QuikLab\QuikLab\branches\QuikLab_Test_Tool_for_PT'
    spec_str=dirName
    results=[]
    folders=[dir]
    dirLocation=[]
    fileLocation=[]
    for folder in folders:
        folders += [os.path.join(folder,x) for x in os.listdir(folder) if os.path.isdir(os.path.join(folder,x))]
    #     print folders
        results += [os.path.relpath(os.path.join(folder,x), start = dir) \
                   for x in os.listdir(folder) if os.path.isfile(os.path.join(folder,x)) and spec_str in x.split('\\')[-1]]

    dirLocation = [ x for x in folders if spec_str in x.split('\\')[-1] ]
    fileLocation = [ x for x in results if spec_str == x.split('\\')[-1] ]

    return dirLocation[0]



if __name__=="__main__":
#     print sys.path
    print searchDir('casebase')
    