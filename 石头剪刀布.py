import random
import easygui as g
import sys

aDict={1:'石头',2:'剪刀',3:'布'}
def game():
    g.msgbox("即将进入石头剪刀布游戏",title="石头剪刀布",ok_button="START",image='皮卡丘.png')
    choice=g.buttonbox("做出你的选择",choices=('石头','剪刀','布'),image='石头剪刀布.png')
    i=random.randint(1,3)
    if str(choice)==aDict[i]:
        g.msgbox("你们打成了平手",title="结果",ok_button="确认",image='握手.png')
    if str(choice)=='石头':
        if aDict[i]=='剪刀':
            g.msgbox("对方出了剪刀，你赢了",title="结果",ok_button="确认",image='剪刀.png')
        if aDict[i]=='布':
            g.msgbox("对方出了布，你输了",title="结果",ok_button="确认",image='布.png')
    if str(choice)=='剪刀':
        if aDict[i]=='布':
            g.msgbox("对方出了布，你赢了",title="结果",ok_button="确认",image='布.png')
        if aDict[i]=='石头':
            g.msgbox("对方出了石头，你输了",title="结果",ok_button="确认",image='石头.png')
    if str(choice)=='布':
        if aDict[i]=='石头':
            g.msgbox("对方出了石头，你赢了",title="结果",ok_button="确认",image='石头.png')
        if aDict[i]=='剪刀':
            g.msgbox("对方出了剪刀，你输了",title="结果",ok_button="确认",image='剪刀.png')
game()
while 1:
    if g.ccbox('你想要再来一局吗？'):
        game()
    else:
        sys.exit(0)
