from pythonProject11 import create_app
# from flask import Flask, render_template
#
# app = Flask(__name__,templelate_folder='C:/Users/Ahmed/PycharmProjects/pythonProject11/tempelates/index.html')
# app=create_app()
#
# @app.route('/')
# @app.route('/index')
# def index():
#
#  return render_template("C:/Users/Ahmed/PycharmProjects/pythonProject11/tempelates/index.html")
#
# if __name__ == '__main__':
#    app.run(debug=True)


app = create_app()
if __name__ == '__main__':
        app.run(debug=True)