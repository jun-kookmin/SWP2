import pickle

dbfilename = 'test3_4.dat'

def readScoreDB():
    try:
        fH = open(dbfilename, 'rb')
    except FileNotFoundError as e:
        print("New DB: ", dbfilename)
        return []

    scdb = []
    try:
        scdb =  pickle.load(fH)
    except:
        print("Empty DB: ", dbfilename)
    else:
        print("Open DB: ", dbfilename)
    fH.close()
    return scdb


# write the data into person db
def writeScoreDB(scdb):
    fH = open(dbfilename, 'wb')
    pickle.dump(scdb, fH)
    fH.close()


def doScoreDB(scdb):

    try:  # 입력값의 개수가 다를 때의 오류
        while(True):
            
            inputstr = (input("Score DB > "))
            if inputstr == "": continue
            parse = inputstr.split(" ")
            
            #add
            if parse[0] == 'add':
                record = {'Name':parse[1], 'Age':parse[2], 'Score':parse[3]}
                print("입력한 값이 추가되었습니다.")
                scdb += [record]
                parse[2] = parse[2]
                parse[3] = parse[3]
               
                ab = int(parse[2])
                
                
            #del   
            elif parse[0] == 'del':
                for p in scdb:
                    if p['Name'] == parse[1]:
                        scdb.remove(p) and reversed(scdb)
                        print("입력하신 값을 삭제하였습니다")
                        
                        
            # 3개 값 입력 inc 이름 amount
            
            elif parse[0] == 'inc':
                parse[2] = parse[2]
                        
                #int선언
                abc = int(parse[2])
                            
                for p in scdb:
                    if p['Name'] == parse[1]:
                        
                        p['Score'] = ab + abc
                        
                        print("Score에 입력하신 값을 더하였습니다.")
                    

            elif parse[0] == 'find':
                for p in scdb:
                    if p['Name'] == parse[1]:

                        print("검색하신 분의 이름은 {}, 나이는 {}, 점수는 {} 입니다.".format(p['Name'], p['Age'], p['Score']))
                    else:
                        print("해당 이름이 아니거나 존재하지 않습니다.")

            #show        
            elif parse[0] == 'show':
                sortKey ='Name' if len(parse) == 1 else parse[1]
                showScoreDB(scdb, sortKey)
            



            #quit    
            elif parse[0] == 'quit':
                break
            else:
                print("Invalid command: " + parse[0])
    except KeyError as e:
        print(e)
        doScoreDB(scdb)
    except IndexError as ex:
        print(ex)
        doScoreDB(scdb)
    


def showScoreDB(scdb, keyname):
    try:
        for p in sorted(scdb, key=lambda person: person[keyname]):
            for attr in sorted(p):
                print(attr + "=" + p[attr], end=' ')
            print()
    except TypeError as ee:
            print("Score={} ".format(p['Score']))

scoredb = readScoreDB()
doScoreDB(scoredb)
writeScoreDB(scoredb)
