# We need to import request to access the details of the POST request
# and render_template, to render our templates (form and response)
# we'll use url_for to get some URLs for the app on the templates
import os
from flask import Flask, render_template, request, url_for
from objects import CreditManager
# Initialize the Flask application
app = Flask(__name__)

# Define a route for the default URL, which loads the form

GUID_TYPE = 0
CREDIT_TYPE = 1

@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        myCreditManager = CreditManager()
        inputs = []
        input_type = CREDIT_TYPE
        #probably want some proper form validation later
        for i in range(1, 5):
            key = 'input'
            key += `i`
            #loop through all the 5 fields
            if key in request.form and request.form[key] is not u'':
                inputs.append(request.form[key])
                if "tag:" in request.form[key]:
                    input_type = GUID_TYPE
        if input_type == CREDIT_TYPE:
            #if input is credit type, then return the guids
            return_data = myCreditManager.return_guids(inputs)
        else:
            #else if input are guids, then return the credits
            return_data = myCreditManager.return_credits(inputs)
        return render_template('form_submit.html', error='', return_data=return_data)
    else:
        return render_template('form_submit.html')


# Run the app :)
port = int(os.environ.get('PORT', 5000))

if __name__ == '__main__':
  app.run( 
        host="0.0.0.0",
        port=port
  )
