import Users
from tkinter import *
import uuid
from tkinter.messagebox import showerror, showinfo

window = Tk()

window.title('Авторизация')

window.geometry('450x230')

window.resizable(False, False)

font_header = ('Arial', 15)
font_entry = ('Arial', 12)
label_font = ('Arial', 11)
base_padding = {'padx': 10, 'pady': 8}
header_padding = {'padx': 10, 'pady': 12}


def clicked():

    username = username_entry.get()
    password = password_entry.get()
    if(str(username) == "root" and str(password) == "123"):
        token = str(uuid.uuid4())
        showinfo(title="Аутентификация", message="Аутентификация прошла успешно! \n Ваш токен : " + token)
        window.destroy()
        form1 = Users.main_form(token)
        form1.user1.mainloop()
    else:
        showerror(title="Ошибка", message="Неправльный логин или пароль")
        return 0


main_label = Label(window, text='Авторизация', font=font_header, justify=CENTER, **header_padding)
main_label.pack()


username_label = Label(window, text='Имя пользователя', font=label_font , **base_padding)
username_label.pack()

username_entry = Entry(window, bg='#fff', fg='#444', font=font_entry)
username_entry.pack()

password_label = Label(window, text='Пароль', font=label_font , **base_padding)
password_label.pack()

password_entry = Entry(window, bg='#fff', fg='#444', font=font_entry, show="●")
password_entry.pack()

send_btn = Button(window, text='Войти', command=clicked)
send_btn.pack(**base_padding)

window.mainloop()