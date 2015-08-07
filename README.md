This is a read me

objects.py includes the creditManager objects

This application was developed and tested under Python 2.7

Using the creditManager with the interactive console
>>> from objects import creditManager
>>> myCreditmanager = creditManager()
credit Manager created

Running Tests
python tests.py

Running WebApp
1. Install flask -> pip install flask
2. python views.py


Q&A on Spec
1. Which part is the guid? Everything within the guid tag?
2. Assumption is python, no framework like django? We would have to display html
3. Whats the format for the credits? just string. 
4. Whats an interface? Is that a GUI? or could that just be a method for the object? Display html
5. You can say handle 10,000 credit or 1,000,000 guids, do you mean that the interface can handle inputs of that many credits/guids, or is the feed contain that many credits/guids?
6. For duplicate guids/credits, so I just return the output twice? 