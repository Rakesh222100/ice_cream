from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        try:
            input_value = request.form['input_value']
            import os
            with open(os.getcwd()+"/temp/{}.txt".format(input_value), "w") as f:
                f.write(input_value)
            print()
            import os 
            env_name = os.getenv("env_name")
            
            if env_name=="develop":
                return "develop config data"  
            elif env_name=="qa":
                return "qa config data" 
            else:
                return "dummy data"
        except Exception as e:
            print(e)
    elif request.method == 'GET':
        return render_template('index.html', result=result)

def check_my_name(name):
    if name == "rakesh":
        return "yes"
    else:
        return "no"
def check_my_password(password):
    if password == "rakinew":
        return "yes"
    else:
        return "no"


if __name__ == '__main__':
    app.run(port=8005,host="0.0.0.0",debug=True)
