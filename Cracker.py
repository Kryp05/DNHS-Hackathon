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
    def directoryBuster(self,crackType="brute"):
        #crack types = brute, dictionary, wordlist
        if crackType=="brute":
            self.bruteForce(self.numbers,self.lowercase,self.uppercase,self.specialCharacters,self.url)
        if crackType=="dictionary":
            self.dictionary(self.threadNum)
        if crackType=="wordlist":
            self.wordlist(self.threadNum,self.wordlist)
    def dictionary(self, threads):
        import nltk
        import threading
        from nltk.corpus import words
        wordlist  = words.words()
        Wordlist=[]
        nltk.download()
        currentValue=0
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
                    self.threads.append(threading.Thread(target=self.ping, args=(str(self.website)+str(Wordlist),)))
                    self.threads[-1].start()
                    self.threads[-1].join()
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
                    self.threads.append(threading.Thread(target=self.ping, args=(str(self.website)+str(Wordlist),)))
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
                self.threads.append(threading.Thread(target=self.ping, args=(str(self.website)+str(i),)))
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
        import nltk
        import threading
        from nltk.corpus import words
        wordlist  = words.words()
        Wordlist=[]
        nltk.download()
        currentValue=0
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
        try:
            ping = requests.head(website)
            if int(ping.status_code) == 200:
                self.foundLinks.append(website)
        except requests.ConnectionError:
            print('Failed to connect, Try Again')
