# Easy Remote Control
A simple remote control server for plex home theater on linux.

### How does it work?
**Easy Remtoe Control** (ERC) uses **simple** http protocol (REST) to transfer commands from a remote control app to the server.

By default the server provides a webpage which can be used as remote control.

### Installation
Just download the source, run following command and create a new startup entry under ubuntu.

```
python setup.py install
```

### How to use it?
You can now call all the routes the server provieds. For example:

* /
	* media
  		* play (playpause)
  		* next
  		* previews
  		* volume
	  		* up
	  		* down
	  		* mute (toggle)
  	* keys
  		* return
  		* escape
  		* arrows
	  		* up
	  		* down
	  		* left
	  		* right

### About
Written by Markus and Florian

*MIT License 2015*
 