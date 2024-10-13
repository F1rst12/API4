from time import sleep
import os
import telegram


def main():
    while True:
        bot = telegram.Bot(
            token= os.environ['TG_TOKEN'])
        files = os.walk("images")
        for file in files:
            file = list(file)
            for image in file[2]:
                with open(f"images/{image}", "rb") as file:
                    bot.send_document(chat_id="@cosmos_img", document=file)
                sleep(14400)


if __name__ == "__main__":
    main()
