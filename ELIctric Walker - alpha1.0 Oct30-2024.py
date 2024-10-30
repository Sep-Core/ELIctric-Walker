import random

while True:
    try:
        lang = int(input("选择语言 / Select a language 1.中文 2.English"))
        if lang in [1,2]:
            break
    except ValueError:
        pass
    print("请输入数字1或2 / Please enter number 1 or 2")
if lang == 1:
    lang = {
        "pause":"按下回车键以继续",
        "rule":"""
        游戏规则与设定：
        1.游戏中的多个班级呈直线排布
        2.Eli将会随机在班级间行走并进入班级查看
          每过一分钟，若Eli在班级门口，则有33.3%的概率进入该班级，否则将
          向下一个班级移动，其移动方向在到达所有班级尽头前不会改变；若Eli
          在班内，则只会离开班级
        3.玩家每分钟可以选择一项操作：1.玩电脑 2.听讲 3.向班外偷窥
          每玩1分钟，玩家将获得1分，同时若此时已经连续游玩了x分钟，则
          将额外获得x-1分
          若玩家选择听课，无事发生
          若玩家选择偷窥，此时Eli距离玩家小于等于5个班级且在班外，玩家
          将获得其准确位置信息；若Eli距离玩家小于等于3个班级且在班内，
          玩家将获得“周边某个班级安静得可怕”提示；否则玩家将不会获得信息
        4.若Eli进入玩家所在班级，玩家将获得提示；若玩家正在玩电脑，则电脑
        将会被没收，分数扣减200分同时游戏直接结束
        """,
        "class_input":"请输入班级数量（至低3个）",
        "number_invalid":"请输入有效的数字",
        "number_less_than_3":"请输入大于3的数字",
        "class_output":"班级总数：%d",
        "game_start":"==========游戏开始==========",
        "your_class":"您所在的班级：%d班",
        "another_minute":"==新的一分钟开始了==",
        "time_remained":"剩余时间：%d分钟",
        "your_score":"您的分数：%d",
        "choice":"这分钟您打算：1.玩电脑 2.听讲 3.向班外偷窥",
        "not_123":"请输入1、2或3",
        "lost_device":"你的电脑被没收了！",
        "fun_time":"你利用了珍贵的一分钟！",
        "afk":"队友：请打开麦克风交流",
        "eli_walking":"发现Eli！他在%d班门口！",
        "weird_silence":"周边某个班级安静得可怕",
        "see_nothing":"你没有看到任何有价值的信息",
        "listen":"你又学了一分钟",
        "eli_came":"Eli刚才进来了！你没有被抓到",
        "class_over":"下课了",
        "score_got":"你得到了%d分！",
        "game_over":"==========游戏结束==========",
        "again":"输入1以退出游戏，输入2以重新开始，输入3以浏览游戏规则"
    }
