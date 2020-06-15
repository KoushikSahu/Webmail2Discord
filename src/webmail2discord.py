import requests, json, time, config

url = "https://mail.nitrkl.ac.in/home/118cs0597@nitrkl.ac.in/inbox.json"
params = dict(
    auth= "qp",
    zauthtoken = config.zauthtoken,
)
webhook = config.webhook

def send_new_mails(data, time):
    for i in data['m']:
        if i['d'] >= time:
            message = dict()
            greet = "You have a webmail!"
            sender = i['e'][1]['a'] + ", " + i['e'][1]['d'] + " says:"
            message['content'] = f"{greet}\n{sender}\nSubject: {i['su']}\nMessage: {i['fr']}"

            response = requests.post(url=webhook, data=json.dumps(message), headers={"Content-Type": "application/json"})
            print(response)
        else: break

def get_data():
    return requests.get(url=url, params=params).json()

if __name__ == "__main__":
    while True:
        curr_time = (time.time()) * 1000
        time.sleep(10)
        data = get_data()
        send_new_mails(data, curr_time)