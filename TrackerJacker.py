class Tracker:

    def __init__(self, currentPrice, websites):
        import os
        os.system('net stop MongoDB')
        try:
            import html5lib
        except Exception:
            os.system('pip install html5lib')
        try:
            import COVID19Py
        except Exception:
            os.system('pip install COVID19Py')
        try:
            import bs4
        except Exception:
            os.system('pip install beautifulsoup4')
        try:
            import requests
        except Exception:
            os.system('pip install requests')
        try:
            import pymongo
        except Exception:
            os.system('pip install pymongo')
        import COVID19Py
        # countries 2 digit codes
        try:
            import pycountry
        except Exception:
            os.system('pip install pycountry')
        #covidTracker
        import pymongo
        DatabaseClinet = pymongo.MongoClient("mongodb://localhost:27017/")
        self.database = DatabaseClinet["amazon"]
        self.countries = pycountry.countries
        self.covid19 = COVID19Py.COVID19(data_source="csbs")
        self.html5lib = html5lib
        self.bs4 = bs4
        self.pymongo = pycountry
        self.requests = requests
        self.websites=websites
        self.price = currentPrice
        self.Quit = False
        self.getMongoData = False
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"}
        self.details = {"name": "", "price": 0, "deal": True, "url": ""}
        self.TrackBootTime()
    def TrackCovid(self,countryName=''):
        locations = self.covid19.getLocations()
        #print(self.covid19.getLocations())
        locationsByTimelines = self.covid19.getLocations(timelines=True)
        locationsByRecovered = self.covid19.getLocations(rank_by='recovered')
        locationsByDeaths = self.covid19.getLocations(rank_by='deaths')
        locationsByConfirmed = self.covid19.getLocations(rank_by='confirmed')
        locationsByCountry = ""
        locationsByCountry = self.covid19.getLocationByCountryCode(self.GetCountryCode(countryName))
        if len(countryName)>1:
            try:
                locationsByCountry = self.covid19.getLocationByCountryCode(self.GetCountryCode(countryName))
            except Exception:
                print("invalid country name")
        allData = self.covid19.getAll()
        previousChanged = self.covid19.getLatestChanges()
        return [locations,locationsByTimelines,locationsByRecovered,locationsByDeaths,locationsByConfirmed,locationsByCountry,previousChanged,allData]
    def GetCountryCode(self,countryName):
        code = self.countries.search_fuzzy(countryName)
        return ''.join(str(code).split("alpha_2='")[1]).split("',")[0]
    def shortenAmazonURL(self,website):
        url = None
        website=str(website)
        if website.find("amazon.in") != -1:
            index = website.find("/dp/")
            if index != -1:
                index2 = index + 14
                url = "https://www.amazon.in" + url[index:index2]
            else:
                index = url.find("/gp/")
                if index != -1:
                    index2 = index + 22
                    url = "https://www.amazon.in" + url[index:index2]
        website = str(website)
        if website.find("amazon.com") != -1:
            index = website.find("/dp/")
            if index != -1:
                index2 = index + 14
                url = "https://www.amazon.com" + url[index:index2]
            else:
                index = url.find("/gp/")
                if index != -1:
                    index2 = index + 22
                    url = "https://www.amazon.com" + url[index:index2]
        return url
    def GetAmazonPrice(self, price):
        import re
        return float(re.sub(r"[^\d.]", "", price))
    def GetAmazonProduct(self,website):
        url = self.shortenAmazonURL(website)
        if url is None:
            self.details=None
        page = self.requests.get(url, headers=self.headers)
        soup = self.bs4.BeautifulSoup(page.content, "html5lib")
        title = soup.find(id="productTitle")
        price = soup.find(id="priceblock_dealprice")
        if price is None:
            price = soup.find(id="priceblock_ourprice")
            self.details["deal"] = False
        if title is not None and price is not None:
            self.details["name"] = title.get_text().strip()
            self.details["price"] = self.GetAmazonPrice(price.get_text())
            self.details["url"] = url
        else:
            self.details = None
        details=self.details
        return details
    def GetDetails(self,details):
        import datetime
        products = self.database["products"]
        ASIN = details["url"][len(details["url"])-10:len(details["url"])]
        details["date"] = datetime.datetime.utcnow()

        try:
            products.update_one({"asin": ASIN},{"$set": {"asin": ASIN},"$push": {"details": details}},upsert=True)
            return True
        except Exception as identifier:
            print(identifier)
            return False
    def GetAll(self):
        return self
    def GetHistory(self,ASINData):
        products = self.database["products"]
        try:
            findProduct = products.find_one({"asin:": ASINData}, {"_id":0})
            if findProduct:
                return findProduct
        except Exception:
            print(Exception)
            return None
    def ProcessAmazonData(self):
        result = "Unfinished"
        for website in self.websites:
            getDetails = self.GetAmazonProduct(website)
            if getDetails == None:
                result = "Unfinished"
            else:
                print(getDetails)
                added = self.database.GetDetails(getDetails)
            if True:
                result = "Finished"
        return result
    def GetData(self):
        import time
        import pymongo
        self.Database()
        while self.Quit == False:
            self.ProcessAmazonData()

            file = open("AmazonDB.txt", "w")
            client = pymongo.MongoClient("mongodb://localhost:27017/")
            db = client["databse"]
            amazonDB = db["amazon"]
            productsDB = db["products"]
            print(amazonDB.find())
            file.write(str(amazonDB.find_one()))
            file.write(str(productsDB.find_one()))
            file.close()
            time.sleep(120)

    def TrackBootTime(self):
        import os
        try:
            import psutil
        except Exception:
            os.system('pip install psutil')
            import psutil
        import datetime
        previousBoot = str(datetime.datetime.fromtimestamp(psutil.boot_time())).split(" ")
        print(previousBoot)
        previousBootSecond = int(previousBoot[1].split(":")[0])*3600+int(previousBoot[1].split(":")[1])*60+float(previousBoot[1].split(":")[2])
        previousBootDate = str(datetime.datetime.fromtimestamp(psutil.boot_time()))[0]

        file = open("All_boot_times.txt","w")
        file.write(str([previousBoot, previousBootSecond]))
        file.close()
        file = open("All_boot_times.txt", "r")
        lines = file.readlines()
        bootTimes = []

        for line in lines:
            bootTimes.append(str(line))
        allBoots = []
        [allBoots.append(i) for i in bootTimes if i not in allBoots]
        bootAmounts = len(allBoots)
        bootAverage=0
        for i in allBoots:
            bootAverage+=float(''.join(i.split(",")[2])[1:-1])
        bootAverage = bootAverage/bootAmounts
        file.close()
        if previousBootSecond > bootAverage:
            print("Boot is faster than the average boot. Average Boot:{0}, Current Boot:{1}".format(bootAverage,previousBootSecond))
        else:
            print("Boot is slower than the average boot. Average Boot:{0}, Current Boot:{1}".format(bootAverage,previousBootSecond))
