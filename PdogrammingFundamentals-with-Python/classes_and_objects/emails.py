class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


information = input()
list_of_objects_with_info = []

while information != 'Stop':
    sender, receiver, content = information.split()
    email_object = Email(sender, receiver, content)
    list_of_objects_with_info.append(email_object)
    information = input()

indices = [int(s) for s in input().split(', ')]

for current_index in indices:
    list_of_objects_with_info[current_index].send()

for current_object in list_of_objects_with_info:
    print(current_object.get_info())


