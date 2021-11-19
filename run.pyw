import sys
import gui
import gui2
from modules.basedate import save_base as sb, new_base, number_of_rows as nr, list_all_id as lai, \
    instance as inst, del_v, plain, foto_list_path as flp, foto_update as fu
from PyQt5.QtTextToSpeech import QTextToSpeech
from PyQt5.QtCore import Qt, pyqtSignal, QSize, pyqtSlot, QDate
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QFileDialog, QMessageBox, QScrollArea, \
    QVBoxLayout
from PyQt5.QtGui import QIcon, QPixmap
import configparser
import shutil
import os
from functools import partial

# from PyQt5.QtChart import QChart, QCandlestickSeries, QCandlestickSet, QChartView


LIST_ID = lai()  # Возвращает список id из базы
new_base()  # Если база отсутствует, то создаем новую
val_combo = ["Вегетативные овощи", "Плодовые овощи"]
val_combo2 = ['Клубнеплодные овощи', 'Корнеплодные овощи', 'Капустные овощи',
              'Луковые овощи', 'Салатно шпинатные овощи', 'Пряные овощи', 'Десертные овощи']
val_combo3 = ['Томатные овощи', 'Тыквенные овощи', 'Бобовые овощи', 'Зерновые овощи']
val_combo4 = ['Картофель', 'Топинамбур']
val_combo5 = ['Морковь', 'Свекла', 'Редис', 'Репа', 'Редька', 'Брюква', 'Петрушка', 'Дайкон']
val_combo6 = ['Капуста белокочанная', 'Капуста краснокочанная', 'Капуста савойская', 'Капуста брюссельская',
              'Капуста цветная', 'Капуста брокколи', 'Капуста кольраби']
val_combo7 = ['Лук репчатый', 'Лук порей', 'Лук батун', 'Чеснок']
val_combo8 = ['Салат', 'Шпинат', 'Щавель']
val_combo9 = ['Укроп', 'Зелень петрушки', 'Сельдерей', 'Пастернак', 'Чабер', 'Эстрагон', 'Базилик', 'Мелисса']
val_combo10 = ['Ревень', 'Спаржа', 'Артишок']
val_combo11 = ['Томаты', 'Баклажаны', 'Острые перцы', 'Сладкие перцы']  # Томатные овощи
val_combo12 = ['Огурцы', 'Кабачки', 'Патиссоны', 'Тыквы', 'Арбузы', 'Дыни']  # Тыквенные овощи
val_combo13 = ['Горох', 'Фасоль', 'Бобы']  # Бобовые овощи
val_combo14 = ['Кукуруза', 'Подсолнечник']  # Зерновые овощи


class Viewer(QMainWindow):
    """Просмотрщик фото"""

    def __init__(self, pxm):
        QMainWindow.__init__(self)
        self.setGeometry(200, 200, 600, 800)
        self.setWindowTitle('vegetables viewer')
        scr = QScrollArea(self)
        pnl = QWidget(self)
        vbox = QVBoxLayout(self)
        self.pxm = pxm
        lbl = QLabel()
        lbl.setPixmap(self.pxm)
        vbox.addWidget(lbl)
        pnl.setLayout(vbox)
        scr.setWidget(pnl)
        self.setCentralWidget(scr)


