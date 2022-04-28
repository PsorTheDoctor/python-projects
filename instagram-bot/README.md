# bots
Example bots that automatically use a browser

## Instagram_bot User's Guide
- Follow these steps to create mupltiple Instagram accounts using the scripts. 
- For email service it uses gazeta.pl polish website, I haven't try any other sites yet.
- It's recommended to use Kali Linux or any VPN / Proxy service with different IP numbers just not to arouse suspicion...
- You'll also need a chrome / chromium browser and any simple image editor

### Getting started

#### Prerequisites
Before install process make sure you're using Python 3, otherwise type in a terminal:

`sudo pip install python3`

#### Libraries
The scripts were written with the use of two basic python libraries: `selenium` and `pyautogui`
Install them by typing:

`sudo pip install selenium`
`sudo pip install pyautogui`

#### Installing
Clone the repository:

`git clone https://github.com/PsorTheDoctor/bots.git`

### Running
Firstly, go to the proper directory:

`cd /*your_path_to_repository*/Instagram_bot`

Before any actions done, you had better go to the `user_db.txt` file and clean it. The data you see is just an example, this is how your proper file should look like.

#### Preparing
After that, come to other two scripts that now interest you: `email_bot.py` nad `insta_bot.py`
Both use `pyautogui` library, which means (now) they're highly sensitive for various element locations. 
Good practice is to run them at first, make a screenshot and open it in any photo / paint editor in order to check the values your cursor has, being hovered on their buttons / capchtas. After that, go to the 39, 52, 54, 56th line at `insta_bot.py` and 43rd, 51st line at `email_bot.py`. It's just a searching for `pyautogui.click()` or method `pyautogui.douibleClick()`. Update your files with correct values.

#### Data customization
Make sure `insta_bot.py` has email factor with the same names as `email_bot.py` had made. They're stored in `user_db.txt` crude database file. I've solved it simply: the accounts of mine were created with the `test_monkey*@gazeta.pl` where * is iteration loop number (you can, and even should change both of name and index, it's 30th line at 'email_bot.py':

`user1 = User('test_monkey' + str(29), '********', 'your_mail@gmail.com', 'male', '2000-12-21')`

and 25th line at `insta_bot.py`:

`email = 'test_monkey' + str(10 + i) + '@gazeta.pl'`
`password = '********'`

Also, don't forget to set a good password. In my scripts I've used one for every account. More creative you'll be, more unique accounts you'll create! 

#### Usage
In order to best usage you should run them one-by-one, e.g.: 

- run first bot by `python3 email_bot.py` to create 5 email accounts;
- run second bot by `python3 insta_bot.py` to create 5 Instagram profiles with emails you have
- make sure they were stored in `user-db.txt` database file

And it's all :) Now try it with different IP just to avoid Capchta and follow steps you've already done.

### Development
Feel free to use or develop further any solution you found here

Have fun and stay resposible!
