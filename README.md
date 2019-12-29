#Publish a Text

These python codes help you to publish a text post on your facebook page using Graph API

#Setup

Required Python Libraries--
1- json
2- requests
3- os
4- sys

#How to Use

1- At first go to facebook developers website and singup as a developer.
2- Then goto Tools and Graph API Explorer.
3- Create your new APP.
4- Select User Token.
5- Give Permission for manage_pages and publish_pages.
6- Now click Get Access Token.
7- Copy the User Access Token and run the code get_page_access_token.py and provide this User Access Token as argument.
        python3 get_page_access_token.py |USER_ACCESS_TOKEN_HERE|
8- If all the info is correct till now you will get your Page Name, ID & Access Token.
9- Copy this Page ID and Page Access Token in the access_token.txt file corresponding to their keys.
10- Run facebook.py with your message to be posted as argument.
