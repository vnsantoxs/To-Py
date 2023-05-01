import mysql.connector
from datetime import date
from tkinter import messagebox, simpledialog

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="vmelchior",
    database="ToPy"
)

cursor = mydb.cursor()
if mydb.is_connected():
    print("Conexão estabelecida com sucesso!")
else:
    print("Falha ao conectar com o banco de dados.")

def add_task():
    data, nome, importante = coll_task()
    sql = "INSERT INTO task (data, nome, importante, estado) VALUES (%s, %s, %s, %s)"
    values = (data, nome, importante, False)
    cursor.execute(sql, values)
    mydb.commit()
    messagebox.showwarning("", "Tarefa inserida")

def read_task():
    sql = "SELECT * FROM task"
    cursor.execute(sql)
    tasks = cursor.fetchall()
    mydb.close()
    return tasks

def del_task():
    sql = "DELETE FROM task WHERE id = %s"
    val = (id,)
    cursor.execute(sql, val)
    mydb.commit()
    mydb.close()
    return True

def important_task():   
    query = "SELECT * FROM task WHERE importante = True"
    cursor.execute(query)
    results = cursor.fetchall()
    mydb.close()
    return results

def done_task():   
    query = "SELECT * FROM task WHERE estado = True"
    cursor.execute(query)
    results = cursor.fetchall()
    mydb.close()
    return results

def today_task():
    today = date.today()
    cursor = mydb.cursor()
    sql = "SELECT * FROM task WHERE data = %s"
    cursor.execute(sql, (today,))
    tasks = cursor.fetchall()

def coll_task():
    nome = simpledialog.askstring("Nome", "Digite o nome da tarefa:", initialvalue="")
    data = simpledialog.askstring("Data", "Digite a data da tarefa (no formato AAAA-MM-DD):", initialvalue="")
    importante = messagebox.askquestion("Importante", "A task é importante?")
    return data, nome, importante

