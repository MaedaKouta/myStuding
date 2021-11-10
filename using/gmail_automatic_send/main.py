import smtplib
import csv
from email.mime.text import MIMEText

#メール送信のクラス
class Send:
    # 初期化
    def __init__(self, AddressTo, subject, text):
        self.password = "＜自分のGmailパスワードを記入＞"
        self.AddressFrom = "＜自分のGmailアドレスを記入＞"
        self.AddressTo = AddressTo
        self.subject = subject
        self.text = text
        self.charset = "UTF-8"

    def send(self):
        #メールの主要設定
        msg = MIMEText(self.text.encode(self.charset), 'plain', self.charset)
        msg['From'] = self.AddressFrom
        msg['To'] = self.AddressTo
        msg['Subject'] = self.subject

        #メールの詳細設定
        smtp = smtplib.SMTP('smtp.gmail.com', 587)
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login(self.AddressTo, self.password)
        smtp.send_message(msg)
        smtp.close()

def MailText(Name):

    text = """
{}さま

お世話になります。
「tetoblog」を運営しております前田と申します。

約束していた物品を、{}さま宛に発送いたしましたので、ご連絡いたしました。
今後とも、よろしくお願いいたします。

""".format(Name, Name)

    return text



file = 'AddressDate.csv'
#データの読み込み
with open(file, 'r') as f:
    date = csv.reader(f)
    header = next(date)  #ヘッダーの読み込み

    for row in date:
        # 名前、アドレスをCSVから取得
        Name = row[0]  #名前
        Email = row[1]  #メールアドレス

        # メール内容
        AddressTo = Email
        subject = "【Python】Gmail送信"
        text = MailText(Name)
        mailer = Send(AddressTo, subject, text)
        mailer.send()