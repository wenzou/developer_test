This is a read me

objects.py includes the creditManager objects

This application was developed and tested under Python 2.7

Running WebApp
1. Install flask -> pip install flask
2. python views.py

Running Tests
python tests.py

Local Performance Tests
Returning credits from one guid
5000 guids = 9s
10000 guids = 14s
100000 guids = 130s
1000000 guids = 1403.785s ~ 23 mins
O(n) performance. 
Return guid from one credit


1000000 guids = 1466.310s

All guids have 5 credits



Q&A on Spec
1. Which part is the guid? Everything within the guid tag?
2. Assumption is python, no framework like django? We would have to display html
3. Whats the format for the credits? just string. 
4. Whats an interface? Is that a GUI? or could that just be a method for the object? Display html
5. You can say handle 10,000 credit or 1,000,000 guids, do you mean that the interface can handle inputs of that many credits/guids, or is the feed contain that many credits/guids?
6. For duplicate guids/credits, so I just return the output twice? 