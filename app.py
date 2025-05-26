from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return '''
        <form action="/generate">
            Enter n: <input type="number" name="n">
            <input type="submit" value="Generate Even Numbers">
        </form>
    '''

@app.route('/generate')
def generate():
    try:
        n = int(request.args.get('n', 0))
        even_numbers = [str(i) for i in range(2, 2*n+1, 2)]
        return '<br>'.join(even_numbers)
    except:
        return 'Invalid input. Please enter a valid number.'

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
