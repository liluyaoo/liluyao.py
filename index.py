
from Competitive_crowdsourcing import competitiveCrowdsourcing
from Collaborative_crowdsourcing import collaborativeCrowdsourcing

def model(choice):
    if choice == '竞争':
        M = input("请输入任务数量：")
        k = input("请输入努力货币化系数（单位：元）：") 
        eff = input("请输入接包方在任务每个阶段的努力程度（单位：小时），用空格隔开：") 
        competitiveCrowdsourcing(M, k, eff)
    elif choice == '协作':
        N = int(input("请输入任务数量："))
        k = int(input("请输入努力货币化系数（单位：元）：")) 
        Qbar = float(input("请输入任务总估价（单位：元）："))
        collaborativeCrowdsourcing(N, k, Qbar)
    else :
        print("请输入竞争或者协作")
print('请选择竞争性众包或者协作性众包，输入竞争或者协作即可：')
choice = input()
model(choice)

