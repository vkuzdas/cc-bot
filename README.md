# cc-bot

Repo for Bonus assignment 5.
Client controlled bot on infected computer.

## How to run
You can run each .py script right after cloning. Just make sure you run the **bot.py** before **controller.py**.

## start-up

1) Open two terminals, one in cc-bot, second in cc-bot/infected.
2) cc_bot/infected$ **python3 bot.py**
(You should see a log in form of *bot_name got created*)
3) cc_bot$ **python3 controller.py**

<p>This is how your terminals should look like :</p>

![image](https://user-images.githubusercontent.com/33172723/209997926-be258824-3830-43d4-8ce2-a11f8c5b2d2d.png)

<p> Controller should see that "Mat9" bot is up, bot itself should wait for commands from controller and there should be "Mat9" in scores.txt in the gist folder https://gist.github.com/vkuzdas/b986ad8f94834deaf526315971868580 .</p>
<p>Make sure that activities.txt file is empty so that there are no overlapping commands. Also make sure to type</p>
bot_name:rmresp
<p> to remove bot responses so that there are no overlapping responses confusing the controller. </p>

## 'w'   (list of users currently logged in)
1) In the controller terminal, after initialization, type "<bot_name>:w" to list currently logged int users
2) **You should always wait at least a minut between each command so there is no merge conflict**
<p>This is how your terminals should look like :</p>

![image](https://user-images.githubusercontent.com/33172723/210000944-d6bdd4bc-53f7-4bb8-a43c-9c7e5aef1b66.png)

<p>Controller got a response with list of logged in users, we can see there is only user 'vk' logged in. This response is also written in history.txt in github. The command itself is encoded as emoji. </p>

## ls <PATH> (list content of specified directory)
1) Type "<bot_name>:ls:.." to list the directory above bot's current command in controller
  
![image](https://user-images.githubusercontent.com/33172723/210002714-00e1cb49-4f79-4630-a747-6aa7f5b03692.png)
  
response in controller
  
![image](https://user-images.githubusercontent.com/33172723/210003018-2184bd41-57bf-4e11-9537-c41a1f15c9c6.png)

## id (if of current user)
1) Type "<bot_name>:id" to view user id
  
response in controller
  
![image](https://user-images.githubusercontent.com/33172723/210003222-c9d6cdbf-4e05-47d9-b1f1-ccb30d1a551f.png)

  
## Copy a file from the bot to the controller
<p>This operation is by far the most merge conflict sensitive and merge conflict inducing aswell :). Do give the bot about a minute or so to do its job. </p>
1) Type "bot_name:cp:echo.sh" once prompted by the controller
2) Wait 1 min
3) See the controller folder


### Explanation:
Once the controller registers valid cp command, it copies mail.png into gist as a steganographic envelope. This enveloped is then pulled by the bot. Bot then zips the file that the controller wants to copy into the pulled envelope. This zipped envelope gets pushed back into repo. Controller then fetches the mail.png, now zipped with the prompted file and unpacks it in controller's folder.
<p>Note: github messes up zipped envelope for some reason and does not display the PNG. The PNG is however viewable for a brief moment right after controller pushes is as envelope. </p>

<p>Controller upon entering copy command</p>
![image](https://user-images.githubusercontent.com/33172723/210003428-284f39f0-34fe-4699-92bf-25fa92c8a1dc.png)
<p> a while later, echo.sh got copied (windows attributes older creation date for some reason)</p>
![image](https://user-images.githubusercontent.com/33172723/210003615-f7b8bcf4-6ac9-4c2f-aac1-e496993ef502.png)


## Execute a binary inside the bot given the name of the binary
1) Type "bot_name:exe:echo.sh" once prompted by the controller
2) There is no output sent to the controller, it is only executed in the bot's folder
![image](https://user-images.githubusercontent.com/33172723/210005397-69a3c091-668c-49a8-b5c6-39a5083d031d.png)




