from datetime import datetime


def string_decode(chaine):
    return chaine.encode('latin1').decode('utf8')


def timestamp_decode(date_ts):
    date_ts = int(str(date_ts)[:-3]) # on enleve les millisecondes
    date_dt = datetime.fromtimestamp(date_ts) # conversion en date yyyy-mm-dd
    time_dt = str(date_dt)[-8:] # on prend les 8 derniers caracteres pour recup l'heure
    date_dt = date_dt.strftime('%d-%m-%Y') + " " + time_dt # on concatene la date en dd-mm-yyyy et l'heure
    return date_dt
