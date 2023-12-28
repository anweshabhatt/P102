import os
import shutil

fromdir="C:/Users/DELL/Downloads"
todir="D:/anwesha"
listOfFile=os.listdir(fromdir)
#print(listOfFile)

for file in listOfFile:
    name,ext=os.path.splitext(file)
    #print(name)
    #print(ext)
    if(ext == ""):
        continue
    if ext in [".doc",".docx",".txt",".pdf"]:
        path1 = fromdir + "/" + file
        path2 = todir + "/" + "Image file"
        path3 = todir + "/" + "Image file" + "/" + file
        print(path1,path3)
        if os.path.exists(path2):
            print("movingFile")
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("moving file")
            shutil.move(path1,path3)
