from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

# HTML template as a Python multi-line string
HTML_PAGE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Button Click App</title>
</head>
<body>

<button onclick="sendPostRequest()">Click Me</button>

<script>
function sendPostRequest() {
    fetch('/button-click', {
        method: 'POST',
    })
    .then(response => response.json())
    .then(data => alert(data.response))
    .catch((error) => {
        console.error('Error:', error);
    });
}
</script>

</body>
</html>
'''

@app.route('/')
def index():
    # Render the HTML page
    return render_template_string(HTML_PAGE)

@app.route('/button-click', methods=['POST'])
def button_click():
    # Logic to handle button click, respond with JSON
    return jsonify({"response": "ok"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
