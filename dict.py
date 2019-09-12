import random
import glob
import math
count=0


while True:
        list_of_files = []
        count = 0
        for i in glob.glob("data/*.txt"):
            list_of_files.append(i)
            #print str(count)+": "+i.decode('cp1251')
            count += 1

        mode = 2
        k = 2

        mode = int(raw_input("Vvedite mode, 1 - print hebrew, 2 - print rus"))
            
        f = open(list_of_files[int(math.fmod(k, len(list_of_files)))],"r")
        en = []
        ru = []
        for words in f:
            en.append(words.split(":")[0])
            ru.append(words.split(":")[1][0:-1])
        f.close()
        flag = [1 for i in range(len(en))]
        count = 0
        while True:
            if flag == [0 for i in range(len(en))]:
                print "All"
                break
            key = random.randint(0, len(en)-1)
            if flag[key] == 0:
                continue
            flag[key] = 0
            count += 1

            if mode == 3:
                raw_input(en[key].decode('cp1251')+" | " + str(count)+"/"+str(len(en)))
                print ru[key].decode('cp1251')
            if mode == 2:
                str1=ru[key].decode('cp1251')+" | " + str(count)+"/"+str(len(en))
                print str1
                raw_input()
                print en[key].decode('cp1251')
            if mode == 1:
                str1=en[key].decode('cp1251')+" | " + str(count)+"/"+str(len(en))
                print str1
                raw_input()
                print ru[key].decode('cp1251')
            print "___________"
            print

