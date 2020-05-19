#pyside2-uic ./GUI/mainApp.ui > ./GUI/ui_mainwindow.py
#cd Z:\documentos\projects\Python_environments\GUI_environment\Lib\site-packages\PySide2\examples

import sys
from PySide2.QtWidgets import QApplication,QMainWindow,QSizePolicy
from PySide2.QtCore import Slot,QPointF,Qt
from PySide2.QtCharts import QtCharts
from PySide2.QtGui import QPainter
from ui_mainwindow import Ui_MainWindow

from random import random, uniform
from math import sin,pi as PI

class MainApp(QMainWindow):
    def __init__(self,ui):
        QMainWindow.__init__(self)
        self.ui = ui
        self.ui.setupUi(self)
        self.ui.dial_IE.valueChanged.connect(self.custom_lcdNumber_IE_display)
        self.ui.dial_AF.valueChanged.connect(self.custom_lcdNumber_AF_display)
        self.initial_values()

        #data Table
        
        # Area Chart
        area_charts_config = {
            "<b>Paw</b> (cmH2O)":((0,15),(-10,60),self.simulate_paw_signal),
            "<b>Flow</b> (L/min)":((0,15),(-100,100),self.simulate_flow_signal),
            "<b>Volume</b> (mL)":((0,15),(0,500),self.simulate_volume_signal)
        }
        area_charts = []
        for title in area_charts_config:
            ranges = area_charts_config[title][:2]
            data_table = area_charts_config[title][2](ranges)
            areachart = self.create_areachart(title,ranges,data_table)
            chart_view =  QtCharts.QChartView(areachart)
            chart_view.setRenderHint(QPainter.Antialiasing, True)
            chart_view.chart().legend().hide()
            #chart_view.setSizePolicy(QSizePolicy.Expanding,
            #    QSizePolicy.Expanding)
            chart_view.setMinimumHeight(200)
            #add chart to vertical layout
            self.ui.verticalLayout_charts.addWidget(chart_view, 0, Qt.AlignTop)

            area_charts.append(areachart)
    
    def generate_random_data(self, value_max, value_count):
        data_list = []
        y_value = 0
        for j in range(value_count):
            constant = value_max / float(value_count)
            y_value += uniform(0, constant)
            x_value = (j + random()) * constant
            value = QPointF(x_value, y_value)
            label = "Slice {}: {}".format(1, j)
            data_list.append((value, label))

        return [data_list]
    
    def simulate_paw_signal(self,ranges,sample_f=50):
        data_list = []
        x_value = 0
        signal_period = 1.7
        j = 0
        while x_value <= ranges[0][1]:
            y_value = 20+15*sin(2*PI*x_value/signal_period) 
            y_value = 25 if y_value>25 else y_value
            value = QPointF(x_value, y_value)
            label = "Slice {}: {}".format(1, j)
            data_list.append((value, label))
            x_value += 1/sample_f
            j+= 1
        return [data_list]
    
    def simulate_volume_signal(self,ranges,sample_f=50):
        data_list = []
        x_value = 0
        signal_period = 1.7
        j = 0
        while x_value <= ranges[0][1]:
            y_value = abs(380*sin(PI*x_value/signal_period))
            value = QPointF(x_value, y_value)
            label = "Slice {}: {}".format(1, j)
            data_list.append((value, label))
            x_value += 1/sample_f
            j+= 1
        return [data_list]
    
    def simulate_flow_signal(self,ranges,sample_f=50):
        data_list = []
        x_value = 0
        signal_period = 1.7
        j = 0
        while x_value <= ranges[0][1]:
            y_value = 50*sin(PI*x_value/signal_period)
            value = QPointF(x_value, y_value)
            label = "Slice {}: {}".format(1, j)
            data_list.append((value, label))
            x_value += 1/sample_f
            j+= 1

        return [data_list]
    
    def initial_values(self):
        #Parametros
        RR = 15
        self.ui.dial_RR.setValue(RR)
        self.ui.lcdNumber_RR.display(RR)
        IE = 2
        self.ui.dial_IE.setValue(IE)
        self.custom_lcdNumber_IE_display(IE)
        AF = 5
        self.ui.dial_AF.setValue(AF)
        self.custom_lcdNumber_AF_display(AF)
        PIP = 20
        self.ui.dial_PIP.setValue(PIP)
        self.ui.lcdNumber_PIP.display(PIP)
        PEEP = 10
        self.ui.dial_PEEP.setValue(PEEP)
        self.ui.lcdNumber_PEEP.display(PEEP)
        VT = 500
        self.ui.dial_VT.setValue(VT)
        self.ui.lcdNumber_VT.display(VT)
        FIO2 = 30
        self.ui.dial_FIO2.setValue(FIO2)
        self.ui.lcdNumber_FIO2.display(FIO2)
        PT = 5
        self.ui.dial_PT.setValue(PT)
        self.ui.lcdNumber_PT.display(PT)

        #Limites
        maxp = 50
        self.ui.spinBox_maxp.setValue(maxp)
        minp = 2
        self.ui.spinBox_minp.setValue(minp)
        minmv = VT*RR-30
        self.ui.spinBox_minvm.setValue(minmv)
    
    @Slot()
    def custom_lcdNumber_IE_display(self,dialInt):
        self.ui.lcdNumber_IE.display("1:{}".format(dialInt))

    @Slot()
    def custom_lcdNumber_AF_display(self,dialInt):
        self.ui.lcdNumber_AF.display("{:.1f}".format(dialInt/10))
    
    def create_areachart(self,title,ranges,data_table):
        chart = QtCharts.QChart()
        chart.setTitle(title)

        # The lower series initialized to zero values
        name = "Series "
        for i in range(len(data_table)):
            upper_series = QtCharts.QLineSeries(chart)
            lower_series = QtCharts.QLineSeries(chart)
            for j in range(len(data_table[i])):
                data = data_table[i][j]
                upper_series.append(data[0])
                lower_series.append(QPointF(data[0].x(), 0))
            area = QtCharts.QAreaSeries(upper_series, lower_series)
            area.setName("{}{}".format(name, i))
            chart.addSeries(area)

        chart.createDefaultAxes()
        chart.axisX().setRange(*ranges[0])
        chart.axisY().setRange(*ranges[1])
        # Add space to label to add space between labels and axis
        chart.axisY().setLabelFormat("%.1f")
        
        return chart

if __name__ == "__main__":
    # Qt Application
    app = QApplication(sys.argv)

    # QMainWindow using QWidget as central widget
    mainw = MainApp(Ui_MainWindow())
    

    mainw.show()
    sys.exit(app.exec_())