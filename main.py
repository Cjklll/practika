import telegram
from datetime import date
from telegram.ext import Updater, CommandHandler, MessageHandler, ConversationHandler
from telegram.ext.filters import Filters

current_date = date.today()
print(current_date)

API_KEY = '6498564072:AAHjvx3ODiPl8MhQ6WmkqBWr7OwS4YZPeq8'

GENDER, AGE, FIO, BORN, FINISH = range(5)

bot = telegram.Bot(token=API_KEY)

# Функция для начала
def start(update, context):
    user_id = update.effective_user.id
    context.user_data.clear()  # Очищаем данные пользователя
    context.bot.send_message(chat_id=user_id, text="Давайте начнем составление анкеты. Пожалуйста, укажите ваш пол.")
    print(GENDER)
    return GENDER

# Функция для обработки пола
def get_gender(update, context):
    user_id = update.effective_user.id
    user_data = context.user_data
    gender = update.message.text
    user_data['gender'] = gender
    context.bot.send_message(chat_id=user_id, text=f"Хорошо, вы указали пол: {gender}. Теперь укажите ваш возраст.")
    return AGE

    # Функция для обработки возраста
def get_age(update, context):
    user_id = update.effective_user.id
    user_data = context.user_data
    age = update.message.text
    user_data['age'] = age
    context.bot.send_message(chat_id=user_id,
                             text=f"Отлично, ваш возраст: {age}. Теперь расскажите нам о ваше ФИО.")
    return FIO

# Функция для обработки ФИО
def get_FIO(update, context):
    user_id = update.effective_user.id
    user_data = context.user_data
    FIO = update.message.text
    user_data['FIO'] = FIO
    context.bot.send_message(chat_id=user_id, text=f"Хорошо, вы указали ФИО: {FIO}. Теперь укажите вашу дату рождения.")
    return BORN


# Функция для обработки даты рождения
def get_BORN(update, context):
    user_id = update.effective_user.id
    user_data = context.user_data
    hobbies = update.message.text
    user_data['BORN'] = BORN
    context.bot.send_message(chat_id=user_id, text=f"Спасибо! Укажите вашу медицинскую организацию.")
    print(BORN)
    return ConversationHandler.END

# Функция для обработки ФИО
#def get_FIO(update, context):
    #   user_id = update.effective_user.id
    #user_data = context.user_data
    #FIO = update.message.text
    #user_data['FIO'] = FIO
    #context.bot.send_message(chat_id=user_id, text=f"Хорошо, вы указали ФИО: {FIO}. Теперь укажите вашу дату рождения.")
    #return BORN
# Функция для завершения диалога
def cancel(update, context):
    user_id = update.effective_user.id
    context.bot.send_message(chat_id=user_id, text="Анкета не была заполнена. Вы можете начать заново, введя /start.")
    return ConversationHandler.END

# Обработка команд и диалога
updater = Updater(token=API_KEY, use_context=True)
dispatcher = updater.dispatcher

conv_handler = ConversationHandler(
    entry_points=[CommandHandler('start', start)],
    states={
        GENDER: [MessageHandler(Filters.text & ~Filters.command, get_gender)],
        AGE: [MessageHandler(Filters.text & ~Filters.command, get_age)],
        FIO: [MessageHandler(Filters.text & ~Filters.command, get_FIO)],
        BORN: [MessageHandler(Filters.text & ~Filters.command, get_BORN)],
    },
    fallbacks=[CommandHandler('cancel', cancel)],
)
dispatcher.add_handler(conv_handler)
# Запуск
updater.start_polling()
updater.idle()