class SecondWindow(QMainWindow):
    """Класс создает модальное окно ввода данных"""
    w2signal = pyqtSignal(str)  # Сигнал постоянных сообщений статусной строки
    w2signal2 = pyqtSignal(str)  # Сигнал временных сообщений статусной строки

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = gui2.Ui_MainWindow()
        self.ui.setupUi(self)
        self.list_path = {}  # Для сохранения путей
        f = open('resources/darkorange.stylesheet', 'r')  # Подключаем стили
        self.styleData = f.read()
        self.setStyleSheet(self.styleData)
        f.close()
        self.setWindowModality(Qt.ApplicationModal)  # Делаем окно модальным
        self.ui.pushButton_4.clicked.connect(self.save_ok)  # Сохраняем изменения
        self.ui.pushButton_5.clicked.connect(self.not_save)  # Отмена ввода
        self.ui.pushButton_6.clicked.connect(self.showDialog)  # Добавляем файлы изображений
        self.ui.comboBox.addItems(val_combo)
        self.sub_lists = val_combo2, val_combo3
        self.sub_lists2 = val_combo4, val_combo5, val_combo6, val_combo7, val_combo8, val_combo9, val_combo10
        self.sub_lists3 = val_combo11, val_combo12, val_combo13, val_combo14
        self.ui.comboBox.currentIndexChanged.connect(self.updateCombo)
        self.ui.comboBox_2.addItems(val_combo2)  # Начальные настройки
        self.ui.comboBox_3.addItems(val_combo4)  # Начальные настройки
        self.ui.dateEdit_3.setDate(QDate.currentDate())  # Начальные настройки
        self.ui.dateEdit_4.setDate(QDate.currentDate())  # Начальные настройки
        self.ui.comboBox_2.currentIndexChanged.connect(self.updateCombo2)  # Немного шаманим

    def updateCombo(self, index):
        """Добавляем список классов овощей"""
        self.ui.comboBox_2.clear()
        self.ui.comboBox_2.addItems(self.sub_lists[index])

    def updateCombo2(self, index):
        """Добавляем список подклассов овощей"""
        self.ui.comboBox_3.clear()
        if self.ui.comboBox.currentIndex() == 0:
            self.ui.comboBox_3.addItems(self.sub_lists2[index])
        else:
            self.ui.comboBox_3.addItems(self.sub_lists3[index])

    def showDialog(self):
        """Диалог для сохранения изображений"""
        image_path = QFileDialog.getOpenFileName(self, 'Выбрать файл изображения', '/vegetable')[0]
        image_name = image_path.split("/")[-1]
        if image_path:
            path = {image_name: image_path}
            self.list_path.update(path)  # Заполняем путями
            tmp = len(self.list_path)
            self.ui.label_8.setText(f"Добавлено {tmp} фото")
            self.temporary_messages2(f"Добавлено {tmp} фото")
            if tmp == 4:
                self.ui.pushButton_6.setEnabled(False)

    def save_ok(self):
        """Функция добавляет новый элемент в базу; выводит сообщение в статусбар;
        сохраняет изображения, если они выбраны; обнуляет поля ввода; закрывает окно"""
        if len(LIST_ID) == 0:
            ident = 1
        else:
            ident = LIST_ID[-1] + 1
        if self.list_path == {}:
            path_image = str(["no-photo-60.png", "no-photo-60.png", "no-photo-60.png", "no-photo-60.png"])
        else:
            path_image = str(list(self.list_path.keys()))
        if sb(ident=ident,
              name=self.ui.lineEdit_5.text(),
              super_class=self.ui.comboBox.currentText(),
              main_class=self.ui.comboBox_2.currentText(),
              child_class=self.ui.comboBox_3.currentText(),
              growing_season=self.ui.checkBox_9.isChecked(),  # вегетационный период
              hybrid=self.ui.checkBox_8.isChecked(),
              thermophilic=self.ui.checkBox_11.isChecked(),  # теплолюбивый
              light_loving=self.ui.checkBox_7.isChecked(),  # Светолюбивый
              hydrophilous=self.ui.checkBox_12.isChecked(),  # Влаголюбивое
              coord_x=int(self.ui.spinBox.text()),
              coord_y=int(self.ui.spinBox_2.text()),
              period1=int(self.ui.spinBox_5.text()),
              period2=int(self.ui.spinBox_4.text()),
              recommended_date=self.ui.dateEdit_3.date().toString(Qt.ISODate),
              temperature=int(self.ui.spinBox_3.text()),
              state=self.ui.checkBox_10.isChecked(),
              fact_date=self.ui.dateEdit_4.date().toString(Qt.ISODate),
              comment=self.ui.textEdit.toPlainText(),
              path_img=path_image
              ):

            if self.list_path:
                for key, value in self.list_path.items():
                    shutil.copy(value, f"image/{key}")  # Копируем изображения
            self.clear_window()
            if not LIST_ID:
                LIST_ID.append(1)
            else:
                LIST_ID.append(LIST_ID[-1] + 1)

            self.temporary_messages2('Сохранение прошло успешно')
            self.messages2()
            self.close()
        else:
            self.temporary_messages2('Ошибка сохранения в базе')
            self.close()

    def not_save(self):
        """Функция закрывает окно ничего не изменяя"""
        self.clear_window()
        self.close()

    def clear_window(self):
        """Функция обнуляет поля ввода"""
        self.list_path = {}
        self.ui.lineEdit_5.clear()
        self.ui.comboBox.addItems(val_combo)
        self.ui.comboBox_2.addItems(val_combo2)
        self.ui.comboBox_3.addItems(val_combo4)
        self.ui.checkBox_9.setCheckState(2)
        self.ui.checkBox_8.setCheckState(0)
        self.ui.checkBox_11.setCheckState(2)
        self.ui.checkBox_7.setCheckState(2)
        self.ui.checkBox_12.setCheckState(2)
        self.ui.spinBox.setValue(0)
        self.ui.spinBox_2.setValue(0)
        self.ui.dateEdit_3.setDate(QDate.currentDate())
        self.ui.spinBox_3.setValue(0)
        self.ui.checkBox_10.setCheckState(0)
        self.ui.dateEdit_4.setDate(QDate.currentDate())
        self.ui.textEdit.clear()
        self.ui.label_8.setText(f"Добавлено 0 фото")
        self.ui.pushButton_6.setEnabled(True)

    def temporary_messages2(self, x):
        self.w2signal2.emit(x)

    def messages2(self):
        self.w2signal.emit(str(nr()))


