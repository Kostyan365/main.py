import sys

from PyQt5 import QtCore, QtWidgets, uic, QtChart

# load both ui file
form_1, base_1 = uic.loadUiType("C:/Users/superadmin/Desktop/Kode/PyQt/QtChart диаграммы/CandlestickChart/CandesticChart2/UI/main.ui")


class Example(base_1, form_1):
    def __init__(self):
        super(base_1, self).__init__()
        self.setupUi(self)

        """data = (
            (1, 7380, 7520, 7380, 7510, 7324),
            (2, 7520, 7580, 7410, 7440, 7372),
            (3, 7440, 7650, 7310, 7520, 7434),
            (4, 7450, 7640, 7450, 7550, 7480),
            (5, 7510, 7590, 7460, 7490, 7502),
            (6, 7500, 7590, 7480, 7560, 7512),
            (7, 7560, 7830, 7540, 7800, 7584),
        )"""
        data =(
            (1, 0, 0, 0, 7),
            (2, 0, 0, 0, 5),
            (3, 0, 0, 0, 3),
            (4, 0, 0, 0, 7),
            (5, 0, 0, 0, 7),
            (6, 0, 0, 0, 7),
            (7, 0, 0, 0, 7),
            (1, 0, 0, 5, 7),
            (2, 0, 6, 7, 5),
            (3, 0, 5, 2, 3),
            (4, 0, 0, 0, 7),
            (5, 0, 0, 0, 7),
            (6, 0, 0, 0, 7),
            (7, 0, 0, 0, 7),
        )
        series = QtChart.QCandlestickSeries()
        series.setDecreasingColor(QtCore.Qt.red)
        series.setIncreasingColor(QtCore.Qt.green)


        tm = []  # stores str type data

        # in a loop,  series and ma5 append corresponding data
        for num, o, h, l, c in data:
            series.append(QtChart.QCandlestickSet(o, h, l, c))
            tm.append(str(num))

        chart = QtChart.QChart()
        chart.addSeries(series)  # candle


        chart.setAnimationOptions(QtChart.QChart.SeriesAnimations)
        chart.createDefaultAxes()
        chart.legend().hide()

        chart.axisX(series).setCategories(tm)


        chartview = QtChart.QChartView(chart)

        self.chart_container.setContentsMargins(0, 0, 0, 0)
        lay = QtWidgets.QHBoxLayout(self.chart_container)
        lay.setContentsMargins(0, 0, 0, 0)
        lay.addWidget(chartview)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
