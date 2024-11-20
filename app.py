from flask import Flask, render_template, request
import web_scrap as s
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        product_name = request.form['product_name']
        product_name = (product_name)
        tags_from_site=s.call_website(product_name)
        data = [str(element) for element in tags_from_site]
        return render_template('results.html',data=tags_from_site,product_name=product_name )
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)