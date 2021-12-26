from flask import Flask , render_template , url_for ,redirect , request
from flask_wtf import FlaskForm 
from wtforms import StringField ,SelectField , IntegerField
from wtforms.validators import DataRequired






app = Flask('/')

class MyForm(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()] ,render_kw={'onchange': "changeGraph()"}, choices=[('line','LineGraph'),('radar', "Radar Graph")])
    Data = SelectField('Date', validators=[DataRequired()] , render_kw={'onchange': "changeData()"},choices=[('Date1','2019-Jan-02'),('Date2', "2020-Jan-21")])



@app.route('/', methods=['GET', 'POST'])
def home():    
    labels = ['SiO2', 'Al2O3', 'Fe2O3', 'CaO', 'MgO', 'SO3', 'T Alk', 'D4 Free CaO', 'LOI 550', 'LOI 1000', 'C3S', 'C3A', 'Blaine', 'Aluminate Orthrombic', 'Aluminate Sum', 'Arcanite', 'Belite_Gamma', 'Calcite', 'Dolomite', 'Gypsum', 'Hemihydrate', 'Portlandite', '45 um', 'Air Cont', 'Alite Sum', 'Aluminate Cubic', 'K2O', 'NA2O', 'Limestone', 'Clinker', 'Pozzolan','SLAG']
    val1 = [19.26, 4.8, 3.63, 62.47, 2.87, 2.8, 0.51, 0.1, 1.01, 2.98, 62.51, 6.59, 401.7, 0, 0, 0.2, 0, 0, 0, 0.5, 0, 0, 2.61, 9.65, 0, 0, 0.2, 0, 8.8, 0, 0, 10.2]
    val2 = [0.17, 0.11, 0.07, 0.17, 0.22, 0.08, 0.03, 0, 0.1, 0.16, 1.43, 0.32, 16.7, 0.5, 0.4, 0, 0, 0.03, 0, 0, 0, 0, 2.3, 0.55, 0, 0.001, 0, 0, 0, 0, 0, 10.8]

    dates = {"Date1" : val1, "Date2" : val2}
    form = MyForm()
    
    
    if request.method =='GET':

        return render_template('chart.html',labels=labels,form=form,dates =dates)

    else :
        type = dict(form.type.choices).get(form.type.data)
        Data = dict(form.Data.choices).get(form.Data.data)
        return str(type)+str(Data)
    





app.config['SECRET_KEY'] = 'any secret string'



if __name__ == '__main__' : 
    app.run(debug=True)