class MyWidget(QMainWindow):
    signal = pyqtSignal(str)
    signal2 = pyqtSignal(str)

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        f = open('resources/darkorange.stylesheet', 'r')  # Подключаем стили
        self.styleData = f.read()
        self.setStyleSheet(self.styleData)
        f.close()
        self.config = configparser.ConfigParser()  # Читаем конфиг
        self.config.read('conf.ini')
        self.current_vegetable = int(self.config['DEFAULT']['current'])  # Текущее растение
        self.w2 = SecondWindow()  # Создаем окно ввода
        self.w2.w2signal.connect(self.messages)
        self.signal.connect(self.messages)
        self.w2.w2signal2.connect(self.temporary_messages)
        self.signal2.connect(self.temporary_messages)
        self.ui = gui.Ui_MainWindow()  # Подключаем gui
        self.ui.setupUi(self)
        self.ui.add_Button.clicked.connect(self.show_window_2)  # Выводим окно ввода
        self.ui.del_Button.clicked.connect(self.del_vegetable)  # Удаляем экземпляр расстения из базы
        self.ui.pushButton_5.clicked.connect(self.plant_seeds)  # Высаживаем семена
        self.ui.pushButton_4.clicked.connect(self.add_foto)
        self.ui.button_right.setIcon(QIcon('resources/arrowright_1244.png'))
        self.ui.button_right.setIconSize(QSize(100, 100))
        self.ui.button_right.clicked.connect(self.right)
        self.ui.button_left.setIcon(QIcon('resources/leftarrow_1245.png'))
        self.ui.button_left.setIconSize(QSize(100, 100))
        self.ui.button_left.clicked.connect(self.left)
        self.speech = QTextToSpeech()
        self.stBar = self.statusBar()
        self.lb = QLabel()
        self.stBar.insertPermanentWidget(0, self.lb)
        self.signal.emit(str(nr()))  # FIXME:
        self.blocking()  # FIXME:
        # self.chart = Chart()  # FIXME:
        # self.ui.graphicsView.setChart(self.chart)
        self.ui.action_2.triggered.connect(partial(self.del_all))
        self.ui.foto1.clicked.connect(partial(self.show_viewer, 0))
        self.ui.foto2.clicked.connect(partial(self.show_viewer, 1))
        self.ui.foto3.clicked.connect(partial(self.show_viewer, 2))
        self.ui.foto4.clicked.connect(partial(self.show_viewer, 3))
        self.wiew()

    def show_viewer(self, data):
        tmp = [self.ui.foto1.pixmap(), self.ui.foto2.pixmap(), self.ui.foto3.pixmap(), self.ui.foto4.pixmap()]
        self.viewer = Viewer(tmp[data])
        # eval(f"self.ui.foto{data}.pixmap()")
        self.viewer.show()

    def add_foto(self):
        tmp = flp(self.current_vegetable)
        if tmp:
            if 'no-photo-60.png' in tmp:
                image_path = QFileDialog.getOpenFileName(self, 'Выбрать файл изображения', '/vegetable')[0]
                if image_path:
                    image_name = image_path.split("/")[-1]
                    shutil.copy(image_path, f"image/{image_name}")  # Копируем изображения
                    tmp.insert(0, image_name)
                    tmp.pop(-1)
                    fu(tmp, self.current_vegetable)
                    self.wiew()

    def show_window_2(self):
        self.w2.show()

    def plant_seeds(self):
        if plain(self.current_vegetable):
            self.ui.label_14.setText('Высажено')
            self.ui.pushButton_5.setEnabled(False)
        else:
            self.signal2.emit("Не удалось высадить семена")

    def wiew(self):
        if self.current_vegetable in LIST_ID:
            if len(LIST_ID) == 0:
                data = (0, 'Овощи отсутствуют', '', '', '', 0, 0, 0, 0, 0, 0, 0, '', 0, 0, '', '', "[]")
            else:

                data = inst(self.current_vegetable)
            tmp = []
            self.ui.label_5.setText(data[1])
            self.ui.label_2.setText(data[2])
            self.ui.label_3.setText(data[3])
            self.ui.label_4.setText(data[4])
            if data[5]:
                tmp.append('Однолетник')
            if data[6]:
                tmp.append('Гибрид')
            if data[7]:
                tmp.append('Теплолюбивое')
            if data[8]:
                tmp.append('Светлолюбивое')
            if data[9]:
                tmp.append('Влаголюбивое')
            self.ui.label_6.setText(",".join(tmp))
            self.ui.label_9.setText(f'Рекомендуемая производителем дата посадки семян на рассаду: {data[14]}')
            self.ui.label_10.setText(f'Фактическая дата посадки семян:  {data[17]}')
            self.ui.label_13.setText(f'Схема посадки {data[10]} x {data[11]}')
            self.ui.label_15.setText(f'Оптимальная для прорастания семян температура почвы: {data[15]}°C')
            if data[16]:
                self.ui.label_14.setText('Высажено')
                self.ui.pushButton_5.setEnabled(False)
            else:
                self.ui.label_14.setText('Ожидает высадки')
                self.ui.pushButton_5.setEnabled(True)
            self.ui.textEdit.setPlainText(data[18])
            x = eval(data[19])
            if len(x) == 0:
                self.ui.foto1.setPixmap(QPixmap("image/no-photo-60.png"))
                self.ui.foto2.setPixmap(QPixmap("image/no-photo-60.png"))
                self.ui.foto3.setPixmap(QPixmap("image/no-photo-60.png"))
                self.ui.foto4.setPixmap(QPixmap("image/no-photo-60.png"))
            if len(x) == 1:
                self.ui.foto1.setPixmap(QPixmap(f"image/{x[0]}"))
                self.ui.foto2.setPixmap(QPixmap("image/no-photo-60.png"))
                self.ui.foto3.setPixmap(QPixmap("image/no-photo-60.png"))
                self.ui.foto4.setPixmap(QPixmap("image/no-photo-60.png"))
            elif len(x) == 2:
                self.ui.foto1.setPixmap(QPixmap(f"image/{x[0]}"))
                self.ui.foto2.setPixmap(QPixmap(f"image/{x[1]}"))
                self.ui.foto3.setPixmap(QPixmap("image/no-photo-60.png"))
                self.ui.foto4.setPixmap(QPixmap("image/no-photo-60.png"))
            elif len(x) == 3:
                self.ui.foto1.setPixmap(QPixmap(f"image/{x[0]}"))
                self.ui.foto2.setPixmap(QPixmap(f"image/{x[1]}"))
                self.ui.foto3.setPixmap(QPixmap(f"image/{x[2]}"))
                self.ui.foto4.setPixmap(QPixmap("image/no-photo-60.png"))
            elif len(x) >= 4:
                self.ui.foto1.setPixmap(QPixmap(f"image/{x[0]}"))
                self.ui.foto2.setPixmap(QPixmap(f"image/{x[1]}"))
                self.ui.foto3.setPixmap(QPixmap(f"image/{x[2]}"))
                self.ui.foto4.setPixmap(QPixmap(f"image/{x[3]}"))
            if 'no-photo-60.png' in x:
                self.ui.pushButton_4.setEnabled(True)
            else:
                self.ui.pushButton_4.setEnabled(False)

    def left(self, data=False):
        if (self.current_vegetable > min(LIST_ID)) or data:
            new_current = LIST_ID.index(self.current_vegetable) - 1
            self.save_config(current=LIST_ID[new_current])
            self.current_vegetable = LIST_ID[new_current]
            self.wiew()

    def right(self, data=False):
        if (self.current_vegetable < max(LIST_ID)) or data:
            new_current = LIST_ID.index(self.current_vegetable) + 1
            self.save_config(current=LIST_ID[new_current])
            self.current_vegetable = LIST_ID[new_current]
            self.wiew()

    def del_vegetable(self):
        global LIST_ID
        self.blocking()
        if nr() == 1:
            del_v(LIST_ID[LIST_ID.index(self.current_vegetable)])
            LIST_ID.clear()

        elif (self.current_vegetable == max(LIST_ID)) or (self.current_vegetable > min(LIST_ID)):
            self.left(data=True)
            del_v(LIST_ID[LIST_ID.index(self.current_vegetable) + 1])
            LIST_ID = lai()

        else:
            self.right(data=True)
            del_v(LIST_ID[LIST_ID.index(self.current_vegetable) - 1])
            LIST_ID = lai()

        self.signal.emit(str(nr()))
        self.signal2.emit("Растение удалено из базы")

    def del_all(self):
        button_reply = QMessageBox.question(self, '', "Вы уверены?",
                                            QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel, QMessageBox.Cancel)
        if button_reply == QMessageBox.Yes:
            if os.path.isfile('base_date/vegetables.db'):
                os.remove('base_date/vegetables.db')
                self.signal2.emit("База успешно удалена")
                self.config['DEFAULT']['current'] = str(1)
                self.config['DEFAULT']['id'] = str(1)
                with open('conf.ini', 'w') as configfile:
                    self.config.write(configfile)
                QApplication.quit()
            else:
                self.signal2.emit("Ошибка удаления базы")

    def blocking(self):
        if len(LIST_ID) < 1:
            self.ui.button_right.setEnabled(False)
            self.ui.button_left.setEnabled(False)
        else:
            self.ui.button_right.setEnabled(True)
            self.ui.button_left.setEnabled(True)

    def save_config(self, current=-1):
        if current != -1:
            self.config['DEFAULT']['current'] = str(current)
            with open('conf.ini', 'w') as configfile:
                self.config.write(configfile)

    @pyqtSlot(str)
    def messages(self, data):
        self.lb.setText(f'В базе содержится {data} овощей, высажено 0 овощей')

    @pyqtSlot(str)
    def temporary_messages(self, data):
        self.stBar.showMessage(data, 2000)
        self.speech.say(data)


