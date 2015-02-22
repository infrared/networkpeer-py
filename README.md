# networkpeer-py

python library for networkpeer.com

# Usage
```python
 from networkpeer import NetworkPeer

 host = 'https://www.networkpeer.com'
 username = "youraccount"
 password = "yourpassword"
 
 np = NetworkPeer(host=host,username=username,password=password)
 np.test()
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

#License
----

MIT


