Goose is a utility that imports google contacts into Mutt or Alpine email.

Goose will:

* format contacts for either Mutt or Alpine (or both at once) 
* scan the csv file and extract only contacts with an email address
* support up to 7 emails per contact
* append a number to each nickname with mutliple emails making them easy to find in Alpine or Mutt
* back up your current contacts to /tmp and create a new contact file in the Mutt/Alpine default locations


There is also exception handling for contacts missing a first name, a last name, or both names (e.g. a company email).

CONTENTS:

[Running Goose](#running)

[Dependencies](#dependencies)

[Notes](#notes)

[Exception Handling](#exception-handling)

[Beginners Help](#beginners-help)

<br><br>
## Running:

Download goose.py open your terminal and execute it with python3 goose.py.

<br><br>
## Dependencies:

Python 3.6 or newer
Modules are all from the default toolkit

<br><br>
## Notes:

Download your contacts from google as a csv file.  You can use outlook or google native format, but google's is preferable as it preserves more data.

Download contacts file to your /user/home/Downloads folder and make sure it's named contacts.csv or google.csv

Your Alpine contacts are expected to use the default: /home/user/.alpine/addressbook

Your Mutt contacts are expected to use the default: /home/user/.mutt/aliases

Before replacing your existing contact files, Goose backs them up to /tmp.

One-way sync only (google --> Alpine/Mutt)

<br><br>
## Exception Handling:

If your contacts are like mine, not every field is populated.  Mutt and Alpine want a very simple format; basically:

    nick_name   Firstname Lastname  email@email.com

1. Missing Last name:
    ```
    Goose's first guess is this is a company contact (e.g., martha@duckbrainsoftware.com):
        nick_name = Company Name   --> Duckbrain_software
        firstname = Firstname      --> Martha
        lastname  = (Company Name) --> (Duckbrain Software)
    If no company name is found:
        nick_name = Firstname      --> Martha
        firstname = Firstname      --> Martha
        lastname  = (domain)       --> (duckbrainsoftware)
    ```

2. Missing First name:
    ```
    Goose figures this is a friend you know by last name:
        nick_name = Lastname
        firstname = _
        lastname  = Lastname
    ```

3. Missing both First and Last names:
    ```
    Goose thinks this is a company (e.g., info@duckbrainsoftware.com)
        nickname  = Company Name   --> duck_brain_software
        firstname = localpart      --> info
        lastname  = (emaildomain)  --> (duckbrainsoftware)
    If there's no company, no First and no Last name, Goose still won't give up:
        nickname  = domain         --> duckbrainsoftware
        firstname = localpart      --> info
        lastname  = (domain)       --> (duckbrainsoftware)
    ```

4. Contacts with multiple emails:
    ```
    Goose creates a new entry for each email, appending a number [_1, _2, _3...]
    ```

* underscores are used to concatenate mutliple words into single entries
* parentheses are used for visual clarity

<br><br>
## Beginners' Help

If you're not used to python scripts, using them is still easy.
* You must goose.py it from your terminal, just like Mutt and Alpine

* Save goose.py in a folder, open that folder and type:
    ```
    python3 goose.py
    ```
* It's much easier to make it executable.  Go to the folder that contains goose.py and:
    ```
    chmod +x goose.py
    ```
    Now, you don't need to type 'python3' to execute it, just type goose.py

* Better yet, take your newly executable script and put it in: 
    ```
    /usr/local/bin
    ```
    Now, you can open any terminal and simply type goose.py to run it.

* Another option - make your own bin anywhere you like - maybe:
    ```
    /home/username/bin
    ```
    and add this location to your $PATH file.  Edit your .bashrc file:
    ```
    # User defined paths:
    PATH=$PATH:~/bin
    ```
    Now, executables you add to this new bin will be executable from any open terminal
