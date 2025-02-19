import csv
import sys
import sqlite3

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog, QTableWidgetItem

import design

#cd pythonProject3
#python -m venv venv
#source venv/bin/activate
#pip install -r requirements.txt

# Для обновления интерфейса выполнить команду: pyuic5 design.ui -o design.py


class App(QtWidgets.QMainWindow, design.Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.open_magaz.triggered.connect(self.open_magaz_file)
        self.save_magaz.triggered.connect(self.save_magaz_file)

    def open_magaz_file(self):
        con = sqlite3.connect('database.db')
        cursor = con.cursor()

        sql = 'SELECT * FROM Artist'
        out = cursor.execute(sql).fetchall()

        self.table_magaz.setColumnCount(len(out[0]))
        self.table_magaz.setRowCount(len(out))

        self.table_magaz.setHorizontalHeaderLabels(["id", "artist"])

        for row in range(self.table_magaz.rowCount()):
            for column in range(self.table_magaz.columnCount()):
                item = QTableWidgetItem(str(out[row][column]))
                print(item.text())
                self.table_magaz.setItem(row, column, item)

    def save_magaz_file(self):
        con = sqlite3.connect('database.db')
        cursor = con.cursor()

        sql = 'SELECT Imya, Nazvanie FROM Artist JOIN Albom ON Artist.id = Albom.id'
        out = cursor.execute(sql).fetchall()

        with open("db.csv", "w") as file:
            writer = csv.writer(file, delimiter="l")
            writer.writerow(("Название", "Исполнитель"))
            writer.writerows(out)

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = App()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
