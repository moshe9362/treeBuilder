
import webbrowser

if __name__ == '__main__':

    firefox = "C:/Program Files (x86)/Mozilla Firefox/firefox.exe %s"
    chrome = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
    url = 'http://localhost:63342/CCai/bot/chatUI/index.html'
    #webbrowser.get(firefox).open(url) |||| #dont work with this url, we need to change the url in order to open it
    #  with firefox
    webbrowser.get(chrome).open(url)
