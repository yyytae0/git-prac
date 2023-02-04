import re

inf = 1e6

class queue:
    list = []
    def pop(self):
        return self.list.pop(0)

    def push(self,nextlist, weight, where):
        for i in range(len(nextlist)):
            temp = nextlist[i][:]
            temp[1] += weight
            temp.append(where)
            self.list.append(temp)
        return
    def isnotempty(self):
        if self.list == []:
            return False
        return True
    def print(self):
        print(*self.list)


class findpath:
    def __init__(self, data):
        self.data = data
        self.nexthop = queue()
        self.checklist = [False for i in range(668)]
        self.Route = [[inf,[]] for i in range(668)]

    def name_num(self,name):
        return int(name[2:])

    def reset(self):
        self.checklist = [False for i in range(668)]
        self.Route = [[inf,[]] for i in range(668)]

    def dfs(self, start, dest):
        self.start = start
        self.dest = dest
        self.checklist[self.start] = True
        self.Route[self.start][0] = 0
        self.Route[self.start][1].append(self.start)
        
        for i in self.data[self.start][2]:
            self.Route[i[0]][0] = i[1]
            self.Route[i[0]][1] = self.Route[self.start][1][:]
            self.Route[i[0]][1].append(i[0])
            self.nexthop.push(self.data[i[0]][2],self.Route[i[0]][0],i[0])

        while self.nexthop.isnotempty():
            temp = self.nexthop.pop()
            now_pos, dist, where = temp

            if dist > self.Route[now_pos][0]:
                continue
            self.Route[now_pos][0] = dist
            self.Route[now_pos][1] = self.Route[where][1][:]
            self.Route[now_pos][1].append(now_pos)
            temp = []
            for i in self.data[now_pos][2]:
                if self.Route[i[0]][0] > self.Route[now_pos][0] + i[1]:
                    temp.append(i)
            self.nexthop.push(temp,self.Route[now_pos][0],now_pos)


        return self.Route[dest]



    def print(self):
        print(self.Route)


def read_data():
    data = [[1,1,1]]
    with open("station.csv", 'r') as file:
        for i in file.readlines():
            if i == ' ':
                return
            temp , next, trash = i.strip().split("\"")
            codename, name, trash = temp.split(",")
            codename = int(codename[2:])
            next = next.replace("),(", ";")
            next = re.sub("[()]","",next)
            next = re.sub("ZZ","",next)
            next = next.split(";")
            nextlist = []
            for i in next:
                temp = list(map(int,i.split(",")))
                if temp not in nextlist:
                    nextlist.append(temp)
                if temp[0] == codename:
                    continue
            data.append([codename, name, nextlist])
    return data
    

