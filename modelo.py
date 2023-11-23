import pydicom 
from PyQt5.QtCore import QObject
import matplotlib.pyplot as plt
import os
class basededatos(QObject):
    def __init__(self):
        super().__init__()
        self.__login = 'medicoAnalitico' #loging 
        self.__password = 'bio12345' 
        self.__carpeta = ""

    def validaruser(self, l, p):
        return self.__login == l and self.__password == p

    def get_path(self, f): 
        self.__carpeta = f

    def picture_creator(self, imagen):
        ds = pydicom.dcmread(self.__carpeta+'/'+imagen)
        pixel_data = ds.pixel_array

        if len(pixel_data.shape) == 3:
            slice_index = pixel_data.shape[0] // 2
            selected_slice = pixel_data[slice_index, :, :]
            plt.imshow(selected_slice, cmap=plt.cm.bone)
        else:

            plt.imshow(pixel_data, cmap=plt.cm.bone)

        plt.axis('off')
        plt.savefig("temp_image.png")

    def obtener_informacion_paciente(self, imagen):
        # Ruta completa del archivo DICOM
        ruta_completa = os.path.join(self.__carpeta, imagen)

        # Leer el archivo DICOM
        ds = pydicom.dcmread(ruta_completa)

        # Obtener información del paciente
        nombre_paciente = ds.PatientName
        id_paciente = ds.PatientID
        fecha_nacimiento = ds.PatientBirthDate
        sexo = ds.PatientSex

        # Puedes agregar más campos según lo que necesites

        # Crear un diccionario con la información del paciente
        info_paciente = {
            'Nombre': str(nombre_paciente),
            'ID': str(id_paciente),
            'Fecha de Nacimiento': str(fecha_nacimiento),
            'Sexo': str(sexo),
            # Agregar más campos si es necesario
        }

        return info_paciente

    
    
