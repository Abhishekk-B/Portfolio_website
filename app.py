from flask import Flask,render_template,send_file

app=Flask(__name__)
app.config['SECRET_KEY'] = 'Thisismysecretkey'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def project():
    return render_template('project.html')


@app.route('/download')
def download():
    path = 'Abhishek_Bhardwaj.pdf'
    return send_file(path, as_attachment=True)


if __name__=='__main__':
    app.run(debug=True)