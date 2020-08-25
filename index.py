from Competitive_crowdsourcing import competitiveCrowdsourcing
from Collaborative_crowdsourcing import collaborativeCrowdsourcing
print('请选择竞争性众包或者协作性众包，输入竞争或者协作即可：')
choice = input()
if choice == '竞争':
    competitiveCrowdsourcing()
elif choice == '协作':
    collaborativeCrowdsourcing()
else :
    print("请输入竞争或者协作")
