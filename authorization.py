import tkinter as tk
from tkinter import messagebox

# Пример базы данных пользователей (логин: пароль)
users_db = {
    'user1': 'password1',
    'user2': 'password2',
    'admin': 'adminpass'
}

class User()


# Функция для проверки логина и пароля
def login():
    username = entry_username.get()
    password = entry_password.get()

    # Проверка, существует ли логин и правильный ли пароль
    if username in users_db and users_db[username] == password:
        messagebox.showinfo("Успех", "Вы успешно вошли!")
    else:
        messagebox.showerror("Ошибка", "Неверный логин или пароль!")


# Создание окна
root = tk.Tk()
root.title("Авторизация")

# Метки и поля для ввода логина и пароля
label_username = tk.Label(root, text="Логин:")
label_username.pack(pady=5)
entry_username = tk.Entry(root)
entry_username.pack(pady=5)

label_password = tk.Label(root, text="Пароль:")
label_password.pack(pady=5)
entry_password = tk.Entry(root, show='*')  # Скрытие символов пароля
entry_password.pack(pady=5)

# Кнопка для входа
button_login = tk.Button(root, text="Войти", command=login)
button_login.pack(pady=10)

# Запуск главного цикла приложения
root.mainloop()
