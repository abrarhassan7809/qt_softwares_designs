import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QSizePolicy
from sidebar_ui import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.icon_only_widget.hide()
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.home_btn_2.setChecked(True)

        self.trade_data_list = [
            {'Brand': 'Trade1', 'Price': 110000, 'Discount': 5000, 'Quantity': 2, 'Total': 220000,
             'Grand Total': 215000},
            {'Brand': 'Trade2', 'Price': 120000, 'Discount': 5000, 'Quantity': 2, 'Total': 240000,
             'Grand Total': 235000},
            {'Brand': 'Trade3', 'Price': 130000, 'Discount': 5000, 'Quantity': 2, 'Total': 260000,
             'Grand Total': 255000},
        ]

        self.order_data_list = [
            {'Brand': 'Order1', 'Price': 110000, 'Discount': 5000, 'Quantity': 2, 'Total': 220000,
             'Grand Total': 215000},
            {'Brand': 'Order2', 'Price': 120000, 'Discount': 5000, 'Quantity': 2, 'Total': 240000,
             'Grand Total': 235000},
            {'Brand': 'Order3', 'Price': 130000, 'Discount': 5000, 'Quantity': 2, 'Total': 260000,
             'Grand Total': 255000},
        ]

        self.history_data_list = [
            {'Brand': 'History1', 'Price': 110000, 'Discount': 5000, 'Quantity': 2, 'Total': 220000,
             'Grand Total': 215000},
            {'Brand': 'History2', 'Price': 120000, 'Discount': 5000, 'Quantity': 2, 'Total': 240000,
             'Grand Total': 235000},
            {'Brand': 'History3', 'Price': 130000, 'Discount': 5000, 'Quantity': 2, 'Total': 260000,
             'Grand Total': 255000},
        ]

        self.load_trade_table()
        self.load_order_table()
        self.load_history_table()

    def load_trade_table(self):
        self.ui.tableWidget_2.setRowCount(len(self.trade_data_list))
        self.ui.tableWidget_2.setColumnCount(len(self.trade_data_list[0]))
        self.ui.tableWidget_2.setHorizontalHeaderLabels(
            ('Brand', 'Price', 'Discount', 'Quantity', 'Total', 'Grand Total'))

        for row, data in enumerate(self.trade_data_list):
            self.populate_trade_data(self.ui.tableWidget_2, row, data)

    def load_order_table(self):
        self.ui.tableWidget_3.setRowCount(len(self.order_data_list))
        self.ui.tableWidget_3.setColumnCount(len(self.order_data_list[0]))
        self.ui.tableWidget_3.setHorizontalHeaderLabels(
            ('Brand', 'Price', 'Discount', 'Quantity', 'Total', 'Grand Total'))

        for row, data in enumerate(self.order_data_list):
            self.populate_order_data(self.ui.tableWidget_3, row, data)

    def load_history_table(self):
        self.ui.tableWidget_4.setRowCount(len(self.history_data_list))
        self.ui.tableWidget_4.setColumnCount(len(self.history_data_list[0]))
        self.ui.tableWidget_4.setHorizontalHeaderLabels(
            ('Brand', 'Price', 'Discount', 'Quantity', 'Total', 'Grand Total'))

        for row, data in enumerate(self.history_data_list):
            self.populate_history_data(self.ui.tableWidget_4, row, data)

    def populate_trade_data(self, table, row, data):
        for col, (key, value) in enumerate(data.items()):
            item = QTableWidgetItem(str(value))
            table.setItem(row, col, item)

    def populate_order_data(self, table, row, data):
        for col, (key, value) in enumerate(data.items()):
            item = QTableWidgetItem(str(value))
            table.setItem(row, col, item)

    def populate_history_data(self, table, row, data):
        for col, (key, value) in enumerate(data.items()):
            item = QTableWidgetItem(str(value))
            table.setItem(row, col, item)

    def on_search_btn_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(5)
        search_text = self.ui.search_input.text().strip()
        if search_text:
            self.ui.label_7.setText(search_text)

    def on_user_btn_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(6)

    def on_home_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def on_home_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def on_trade_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def on_trade_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def on_order_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def on_order_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def on_history_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(3)

    def on_history_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(3)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    with open("style.qss", "r") as style_file:
        style_str = style_file.read()
    app.setStyleSheet(style_str)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
