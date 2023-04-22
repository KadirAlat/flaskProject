from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy




app = Flask(__name__)
app.secret_key= "Secret Key"




app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/sys'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


#Creating model table for our CRUD database
class Data(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    konu = db.Column(db.String(100))
    tarih = db.Column(db.Date)
    baslangic = db.Column(db.Time)
    bitis = db.Column(db.Time)
    katilimcilar = db.Column(db.String(200))


    def __init__(self, konu, tarih, baslangic,bitis,katilimcilar):

        self.konu = konu
        self.tarih = tarih
        self.baslangic = baslangic
        self.bitis = bitis
        self.katilimcilar = katilimcilar



@app.route('/')
def Index():
    all_data = Data.query.all()

    return render_template("index.html",toplanti=all_data)







@app.route('/insert', methods = ['POST'])
def insert():

    if request.method == 'POST':
        id = request.form['id']
        konu = request.form['konu']
        tarih = request.form['tarih']
        baslangic = request.form['baslangic']
        bitis = request.form['bitis']
        katilimcilar = request.form['katilimcilar']


        my_data = Data(konu, tarih, baslangic,bitis,katilimcilar)
        db.session.add(my_data)
        db.session.commit()

        flash("Employee Inserted Successfully")

        return redirect(url_for('Index'))


#değişiklik yaptım
@app.route('/update', methods = ['GET', 'POST'])
def update():

    #print(request.method)
    if request.method == 'POST':
        my_data = Data.query.get(request.form.get('id'))

        my_data.konu = request.form['konu']
        my_data.tarih = request.form['tarih']
        my_data.baslangic = request.form['baslangic']
        my_data.bitis = request.form['bitis']
        my_data.katilimcilar = request.form['katilimcilar']

        db.session.commit()
        flash("Güncelleme İşlemi Yapıldı")

        return redirect(url_for('Index'))





@app.route('/delete/<id>/', methods = ['GET', 'POST'])
def delete(id):
    my_data = Data.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    flash("Silme İşlemi Yapıldı")

    return redirect(url_for('Index'))






if __name__ == "__main__":
    app.run(debug=True)