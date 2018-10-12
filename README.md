Goose is a utility that imports google contacts into Mutt or Alpine email.

Goose will:

* format contacts for either Mutt or Alpine (or both at once) 
* scan the csv file and extract only contacts with an email address
* support up to 7 emails per contact
* append a number to each nickname with mutliple emails making them easy to find in Alpine or Mutt
* back up your current conacts to /tmp and create a new contact file in the Mutt/Alpine default locations


There is also exception handling for contacts missing a first name, a last name, or both names (e.g. a company email).

Notes:
    
Download your contacts from google as a csv file.  You can use outlook or google native format, but google's is prefereable as it has more data.

Download contacts file to your /user/home/Downloads folder and make sure it's named contacts.csv or google.csv

Your Alpine contacts are expected to use the default: /home/user/.alpine/addressbook

Your Mutt contacts are expected to use the default: /home/user/.mutt/aliases

One-way sync only (google --> Alpine/Mutt)

