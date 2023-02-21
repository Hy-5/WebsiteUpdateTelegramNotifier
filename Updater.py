import subprocess, sys, time, os, requests

necessaryImports = ["requests", "telegram_send", "telebot", "telethon"]
api_id=""
api_hash=""
token=""

url="https://www.reddit.com/r/hardwareswap/new/"
keyword="GPU"
phoneNumber=""



def moduleCheck():
    for i in necessaryImports:
        print(i)
        try:
            __import__(i)
        except ImportError:
            print(f"{i} missing. Installing {i} now")
            subprocess.check_call(["pip", "install", i])
            try:
                __import__(i)
            except:
                subprocess.run(["pip install --force-reinstall -v \"python-telegram-bot==13.5\" "])
    return


def urlChecker():
    while True:
        response=requests.get(url)
        if keyword in response.text:
            print(f"Found {keyword} at {time.strftime('%Y-%m-%d %H:%M:%S')}")

        time.sleep(30)
    return



def main(argv):
    moduleCheck()
    urlChecker()

    return


if __name__=='__main__':
    main(sys.argv[1:])