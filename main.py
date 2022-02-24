mport telebot
import psycopg2
from week import weeker
from telebot import types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
conn = psycopg2.connect(database="bot_r",
                        user="postgres",
                        password="09092002bN!",
                        host="localhost",
                        port="5432",)
cursor = conn.cursor()
s = int(weeker())


token = "2101948819:AAFInV9zr2LyHV62ujd1-2gpKHEMcfJeGK0"
bot = telebot.TeleBot(token)



@bot.message_handler(commands=['start'])
def start_message(message):
    keyboard1 =types.ReplyKeyboardMarkup()
    button1 = types.KeyboardButton("Понедельник")
    button2 = types.KeyboardButton("Вторник")
    button3 = types.KeyboardButton("Среда")
    button4 = types.KeyboardButton("Четверг")
    button5 = types.KeyboardButton("Пятница")
    button6 = types.KeyboardButton("Расписание на текущую неделю")
    button7 = types.KeyboardButton("Расписание на следующую неделю")
    keyboard1.row(button1, button2)
    keyboard1.row(button3, button4)
    keyboard1.row(button5, button6)
    keyboard1.row(button7)
    bot.send_message(message.chat.id,'Привет',reply_markup=keyboard1)








@bot.message_handler(commands=['help'])
def start_message(message):
  bot.send_message(message.chat.id, 'Я умею:\n   \n /week - определение недели\n   \n/mtuci - вывод ссылки на официальный сайт МТУСИ\n   \n Для просмотра интересующего вас расписания воспользуйтесь графическими конпками. ')

@bot.message_handler(commands=['week'])
def start_message(message):
  if s == 1:
      bot.send_message(message.chat.id, 'Сейчас нижняя неделя')
  elif s == 0:
      bot.send_message(message.chat.id, 'Сейчас верхняя неделя')
@bot.message_handler(commands=['mtuci'])
def start_message(message):
      bot.send_message(message.chat.id, 'https://mtuci.ru/')

