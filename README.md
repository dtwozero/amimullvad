# amimullvad.py
<img src="/img/ami_screenshot.png" alt="amimullvad screenshot">

## Description
Some of us are already in our terminal and need confirmation that we're connected to our vpn. Opening a browser and going ot the am.i.mullvad.net link isn't always fast enough. This python script verifies from your terminal if you're in fact connected to mullvad's VPN.
All you have to do is connect to mullvad however you have your machine configured to do and run this script to verify that it's working correctly.

## Requirements
The banner is using `figlet`. 

###Ubuntu/Debian

`apt-get install figlet`

or

###Arch Linux
`pacman -S figlet`


Are people still using Fedora? do i really need to add that line?

This script requires `json, requests, os,` and `termcolor` to run. I think most of you should already have most of these already installed. 

`pip install termcolor`

`pip install json`

`pip install requests`

### Usage:

`./amimullvad.py`

That's it. Enjoy!
