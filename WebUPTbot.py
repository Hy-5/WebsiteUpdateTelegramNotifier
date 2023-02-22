import subprocess, sys, time, requests

#Downloads or imports necessary windows modules
necessaryImports = ["requests", "telebot"]
for i in necessaryImports:
    #print(i)
    try:
        __import__(i)
    except ImportError:
        print(f"{i} missing. Installing {i} now")
        subprocess.check_call(["pip", "install", i])
        try:
            __import__(i)
        except:
            subprocess.run(["pip install --force-reinstall -v \"python-telegram-bot==13.5\" "])

import telegram


#Add your bots id, hash and token as a string
api_id=""
api_hash=""
botToken=""

#Add the url you want to check and the specific keyword you want to look for
url=""
keyword=""

#By default the bot only sends the URL as a message. Replace "<text=url>" line 32 by "<text=THESTRINGOFYOURCHOICE>" if you wish to send something else instead.
def sendNotif():
    bot=telegram.Bot(token=botToken)
    bot.send_message(chat_id=api_id, text=url)
    return


#Checks the given URL for the given keyword
def urlChecker():
    while True:
        #print("Running...")
        response=requests.get(url)
        if keyword.lower() in response.text.lower():
            print(f"Found {keyword} at {time.strftime('%Y-%m-%d, %H:%M:%S')}")
            sendNotif()

        time.sleep(30)
    return



def main(argv):
    urlChecker()
    return


if __name__=='__main__':
    main(sys.argv[1:])