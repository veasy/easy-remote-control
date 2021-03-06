# Easy Remote Control  [![Code Climate](https://codeclimate.com/github/Veasy/easy-remote-control/badges/gpa.svg)](https://codeclimate.com/github/Veasy/easy-remote-control)
A simple remote control server for plex home theater on linux.

### How does it work?
**Easy Remtoe Control** (ERC) uses **simple** http protocol (REST) to transfer commands from a remote control app to the server.

By default the server provides a webpage which can be used as remote control.

### Installation
Just download the source, run following command and create a new startup entry under ubuntu.

```
start_erc-server.sh
```

### Application
The application is implemented for mobile devices and so you can just navigate to the ip address of your server and the port number `5000`. Here are some screenshots from the server app:

![Controls](images/all.jpg)
*Screenshots of the webapp*

### How to use it?
You can now call all the routes the server provieds. For example:

* /
	* media
  		* play (playpause)
  		* next
  		* previous
  		* volume
	  		* up
	  		* down
	  		* mute (toggle)
	* app/[name]
		* focus
		* start
		* stop
  	* keys
  		* return
  		* escape
	  	* up
	  	* down
	  	* left
	  	* right

### About
Written by Markus and Florian

*The MIT License (MIT)*

*Copyright (c) 2015 Veasy*
