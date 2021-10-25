from smtplib import SMTP
from email.message import EmailMessage
import requests

SENDER = "ceomsupport@ou.edu"
HOST = "relay.ou.edu"
PORT = 25
RECEIVERS = ["ceomsupport@ou.edu", "jonathan.g.miller@ou.edu"]
URL_TO_CHECK = "https://www.ceom.ou.edu"

r = requests.get(URL_TO_CHECK)
message = EmailMessage()

if r.status_code != 200:
    message['Subject'] = "CEOM Website Health Check Failure"
    message.set_content(f"Health check failed! Could not reach {URL_TO_CHECK}.\nStatus code: {r.status_code}.\n\n{r.text}")

message['From'] = SENDER
message['To'] = RECEIVERS

with SMTP(host=HOST, port=PORT) as smtp:
    smtp.send_message(message)



