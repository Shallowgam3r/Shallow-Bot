# Shallow-Bot

Welcome to ShallowBot! 
ShallowBot is a twitter program written in the [Python Twitter](https://github.com/bear/python-twitter) library!
The bot constructs tweets in a manner that appears to be fully randomized. Essentially, it pulls tweets from the assigned account, and makes its own tweets!
The account can be seen live on Twitter under the handle [@ShallowRobot](https://twitter.com/shallowrobot)


Down below I will show you how to start up your own ShallowBot from scratch!

# <h3> Installation Requirements 
- GIT [Windows](https://git-scm.com/download/win) / [Mac](https://git-scm.com/download/mac) 
- [PYTHON](https://www.python.org/downloads/)
- PIP [download](https://pip.pypa.io/en/stable/installing/)
  
  
# <h3> Other requirements  <h4> Make a Twitter account
  - You'll need a twitter account (Obviously). Maybe consider creating a new account! Use a fresh email and youll need to have a phone number attatched to your account. Here is a link to a free phone service that I reccomend [Google Voice](https://voice.google.com)
  Feel free to add a profile picture aswell to spice things up! Afterall, it is your account!
# <h4> Make a Twitter Dev account
  - While still logged into your new Twitter account, head on over to [Dev Twitter](https://developer.twitter.com/). You'll have to apply for a developers account (Easy). Just be honest and completely fill in all of the required areas. If you have any questions feel free to ask me! Usually after you apply for the dev account, Twitter takes about 2-3 hours to accept it! Once your dev account is accepted, you can proceed to the next step in setting up your ShallowBot!
    
  - Now that you have your dev account, the first thing you want to do is create a new app. For convenience, use the same name that you used with your new twitter account.Once you’ve named and created your app, you’re going to immediately want to adjust its permissions to **Read and Write**. In order to post to Twitter from a program, it needs to have a mobile number connected to the account — which is why you needed to create one earlier.
  
  - Next, go to the API Keys page and click **Generate my Access Token,** and keep the window open while it works. You’ll need those keys and tokens in just a few minutes.   
  
  # <h3> Installation Guide
   - Open Git Bash (Run as administrator). On the first line, copy and paste this:     
                            
      ```git clone https://github.com/Shallowgam3r/Shallow-Bot.git```
      
   - Change into the correct directory by typing ```cd Shallow-Bot```
           
   - Next, copy and paste this code: ```pip install python-twitter```
   
   - Alter ```settings.json``` as you see fit, in particular, the ```"account"``` you wish to be scanning for tweets.
   - Edit ```auth.json's``` properties to reflect those of which pertain to your own account information. Basically your *keys* and *tokens*. 
   - If everything has been done correctly, running ```python ShallowBot.py``` should start up your Shallow Bot!
   
   # <h3> Settings.json
  - ```"account"``` - The handle of the account you wish to be scanning, not including the @. **The account must have over 3,600 tweets for it to work!**
  - ```"filter"``` - If set to true, then the bot won't randomly mention users or tweet links.
  - ```"sleep_minutes"``` - The amount of minutes you wish for the bot to wait between tweets. Twitter's API will revoke your application if this goes below 10 minutes, so take caution in setting this too low.
  - ```"use\_env\_variables"``` - If true, will make the bot pull the credentials from the host's environment. This is useful if you intend to make the sourcecode completely public, since having it exposed in json is insecure. (I personally leave this on false. Things work much better).
   
  Enjoy your ShallowBot!
