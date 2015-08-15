This is a read me

objects.py includes the creditManager and FasterCreditManager

This application was developed and tested under Python 2.7



##Running WebApp
1. Install flask -> pip install flask
2. python views.py


##Running Tests
python tests.py

To run tests with large sets of data of xml data. 

1. In tests.py under setUp method, 
2. Update the self.local_xml_file to an absolute path to a file under the test_data folder
3. The testdata10000, means that there are 10000 guids, and 5 credits per guid. 


##Local Performance Tests
###Performance Test using cElementTree Library with iterate method - this is the FasterCreditManager
Returning credits from one guid

Best Case - guid at the beginning of the xml

* 5000 guids = 0.86s
* 10000 guids =  1.4s
* 100000 guids = 1.7s
* 1000000 guids = 1.7s

Constant O(1) performance

Worst Case - guid at the end of the xml

* 5000 guids = 1.8s
* 10000 guids = 4.14
* 100000 guids = 11.68s
* 1000000 guids = 114s

O(N) performance - this is pretty bad, but without the overhead of loading the elements into memory. 

Return guid from one credit

Best Case - credit at the beginning of the xml

* 5000 guids = 0.81s
* 10000 guids =  0.97s
* 100000 guids = 0.88s
* 1000000 guids = 0.88s

Constant O(1) performance

Worst Case - credit at the end of the xml

* 5000 guids = 1.57s
* 10000 guids =  2.16s
* 100000 guids = 15.9s
* 1000000 guids = 118.69s

O(N) performance - this is pretty bad, but without the overhead of loading the elements into memory. 

###Performance Test using cElementTree Library - this is the creditManager
Returning credits from one guid

* 5000 guids = 5.859s
* 10000 guids = 12s
* 100000 guids = 32.2221s
* 1000000 guids = 206s

O(Log(N)) performance 

Return guid from one credit

* 5000 guids = 6.2s
* 10000 guids = 9s
* 100000 guids = 32s
* 1000000 guids = 298.29s

O(N) performance

Please note that absolute values of these number don't matter as I am running my local machine slowly in order to show the difference as the input changes
It is more important to analyze the relative speed of these inputs. All test ran under the same environments

###Previous performance tests
Returning credits from one guid

* 5000 guids = 9s
* 10000 guids = 14s
* 100000 guids = 130s
* 1000000 guids = 1403.785s ~ 23 mins

O(n) performance. 

Return guid from one credit

* 1000000 guids = 1466.310s

All guids have 5 credits


##Q&A on Spec

1. Which part is the guid? Everything within the guid tag?
2. Assumption is python, no framework like django? We would have to display html
3. Whats the format for the credits? just string. 
4. Whats an interface? Is that a GUI? or could that just be a method for the object? Display html
5. You can say handle 10,000 credit or 1,000,000 guids, do you mean that the interface can handle inputs of that many credits/guids, or is the feed contain that many credits/guids?
6. For duplicate guids/credits, so I just return the output twice? 
7. For item number 4, I assumed now that is you input multiple credits, and you return the guid if there is one that contains all the credit inputs. 
