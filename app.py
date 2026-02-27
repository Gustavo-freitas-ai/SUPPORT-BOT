from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

question = '''
Olá 👋 Seja bem-vindo!
Qual a sua dúvida?
'''
question2 = '''
[1] Horário de atendimento
[2] Preço dos planos
[3] Suporte
'''

def init_db():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS mensagens (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario TEXT NOT NULL,
            mensagem TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()

init_db()

def resposta_bot(mensagem):
    mensagem = mensagem.lower()

    if mensagem == "1":
        return "Nosso horário de atendimento é das 8h às 18h."

    elif mensagem == "2":
        return "Nossos planos começam em R$ 99."

    elif mensagem == "3":
        return "Nosso suporte funciona 24 horas."

    elif "oi" in mensagem:
        return question

    elif "preço" in mensagem or "preco" in mensagem:
        return "Nossos planos começam em R$ 99."

    elif "suporte" in mensagem:
        return "Nosso suporte funciona 24 horas."

    else:
        return "Desculpe, não entendi. Digite 1, 2 ou 3."

@app.route("/", methods=["GET", "POST"])
def chat():

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    if request.method == "GET":

        cursor.execute("SELECT COUNT(*) FROM mensagens")
        total = cursor.fetchone()[0]

        if total == 0:
            cursor.execute(
                "INSERT INTO mensagens (usuario, mensagem) VALUES (?, ?)",
                ("Suporte", question)
            )
            cursor.execute(
                "INSERT INTO mensagens (usuario, mensagem) VALUES (?, ?)",
                ("Suporte", question2)
            )
            conn.commit()

    if request.method == "POST":

        mensagem_usuario = request.form["mensagem"]

        cursor.execute(
            "INSERT INTO mensagens (usuario, mensagem) VALUES (?, ?)",
            ("Usuário", mensagem_usuario)
        )

        resposta = resposta_bot(mensagem_usuario)

        cursor.execute(
            "INSERT INTO mensagens (usuario, mensagem) VALUES (?, ?)",
            ("Suporte", resposta)
        )

        conn.commit()
        conn.close()

        return redirect("/")

    cursor.execute("SELECT usuario, mensagem FROM mensagens")
    mensagens = cursor.fetchall()

    conn.close()

    return render_template("index.html", mensagens=mensagens)

if __name__ == "__main__":
    app.run(debug=True)