@bot.message_handler(content_types={'text'})
def manipulator(message):
  if message.text == "Понедельник" and s == 0:
      cursor.execute("select timetable.start_time, subject.name, teacher.full_name, timetable.room_numb from timetable join subject on timetable.subject = subject.id join teacher on timetable.teacher = teacher.id where timetable.day = 'Понедельник1';")
      out = cursor.fetchall()
      out1 = str("")
      for row in out:
          for i in range(4):
            out1 = out1 + str(row[i]) +'  '
          out1 +='\n'

      bot.send_message(message.chat.id,out1)
  elif message.text == "Вторник" and s == 0:
      cursor.execute(
          "select timetable.start_time, subject.name, teacher.full_name, timetable.room_numb from timetable join subject on timetable.subject = subject.id join teacher on timetable.teacher = teacher.id where timetable.day = 'Вторник1';")
      out = cursor.fetchall()
      out1 = str("")
      for row in out:
          for i in range(4):
              out1 = out1 + str(row[i]) + '  '
          out1 += '\n'

      bot.send_message(message.chat.id, out1)
  elif message.text == "Среда" and s == 0:
      cursor.execute(
          "select timetable.start_time, subject.name, teacher.full_name, timetable.room_numb from timetable join subject on timetable.subject = subject.id join teacher on timetable.teacher = teacher.id where timetable.day = 'Среда1';")
      out = cursor.fetchall()
      out1 = str("")
      for row in out:
          for i in range(4):
              out1 = out1 + str(row[i]) + '  '
          out1 += '\n'

      bot.send_message(message.chat.id, out1)
  elif message.text == "Четверг" and s == 0:
      cursor.execute(
          "select timetable.start_time, subject.name, teacher.full_name, timetable.room_numb from timetable join subject on timetable.subject = subject.id join teacher on timetable.teacher = teacher.id where timetable.day = 'Четверг1';")
      out = cursor.fetchall()
      out1 = str("")
      for row in out:
          for i in range(4):
              out1 = out1 + str(row[i]) + '  '
          out1 += '\n'

      bot.send_message(message.chat.id, out1)
  elif message.text == "Пятница" and s == 0:
      cursor.execute(
          "select timetable.start_time, subject.name, teacher.full_name, timetable.room_numb from timetable join subject on timetable.subject = subject.id join teacher on timetable.teacher = teacher.id where timetable.day = 'Пятница1';")
      out = cursor.fetchall()
      out1 = str("")
      for row in out:
          for i in range(4):
              out1 = out1 + str(row[i]) + '  '
          out1 += '\n'

      bot.send_message(message.chat.id, out1)
  if message.text == "Понедельник" and s == 1:
      cursor.execute("select timetable.start_time, subject.name, teacher.full_name, timetable.room_numb from timetable join subject on timetable.subject = subject.id join teacher on timetable.teacher = teacher.id where timetable.day = 'Понедельник0';")
      out = cursor.fetchall()
      out1 = str("")
      for row in out:
          for i in range(4):
            out1 = out1 + str(row[i]) +'  '
          out1 +='\n'

      bot.send_message(message.chat.id,out1)
  elif message.text == "Вторник" and s == 1:
      cursor.execute(
          "select timetable.start_time, subject.name, teacher.full_name, timetable.room_numb from timetable join subject on timetable.subject = subject.id join teacher on timetable.teacher = teacher.id where timetable.day = 'Вторник0';")
      out = cursor.fetchall()
      out1 = str("")
      for row in out:
          for i in range(4):
              out1 = out1 + str(row[i]) + '  '
          out1 += '\n'

      bot.send_message(message.chat.id, out1)
  elif message.text == "Среда" and s == 1:
      cursor.execute(
          "select timetable.start_time, subject.name, teacher.full_name, timetable.room_numb from timetable join subject on timetable.subject = subject.id join teacher on timetable.teacher = teacher.id where timetable.day = 'Среда0';")
      out = cursor.fetchall()
      out1 = str("")
      for row in out:
          for i in range(4):
              out1 = out1 + str(row[i]) + '  '
          out1 += '\n'

      bot.send_message(message.chat.id, out1)
  elif message.text == "Четверг" and s == 1:
      cursor.execute(
          "select timetable.start_time, subject.name, teacher.full_name, timetable.room_numb from timetable join subject on timetable.subject = subject.id join teacher on timetable.teacher = teacher.id where timetable.day = 'Четверг0';")
      out = cursor.fetchall()
      out1 = str("")
      for row in out:
          for i in range(4):
              out1 = out1 + str(row[i]) + '  '
          out1 += '\n'

      bot.send_message(message.chat.id, out1)
  elif message.text == "Пятница" and s == 1:
      cursor.execute(
          "select timetable.start_time, subject.name, teacher.full_name, timetable.room_numb from timetable join subject on timetable.subject = subject.id join teacher on timetable.teacher = teacher.id where timetable.day = 'Пятница0';")
      out = cursor.fetchall()
      out1 = str("")
      for row in out:
          for i in range(4):
              out1 = out1 + str(row[i]) + '  '
          out1 += '\n'

      bot.send_message(message.chat.id, out1)
  elif message.text == "Расписание на текущую неделю":
      cursor.execute(
          "select timetable.start_time, subject.name, teacher.full_name, timetable.room_numb from timetable join subject on timetable.subject = subject.id join teacher on timetable.teacher = teacher.id where timetable.day = 'Понедельник0';")
      out = cursor.fetchall()
      out1 = str("")
      for row in out:
          for i in range(4):
              out1 = out1 + str(row[i]) + '  '
          out1 += '\n'

      bot.send_message(message.chat.id, out1)
      cursor.execute(
          "select timetable.start_time, subject.name, teacher.full_name, timetable.room_numb from timetable join subject on timetable.subject = subject.id join teacher on timetable.teacher = teacher.id where timetable.day = 'Вторник0';")
      out = cursor.fetchall()
      out1 = str("")
      for row in out:
          for i in range(4):
              out1 = out1 + str(row[i]) + '  '
          out1 += '\n'

      bot.send_message(message.chat.id, out1)
      cursor.execute(
          "select timetable.start_time, subject.name, teacher.full_name, timetable.room_numb from timetable join subject on timetable.subject = subject.id join teacher on timetable.teacher = teacher.id where timetable.day = 'Среда0';")
      out = cursor.fetchall()
      out1 = str("")
      for row in out:
          for i in range(4):
              out1 = out1 + str(row[i]) + '  '
          out1 += '\n'

      bot.send_message(message.chat.id, out1)
      cursor.execute(
          "select timetable.start_time, subject.name, teacher.full_name, timetable.room_numb from timetable join subject on timetable.subject = subject.id join teacher on timetable.teacher = teacher.id where timetable.day = 'Четверг0';")
      out = cursor.fetchall()
      out1 = str("")
      for row in out:
          for i in range(4):
              out1 = out1 + str(row[i]) + '  '
          out1 += '\n'

      bot.send_message(message.chat.id, out1)
      cursor.execute(
          "select timetable.start_time, subject.name, teacher.full_name, timetable.room_numb from timetable join subject on timetable.subject = subject.id join teacher on timetable.teacher = teacher.id where timetable.day = 'Пятница0';")
      out = cursor.fetchall()
      out1 = str("")
      for row in out:
          for i in range(4):
              out1 = out1 + str(row[i]) + '  '
          out1 += '\n'

      bot.send_message(message.chat.id, out1)


  elif message.text == "Расписание на следующую неделю":
      cursor.execute(
          "select timetable.start_time, subject.name, teacher.full_name, timetable.room_numb from timetable join subject on timetable.subject = subject.id join teacher on timetable.teacher = teacher.id where timetable.day = 'Понедельник1';")
      out = cursor.fetchall()
      out1 = str("")
      for row in out:
          for i in range(4):
              out1 = out1 + str(row[i]) + '  '
          out1 += '\n'

      bot.send_message(message.chat.id, out1)
      cursor.execute(
          "select timetable.start_time, subject.name, teacher.full_name, timetable.room_numb from timetable join subject on timetable.subject = subject.id join teacher on timetable.teacher = teacher.id where timetable.day = 'Вторник1';")
      out = cursor.fetchall()
      out1 = str("")
      for row in out:
          for i in range(4):
              out1 = out1 + str(row[i]) + '  '
          out1 += '\n'

      bot.send_message(message.chat.id, out1)
      cursor.execute(
          "select timetable.start_time, subject.name, teacher.full_name, timetable.room_numb from timetable join subject on timetable.subject = subject.id join teacher on timetable.teacher = teacher.id where timetable.day = 'Среда1';")
      out = cursor.fetchall()
      out1 = str("")
      for row in out:
          for i in range(4):
              out1 = out1 + str(row[i]) + '  '
          out1 += '\n'

      bot.send_message(message.chat.id, out1)
      cursor.execute(
          "select timetable.start_time, subject.name, teacher.full_name, timetable.room_numb from timetable join subject on timetable.subject = subject.id join teacher on timetable.teacher = teacher.id where timetable.day = 'Четверг1';")
      out = cursor.fetchall()
      out1 = str("")
      for row in out:
          for i in range(4):
              out1 = out1 + str(row[i]) + '  '
          out1 += '\n'

      bot.send_message(message.chat.id, out1)
      cursor.execute(
          "select timetable.start_time, subject.name, teacher.full_name, timetable.room_numb from timetable join subject on timetable.subject = subject.id join teacher on timetable.teacher = teacher.id where timetable.day = 'Пятница1';")
      out = cursor.fetchall()
      out1 = str("")
      for row in out:
          for i in range(4):
              out1 = out1 + str(row[i]) + '  '
          out1 += '\n'

      bot.send_message(message.chat.id, out1)





bot.infinity_polling()

