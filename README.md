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
If you're new to non-graphical Python programs, using them is still easy.

* You can always run one by navigating into its folder using your terminal and typing:
  ```
  python3 _programname_
  ```
  I use python3 in the example to be certain, but a thoughtfully formatted script should be ok with just 'python' - sometimes a fatal syntax error is a clue your script is calling the wrong version of Python.
  
* You can make life easier by making the script executable:
  ```
  chmod +x _programname_
  ```
  This means you can do away with 'python3' and just type:
  ```
  _programname_
  ```
* You can now go step further and place your script in an executable directory, such as:
  ```
  mv _programname_ /usr/local/bin
  ```
  /usr/bin/local is one of several possible locations common in Linux.  Doing so means that simply opening a terminal and typing the programname will run the script.  No need to go to the directory itself.

* Lastly, you can go a step further still and make your own executable directory, such as:
  ```
  mkdir -p /home/_username_/bin
  ```
  Then you would add this line to your .bash_profile:
  ```
  PATH=$PATH:/home/_username_/bin
  ```
  and
  ```
  reboot
  ```
  Of course _username_ is your user's name.  And of course you're not running your system as root...
