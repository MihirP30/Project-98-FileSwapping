def swapFileData():
    file1 = input("Enter the first file: ")
    dataA = open(file1,"r")
    str1 = dataA.read()
    dataA.close()

    file2 = input("Enter the second file: ")
    dataB = open(file2,"r")
    str2 = dataB.read()
    dataB.close()


    file2 = open(file2,'w')
    file2.write(str1)
    file2.close()

    file1 = open(file1,'w')
    file1.write(str2)
    file1.close()


swapFileData()