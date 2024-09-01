from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/')
def captura_ip():
    user_ip = request.remote_addr
    
    file_path = r'C:\Users\Gustavo\Desktop\pegar o ip\ipdovagaba.txt'
    with open(file_path, 'a') as file:
        file.write(f'{user_ip}\n')

    html_content = '''
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Te Peguei</title>
        <style>
            body {
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
                font-family: Arial, sans-serif;
                background-color: #f0f0f0;
            }
            h1 {
                font-size: 3em;
                color: #333;
            }
        </style>
    </head>
    <body>
        <h1>Te peguei</h1>
    </body>
    </html>
    '''
    return render_template_string(html_content)

if __name__ == '__main__':
    app.run(debug=True)
