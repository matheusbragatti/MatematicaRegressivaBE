import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True





alunos = [
    {
    'id':123,
    'nome':'Leo',
    'email':'leo.com',
    'escolaridade':'superior completo',
    'idade':23},
    {
    'id':6521,
    'nome':'Matheus',
    'email':'matheus.com',
    'escolaridade':'superior incompleto',
    'idade': 27
    }
]

aulas = [
    {
    'id':1,
    'nome_aula':'soma',
    'progresso':80,
    'progresso_max':80},
    {
    'id':2,
    'nome_aula':'soma',
    'progresso':60,
    'progresso_max':90,
    }
]

perfis = [
    {
    'id':22,
    'recomendacoes':'Estudar mais soma',
    'Login':'Xaps',
    'Password':1232},
    {
    'id':28,
    'recomendacoes':'Estudar mais subtração',
    'Login':'Lee',
    'Password':12321},
]

materiaCard = [
    {
        'id':10,
        'name':'materia1',
        'description':'primeira materia do site matematica regressiva',
        'currentProgress':0,
        'maxProgress':74
    },
    {
        'id':456,
        'name':'materia2',
        'description':'segunda materia do site para test',
        'currentProgress':6,
        'maxProgress':11
    },
    {
        'id':77,
        'name':'materia3',
        'description':'terceira materia do curso',
        'currentProgress':2,
        'maxProgress':9
    }
]

aulaCard = [
    {
        'id':10,
        'name':'Aula1',
        'description':'Comecando a aprender',
        'currentProgress':0,
        'maxProgress':74
    },
    {
        'id':456,
        'name':'Aula2',
        'description':'segunda aula test',
        'currentProgress':6,
        'maxProgress':11
    },
    {
        'id':77,
        'name':'Aula3',
        'description':'terceira do curso',
        'currentProgress':2,
        'maxProgress':9
    },
        {
        'id':77,
        'name':'Aula4',
        'description':'quarta e ultima aula',
        'currentProgress':6,
        'maxProgress':33
    }
]

materias = [
    {
        'nome':'nome1',
        'id':10,
        'ProgressoAtual':100,
        'ProgressoMax':100,
        'Conteudo':'Matematica aplicada'},
    {
        'nome':'nome2',
        'id':11,
        'ProgressoAtual':110,
        'ProgressoMax':100,
        'Conteudo':'Matematica basica 2'
    },
]

exercicios = [
    {
    'id':5,
    'ProgressoAtual':10,
    'ProgressoMaximo':47,
    'Exercicio':'Tabuada numeral 2',
    'PossiveisErros':'Multiplicação'},
    {
    'id':12,
    'ProgressoAtual':30,
    'ProgressoMaximo':47,
    'Exercicio':'Tabuada numeral 9',
    'PossiveisErros':'Multiplicação'},
]

erros = [
    {
    'id':10,
    'MateriaRecomendada':'Geometria',
    'Exercícios':'Hipotenusas',
    'PossiveisErros':'Multiplicação',
    'NumTotalErros':10},
    {
    'id':100,
    'MateriaRecomendada':'Trigonometria',
    'Exercícios':'Exercicio 1',
    'PossiveisErros':'Geometria',
    'NumTotalErros': 1,},
]    

@app.route('/', methods=['GET'])
def home():
    return "<h1>Matematica Regressiva</h1><p>Bem vindo a nossa Home Page</p>"

@app.route('/aluno', methods=['GET'])
def aluno():
    id = int(request.args['id'])

    for aluno in alunos:
        if aluno['id'] == id:
            resultado = aluno

    return resultado


@app.route('/aluno/getAlunoPorPosicao', methods=['GET'])
def alunok():
    position = int(request.args['position'])

 
    return alunos[position]

@app.route('/aula', methods=['GET'])
def aula():
    id = int(request.args['id'])

    for aula in aulas:
        if aula['id'] == id:
            resultado = aula

    return resultado

@app.route('/aula/getAulaPorPosicao', methods=['GET'])
def aulaposition():
   position = int(request.args['position'])

 
   return aulas[position]    

@app.route('/perfil', methods=['GET'])
def perfil():
    id = int(request.args['id'])

    for perfil in perfis:
        if perfil['id'] == id:
            resultado = perfil

    return resultado

@app.route('/perfil/getPerfilPorPosicao', methods=['GET'])
def perfilposition():
   position = int(request.args['position'])

 
   return perfis[position]

@app.route('/materias', methods=['GET'])
def getMaterias():
    apiRequest = request.args['id']

    response = pegarMaterias(apiRequest)

    return response


@app.route('/materia', methods=['POST'])
def createMaterias():
    apiRequest = request.args['']

    response = criarMateriaNova(apiRequest)


    return "Materia criada com sucesso"


@app.route('/materia', methods=['GET'])
def materia():
    id = int(request.args['id'])

    for materia in materias:
        if materia['id'] == id:
            resultado = materia

    return resultado

@app.route('/materia/getMateriaPorPosicao', methods=['GET'])
def materiaposition():
   position = int(request.args['position'])

 
   return materias[position]

@app.route('/exercicio', methods=['GET'])
def exercicio():
    id = int(request.args['id'])

    for exercicio in exercicios:
        if exercicio['id'] == id:
            resultado = exercicio

    return resultado

@app.route('/exercicio/getExercicioPorPosicao', methods=['GET'])
def exercicioposition():
   position = int(request.args['position'])

 
   return exercicios[position]

@app.route('/erro', methods=['GET'])
def erro():
    id = int(request.args['id'])

    for erro in erros:
        if erro['id'] == id:
            resultado = erro

    return resultado

@app.route('/erro/getErroPorPosicao', methods=['GET'])
def erroposition():
   position = int(request.args['position'])

 
   return erros[position]


@app.route('/materiaCard', methods=['GET'])
def getAllMateria():
    

    return jsonify(materiaCard)


@app.route('/materiaCard', methods=['POST'])
def postMateria():
    requestData = request.json
    print(requestData)
    print('entrou no POSTmateriaCard')
    materiaCard.append(requestData)

    return jsonify(materiaCard)


@app.route('/aulaCard', methods=['GET'])
def getAllAula():
    

    return jsonify(aulaCard)


@app.route('/aulaCard', methods=['POST'])
def postAula():
    requestData = request.json
    print(requestData)
    print('entrou no POSTaulaCard')
    aulaCard.append(requestData)

    return jsonify(aulaCard)


app.run()