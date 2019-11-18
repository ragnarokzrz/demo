import os
import re


datapath = "D:\\project\\data2"
filenamList = os.listdir(datapath)  # 将目录下的而文件全部读取

txtPath = "default.txt"

def reachData():
    """查询日志中cost超过999的日志"""

    #判断文件是否存在,存在则删除
    if os.path.exists(txtPath):
        os.remove(txtPath)
    for filename in filenamList:
        filepath = "D:\\project\\data\\"+filename
        with open(filepath,"r",encoding="utf8") as file:
            fileL = file.readlines()
            for index,line in enumerate(fileL):
                lines = line.replace(" ","")
                if  re.search(r'cost:\d{4,5}',lines):
                    print(filename)
                    print(index + 1, "***",line)
                    with open(txtPath,"a",encoding="utf8") as f:
                        f.write(filename+"\n"+str(index+1)+"**"+line)


if __name__ == '__main__':
    reachData()