import schedule #pip install schedule
import time
from datetime import time

@repeat(every().day)
def tarefa():
    print("Tome seu remédio,não dá mole!")
# Exemplos
    #schedule.every(5).seconds.do(tarefa)
    #schedule.every().hour.at(" :19").do(tarefa)
    #schedule.every().second.until(time(14, 22, 10)).do(tarefa)
    schedule.every().day.at("09:00")do(tarefa)

    while True: 
        schedule.run_pending()
        tm.time.sleep(1)
