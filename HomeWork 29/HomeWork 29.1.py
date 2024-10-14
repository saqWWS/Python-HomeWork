class ReadEmail:
    def __init__(self, from_address: str, file):
        self.from_address = from_address
        self.file = file

    def read_email(self):
        with open(self.file, 'r') as file:
            content = file.read()
        return content

    def __str__(self):
        return f"From: {self.from_address}"


read = ReadEmail("example@.ex", "lorem_ipsum.txt")

print(read)
print(read.read_email())


class SendEmail:
    def __init__(self, to_address: str, text: str, file):
        self.to_address = to_address
        self.text = text
        self.file = file

    def send_email(self):
        return f"Sending email to {self.to_address} with the text: {self.text}"

    def write_text(self):
        with open(self.file, 'w+') as file:
            file.write(self.text)
        return f"Content written to {self.file}"


send = SendEmail("recipient@example.com", "Hello! This is the email content.", "email_content.txt")

print(send.write_text())
print(send.send_email())


# GOOD VERSION


class ReadSendEmail:
    """
     In a bad version, there aren't many blunders,
     but it's more understandable this way,
     two different classes that do different things,
     it's easier for the reader to work with this way
    """

    def __init__(self, from_address: str, to_address: str, text: str, file_read, file_send):
        self.from_address = from_address
        self.to_address = to_address
        self.text = text
        self.file_read = file_read
        self.file_send = file_send

    def read_email(self):
        print(f"Message send from: {self.from_address}")
        with open(self.file_read, 'r') as file:
            content = file.read()
        return content

    def send_email(self):
        return f"Sending email to {self.to_address} with the text: {self.text}, from {self.from_address}"

    def write_text(self):
        with open(self.file_send, 'w+') as file:
            file.write(self.text)
        return f"Content written to {self.file_send}"


read_and_send = ReadSendEmail("from@.ex", "to@.ex", "Hello World", "lorem_ipsum.txt", "email_content.txt")

print(read_and_send.read_email(), "\n")
print(read_and_send.write_text(), "Text:", read_and_send.text)

# BAD VERSION
