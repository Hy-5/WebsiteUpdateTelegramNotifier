import subprocess, sys, time, requests

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

api_id=""
api_hash=""
botToken=""

url=""
keyword=""


def sendNotif():
    bot=telegram.Bot(token=botToken)
    bot.send_message(chat_id=api_id, text=url)
    return



def urlChecker():
    while True:
        print("Running...")
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