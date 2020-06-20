import telebot
import mysql.connector

import mytoken

from datetime import datetime
TOKEN = mytoken.TOKEN
MyBot = telebot.TeleBot(TOKEN)
myDb = mysql.connector.connect(host='localhost',user='root',database='db_belajarbot')
sql = myDb.cursor()
from telebot import apihelper
waktuSekarang=datetime.now()

class mybot:
    def __init__(self):
        self.message

    @MyBot.message_handler(commands=['start'])
    def start(message):
        photo = open('img/aan.jpg','rb')
        MyBot.send_photo(message.from_user.id,photo)
        teks = mytoken.SAPA + "\n" \
                              "Admin & Developer By @muhammad farhan" + "\n"\
                              "Smk Taruna Bhakti" + "\n"\
                              "ketik /help untuk memandu anda" + "\n"\
                              "" + "\n"\
                              "Time : " + str(waktuSekarang)
        MyBot.reply_to(message,teks)

    @MyBot.message_handler(commands=['help'])
    def help(message):
        teks = "Hay" + "\n" \
                  "" + "\n"\
                  "/start : Untuk Memulai Bot mafia" + "\n" \
                  "" + "\n" \
                  "/datasiswa : Untuk Menampilkan Data Siswa"
        MyBot.reply_to(message, teks)

    @MyBot.message_handler(commands=['datasiswa'])
    def menu_data_siswa(message):
        query = "select nipd,nama,kelas from tabel_siswa"
        sql.execute(query)
        data = sql.fetchall()
        jmldata = sql.rowcount
        kumpuldata = ''
        if(jmldata>0):
            no = 0
            for x in data:
                no += 1
                kumpuldata = kumpuldata + str(x)
                print(kumpuldata)
                kumpuldata = kumpuldata.replace('(','' +"\n")
                kumpuldata = kumpuldata.replace(')','' +"\n")
                kumpuldata = kumpuldata.replace("'",'')
                kumpuldata = kumpuldata.replace(',','')     
        else:
            print('data kosong')
        # MyBot.send_message(message.from_user.id,str(kumpuldata))
        MyBot.reply_to(message,str(kumpuldata))

print(myDb)
print("-- Bot sedang berjalan --")
MyBot.polling(none_stop=True)