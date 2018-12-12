# amimullvad.py
![alt text] [/img/ami_screenshot.png "AmiMullvad"]

Some of us are already in our terminal and need confirmation that we're connected to our vpn. Opening a browser and going ot the am.i.mullvad.net link isn't always fast enough. This python script verifies from your terminal if you're in fact connected to mullvad's VPN.
All you have to do is connect to mullvad however you have your machine configured to do and run this script to verify that it's working correctly.

This script requires `json, requests, os,` and `termcolor` to run. I think most of you should already have most of these already installed. 

`pip install termcolor`

`pip install json`

`pip install requests`

### Usage:

`./amimullvad.py`

That's it. Enjoy!
