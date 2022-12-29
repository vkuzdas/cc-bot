# cc-bot

repo for Bonus assignment 5
client controlled bot on infected computer

## How to run
You can run each .py script right after cloning. Just make sure you run the **bot.py** before **controller.py**.

### start-up
1) Open two terminals, one in cc-bot, second in cc-bot/infected.
2) cc_bot/infected$ **python3 bot.py**
(You should see a log in form of *<bot_name> got created*)
3) cc_bot$ **python3 controller.py**
<p>This is how your terminals should look like :</p>
![image](https://user-images.githubusercontent.com/33172723/209997926-be258824-3830-43d4-8ce2-a11f8c5b2d2d.png)
<p> Controller should see that "Mat9" bot is up, bot itself should wait for commands from controller and there should be "Mat9" in scores.txt in the gist folder</p>
<p>Make sure that activities.txt file is empty so that there are no overlapping commands. Also make sure to type</p>
*<bot_name>:rmresp*
<p> to remove bot responses so that there are no overlapping responses confusing the controller. </p>

### 'w'   (list of users currently logged in)
1) In the controller terminal, after initialization, type "<bot_name>:w" to list currently logged int users
<p>**You should always wait at least a minut between each command so there is no merge conflict**</p>
<p>



