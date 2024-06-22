from django.utils import timezone
from apps.utils.math.globales import DIAS_POR_MES
import datetime

def calcular_edad(fecha):

    year_nacimiento = fecha.year
    mes_nacimiento = fecha.month
    dia_nacimiento = fecha.day

    fecha_actual = datetime.date.today()
    mes_actual = fecha_actual.month
    year_actual = fecha_actual.year

    dias_cerrados = 0
    dias = 0

    for i in range(1, mes_actual-1):
        dias_cerrados += DIAS_POR_MES[i]

    dias += dias_cerrados

    for i in range(dia_nacimiento, DIAS_POR_MES[mes_nacimiento]):
        dias += 1
    
    for i in range(year_nacimiento, year_actual):
        if i % 4 == 0 and (i % 100 != 0 or i % 400 ==0):
            dias += 366
        else: dias += 365

    edad = dias % 365
    

    return edad