# Taiz Ebooks
A twitter bot built on the [python-twitter](https://github.com/bear/python-twitter) library. The bot randomly constructs tweets in a similar fashion to traditional [ebooks accounts](https://en.wikipedia.org/wiki/Horse_ebooks). The account can be seen live on Twitter under the handle [@Taiz_ebooks](https://twitter.com/taiz_ebooks).

## Installation Requirements
- Git
- Python
- Pip

## Installation Guide
1. From the command prompt, run ``git clone https://github.com/TylerWalker12/twitter-ebooks.git``.
2. Change into the directory ``cd twitter-ebooks``.
3. Run ``pip install python-twitter``.
4. Alter ``settings.json`` as you see fit, in particular, the ``"account"`` you wish to be parodying.
5. Rename ``example-auth.json`` to ``auth.json``.
6. Edit ``auth.json``'s properties to reflect those of which pertain to your own account information. For an in-depth guide on how to retrieve these fields, please consult the [the twitter-python docs](https://python-twitter.readthedocs.io/en/latest/getting_started.html).
7. If everything has been done correctly, running ``python bot.py`` should start the bot.

## settings.json
Below is a brief overview of the settings available in the ``settings.json`` file:
- ``"account"`` - The handle of the account you wish to be imitating, not including the @.
- ``"filter"`` - If set to true, then the bot won't randomly mention users or tweet links.
- ``"sleep_minutes"`` - The amount of minutes you wish for the bot to wait between tweets. Twitter's API will revoke your application if this goes below 10 minutes, so take caution in setting this too low.
- ``"use\_env\_variables"`` - If true, will make the bot pull the credentials from the host's environment. This is useful if you intend to make the sourcecode completely public, since having it exposed in json is insecure.

## auth.json
The parameters required in this can be obtained by your twitter applications settings page, more information on how to obtain these can be found on [the twitter-python docs](https://python-twitter.readthedocs.io/en/latest/getting_started.html).
