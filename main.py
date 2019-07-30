from flask import Flask, render_template, request, url_for
from spider import court_science_magic, send_pdf_path

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/main', methods = ['POST'])
def main():
    if request.method == 'POST':
        user_csv = request.files['myCSV']
        csv_name = user_csv.filename
        user_csv.save(csv_name)
        print(csv_name)
        user_stats = []
        for i in range(11):
            if request.form['stat' + str(i + 1)] != 'false':
                user_stats.append(request.form['stat' + str(i + 1)])
        print(user_stats)
        court_science_magic(csv_name, user_stats)
        pdf_filepath = send_pdf_path()

        return render_template('response.html', pdf_filepath=pdf_filepath)


if __name__ == '__main__':
    app.run()