from flask import Flask, request, render_template
import re
import string
import pandas as pd


app = Flask(__name__)
@app.route('/')
def index():
    return render_template("new.html")
@app.route('/', methods=['POST'])
def perfrom():
    val = request.form['test']

    frequency = {}
    file_content = open('ttt.txt', 'r')
    words_string= file_content.read().lower()
    match_pattern = re.findall(r'\b[a-z]{3,15}\b', words_string)

    for word in match_pattern:
        count = frequency.get(word, 0)
        frequency[word] = count + 1

    frequency_list = frequency.keys()
    df1 = pd.DataFrame(frequency_list,columns=['Word','Frequency'])
    df1 = df1.sort_values('Frequency',ascending=False)
    df2 = df1.head(val)

    return render_template("disp.html", tables=[df2.to_html(classes='data')], titles=df.columns.values)
if __name__ == '__main__':
    app.debug = True
    app.run()
