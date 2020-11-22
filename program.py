import TrackerJacker
import Cracker
import time
website="https://www.amazon.in/gp/product/B00IJRV2D0?pf_rd_p=f2b20090-067d-415f-953d-b8dcecc9109f&pf_rd_r=VFJ98F93X80YWYQNR3GN"
tracker = TrackerJacker.Tracker("$100", ["https://www.amazon.in/gp/product/B00IJRV2D0?pf_rd_p=f2b20090-067d-415f-953d-b8dcecc9109f&pf_rd_r=VFJ98F93X80YWYQNR3GN=ATVPDKIKX0DER"])
tracker.GetAmazonProduct(website)
#note: do not run the directory buster on a website you are not allowed to use it on
cracker = Cracker.crack("https://treasure4094240317.cityinthe.cloud/",10,True,True,True,True,False,"Rockyou.txt",912ec803b2ce49e4a541068d495ab570)
cracker.directoryBuster("brute")
cracker.PasswordDehasher("wordlist")
def amazonDBRun(website, tracker):
    details = tracker.GetAmazonProduct(website)
    result = ""
    print(details)
    if details is None:
        result = "not done"
    else:
        inserted = tracker.GetDetails(details)
        if inserted:
            result = "done"
        else:
            result = "not done"
    return result
while True:
    print(amazonDBRun(website,tracker))
    time.sleep(80)
