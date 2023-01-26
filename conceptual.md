### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?
Python is used for back end development while JS can be used do develop both the back end and front end of the application. One of the biggest differences is that python uses indentation while JS uses curly braces. JS uses let and var to define variables while python just uses a = sign. Python is snake_cased while JS is lowerCamelCase. 

Python is a multi-threaded language that is used more predominantly in backend situations whereas Javascript is single threaded and used as the front-end language for most modern websites. Python also doesn't treat 0/Undefined in the same way Javascript does and has much more verbose error handling.


- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.
  
  You can use the get method: `dict.get('student')`. This will return None if the key doesn't exist. You can also use try except as well:

```py
try:
dict['student']
except:
print('This is not a key in the dictionary')
```
One last thing you could do is use an if statement to check if the key exists before accessing:

```py
if student in dict:
dict['student']

- What is a unit test?
unit test tests a function at a time or a small section of the code. It does not test the framework itself but rather tests one unit of functionality like one function or one method. you can do this with doctests.


- What is an integration test?
integration tests work in that they test how all of the components work together. you write the integration tests iwth unittest framework. 


- What is the role of web application framework, like Flask?
Flask has a set of functions, classes that help you define what requests to repsond to and how to respond to them. frameworks are designed to support the development of web applications and provide a way to build and deploy them on the world wide web. it also makes testing easy and comes with documentation. 

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?
 You would use a URL parameter such as '/foods/pretzel' when it feels more like subject of the page. 
 you would use a query parameter such as 'foods?type=pretzel' when it feels more like its just exrra info about the page or when its used coming from a form. 

- How do you collect data from a URL placeholder parameter using Flask?
@app.route('/landingpage<id>')  # /landingpageA
def landing_page(id):
you can specify the variable in the app.route and then use that variable as a parameter in the routing function. 
@app.route('/foods/<food>')
def grocery(food):
    x = food

- How do you collect data from the query string using Flask?
request.args['term']. request.args is a dict-like object of query parameters.

- How do you collect data from the body of the request using Flask?
request.form['comment']. request.form is a dict-like object of POST parameters.

- What is a cookie and what kinds of things are they commonly used for? 
cookies are a way to store small bits of info on client(browser). the server tells the browswer to store these and they will be referencable as long as the browswer remains open. 

- What is the session object in Flask?
session object is built off using cookies and allows the client to remember lots of info without having to create many diff cookies. it contains info for the current brower and they preserve types of info and users cant modify the data.

- What does Flask's `jsonify()` do?
jsonify will take JSON serializeable data in python and convert it to a JSON string.
jsonify will return flask variables\data that need to be turned into the JSON format for frontend API's to consume.
