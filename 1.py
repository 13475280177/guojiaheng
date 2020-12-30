#郭嘉恒 信息与计算科学 201701070709
import os
class chengji():
    def openfile(self,name):
        data=[]
        with open(name,'r') as f:
             i = f.readlines() #读取文件中行数
             for row in i:
                 tmp_list = row.split(' ')
                 tmp_list[-1]=tmp_list[-1].replace('\n','')#把换行符替换为空
                 data.append(tmp_list)
             return data
    def count(self,name):
        data=self.openfile(name)
        hang=len(data) #行数
        tem=[]
        for i in range(0,hang):
            tem.append(len(data[i]))
            if tem[i] != tem[i-1] and i!=0:
                print('成绩记录有缺失，请重新编辑')
                return 1
        sum = []
        lie=len(data[0]) #列数
        max=0
        for i in range(0,hang): #计算最高成绩，A10分，X是0分，O是5分
            tem=0
            trans=0
            for j in range(2,lie):
                if (data[i][j] == 'A')| (data[i][j] == ''):
                    trans=10
                if data[i][j] == 'X':
                    trans=0
                if data[i][j] == 'O':
                    trans=5
                tem=trans+tem
            sum.append(tem)

            if sum[i] >= max:
                max=sum[i]
        rate=0#调整比例
        if max > 100 :     #向下调整
            rate=100/max
            for i in range(0,hang):
                sum[i]=rate*sum[i]
        if lie < 12:       #向上调整
            rate=10/(lie-2)#前两列为姓名学号，所以减去两列
            for i in range(0,hang):
                sum[i]=rate*sum[i]
        return sum



    def rewrite(self,name1,name2):
        data=self.openfile(name1)
        hang=len(data)
        lie =len(data[0])
        sum = self.count(name1)
        for i in range(0,hang):
            data[i].append(sum[i])
        for i in range(0,hang):  #冒泡排序，按学号升序重新排成绩
            for j in range(i+1,hang):
                if int(data[j][1])<=int(data[i][1]):
                    tem=data[i]
                    data[i]=data[j]
                    data[j]=tem
        with open(name2,'w') as f:
            for i in range(0,hang):
                for j in range(0,lie+1):
                    if j!=lie:  #估算成绩保留两位小数
                        f.write(str(data[i][j]))
                        f.write(' ')
                    else:
                        f.write(str("%.2f" % data[i][j]))#最后一列保留两位小数
                f.write('\r\n')



if __name__ == '__main__':  #默认情况调用
    a=chengji()
    a.rewrite('1.txt', '2.txt')








