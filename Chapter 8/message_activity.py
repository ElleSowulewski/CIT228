def show_messages(messages):
    for m in messages:
        print(m)

def send_messages(messages, sent_messages):
    for m in messages:
        sent_messages = messages.copy()
        print(f"The message {m} is sent!")
