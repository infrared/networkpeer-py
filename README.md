# networkpeer-py

python library for networkpeer.com

# Usage
```python
 from networkpeer import NetworkPeer

 host = 'https://www.networkpeer.com'
 username = "youraccount"
 password = "yourpassword"
 
 np = NetworkPeer(host=host,username=username,password=password)
```

# URL
##### create_url(**kwargs)
Create a new url with a list of content

parameters:

* **url** - The URL
* **content** - A liste of content
* **end** - (optional) The url to redirect to after content

Example
```python
np.create_url(url="/foo",content=["bar","baz"], end="/home")
```
##### update_url(**kwargs)
Similar to **create_url**, but updates

parameters:

* **url** - The URL
* **content** - A liste of content
* **end** - (optional) The url to redirect to after content

```python
np.update_url(url="/foo",content=["baz", "bar"], end="/home")
```
##### get_url(**kwargs)
Get URL information

parameters:
* **url** - The URL


```python
np.get_url(url="/foo")
```

##### create_content(**kwargs)
Create content

parameters:

* **view** - The view to use
* **nama** - unique name for the content
* **markdown** or **body** - markdown or body content

```python
markdown="### Super Page!###
create_content(view="simple",name="super-page",markdown=markdown)
```

# Full Example

```python
 from networkpeer import NetworkPeer

 host = 'https://www.networkpeer.com'
 username = "youraccount"
 password = "yourpassword"

 np = NetworkPeer(host=host,username=username,password=password)

 np.create_url(url="/foobar",content=["page-one","page-two"], end="/")
 
 page_one="""### Page One
 this is awesome
 **markdown rocks**
 """
 page_two="""### Wow Page Two!
 another page that does something
 """


 np.create_content(view="simple",name="page-one",markdown=page_one)
 np.create_content(view="simple",name="page-two",markdown=page_two)

 page_three="""### Here's page three
 blah blah blah
 """

 np.create_content(view="simple",name="page-three",markdown=page_three)

 # add update the URL to include page-three
 
 np.create_url(url="/foobar",content=["page-one","page-two","page-three"], end="/")
```
#License
----

MIT


