from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

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

    if "oi" in mensagem:
        return "Olá! Como posso ajudar?"
    elif "preço" in mensagem:
        return "Nossos planos começam em R$ 99."
    elif "suporte" in mensagem:
        return "Nosso suporte funciona 24 horas."
    else:
        return "Desculpe, ainda estou aprendendo."

@app.route("/", methods=["GET", "POST"])
def chat():

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    if request.method == "POST":

        mensagem_usuario = request.form["mensagem"]

        cursor.execute(
            "INSERT INTO mensagens (usuario, mensagem) VALUES (?, ?)",
            ("Usuário", mensagem_usuario)
        )

        resposta = resposta_bot(mensagem_usuario)

        cursor.execute(
            "INSERT INTO mensagens (usuario, mensagem) VALUES (?, ?)",
            ("Bot", resposta)
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