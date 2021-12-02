from application import app, db, csv_into_bd

# Первичные функции старта
def startScripts():
    db.create_all()     # Создание таблиц в БД
    csv_into_bd()   # Ввод данных из CSV в БД

# Запуск приложения
if __name__ == '__main__':
    startScripts()
    app.run(debug=True)