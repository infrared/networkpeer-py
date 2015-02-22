"""
    NetworkPeer
    ~~~~~~~~~~~

    :copyright: (c) 2014 by Michael Kroher
    :license: MIT
"""


import requests
import json
import re


class NetworkPeer(object):

    def __init__(self,**kwargs):
        acceptable = [ "host","username","password" ]
        for k in kwargs.keys():
            if k in acceptable:
                self.__setattr__(k, kwargs[k])


    def get_url(self,**kwargs):
        """ Get URL information
        Syntax:
            get_url(**kwargs)

        args:
            url <str>

        Example:
            get_url(url="/foo")

        """


        r = requests.post(self.host +'/builder/get/url', json=kwargs, auth=(self.username, self.password))
        if r.status_code == "403":
            print "Unauthorized, or invalid credentials"
        print(r.text)


    def create_url(self,**kwargs):
        """Create a URL with content
        
        Syntax:
            create_url(**kwargs)

        args:
            url <str>
            content <list>
            end <str>  (optional)

        Example:
            create_url(url="/foo",content=["bar","baz"],end="/")
        """

        r = requests.post(self.host +'/builder/create/url', json=kwargs, auth=(self.username, self.password))
        if r.status_code == "403":
            print "Unauthorized, or invalid credentials"
        print(r.text)

    def update_url(self,**kwargs):
        """Update a URL content list
        
        Syntax:
            update_url(**kwargs)

        args:
            url (str)
            content (list)

        Example:
            update_url(url="/foo",content=["bar","baz"], end="/")
        """

        r = requests.post(self.host +'/builder/update/url', json=kwargs, auth=(self.username, self.password))
        if r.status_code == "403":
            print "Unauthorized, or invalid credentials"
        print(r.text)
