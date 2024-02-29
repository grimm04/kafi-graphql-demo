import requests
message = "Tes"

send = 'https://api.telegram.org/bot2031631263:AAFbtvqCi1-xDweOQ2uzG0Z73P9x7dJIC_w/sendMessage?chat_id=-1001564459174&text={}'.format(message)
requests.get(send)
# return send 