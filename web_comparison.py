
import filecmp
def filecompare(file1,file2,department):
    if filecmp.cmp(file1,file2)==True:
        print(department,filecmp.cmp(file1,file2))
    else:
        f1 = open(file1, "r")
        f2 = open(file1, "r")
        data1= f1.read()
        data2= f2.read()
        data_into_list1 = data1.split("\n")
        data_into_list2 = data2.split("\n")
        diff1=[]
        diff2=[]
        for i in len(data_into_list1):
            if data_into_list1[i]==data_into_list2[i]:
                diff1.append(data_into_list1[i])
                diff2.append(data_into_list2[i])
        print(department)
        print(file1+'different place')
        print(diff1)
        print(file2+'different place')
        print(diff2)
        f1.close()
        

# import error_test
# url='https://www.apr.soushu2029.com/forum.php?mod=forumdisplay&fid=40&mobile=2'
# response = error_test.url_checker(url)
# print(response)
