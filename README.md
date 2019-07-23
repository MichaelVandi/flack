# Project 2

Web Programming with Python and JavaScript

This project is low-key time consuming, because the contents are so straightforward you'd think its something you can do in a few hours but as you try to get certain conditions right, it takes more time than proposed.
Also, I'm sort of a slack fanboy... happy to work on a slack parody like project.

Display Name Feature: I stored the display name in session and it worked in chrome and opera mini, even when I closed the entire browser. Somehow Microsoft edge did not save the display name when I closed the entire edge browser, but it did save the name if i just closed the flack tab, and I couldn't understand why... must be some edge feature or something.

Personal Touches:
-Slack has a slacbot, so I added a flackbot user as well, it sends a message to every channel when it is first created
something like: New channel created + date and time
-Channels are stored both in the DOM and Flask Server, so new users can see existing channels when they open the app for the first time
-Everyone is notified when a new channel is created
-Flack does not allow you to send a message is you did not select a channel first
-The input field clears up after a text was sent
-Simple U.I.

What's in each file
chat.html: html code for the chat page
index.html: html code for page to enter display name
application.py: Python code for Flask app, has two html routes and a few socketio "connections"
index.js: Javascript code that fuels the UI