"""class Chart(QChart):
    def __init__(self):
        super().__init__()
        data = (
            (1, 0, 0, 0, 7),
            (2, 0, 0, 0, 5),
            (3, 0, 0, 0, 3),
            (4, 0, 0, 0, 7),
            (5, 0, 0, 0, 7),
            (6, 0, 0, 0, 7),
            (7, 0, 0, 0, 7),
            (8, 0, 0, 5, 7),
            (9, 0, 6, 7, 5),
            (10, 0, 5, 2, 3),
            (11, 0, 0, 0, 7),
            (12, 0, 0, 0, 7),
            (13, 0, 0, 0, 7),
            (14, 0, 0, 0, 7),
        )
        data = [(i, 0, 0, 0, 5) for i in range(1, 150)]
        series = QCandlestickSeries()
        series.setDecreasingColor(Qt.red)
        series.setIncreasingColor(Qt.green)
        tm = []  # stores str type data
        # in a loop,  series and ma5 append corresponding data
        for num, o, h, l, c in data:
            series.append(QCandlestickSet(o, h, l, c))
            tm.append(str(num))

        self.addSeries(series)  # candle
        self.setAnimationOptions(QChart.SeriesAnimations)
        self.createDefaultAxes()
        self.legend().hide()
        self.axisX().setCategories(tm)"""

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('plastique')
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
