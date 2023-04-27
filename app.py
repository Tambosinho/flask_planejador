from flask import Flask, render_template, request
import datetime

app = Flask(__name__)


name = ""
email = ""
serie = ""
olimpiada = ""

# Define global variables to store the number of clicked cells in each column
seg_count = 0
ter_count = 0
qua_count = 0
qui_count = 0
sex_count = 0
sab_count = 0
dom_count = 0


@app.route('/')
def index():


    return render_template('index.html')

@app.route('/resultado', methods=['POST'])
def resultado():

    global name
    global email
    global serie
    global olimpiada
    global seg_count, ter_count, qua_count, qui_count, sex_count, sab_count, dom_count

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        serie = request.form['serie']
        olimpiada = request.form['olimpiada']
        return "Form submitted successfully."+f"Name: {name}, Email: {email}"+ f"<br> A serie é: {serie}" + f" A olimpiada é: {olimpiada}"  
    


        
        # Iterate over each column and count the number of clicked cells

        for i in range(1, 8):
            column_count = 0
            for j in range(1, 11):
                cell_id = f'{j}AM_{i}'
                cell_value = request.form.get(cell_id)
                if cell_value == 'blue':
                    column_count += 1
            
            # Update the corresponding global variable with the count
            if i == 1:
                seg_count = column_count
            elif i == 2:
                ter_count = column_count
            elif i == 3:
                qua_count = column_count
            elif i == 4:
                qui_count = column_count
            elif i == 5:
                sex_count = column_count
            elif i == 6:
                sab_count = column_count
            elif i == 7:
                dom_count = column_count

    
@app.route('/teste')
def teste():

    return f"""
    Este é um teste, apenas. Abaixo devem aparecer algumas informações: \n \n 
    Nome: {name}\n 
    Email: {email}\n 
    Serie: {serie}\n 
    Olimpiada: {olimpiada}\n 
    Numero de dias até a sua prova: {dias_ate_OBF} \n 
    Contagem de cada dia da semana: 
    Segunda: {seg_count}
    Terça: {ter_count}
    Quarta: {qua_count}
    Quinta: {qui_count}
    Sexta: {sex_count}
    Sab: {sab_count}
    Dom: {dom_count}
    """



# calcular dias até a OBF (tem q adicionar pra outras olimpiadas)

OBF_data = datetime.date(year=2023, month=9, day=21) # aqui define a data da obf
today = datetime.date.today()

global dias_ate_OBF

dias_ate_OBF = (OBF_data - today).days # aqui retorna o numero de dias







if __name__ == '__main__':
    app.run(debug=True)

