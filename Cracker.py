class Crack:
    def __init__(self,webSite,threadNum,numbers,lowercase,uppercase,specialCharacters,URL,wordlist,hashes):
        self.numbers = numbers
        self.lowercase = lowercase
        self.uppercase = uppercase
        self.specialCharacters = specialCharacters
        self.url = URL
        self.website = webSite
        self.threads = []
        self.threadNum=threadNum
        self.quit = False
        self.wordlist = wordlist
        self.hashes = hashes
        self.foundLinks=[]
        self.foundHashes=[]
    def PasswordDehasher(self,crackType="brute"):
        #crack types = brute, dictionary, wordlist
        if crackType=="brute":
            self.passwordBruteForce(self.numbers,self.lowercase,self.uppercase,self.specialCharacters,self.url)
        if crackType=="dictionary":
            self.passwordDictionary(self.threadNum)
        if crackType=="wordlist":
            self.passwordWordlist(self.threadNum,self.wordlist)
    def passwordDictionary(self, threads):
        import threading
        wordlist = "lowercase.txt"
        file = open(wordlist, "r")
        wordlst = []
        for i in file.readlines():
            wordlst.append(i)
            print(wordlst[-1])
        wordlist = "uppercase.txt"
        file = open(wordlist, "r")
        for i in file.readlines():
            wordlst.append(i)
        wordlist  = wordlst
        Wordlist=[]
        currentValue=0
        for i in range(0,len(wordlist),threads):
            Wordlist.append([])
            for i2 in range(0,threads):
                if 116209 > i * threads + i2:
                    Wordlist[int(i / threads)].append(wordlist[i * threads + i2])
                else:
                    i = i

        while self.quit == False:
            currentValue+=1
            checkStrings = []
            self.threads=[]
            for i2 in range(0,len(Wordlist)):
                for i in Wordlist[i2]:
                    self.threads.append(threading.Thread(target=self.hash, args=(str(self.website)+str(Wordlist),)))
                    self.threads[-1].start()
                    self.threads[-1].join()
        if (self.quit):
            for i in self.threads:
                i.join()
    def passwordWordlist(self, threads,wordlist):
        import threading
        Wordlist=[]
        currentValue = 0
        for i in range(0,wordlist,threads):
            Wordlist.append([])
            for i2 in range(0,threads):
                Wordlist[i].append(wordlist[i*6+i2])
        while self.quit == False:
            currentValue+=1
            checkStrings = []
            self.threads=[]
            for i2 in range(0,Wordlist):
                for i in Wordlist[i2]:
                    self.threads.append(threading.Thread(target=self.hash, args=(str(self.website)+str(Wordlist),)))
                    self.threads[-1].start()
                    self.threads[-1].join()
        if (self.quit):
            for i in self.threads:
                i.join()
    def passwordBruteForce(self, threads=1, numbers = True, lowercase = True, uppercase = True, specialCharacters = True, URL = True):
        import threading
        currentValue = 0
        finalString = ""
        if len(finalString)<1:
            num="0123456789"
            Lowercase="abcdefghijklmnopqrstuvwxyz"
            Uppercase="ABCDEFGHIJKMMNOPQRSTUVWXYZ"
            URLSpecialCharacters="-_.  ~"
            SpecialCharacters=""" !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
            finalString=''
            if numbers:
                finalString += num
            if uppercase:
                finalString += Uppercase
            if lowercase:
                finalString += Lowercase
            if URL:
                if specialCharacters:
                    finalString+=URLSpecialCharacters
            else:
                if specialCharacters:
                    finalString+=SpecialCharacters
        if threads < 1:
            threads = 1
        while self.quit == False:
            currentValue+=1
            checkStrings = []
            for i in range(1,threads):
                checkStrings.append(self.getTestString(finalString, currentValue))
            self.threads=[]
            for i in checkStrings:
                print(self.Wordlist)
                self.threads.append(threading.Thread(target=self.hash, args=(str(self.website)+str(i),)))
                self.threads[-1].start()
                self.threads[-1].join()
        if (self.quit):
            for i in self.threads:
                i.join()
    def directoryBuster(self,crackType="brute"):
        #crack types = brute, dictionary, wordlist
        if crackType=="brute":
            self.bruteForce(self.numbers,self.lowercase,self.uppercase,self.specialCharacters,self.url)
        if crackType=="dictionary":
            self.dictionary(self.threadNum)
        if crackType=="wordlist":
            self.wordlist(self.threadNum,self.wordlist)
    def dictionary(self, threads):
        import threading
        wordlist = "lowercase.txt"
        file = open(wordlist, "r")
        wordlst = []
        for i in file.readlines():
            wordlst.append(i[0:-1])
        wordlist = "uppercase.txt"
        file.close()
        file = open(wordlist, "r")
        for i in file.readlines():
            wordlst.append(i[0:-1])
        file.close()
        wordlist = wordlst
        currentValue = 0
        Wordlist = []
        for i in range(0, len(wordlist), threads):
            Wordlist.append([])
            for i2 in range(0, threads):
                # print(wordlist[i * threads + i2],i * threads + i2)
                if 116209 > i * threads + i2:
                    Wordlist[int(i / threads)].append(wordlist[i * threads + i2])
                else:
                    i = i

        while self.quit == False:
            currentValue += 1
            checkStrings = []
            self.threads = []
            for i2 in range(0, len(Wordlist)):
                for i in Wordlist[i2]:
                    self.threads.append(threading.Thread(target=self.ping, args=(self.website+(i),)))
                    self.threads[-1].start()
                for i in self.threads:
                    i.join()
        if (self.quit):
            for i in self.threads:
                i.join()
    def wordlist(self, threads,wordlist):
        import threading
        Wordlist=[]
        currentValue = 0
        for i in range(0,wordlist,threads):
            Wordlist.append([])
            for i2 in range(0,threads):
                Wordlist[i].append(wordlist[i*6+i2])
        while self.quit == False:
            currentValue+=1
            checkStrings = []
            self.threads=[]
            for i2 in range(0,Wordlist):
                for i in Wordlist[i2]:
                    self.threads.append(threading.Thread(target=self.ping, args=(str(Wordlist),)))
                    self.threads[-1].start()
                    self.threads[-1].join()
        if (self.quit):
            for i in self.threads:
                i.join()
    def bruteForce(self, threads=1, numbers = True, lowercase = True, uppercase = True, specialCharacters = True, URL = True):
        import threading
        currentValue = 0
        finalString = ""
        if len(finalString)<1:
            num="0123456789"
            Lowercase="abcdefghijklmnopqrstuvwxyz"
            Uppercase="ABCDEFGHIJKMMNOPQRSTUVWXYZ"
            URLSpecialCharacters="-_.  ~"
            SpecialCharacters=""" !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
            finalString=''
            if numbers:
                finalString += num
            if uppercase:
                finalString += Uppercase
            if lowercase:
                finalString += Lowercase
            if URL:
                if specialCharacters:
                    finalString+=URLSpecialCharacters
            else:
                if specialCharacters:
                    finalString+=SpecialCharacters
        if threads < 1:
            threads = 1
        while self.quit == False:
            currentValue+=1
            checkStrings = []
            for i in range(1,threads):
                checkStrings.append(self.getTestString(finalString, currentValue))
            self.threads=[]
            for i in checkStrings:
                self.threads.append(threading.Thread(target=self.ping, args=(str(i),)))
                self.threads[-1].start()
                self.threads[-1].join()
        if (self.quit):
            for i in self.threads:
                i.join()
    def hash(self,string):
        String = string.encode()
        import hashlib
        hashes=[
            [hashlib.sha224(String).hexdigest(),"sha224"],
            [hashlib.sha256(String).hexdigest(),"sha256"],
            [hashlib.sha384(String).hexdigest(),"sha384"],
            [hashlib.sha512(String).hexdigest(),"sha512"],
            [hashlib.md5(String).hexdigest(),"md5"]]
        for i in hashes:
            if i[0] in self.hashes:
                print ("Found hash! String:{0} Hash{1}".format(string,i[1]))
                self.foundHashes.append([i[0],i[1],string])

    def getTestString(self,finalString,currentValue=0):

        output = ""
        for i in self.baseConversion(len(finalString),currentValue):
            output=i+output
        return output

    def baseConversion(self, baseNum, BaseTenNum):
        import math
        convertedBase=[]
        while BaseTenNum > 0:
            convertedBase.append(str(BaseTenNum%baseNum))
            BaseTenNum = math.floor(BaseTenNum/baseNum)
        return list(''.join(list(convertedBase))[::-1])
    def ping(self,website):
        import requests
        website=str(website)
        #print("Testing website: "+website)
        try:
            ping = requests.head(website)
            if int(ping.status_code) != 404:
                if website not in self.foundLinks:
                    print("Found one link: "+ website)
                    self.foundLinks.append(website)
        except requests.ConnectionError:
            print('Failed to connect, Try Again')
