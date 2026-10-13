from abc import ABC, abstractmethod

class Notification(ABC):
    def __init__(self, message: str):
        self.message = message

    @abstractmethod
    def send(self) -> None:
        pass

    def show_notification(self, method: str) -> None:
        print(f'=== {method.upper()} NOTIFICATION ===')
        print(f'{method}: {self.message}')
        print('======================================')

class EmailNotification(Notification):
    def send(self) -> None:
        self.show_notification('Email')

class SMSNotification(Notification):
    def send(self) -> None:
        self.show_notification('SMS')

class PushNotification(Notification):
    def send(self) -> None:
        self.show_notification('Push')

def main() -> None:
    notifications: list[Notification] = [
        EmailNotification('Your account was created!'),
        SMSNotification('Your otp is 123456'),
        PushNotification('You have a new notification')
    ]

    for notification in notifications:
        notification.send()
        print()

if __name__ == "__main__":
    main()
