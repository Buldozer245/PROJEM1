from flask import Flask, render_template
def belge_ac(): 
    with open("discord_mesajlari.txt", "r", encoding="utf-8") as file:
        lines = file.readlines() 

        #selected = lines[-1]
        file.close()
        return lines




app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/hakkimda')
def hakkimda():
    return render_template('hakkimda.html')


@app.route('/iklim')
def iklim():
    text = belge_ac()
    return render_template('iklim.html', text = text)






























def run_flask():
    app.run(debug=False)

if __name__ == '__main__':
    app.run(debug=True)