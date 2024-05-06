from flask import Flask, render_template, request, redirect, url_for
from confiDB import * 


app = Flask(__name__)
application = app

app.secret_key = '97110c78ae51a45afcb3380af008f90b23a5d1616bf19bc29098105da20fe'


@app.route('/', methods=['GET','POST'])
def inicio():
    return render_template('public/index.html')

docs = ["file 1"]  
@app.route('/buscar-empleado', methods=['GET','POST'])
def BuscarEmpleado():
    if request.method    == "POST":
        search           = request.form['buscar']
        conexion_MySQLdb = connectionBD() 
        cur      = conexion_MySQLdb.cursor(dictionary=True)
        querySQL = cur.execute("SELECT wd.doc, pr.rank FROM word_doc wd INNER JOIN page_rank pr ON wd.doc = pr.id_doc WHERE wd.word = '%s' ORDER BY pr.rank DESC" % (search,))
        resultadoBusqueda = cur.fetchone()  
        cur.close() 
        conexion_MySQLdb.close()
        return render_template('public/resultadoBusqueda.html', miData = resultadoBusqueda, doc = docs[resultadoBusqueda.doc], busqueda = search)
    return redirect(url_for('inicio'))  
   

@app.errorhandler(404)
def not_found(error):
        return redirect(url_for('inicio'))
    
    

if __name__ == "__main__":
    app.run(debug=True, port=8000)

