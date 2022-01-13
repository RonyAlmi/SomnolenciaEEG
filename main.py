# ------------------------------------------------------
# ---------------------- main.py -----------------------
# ------------------------------------------------------
import sys
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QMessageBox, QDialog
from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar)
from PyQt5 import uic
from PyQt5.QtGui import QIcon, QFont
import numpy as np
import random
import serial
import seaborn as sns
from scipy import signal
from scipy.integrate import simps
import mne
import pandas as pd
from matplotlib.pyplot import pause
import collections
import winsound
from gtts import gTTS
from playsound import playsound
from pylsl import StreamInlet, resolve_byprop  # Module to receive EEG data
from muselsl import stream
from ventana import Ui_comunicacion
from EEG_ALFA_2 import Ui_MainWindow

tts = gTTS('cierra los ojos', lang='es')
# Nota: podríamos llamar directamente a save
with open("close.mp3", "wb") as archivo:
    tts.write_to_fp(archivo)

tts2 = gTTS('puede abrir los ojos', lang='es')
# Nota: podríamos llamar directamente a save
with open("open.mp3", "wb") as archivo2:
    tts2.write_to_fp(archivo2)

tts3 = gTTS('Bienvenido a sistema de detección de somnolencia', lang='es')
# Nota: podríamos llamar directamente a save
with open("bienvenida.mp3", "wb") as archivo3:
    tts3.write_to_fp(archivo3)

tts4 = gTTS('Somnolencia detectada', lang='es')
# Nota: podríamos llamar directamente a save
with open("somnolencia.mp3", "wb") as archivo4:
    tts4.write_to_fp(archivo4)

tts5 = gTTS('Conductor apto para iniciar labores de manejo', lang='es')
# Nota: podríamos llamar directamente a save
with open("alerta.mp3", "wb") as archivo5:
    tts5.write_to_fp(archivo5)

class ventana(QDialog, Ui_comunicacion):
    def __init__(self):
        QDialog.__init__(self)
        #loadUi("ventana.ui", self)
        #clase principal del archivo ventana.py
        Ui_comunicacion.__init__(self)
        self.setupUi(self)
        self.puertos()
        self.select_sensores()
        self.button_aceptar.clicked.connect(self.aceptar_puerto)

    def message_information_mw(self):
        # QMessageBox.setStyleSheet(self, "QLabel{ color: white}")
        # QMessageBox.setStyleSheet(self, "background-color: rgb(0, 0, 0)")
        msg = QMessageBox.information(self, "Informacion", "Cerrar los ojos para iniciar toma de datos Neurosky",
                                QMessageBox.Ok | QMessageBox.Cancel)
        if msg == QMessageBox.Ok:
            mensaje="ok"
        elif msg == QMessageBox.Cancel:
            mensaje="cancel"
        return mensaje
    def message_information_muse(self):
        msg = QMessageBox.information(self, "Informaciòn", "CERRAR LOS OJOS PARA INICIAR TOMA DE DATOS MUSE",
                                      QMessageBox.Ok | QMessageBox.Cancel)
        if msg == QMessageBox.Ok:
            mensaje="ok"
        elif msg == QMessageBox.Cancel:
            mensaje="cancel"
        return mensaje

    def message_critical_transmicion_mw(self):
        QMessageBox.critical(self, "Error", "No se pudo conectar con auricular MINDWAVE ",
                             QMessageBox.Ok)

    def message_critical_transmicion2_mw(self):
        QMessageBox.critical(self, "Error", "No hay Transmision de datos Neurosky ",
                             QMessageBox.Ok)

    def message_warning_somnolencia(self):
        QMessageBox.warning(self, "ADVERTENCIA", "SOMNOLENCIA DETECTADA",
                            QMessageBox.Ok)

    def message_critical_transmicion_muse(self):
        QMessageBox.critical(self, "Error", "No se pudo conectar con auricular MUSE, ",
                             QMessageBox.Ok)

    def message_critical_transmicion2_muse(self):
        QMessageBox.critical(self, "Error", "No hay datos guardados MUSE ",
                             QMessageBox.Ok)

    def message_critical_datanull(self):
        QMessageBox.critical(self, "Error", "No hay suficientes datos, Dispositivo mal colocado ",
                             QMessageBox.Ok)

    def aceptar_puerto(self):
        #app.closeAllWindows()
        puerto=self.comboB.currentText() # copiar puerto com del combobox
        #print(puerto)
        self.close()

    def puertos(self):
        v_puertos = np.array([])
        for iPuerto in range(10):
            try:
                puerto = 'COM' + str(iPuerto)
                port = serial.Serial(puerto)
                port.close()
                v_puertos = np.append(v_puertos, [puerto])
            except:
                pass
        #print(v_puertos)
        self.comboB.addItems(v_puertos)

    def select_sensores(self):
        sensores=["2 Sensores", "4 Sensores"]
        self.comboB_muse.addItems(sensores)
        self.comboB_muse.currentText()  # copiar puerto com del combobox

