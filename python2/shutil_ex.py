# shutil사용해서 쉽게 copy하기기
import shutil
import os

# shutil.copy("./python2/temp/in.txt", "./python2/temp/copy_in2.txt")
# shutil.move("./python2/temp/in.txt", "./python2/temp/move_in.txt")

if( not os.path.exists("./python2/temp/sss")):
    os.mkdir("./python2/temp/sss")


# 해당 폴더 안에 파일 목록들 보기
for dirName, subDirList, fNames in os.walk("./python2/temp"):
    for fName in fNames : 
        print( os.path.join(dirName, fName))
    for s in subDirList:
        print(s)
if (os.path.exists("./python2/temp/data1.txt")):
    os.remove("./python2/temp/data1.txt")

# 파일 크기알기
if (os.path.exists("./python2/temp/css.gif")):
    file_size = os.path.getsize("./python2/temp/css.gif")
    print( file_size/1024/1024, 'mb')

# 파일 압축하기
import zipfile
newZIp = zipfile.ZipFile("./new.zip", "w")
newZIp.write("./python2/temp/css.gif", compress_type=zipfile.ZIP_DEFLATED)
newZIp.close()

# 압축된 파일을 풀기
extZip = zipfile.ZipFile('./new.zip','r')
extZip.extractall("./python2/temp/ss")
extZip.close()