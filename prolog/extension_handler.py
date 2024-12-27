import email
import smtplib
import strip_ansi
class NoOutputHandler:
    @staticmethod
    def handle(name, message, level):
        pass

class NoColorHandler:
    @staticmethod
    def handle(name, message, level):
        print(f"[{level}] {name}: {message}")

# 漂亮颜色Handler
class BeautifulColorHandler:
    @staticmethod
    def handle(name, message, level):
        colors = {
            "DEBUG": "\033[34m",
            "INFO": "\033[32m",
            "WARNING": "\033[33m",
            "ERROR": "\033[31m",
            "CRITICAL": "\033[1;41m"
        }
        color = colors.get(level, "\033[0m")
        print(f"{color}[{level}] {name}: {message}\033[0m")

class SMTPHandler:
    def __init__(self, host, port, username, password, sender, recipients):
        self.host = host
        self.port = port
        self.username = username
        self.password = password        
        self.sender = sender
        self.recipients = recipients
    @staticmethod
    def handle(self, name, message, level):
        msg = email.message.Message()
        msg['From'] = self.sender
        msg['To'] = ", ".join(self.recipients)
        msg['Subject'] = f"[{level}] {name}"
        msg.set_payload(message)
        with smtplib.SMTP(self.host, self.port) as server:
            server.starttls()
            server.login(self.username, self.password)
            server.sendmail(self.sender, self.recipients, msg.as_string())

class JSONHandler:
    @staticmethod
    def handle(name, message, level):
        print(f'{{"name": "{name}", "level": "{strip_ansi.strip_ansi(level)}", "message": "{strip_ansi.strip_ansi(message)}"}}')

class XMLHandler:
    @staticmethod
    def handle(name, message, level):
        print(f'<log><name>{name}</name><level>{strip_ansi.strip_ansi(level)}</level><message>{strip_ansi.strip_ansi(message)}</message></log>')