else:
    lang = {
        "pause":"Click ENTER to continue",
        "rule":"""
        Game Rule and Settings:
        1. There are several classes totally (depends on your input later)
        2. These classes are arranged linearly
        3. Eli will walk randomly through these classes:
           for each minute, if Eli stands at the door of a class,
           he have the probability of 33.3% to walk into the class,
           else he will just move away to the next class;
           if Eli stands in a class, he can only walk outside this class.
        4. Eli's moving direction between classes is constant until he
           reaches the end of the row of classes
        5. For each minute, you have three choices:
           play the game, you will get 1 score, if you have played for
           several minutes, you will get some extra scores of the number
           the time in minute that you kept playing;
           listen to the class, nothing will happen;
           peek outside the class, you will get Eli's specific position
           if he is outside the class and the distance between you and
           Eli is lower or equal to 5 classes; you will find a weird
           silence in some nearby classes if Eli is inside a class and
           distant from you lower or equal to 3 classes; or you will get
           nothing
        6. If you are playing while Eli comes into your class, your device
           will be taken and you will be deducted 15 scores. In the rest of
           class, you will not be able to play anymore.
        """,
        "class_input":"How many classes you want to have? (At least 3) ",
        "number_invalid":"Please type in a valid number",
        "number_less_than_3":"Please type in a number bigger or equal than 3",
        "class_output":"Now you have %d classes",
        "game_start":"==========Game Start==========",
        "your_class":"You are in class %d",
        "another_minute":"==Another new minute==",
        "time_remained":"Time remained: %d minute",
        "your_score":"Your score: %d",
        "choice":"For this minute, you want to: 1.play 2.listen 3.peek (Please type in the number) ",
        "not_123":"Please type in 1, 2 or 3",
        "lost_device":"You lost your device!",
        "fun_time":"Another fun time!",
        "afk":"Your teammates wants to talk with you in voice",
        "eli_walking":"Eli walking! He is at the door of class %d",
        "weird_silence":"It's a weird silence in some nearby class",
        "see_nothing":"You didn't see anything",
        "listen":"You studied for a another minute",
        "eli_came":"Eli came in in this minute! You were not caught!",
        "class_over":"Class is over",
        "score_got":"You got %d score",
        "game_over":"==========Game Over==========",
        "again":"Enter 1 to quit, 2 to play again, 3 to view game rule "
    }

print("""
ELIctric Walker - alpha1.0 Oct30-2024

IDCraft Community
""")
input(lang["pause"])
print(lang["rule"])

while True:
    t = 40
    score = 0
    co_score = 1
    while True:
        try:
            classes = abs(int(input(lang["class_input"])))
        except ValueError:
            print(lang["number_invalid"])
        else:
            if classes < 3:
                print(lang["number_less_than_3"])
            else:
                break
    print(lang["class_output"]%classes)
    clas = random.randint(1,classes)
    eli = [False, random.randint(1,classes), random.choice([1,-1])]
    print(lang["game_start"])
    print(lang["your_class"]%clas)
    while t:
        if not eli[0]:
            if not random.randint(0,2):
                eli[0] = not eli[0]
            else:
                eli[1] += eli[2]
                if eli[1] == classes+1:
                    eli[1] = classes-1
                    eli[2] = -eli[2]
                elif not eli[1]:
                    eli[1] = 2
                    eli[2] = -eli[2]
        else:
            eli[0] = not eli[0]
        print(lang["another_minute"])
        print(lang["time_remained"]%t)
        print(lang["your_score"]%score)
        while True:
            try:
                o = int(input(lang["choice"]))
                if o in [1,2,3]:
                    break
                else:
                    print(lang["not_123"])
            except ValueError:
                print(lang["number_invalid"])
        if o == 1:
            if eli == [True, clas, eli[2]]:
                print(lang["lost_device"])
                score -= 200
                break
            else:
                print(lang["fun_time"])
                score += co_score
                co_score += 1
        elif o == 2:
            print(lang["listen"])
            print(lang["afk"])
            co_score = 1
        elif o == 3:
            if abs(clas-eli[1]) <= 5 and not eli[0]:
                print(lang["eli_walking"]%eli[1])
            elif abs(clas-eli[1]) <= 3 and eli[0]:
                print(lang["weird_silence"])
            else:
                print(lang["see_nothing"])
            co_score = 1
        if eli == [True, clas, eli[2]]:
            print(lang["eli_came"])
        t -= 1
        input(lang["pause"])
    print(lang["class_over"])
    print(lang["your_class"] % clas)
    if score < 0:
        score = 0
    print(lang["score_got"]%score)
    print(lang["game_over"])
    while True:
        try:
            again = int(input(lang["again"]))
            if again in [1, 2]:
                break
            elif again == 3:
                print(lang["rule"])
            else:
                print(lang["not_123"])
        except ValueError:
            print(lang["number_invalid"])
    if again == 2:
        pass
    elif again == 1:
        break
print("Program Exited")