import os, re

def getFiles(dirName):
    listOfFile = os.listdir(dirName)
    completeFileList = list()
    for file in listOfFile:
        completePath = os.path.join(dirName, file)
        if os.path.isdir(completePath):
            completeFileList = completeFileList + getFiles(completePath)
        else:
            completeFileList.append(completePath)

    return completeFileList

def main():
    print("Python Program to print list the files in a directory.")

    Dir = input(r"Enter the path of the folder: ")
    print(f"Files in the directory: {Dir}")

    pathList = getFiles(Dir)
    #print(*pathList, sep="\n")

    for path in pathList:
        fileName = path.split("\\")[-1]
        extension = fileName.split(".")[-1]
        regX=re.compile("(.*)\.[s,S](\d*)[e,E](\d*).(\d*)p")
        match = regX.match(fileName)
        print(f"{match}.{extension}")

    #show_p = re.compile("(.*?)\.s(\d{1,2})e(\d{1,2})")
    #print(show_p.match("some.other.tv.show.s04e05.episode_name.avi").groups())
   #files = os.listdir(Direc)
   #print(files)
   #files = [f for f in files if os.path.isfile(Direc+'/'+f)] #Filtering only the files.
   #print(*files, sep="\n")


if __name__ == "__main__":
    main()