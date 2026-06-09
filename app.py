from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hitung():
    result = None # Tampilan hasil awal (None)

    if request.method == 'POST':
        # Mengambil input dari form HTML
        num1 = float(request.form['angka1'])
        num2 = float(request.form['angka2'])
        operator = request.form['operator']

        # Logika Matematika
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                result = 'Error: Pembagian dengan nol!'
        else:
            result = 'Error: Operator tidak valid'

    return render_template('index.html', result=result)

if __name__ == "__main__":
    app.run(debug=True)