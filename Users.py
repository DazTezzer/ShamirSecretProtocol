from tkinter import *
import Shamir_Protocol as sh
from tkinter.messagebox import showerror
import random


class main_form():
    def __init__(self, token):
        self.user1 = Tk()
        self.user1.title("Отправитель")
        self.user1.geometry('850x550')
        self.user1.resizable(width=False, height=False)
        self.secret = ""
        self.FIELD_SIZE = ""
        self.shares = ""
        self.pool = ""
        self.t, self.n = 3, 5
        self.gen = Button(self.user1, text="Сгенерировать большое простое число", command=self.gen_click).grid(column=0,
                                                                                                               row=0,
                                                                                                               padx=10,
                                                                                                               pady=15)
        self.gen_label = Label(self.user1, text="Большое простое число P : \n", wraplength=200)
        self.gen_label.grid(column=1, row=0, padx=100, pady=0)
        self.check = Button(self.user1, text="Проверка на простое число", command=self.check_click)
        self.check.grid(column=0, row=1, padx=10, pady=10)
        self.ferm_check = Label(self.user1, text="Теорема Ферма - ")
        self.ferm_check.grid(column=1, row=1, padx=10, pady=0)
        self.miller_check = Label(self.user1, text="Миллера Рабина - ")
        self.miller_check.grid(column=1, row=2, padx=10, pady=0)

        self.s = Label(self.user1, text="Секретное сообщение s")
        self.s.grid(column=0, row=3, padx=10, pady=0)
        self.s1 = Label(self.user1, text="Всего точек n = 5 \n количсетво точек для востановления к = 3 \n k-1 = 2")
        self.s1.grid(column=1, row=3, padx=10, pady=0)

        self.secret_text = Text(self.user1, width=50, height=20)
        self.secret_text.grid(column=0, row=4, padx=10, pady=0)
        self.Shares = Text(self.user1, width=50, height=20, state=DISABLED)
        self.Shares.grid(column=1, row=4, padx=10, pady=0)

        self.create_shares = Button(self.user1, text="Создать shares", state=DISABLED, command=self.create_shares_click)
        self.create_shares.grid(column=0, row=5, padx=10, pady=10)
        self.send_Combining_shares = Button(self.user1, text="Отправить получателям", state=DISABLED,
                                            command=self.send_Combining_shares_click)
        self.send_Combining_shares.grid(column=1, row=5, padx=10, pady=10)

        self.user2 = Tk()
        self.user2.title("Получатель 1")
        self.user2.geometry('850x700')
        self.user2.resizable(width=False, height=True)
        self.check2 = Label(self.user2, text="0")
        user = self.user2
        self.Combining_shares2 = Text(user, width=50, height=20, state=DISABLED)
        self.Combining_shares2.grid(column=0, row=2, padx=10, pady=0)
        self.reconstructed_secret_text2 = Text(user, width=50, height=20, state=DISABLED)
        self.reconstructed_secret_text2.grid(column=1, row=2, padx=10, pady=0)
        self.reconstruct_secret_text2 = Button(user, text="Восстановить секрет",
                                               command=lambda :self.reconstruct_secret_text_click(self.reconstructed_secret_text2,self.check2), state=DISABLED)
        self.reconstruct_secret_text2.grid(column=1, row=0, padx=10, pady=15)

        self.user2_s = Label(self.user2, text="", wraplength=400)
        self.user2_s.grid(column=0, row=0, padx=10, pady=0)

        self.send2_2 = Button(user, text="Отправить Получателю 2", state=DISABLED, command= lambda: (self.send(self.send2_2,self.user2_s["text"],self.Combining_shares3,self.check3)))
        self.send2_2.grid(column=0, row=3, padx=10, pady=10)
        self.send2_3 = Button(user, text="Отправить Получателю 3", state=DISABLED, command= lambda: self.send(self.send2_3,self.user2_s["text"],self.Combining_shares4,self.check4))
        self.send2_3.grid(column=1, row=3, padx=10, pady=10)
        self.send2_4 = Button(user, text="Отправить Получателю 4", state=DISABLED, command= lambda: self.send(self.send2_4,self.user2_s["text"],self.Combining_shares5,self.check5))
        self.send2_4.grid(column=0, row=4, padx=10, pady=10)
        self.send2_5 = Button(user, text="Отправить Получателю 5", state=DISABLED, command= lambda: self.send(self.send2_5,self.user2_s["text"],self.Combining_shares6,self.check6))
        self.send2_5.grid(column=1, row=4, padx=10, pady=10)

        self.user3 = Tk()
        self.user3.title("Получатель 2")
        self.user3.geometry('850x700')
        self.user3.resizable(width=False, height=True)
        self.check3 = Label(self.user3, text="0")
        user = self.user3
        self.Combining_shares3 = Text(user, width=50, height=20, state=DISABLED)
        self.Combining_shares3.grid(column=0, row=2, padx=10, pady=0)
        self.reconstructed_secret_text3 = Text(user, width=50, height=20, state=DISABLED)
        self.reconstructed_secret_text3.grid(column=1, row=2, padx=10, pady=0)

        self.user3_s = Label(self.user3, text="", wraplength=400)
        self.user3_s.grid(column=0, row=0, padx=10, pady=0)

        self.reconstruct_secret_text3 = Button(user, text="Восстановить секрет",
                                               command=lambda :self.reconstruct_secret_text_click(self.reconstructed_secret_text3,self.check3), state=DISABLED)
        self.reconstruct_secret_text3.grid(column=1, row=0, padx=10, pady=15)
        self.send3_1 = Button(user, text="Отправить Получателю 1", state=DISABLED, command= lambda: self.send(self.send3_1,self.user3_s["text"],self.Combining_shares2,self.check2))
        self.send3_1.grid(column=0, row=3, padx=10, pady=10)
        self.send3_3 = Button(user, text="Отправить Получателю 3", state=DISABLED, command= lambda: self.send(self.send3_3,self.user3_s["text"],self.Combining_shares4,self.check4))
        self.send3_3.grid(column=1, row=3, padx=10, pady=10)
        self.send3_4 = Button(user, text="Отправить Получателю 4", state=DISABLED, command= lambda: self.send(self.send3_4,self.user3_s["text"],self.Combining_shares5,self.check5))
        self.send3_4.grid(column=0, row=4, padx=10, pady=10)
        self.send3_5 = Button(user, text="Отправить Получателю 5", state=DISABLED, command= lambda: self.send(self.send3_5,self.user3_s["text"],self.Combining_shares6,self.check6))
        self.send3_5.grid(column=1, row=4, padx=10, pady=10)

        self.user4 = Tk()
        self.user4.title("Получатель 3")
        self.user4.geometry('850x700')
        self.user4.resizable(width=False, height=True)
        self.check4 = Label(self.user4, text="0")
        user = self.user4
        self.Combining_shares4 = Text(user, width=50, height=20, state=DISABLED)
        self.Combining_shares4.grid(column=0, row=2, padx=10, pady=0)
        self.reconstructed_secret_text4 = Text(user, width=50, height=20, state=DISABLED)
        self.reconstructed_secret_text4.grid(column=1, row=2, padx=10, pady=0)

        self.user4_s = Label(self.user4, text="", wraplength=400)
        self.user4_s.grid(column=0, row=0, padx=10, pady=0)

        self.reconstruct_secret_text4 = Button(user, text="Восстановить секрет",
                                               command=lambda :self.reconstruct_secret_text_click(self.reconstructed_secret_text4,self.check4), state=DISABLED)
        self.reconstruct_secret_text4.grid(column=1, row=0, padx=10, pady=15)
        self.send4_1 = Button(user, text="Отправить Получателю 1", state=DISABLED, command= lambda: self.send(self.send4_1,self.user4_s["text"],self.Combining_shares2,self.check2))
        self.send4_1.grid(column=0, row=3, padx=10, pady=10)
        self.send4_2 = Button(user, text="Отправить Получателю 2", state=DISABLED, command= lambda: self.send(self.send4_2,self.user4_s["text"],self.Combining_shares3,self.check3))
        self.send4_2.grid(column=1, row=3, padx=10, pady=10)
        self.send4_4 = Button(user, text="Отправить Получателю 4", state=DISABLED, command= lambda: self.send(self.send4_4,self.user4_s["text"],self.Combining_shares5,self.check5))
        self.send4_4.grid(column=0, row=4, padx=10, pady=10)
        self.send4_5 = Button(user, text="Отправить Получателю 5", state=DISABLED, command= lambda: self.send(self.send4_5,self.user4_s["text"],self.Combining_shares6,self.check6))
        self.send4_5.grid(column=1, row=4, padx=10, pady=10)

        self.user5 = Tk()
        self.user5.title("Получатель 4")
        self.user5.geometry('850x700')
        self.user5.resizable(width=False, height=True)
        self.check5 = Label(self.user5, text="0")
        user = self.user5
        self.Combining_shares5 = Text(user, width=50, height=20, state=DISABLED)
        self.Combining_shares5.grid(column=0, row=2, padx=10, pady=0)
        self.reconstructed_secret_text5 = Text(user, width=50, height=20, state=DISABLED)
        self.reconstructed_secret_text5.grid(column=1, row=2, padx=10, pady=0)

        self.user5_s = Label(self.user5, text="", wraplength=400)
        self.user5_s.grid(column=0, row=0, padx=10, pady=0)

        self.reconstruct_secret_text5 = Button(user, text="Восстановить секрет",
                                               command=lambda :self.reconstruct_secret_text_click(self.reconstructed_secret_text5,self.check5), state=DISABLED)
        self.reconstruct_secret_text5.grid(column=1, row=0, padx=10, pady=15)
        self.send5_1 = Button(user, text="Отправить Получателю 1", state=DISABLED, command= lambda: self.send(self.send5_1,self.user5_s["text"],self.Combining_shares2,self.check2))
        self.send5_1.grid(column=0, row=3, padx=10, pady=10)
        self.send5_2 = Button(user, text="Отправить Получателю 2", state=DISABLED, command= lambda: self.send(self.send5_2,self.user5_s["text"],self.Combining_shares3,self.check3))
        self.send5_2.grid(column=1, row=3, padx=10, pady=10)
        self.send5_3 = Button(user, text="Отправить Получателю 3", state=DISABLED, command= lambda: self.send(self.send5_3,self.user5_s["text"],self.Combining_shares4,self.check4))
        self.send5_3.grid(column=0, row=4, padx=10, pady=10)
        self.send5_5 = Button(user, text="Отправить Получателю 5", state=DISABLED, command= lambda: self.send(self.send5_5,self.user5_s["text"],self.Combining_shares6,self.check6))
        self.send5_5.grid(column=1, row=4, padx=10, pady=10)



        self.user6 = Tk()
        self.user6.title("Получатель 5")
        self.user6.geometry('850x700')
        self.user6.resizable(width=False, height=True)
        self.check6 = Label(self.user6, text="0")
        user = self.user6
        self.Combining_shares6 = Text(user, width=50, height=20, state=DISABLED)
        self.Combining_shares6.grid(column=0, row=2, padx=10, pady=0)
        self.reconstructed_secret_text6 = Text(user, width=50, height=20, state=DISABLED)
        self.reconstructed_secret_text6.grid(column=1, row=2, padx=10, pady=0)

        self.user6_s = Label(self.user6, text="", wraplength=400)
        self.user6_s.grid(column=0, row=0, padx=10, pady=0)

        self.reconstruct_secret_text6 = Button(user, text="Восстановить секрет",
                                               command=lambda :self.reconstruct_secret_text_click(self.reconstructed_secret_text6,self.check6), state=DISABLED)
        self.reconstruct_secret_text6.grid(column=1, row=0, padx=10, pady=15)
        self.send6_1 = Button(user, text="Отправить Получателю 1", state=DISABLED, command= lambda: self.send(self.send6_1,self.user6_s["text"],self.Combining_shares2,self.check2))
        self.send6_1.grid(column=0, row=3, padx=10, pady=10)
        self.send6_2 = Button(user, text="Отправить Получателю 2", state=DISABLED, command= lambda: self.send(self.send6_2,self.user6_s["text"],self.Combining_shares3,self.check3))
        self.send6_2.grid(column=1, row=3, padx=10, pady=10)
        self.send6_3 = Button(user, text="Отправить Получателю 3", state=DISABLED, command= lambda: self.send(self.send6_3,self.user6_s["text"],self.Combining_shares4,self.check4))
        self.send6_3.grid(column=0, row=4, padx=10, pady=10)
        self.send6_4 = Button(user, text="Отправить Получателю 4", state=DISABLED, command= lambda: self.send(self.send6_4,self.user6_s["text"],self.Combining_shares5,self.check5))
        self.send6_4.grid(column=1, row=4, padx=10, pady=10)

        self.user1.protocol("WM_DELETE_WINDOW", lambda: (
            self.user1.destroy(), self.user2.destroy(), self.user3.destroy(), self.user4.destroy(),
            self.user5.destroy(),
            self.user6.destroy()))
        self.user2.protocol("WM_DELETE_WINDOW", lambda: (
            self.user1.destroy(), self.user2.destroy(), self.user3.destroy(), self.user4.destroy(),
            self.user5.destroy(),
            self.user6.destroy()))
        self.user3.protocol("WM_DELETE_WINDOW", lambda: (
            self.user1.destroy(), self.user2.destroy(), self.user3.destroy(), self.user4.destroy(),
            self.user5.destroy(),
            self.user6.destroy()))
        self.user4.protocol("WM_DELETE_WINDOW", lambda: (
            self.user1.destroy(), self.user2.destroy(), self.user3.destroy(), self.user4.destroy(),
            self.user5.destroy(),
            self.user6.destroy()))
        self.user5.protocol("WM_DELETE_WINDOW", lambda: (
            self.user1.destroy(), self.user2.destroy(), self.user3.destroy(), self.user4.destroy(),
            self.user5.destroy(),
            self.user6.destroy()))
        self.user6.protocol("WM_DELETE_WINDOW", lambda: (
            self.user1.destroy(), self.user2.destroy(), self.user3.destroy(), self.user4.destroy(),
            self.user5.destroy(),
            self.user6.destroy()))

    def send(self,button,text,box,bruh):
        a = int(bruh["text"])
        a += 1
        bruh.config(text=str(a))
        button.config(state=DISABLED)
        self.add_text(box,text)

    def gen_click(self):
        self.check.config(state=NORMAL)
        self.create_shares.config(state=DISABLED)
        self.send_Combining_shares.config(state=DISABLED)
        self.ferm_check.config(text="Теорема Ферма - ")
        self.miller_check.config(text="Миллера Рабина - ")
        self.FIELD_SIZE = sh.gen_q()
        self.gen_label.config(text="Большое простое число P : \n" + str(self.FIELD_SIZE))

    def check_click(self):
        if sh.is_prime_q(self.FIELD_SIZE):
            self.ferm_check.config(text="Теорема Ферма - Простое")
            self.miller_check.config(text="Миллера Рабина - Простое")
            self.create_shares.config(state=NORMAL)
            self.check.config(state=DISABLED)

    def create_shares_click(self):
        self.delete_text(self.Shares)

        self.secret = sh.int_from_bytes((str(self.secret_text.get("1.0", END)) + "0").encode("utf-8"))
        print(str(self.secret))
        if str(self.secret) == "2608":
            showerror(title="Ошибка", message="Поле ввода пустое")
            return 0
        self.shares = sh.generate_shares(self.n, self.t, self.secret, self.FIELD_SIZE)
        for i in range(len(self.shares)):
            old_tuple = self.shares[i]
            new_tuple = (*old_tuple, i)
            self.shares[i] = new_tuple
            self.add_text(self.Shares, "n" + str(i) + " = " + str(self.shares[i][1]) + "\n\nF(x) x = " + str(
                self.shares[i][0]) + "\n\np = " + str(
                self.FIELD_SIZE) + "\n\nk-1 = 2 \n\n--------------------------------------------------\n")

        self.send_Combining_shares.config(state=NORMAL)

    def send_Combining_shares_click(self):

        self.check2.config(text="0")
        self.check3.config(text="0")
        self.check4.config(text="0")
        self.check5.config(text="0")
        self.check6.config(text="0")

        self.delete_text(self.reconstructed_secret_text2)
        self.delete_text(self.reconstructed_secret_text3)
        self.delete_text(self.reconstructed_secret_text4)
        self.delete_text(self.reconstructed_secret_text5)
        self.delete_text(self.reconstructed_secret_text6)

        self.pool = random.sample(self.shares, self.t)

        self.delete_text(self.Combining_shares2)
        self.delete_text(self.Combining_shares3)
        self.delete_text(self.Combining_shares4)
        self.delete_text(self.Combining_shares5)
        self.delete_text(self.Combining_shares6)

        self.user2_s.config(text="")

        self.user2_s.config(text="n" + str(self.shares[0][2]) + " = " + str(self.shares[0][1]) + "\n\nF(x) x = " + str(
            self.shares[0][0]) + "\n\np = " + str(
            self.FIELD_SIZE) + "\n\nk-1 = 2 \n\n--------------------------------------------------\n")

        self.user3_s.config(text=
                      "n" + str(self.shares[1][2]) + " = " + str(self.shares[1][1]) + "\n\nF(x) x = " + str(
                          self.shares[1][0]) + "\n\np = " + str(
                          self.FIELD_SIZE) + "\n\nk-1 = 2 \n\n--------------------------------------------------\n")
        self.user4_s.config(text=
                      "n" + str(self.shares[2][2]) + " = " + str(self.shares[2][1]) + "\n\nF(x) x = " + str(
                          self.shares[2][0]) + "\n\np = " + str(
                          self.FIELD_SIZE) + "\n\nk-1 = 2 \n\n--------------------------------------------------\n")
        self.user5_s.config(text=
                      "n" + str(self.shares[3][2]) + " = " + str(self.shares[3][1]) + "\n\nF(x) x = " + str(
                          self.shares[3][0]) + "\n\np = " + str(
                          self.FIELD_SIZE) + "\n\nk-1 = 2 \n\n--------------------------------------------------\n")
        self.user6_s.config(text=
                      "n" + str(self.shares[4][2]) + " = " + str(self.shares[4][1]) + "\n\nF(x) x = " + str(
                          self.shares[4][0]) + "\n\np = " + str(
                          self.FIELD_SIZE) + "\n\nk-1 = 2 \n\n--------------------------------------------------\n")

        self.reconstruct_secret_text2.config(state=NORMAL)
        self.reconstruct_secret_text3.config(state=NORMAL)
        self.reconstruct_secret_text4.config(state=NORMAL)
        self.reconstruct_secret_text5.config(state=NORMAL)
        self.reconstruct_secret_text6.config(state=NORMAL)

        self.send2_2.config(state=NORMAL)
        self.send2_3.config(state=NORMAL)
        self.send2_4.config(state=NORMAL)
        self.send2_5.config(state=NORMAL)

        self.send3_1.config(state=NORMAL)
        self.send3_3.config(state=NORMAL)
        self.send3_4.config(state=NORMAL)
        self.send3_5.config(state=NORMAL)

        self.send4_2.config(state=NORMAL)
        self.send4_1.config(state=NORMAL)
        self.send4_4.config(state=NORMAL)
        self.send4_5.config(state=NORMAL)

        self.send5_2.config(state=NORMAL)
        self.send5_3.config(state=NORMAL)
        self.send5_1.config(state=NORMAL)
        self.send5_5.config(state=NORMAL)

        self.send6_2.config(state=NORMAL)
        self.send6_3.config(state=NORMAL)
        self.send6_4.config(state=NORMAL)
        self.send6_1.config(state=NORMAL)

    def reconstruct_secret_text_click(self, box,bruh):
        print(bruh["text"])

        a = int(bruh["text"])
        if (a >= 2):
            self.delete_text(self.reconstructed_secret_text2)
            self.delete_text(self.reconstructed_secret_text3)
            self.delete_text(self.reconstructed_secret_text4)
            self.delete_text(self.reconstructed_secret_text5)
            self.delete_text(self.reconstructed_secret_text6)

            out = sh.bytes_from_int(sh.reconstruct_secret(self.pool)).decode('utf-8')
            new_s = str(out)[:-1]
            self.add_text(box, str(new_s))
        else:
            return 0

    def add_text(self, widget, text):
        widget.config(state=NORMAL)
        widget.insert(END, text)
        widget.config(state=DISABLED)

    def delete_text(self, widget):
        widget.config(state=NORMAL)
        widget.delete("1.0", END)
        widget.config(state=DISABLED)