class MatplotlibWidget(QMainWindow, Ui_MainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        #loadUi("EEG_ALFA_2.ui", self)
        self.showMaximized()
        #clase principal del archivo EEG_ALFA_2.py correspondiente a la conversion de la interfaz qt python
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        try:
            stream('Muse-E49D')
        except:
            print()
        streams = resolve_byprop('type', 'EEG', timeout=2)
        if len(streams) == 0:
            print('Can\'t find EEG stream.')
        self.setStyleSheet("background-color: black;")
        self.statusBar().showMessage("Bienvenid@")
        # boton iniciar toma de datos
        self.pushButton_signal.clicked.connect(self.update_graph)
        #self.addToolBar(NavigationToolbar(self.MplWidget.canvas, self))
        self.setWindowTitle("INDICADOR DE SOMNOLENCIA")
        self.ventana=ventana()
        #crear menu
        menu = self.menuBar()
        menu_inicio = menu.addMenu("&Inicio")
        menu_config = menu.addMenu("&Configuracion")
        #agregar un ekemento accion al menu
        self.count=1
        menu_inicio_cerrar = QAction(QIcon(), "&Cerrar", self)
        menu_inicio_cerrar.setShortcut("Ctrl+x")  # atajo de teclado
        menu_inicio_cerrar.setStatusTip("Cerrar")  # mensaje en la barra de estado
        menu_inicio_cerrar.triggered.connect(self.menu_cerrar)
        menu_inicio.addAction(menu_inicio_cerrar)

        menu_config_puerto = QAction(QIcon(), "&Puerto", self)
        menu_config_puerto.setShortcut("Ctrl+p")  # atajo de teclado
        menu_config_puerto.setStatusTip("Puerto")  # mensaje en la barra de estado
        menu_config_puerto.triggered.connect(self.menu_config)
        menu_config.addAction(menu_config_puerto)
        #QMessageBox.information(self, "Help", "Configura el dispositivo para iniciar", QMessageBox.Discard)
        #self.puertos()
        #self.MplWidget.canvas.axes.pausar = plt.pause(0.01)
        grafica1 = np.loadtxt('A29.txt')
        grafica2 = np.loadtxt('E19.txt')
        # Plot index alpha
        y = []
        rw = np.array([])
        self.MplWidget.canvas.axes.clear()
        self.MplWidget.canvas.axes2.plot(np.arange(58), grafica2[0:58], lw=2.5, color='red')
        self.MplWidget.canvas.axes2.plot(y, color='green')
        #self.MplWidget.canvas.axes2.get_xaxis().set_visible(True)
        self.MplWidget.canvas.axes2.set_xticks(range(0, 60, 10))
        #self.MplWidget.canvas.axes.set_yticks(range(0, 5, 2))
        #self.MplWidget.canvas.axes.scatter(np.arange(len(index)), index, lw=1.5, color='blue')
        self.MplWidget.canvas.axes2.set_title(' Anàlisis de Somnolencia', fontsize=12, loc='left',position=(0.04, 0.5))
        self.MplWidget.canvas.axes2.legend( ('Somnolencia', 'Analisis'), fontsize= 'small', loc="upper right")

        self.MplWidget.canvas.axes.plot(np.arange(len(grafica1)), grafica1, lw=2.5, color='blue')
        #self.MplWidget.canvas.axes.get_xaxis().set_visible(True)
        #self.MplWidget.canvas.axes.set_xticks(range(0, 60, 10))
        self.MplWidget.canvas.axes.set_title('Ondas EEG', fontsize=12, position=(0.08, 0.9) )  #loc='left'
        #self.MplWidget.canvas.axes.plot(rw)

        playsound("bienvenida.mp3")

    def menu_cerrar(self):
        #QMessageBox.information(self, "Cerrar", "Acción Cerar", QMessageBox.Ok | QMessageBox.Cancel)
        #QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel
        self.close()

    def menu_config(self):
        #QMessageBox.information(self, "Cerrar", "Acción Cerar", QMessageBox.Discard)
        self.ventana.exec_()

    def update_graph(self):
        #EEG mindwave
        if self.ventana.radioButton_MW.isChecked():
            puerto=self.ventana.comboB.currentText() # copiar puerto com del combobox
            try:
                srl = serial.Serial(puerto, baudrate=57600, timeout=0.2)
            except:
                self.ventana.message_critical_transmicion_mw()
                return
            sf = 512.
            list1 = collections.deque()
            rw = np.array([])
            #QMessageBox.information(self, "Informacion", "Cerrar los ojos para iniciar toma de datos Neurosky", QMessageBox.Ok | QMessageBox.Cancel)
            msg_information=self.ventana.message_information_mw()
            playsound("close.mp3")
            if msg_information == "cancel":
                print(msg_information)
                return
            self.label_estado.setText("Procesando datos...")
            self.label_estado.setStyleSheet("background-color: rgb(0, 0, 127); color: white")
            self.label_estado.setFont(QFont('Arial', 16))
            print("test0")
            while True:
                try:
                    p1 = srl.read(1).hex()  # read first 2 packets
                    p2 = srl.read(1).hex()
                    if p1 == '':
                        self.label_estado.setText("Inicie nueva transmision...")
                        self.label_estado.setStyleSheet("background-color: rgb(0, 0, 127); color: white")
                        self.label_estado.setFont(QFont('Arial', 16))
                        self.ventana.message_critical_transmicion2_mw()
                        return
                    while p1 != 'aa' or p2 != 'aa':
                        p1 = p2
                        p2 = srl.read(1).hex()
                    else:
                        # a valid packet is available
                        payload = []
                        checksum = 0;
                        payloadLength = int(srl.read(1).hex(), 16)
                        for i in range(payloadLength):
                            tempPacket = srl.read(1).hex()
                            payload.append(tempPacket)
                            checksum += int(tempPacket, 16)
                        checksum = ~checksum & 0x000000ff
                        if checksum == int(srl.read(1).hex(), 16):
                            i = 0
                            code = payload[i]
                            if (code == '80'):  # raw value
                                i = i + 1  # for length/it is not used since length =1 byte long and always=2
                                i = i + 1;
                                val0 = int(payload[i], 16)
                                i = i + 1;
                                rawValue = val0 * 256 + int(payload[i], 16)
                                if rawValue > 32768:
                                    rawValue = rawValue - 65536
                                list1.append(rawValue)
                                # print(rawValue)
                                if len(list1) == 512 * 60:
                                    srl.close()
                                    frequency = 1000
                                    duration = 500
                                    winsound.Beep(frequency, duration)
                                    playsound("open.mp3")
                                    print(len(list1))
                                    break
                                rw = np.append(rw, [rawValue])
                                if len(rw) == 256:
                                    self.MplWidget.canvas.axes.clear()
                                    self.MplWidget.canvas.axes.plot(rw, lw=.5, color='blue')
                                    # self.MplWidget.canvas.axes.set_ylim([np.amin(rw)-100, np.amax(rw)*3.5])
                                    self.MplWidget.canvas.axes.set_title('Ondas EEG', fontsize=7, position=(0.13, 0.9))
                                    self.MplWidget.canvas.flush_events()
                                    self.MplWidget.canvas.draw()
                                    for j in range(256):
                                        rw = np.delete(rw, [0])
                                        # del rw[0]
                            else:
                                pass
                except:
                    print("tesjhhg")
                    return

            srl.close()

            data_raw = np.array(list1)
            name="raw"+str(self.count)
            np.savetxt(name + ".txt", data_raw)
            data = np.vstack((data_raw, data_raw))  # generando matriz 2x32070
            # Initialize info structure
            info = mne.create_info(
                ch_names=['EEG_11', 'EEG'],
                ch_types=['eeg', 'eeg'],
                sfreq=512)

            raw = mne.io.RawArray(data, info)
            raw_highpass = raw.copy().filter(l_freq=0.2, h_freq=40)  # filtro pasabanda
            data_filter = raw_highpass.get_data(picks=0)[0]  # obtener datos de la primera fila de dais filtrados

        #muse
        elif self.ventana.radioButton_Muse.isChecked():
            try:
                streams = resolve_byprop('type', 'EEG', timeout=2)
                if len(streams) == 0:
                    raise RuntimeError('Can\'t find EEG stream.')
                # Set active EEG stream to inlet and apply time correction
                print("Start acquiring data")
                inlet = StreamInlet(streams[0], max_chunklen=1)

                info = inlet.info()
                description = info.desc()
                Nchan = info.channel_count()
                ch = description.child('channels').first_child()
                ch_names = [ch.child_value('label')]
                for i in range(1, Nchan):
                    ch = ch.next_sibling()
                    ch_names.append(ch.child_value('label'))
            except:
                self.ventana.message_critical_transmicion_muse()
                return
            raw_m = np.array([])
            rw = np.array([])
            res = []
            print('Press Ctrl-C in the console to break the while loop.')
            # list_muse = collections.deque()
            try:
                msg_information_muse=self.ventana.message_information_muse()
                playsound("close.mp3")
                if msg_information_muse == "cancel":
                    return
                # The following loop acquires data, computes band powers, and calculates neurofeedback metrics based on those band powers
                self.label_estado.setText("Procesando datos...")
                self.label_estado.setStyleSheet("background-color: rgb(0, 0, 127); color: white")
                self.label_estado.setFont(QFont('Arial', 16))
                for v in range(256*60):
                    """ 3.1 ACQUIRE DATA """
                    # Obtain EEG data from the LSL stream
                    raw_muse, timestamp = inlet.pull_chunk(
                        timeout=1, max_samples=1)
                    res.append(raw_muse)

                    raw_m = np.array(raw_muse)
                    rw = np.append(rw, [raw_m[0, 1]])
                    # raw_muse.pop(0)
                    # list_muse.append(eeg_data)
                    if len(rw) == 128:
                        self.MplWidget.canvas.axes.clear()
                        self.MplWidget.canvas.axes.plot(rw, lw=2.5, color='blue')
                        #self.MplWidget.canvas.axes.set_ylim([np.amin(rw), np.amax(rw)])
                        self.MplWidget.canvas.axes.set_title('Ondas EEG', fontsize=12, position=(0.08, 0.9))
                        self.MplWidget.canvas.flush_events()
                        self.MplWidget.canvas.draw()
                        for j in range(128):
                            rw = np.delete(rw, [0])
                    # --------eliminar-----------------
                    #if v==256*15:
                    #   playsound("close.mp3")
                    i#f v==256*105:
                    #  playsound("open.mp3")
                    #--------------------------------
                res = np.concatenate(res, axis=0)
                dat = pd.DataFrame(data=res, columns= ch_names)
                test = "test" + str(self.count)
                dat.to_csv(test+".csv", float_format='%.3f', index=False)
                #print(rwm)
                print(len(rw))
            #except KeyboardInterrupt:
            except:
                self.ventana.message_critical_transmicion2_muse()
                print('Closing!')
                return
            frequency = 1000
            duration = 500
            winsound.Beep(frequency, duration)
            playsound("open.mp3")

            df = pd.read_csv(test+".csv")
            TP9 = np.array(df['TP9'])
            AF7 = np.array(df['AF7'])
            AF8 = np.array(df['AF8'])
            TP10 = np.array(df['TP10'])
            sf = len(TP9) / 60
            # print(sf)
            data = np.vstack((TP9, AF7, AF8, TP10))  # generando matriz 4x32070

            # Initialize info structure
            info = mne.create_info(
                ch_names=['EEG_TP9', 'EEG_AF7', 'EEG_AF8', 'EEG_TP10'],
                ch_types=['eeg', 'eeg', 'eeg', 'eeg'],
                sfreq=sf
            )

            raw = mne.io.RawArray(data, info)
            raw_highpass = raw.copy().filter(l_freq=0.2, h_freq=40)  # filtro pasabanda
            if self.ventana.comboB_muse.currentText() == "4 Sensores":
                filter_array = raw_highpass.get_data()  # obtener datos filtrados
                data_filter = np.apply_along_axis(sum, 0,filter_array) / 4  # generar una sola señal alfa a partir de las4 bandas o electrodos

                # print(data_filter)
            if self.ventana.comboB_muse.currentText() == "2 Sensores":
                filter_array = raw_highpass.get_data()[1:3]  # obtener datos filtrados
                data_filter = np.apply_along_axis(sum, 0,filter_array) / 2  # generar una sola señal alfa a partir de las4 bandas o electrodos
            np.savetxt('data_filter.txt', data.T)
    #------------------------------------------final toma de datos------------------------------------------------------

        sf2=int(sf)
        low, high = 8, 12  # Define delta lower and upper limits
        win = 0.25 * sf  # Define window length
        alfa_abs = np.array([])
        i = 0
        j = sf2*2
        for v in range(30):
            epoca = data_filter[i:j]
            b = np.greater(epoca, 350)
            c = np.less(epoca, -350)  # Devuelve True si el elemento del array a es mayor que 100.
            estado = b.any() | c.any()  # Devuelve True si alguno de los elementos del array es True
            if not estado:
                freqs, psd = signal.welch(epoca, sf, nperseg=win)
                idx_alpha = np.logical_and(freqs >= low, freqs <= high)
                freq_res = freqs[1] - freqs[0]
                alpha_power = simps(psd[idx_alpha], dx=freq_res)
                alfa_abs = np.append(alfa_abs, [alpha_power])
                # print('Absolute alfa power: %.3f uV^2' % alpha_power)
            i = i + sf2 * 2
            j = j + sf2 * 2
        print(len(alfa_abs))
        alfa_abs = list(filter(lambda n : n<300, alfa_abs))
        #print(alfa_abs)
        if self.ventana.radioButton_MW.isChecked():
            alfa_abs = np.delete(alfa_abs, [0, 1])
        np.savetxt(str(self.count) + ".txt", alfa_abs)
        media = np.mean(alfa_abs)
        d_st = np.std(alfa_abs)

        index = np.array([])
        for k in range(len(alfa_abs)):
            z = (alfa_abs[k] - media) / d_st
            index = np.append(index, [z])

        if self.ventana.radioButton_MW.isChecked():
            nom = "MW"+str(self.count)
        elif self.ventana.radioButton_Muse.isChecked():
            nom = "MU" + str(self.count)
        #np.savetxt(nom+".txt", index)
        self.count=self.count+1

        ventana = 3
        b = np.ones(ventana) * (1 / ventana)
        a = 1
        index_ = signal.lfilter(b, a, index)
        #normalizacion entre 0-1
        try:
            normal = []
            x = np.arange(0, len(index))
            for i in range(len(index)):
                normal.append((index[i] - np.amin(index)) / (np.amax(index) - np.amin(index)))
            print(len(normal))
            ventana = 3
            b = np.ones(ventana) * (1 / ventana)
            a = 1
            normal_filter = signal.lfilter(b, a, normal)
            area1 = simps(normal_filter[0:6], x[0:6])
            area2 = simps(normal_filter[6:12], x[6:12])
            area3 = simps(normal_filter[12:18], x[12:18])
            area4 = simps(normal_filter[18:len(normal)-1], x[18:len(normal)-1])
            #area4 = simps(normal_filter[30:40], x[30:40])
            #area5 = simps(normal_filter[40:50], x[40:50])
            promedio = (area2 + area3+ area4) / 3
            # 2 estados de somnolencia
        except:
            if len(normal_filter)<=20:
                self.ventana.message_critical_datanull()
                self.label_estado.setText("Datos insuficientes, Iniciar toma de datos nuevamente")
                self.label_estado.setStyleSheet("background-color: rgb(0, 85, 127); color: white")
                self.label_estado.setFont(QFont('Arial', 16))

        y = []
        grafica2 = np.loadtxt('E19.txt')
        self.MplWidget.canvas.axes2.clear()
        self.MplWidget.canvas.axes2.plot(np.arange(58), grafica2[0:58], lw=2, color='red')
        #self.MplWidget.canvas.axes2.plot(np.arange(len(index_)), index_, lw=2.5, color='yellow')
        #self.MplWidget.canvas.axes2.plot(np.arange(len(normal)), normal, lw=.5, color='yellow')
        self.MplWidget.canvas.axes2.plot(y, color='green', lw=3.5)
        # self.MplWidget.canvas.axes2.get_xaxis().set_visible(True)
        self.MplWidget.canvas.axes2.set_xticks(range(0, 60, 10))
        # self.MplWidget.canvas.axes.set_yticks(range(0, 5, 2))
        # self.MplWidget.canvas.axes.scatter(np.arange(len(index)), index, lw=1.5, color='blue')
        self.MplWidget.canvas.axes2.set_title(' Anàlisis de Somnolencia', fontsize=12, loc='left', position=(0.04, 0.5))
        self.MplWidget.canvas.axes2.legend(('Somnolencia', 'Analisis'), fontsize='small', loc="upper right")

        for i in range(len(index)):
            y.append(index[i])
            #estados.append((index[i] - np.amin(index)) / (np.amax(index)-np.amin(index)))
            #print(y[i])
            self.MplWidget.canvas.axes2.plot(y, lw=2.5, color="green")
            #self.MplWidget.canvas.figure.pause(0.05)
            self.MplWidget.canvas.flush_events()
            self.MplWidget.canvas.draw()

        try:
            if area1 > 2.1 * promedio:
                print("somnolencia")
                playsound("somnolencia.mp3")
                self.label_estado.setText("SOMNOLIENTO")
                self.label_estado.setStyleSheet("background-color: rgb(200, 0, 0); color: white")
                self.label_estado.setFont(QFont('Arial', 18))
                self.ventana.message_warning_somnolencia()
            else:
                print("alerta")
                playsound("alerta.mp3")
                self.label_estado.setText("NO SOMNOLIENTO")
                self.label_estado.setStyleSheet("background-color: rgb(0, 85, 0); color: white")
                self.label_estado.setFont(QFont('Arial', 18))
        except:
            print("error en cantidad de datos tomados")

app = QApplication([])
window = MatplotlibWidget()
#window = Window()
#window.show()
window.showFullScreen()
app.exec_()
