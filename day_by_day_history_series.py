import psycopg2
from datetime import date, timedelta, datetime

conn = psycopg2.connect(
    "host=localhost dbname=nomeDoBanco user=postgres password=123456")
cur = conn.cursor()

def quesito2(data):

    cur.execute(
        f"select date_ref, count(accountid) from cases where date_ref between '{data}'::date - interval '30 days' and '{data}'::date group by date_ref")
    recset = cur.fetchall()

    datas_week = []
    numero_de_chamados = []
    total_de_chamados = 0

    print("|Dia do chamado|Quantidade de chamados|")
    for rec in recset:
        datas_week = rec[0]
        numero_de_chamados = rec[1]
        total_de_chamados = total_de_chamados + rec[1]
        print("| ", datas_week, " | ", numero_de_chamados, " |")

    data_end = datetime.strptime(data, "%d/%m/%Y")
    data_start = data_end - timedelta(30)

    print("O Total de chamados entre o dia ", data_start,
          " e o dia ", data_end, " foi de ", total_de_chamados)


if __name__ == "__main__":

    data = input(
        'Qual Dia deseja um relátorio dia a dia referente aos ultimos 30 dias? FORMATO dd/mm/yyyy ')
    quesito2(data)
    