import wget
import winreg
import os

downloads_folder = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders", 0, winreg.KEY_READ | winreg.KEY_WOW64_32KEY)
downloads_folder = winreg.QueryValueEx(downloads_folder, r"{374DE290-123F-4565-9164-39C4925E467B}")[0]
apptype = str
urls = {
    "chrome": "http://dl.google.com/chrome/install/375.126/chrome_installer.exe",
    "firefox": "https://download.mozilla.org/?product=firefox-stub&os=win&lang=en-US",
    "vscode": "https://aka.ms/win32-x64-user-stable",
    "clion": "https://download.jetbrains.com/cpp/CLion-2020.2.4.exe",
    "pycharm": "https://download.jetbrains.com/python/pycharm-community-2020.2.3.exe",
}
def installer(app: apptype):
    """The bulk installer. Takes in the app as an argument.

    Web Browsers:
        chrome
        firefox
    
    IDEs:
        vscode
        clion
        pycharm
    """
    installFolder = os.path.join(os.path.expandvars(downloads_folder), f'{app}Setup.exe')
    d = wget.download(urls[app], installFolder)
    return installFolder

print(installer("pycharm"))