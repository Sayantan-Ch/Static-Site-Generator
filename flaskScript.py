from flask import Flask, Response , render_template , request
import urllib.request , json
app = Flask(__name__)

@app.route('/')
def homePage():
   return render_template('frontend.html')


@app.route('/shreyansh/')
def siteGenerated():
    
    for i in range(3):
        url='https://www.boredapi.com/api/activity'
        response = urllib.request.urlopen(url)
        data = response.read()
        dict = json.loads(data)
        print(dict['activity'])
    return "hello"


@app.route('/generation')
def generatingSites():
   quantity=request.args.get('Quantity')
   url='https://www.boredapi.com/api/activity'
   response = urllib.request.urlopen(url)
   data = response.read()
   dict = json.loads(data)
   return render_template('testing.html',data=dict)


if __name__ == '__main__':
   app.run(debug=True , port=5004)


