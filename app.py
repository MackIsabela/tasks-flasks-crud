from flask import Flask, request, jsonify
from models.task import Task

app = Flask(__name__)

#CRUD 
# CREAT READ UPDATE DELETE
#TABELA: TAREFA

tasks = []
task_id_control = 1

@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()  #data puxa o dicionario criado na task
    new_task =  Task(id=task_id_control, title=data['title'], description=data.get("description", ""))
    task_id_control += 1
    tasks.append(new_task)
    print(tasks)
    return jsonify({"message": "Nova tarefa criada com sucesso"})

if __name__ == "__main__":
    app.run(debug=True)