class ChatBot:
    def __init__(self):
        self.schedule = {}

    def chat(self, message):
        # Здесь будет логика обработки сообщений от пользователя
        pass

    def set_schedule(self, user_id, event, time):
        self.schedule[user_id] = (event, time)

    def notify(self, user_id):
        event, time = self.schedule.get(user_id, (None, None))
        if event and time:
            # Здесь будет логика отправки уведомлений пользователю
            pass

class Application:
    def __init__(self):
        self.chat_bot = ChatBot()

    def receive_message(self, user_id, message):
        self.chat_bot.chat(message)

    def set_schedule(self, user_id, event, time):
        self.chat_bot.set_schedule(user_id, event, time)

    def notify_users(self):
        for user_id in self.chat_bot.schedule.keys():
            self.chat_bot.notify(user_id)
