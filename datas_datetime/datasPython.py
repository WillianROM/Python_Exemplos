from datetime import datetime, timedelta
# timedelta é para fazer cálculos envolvendo datas

# data
agora = datetime.now()

print(agora)
print(agora.date())
print(agora.day)
print(agora.month)
print(agora.year)
print(agora.hour)
print(agora.minute)
print(agora.second)

# Variações de datas
amanha = agora + timedelta(days=1)

print(amanha)

proxima_semana = agora + timedelta(weeks=1)

print(proxima_semana)


data_contrato = datetime(year=2022, month=9, day=7)
print(data_contrato)

atraso = agora - data_contrato
print(atraso.days)

# extrair datas em outros formatos
data_venda = "22-10-2022"
data_venda = datetime.strptime(data_venda,"%d-%m-%Y")
print(data_venda)

# formato brasileiro
print(agora.strftime("%d/%m/%Y"))

# Nome dos dias das semanas em inglês
print(agora.strftime("%A"))


# Fuso-horário - (referência é UTC) - Precisa usar a biblicoteca zoneinfo - pip install tzdata
import zoneinfo
print(zoneinfo.available_timezones()) # Vai trazer os nomes das zonas horárias para utilizar no zoneinfo.ZoneInfo conforme abaixo que o exemplo é Egito
zona = zoneinfo.ZoneInfo('Egypt')
agora_egypt = agora.astimezone(zona)
print(agora_egypt)

