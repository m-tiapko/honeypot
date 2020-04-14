#!/usr/bin/python3
import pyinotify
from telethon import TelegramClient
from telethon import sync, events
import requests
 
api_id = 
api_hash = 
 
client  = TelegramClient('Big_Bro', api_id, api_hash)
 
client.start()
 
dlgs = client.get_dialogs()
 
class MyEventHandler(pyinotify.ProcessEvent):
    def process_IN_ACCESS(self, event):
        client.send_message('Mike', "Someone entered the system!")
 
    def process_IN_ATTRIB(self, event):
        client.send_message('Mike', "Someone entered the system!")
 
    def process_IN_CLOSE_NOWRITE(self, event):
        client.send_message('Mike', "Someone entered the system!")
 
    def process_IN_CLOSE_WRITE(self, event):
        client.send_message('Mike', "Someone entered the system!")
 
    def process_IN_CREATE(self, event):
        client.send_message('Mike', "Someone entered the system!")
 
    def process_IN_DELETE(self, event):
        client.send_message('Mike', "Someone entered the system!")
 
    def process_IN_MODIFY(self, event):
        client.send_message('Mike', "Someone entered the system!")
 
    def process_IN_OPEN(self, event):
        client.send_message('Mike', "Someone entered the system!")
 
def main():
    wm = pyinotify.WatchManager()
    wm.add_watch('/root/', pyinotify.ALL_EVENTS, rec=True)
    eh = MyEventHandler()
    notifier = pyinotify.Notifier(wm, eh)
    notifier.loop()
 
if __name__ == '__main__':
    main()
