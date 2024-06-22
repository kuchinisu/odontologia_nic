import datetime

PRESENT_YEAR = datetime.date.today().year

DIAS_POR_MES = {
    1:31,
    2:28 if not PRESENT_YEAR % 4 and(
        PRESENT_YEAR % 100 != 0 or PRESENT_YEAR % 400 == 0
        ) == 0 else 29 ,
    3:31,
    4:30,
    5:31,
    6:30,
    7:31,
    8:31,
    9:30,
    10:31,
    11:30,
    12:31,
}