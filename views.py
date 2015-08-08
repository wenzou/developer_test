# We need to import request to access the details of the POST request
# and render_template, to render our templates (form and response)
# we'll use url_for to get some URLs for the app on the templates
from flask import Flask, render_template, request, url_for
from objects import CreditManager
# Initialize the Flask application
app = Flask(__name__)

# Define a route for the default URL, which loads the form
@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        myCreditManager = CreditManager()
        guid_string=request.form['input1']
        guids = guid_string.split(';')
        creditsRequest=request.form['credits']
        creditsFromGuids = myCreditManager.return_credits([guids])
        return render_template('form_submit.html', guids=guids, credits=creditsFromGuids)
    else:
        return render_template('form_submit.html')


# Define a route for the action of the form, for example '/hello/'
# We are also defining which type of requests this route is 
# accepting: POST requests in this case
@app.route('/hello/', methods=['POST'])
def hello():
    myCreditManager = CreditManager()
    guids=request.form['guids']
    email=request.form['youremail']
    creditsFromGuids = myCreditManager.return_credits([guids])
    print creditsFromGuids
    return render_template('form_action.html', name=email, credits=creditsFromGuids)

# Run the app :)
if __name__ == '__main__':
  app.run( 
        host="0.0.0.0",
        port=int("5000")
  )
