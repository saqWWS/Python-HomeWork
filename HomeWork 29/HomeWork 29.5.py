import abc


class Notifier(abc.ABC):
    @abc.abstractmethod
    def send_notification(self, message: str):
        ...


class EmailNotifier(Notifier):
    def send_notification(self, message: str):
        return f"Sending email notification: {message}"


class SMSNotifier(Notifier):
    def send_notification(self, message: str):
        return f"Sending SMS notification: {message}"


class PushNotifier(Notifier):
    def send_notification(self, message: str):
        return f"Sending push notification: {message}"


class UserNotificationService:
    def __init__(self, notifiers: list):
        self.notifiers = notifiers

    def notify_user(self, message: str):
        for notifier in self.notifiers:
            notifier.send_notification(message)


email_notifier = EmailNotifier()
sms_notifier = SMSNotifier()
push_notifier = PushNotifier()

notification_service = UserNotificationService([email_notifier, sms_notifier, push_notifier])

notification_service.notify_user("Your order has been sent!")


# GOOD VERSION

class EmailNotifier:
    def send_notification(self, message: str):
        return f"Sending email notification: {message}"


class SMSNotifier:
    def send_notification(self, message: str):
        return f"Sending SMS notification: {message}"


class UserNotificationService:
    """
    this feature helps to depend on interfaces or abstract classes
    rather than classes with concrete implementations.

    """

    def __init__(self):
        self.email_notifier = EmailNotifier()
        self.sms_notifier = SMSNotifier()

    def notify_user(self, message: str):
        self.email_notifier.send_notification(message)
        self.sms_notifier.send_notification(message)


# Usage
notification_service = UserNotificationService()

notification_service.notify_user("Your order has been sent!")

# BAD VERSION
