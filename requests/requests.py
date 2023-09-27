from flask import Flask, request, url_for
app = Flask(__name__)

@app.route("/")
def root():
    return "root"

@app.route("/hello/<name>")
def hello(name):
    return "Hello %s" % name

@app.route("/add/<int:first>/<int:second>")
def add(first, second):
    return str(first+second)

@app.route("/hello/")
def hello2():
    name = request.args.get("name", "")
    if name == "":
        return "no param supplied"
    else:
        return "Hello %s" % name

@app.route("/display")
def display():
    start = '<img src ="'
    url = url_for('static', filename='uploads/upload.png')
    end = '"/>'
    return start+url+end, 200
    #return '<imgsrc="'+url_for('static', filename='uploads/upload.png')+'"/>'

@app.route("/account/", methods=["GET", "POST"])
def account():
    if request.method == "POST":
        print(request.form)
        name = request.form["name"]
        return "hello %s" % name
    else:
        page = """
        <html>
            <body>
                <form action="" method="post" name="form">
                    <label for="name">Name:</label>
                    <input type="test" name="name" id="name"/>
                    <input type="submit" name="submit" id="submit"/>
                </form>
            </body>
        </html>"""
        return page

@app.route("/upload/", methods=["POST", "GET"])
def upload():
    if request.method == "POST":
        f = request.files["datafile"]
        f.save("static/uploads/upload.png")
        return "file uploaded"
    else:
        page2="""
        <html>
            <body>
                <form action="" method="POST" name="form" enctype="multipart/form-data">
                    <input type="file" name="datafile"/>
                    <input type="submit" name="submit" id="submit"/>
                </form>
            </body>
        </html>
        """
        return page2, 200

if __name__ == "__name__":
    app.run(host="0.0.0.0", debug=True)
