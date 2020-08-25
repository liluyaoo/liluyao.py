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
# 进行到：疑惑为什么Q的更改，不影响最后的收入，发现是因为数据一直处在众包任务量较低，接包方不受众包任务量的影响，明天开始进行众包任务量较高时的数据检测，今天就这样      20.08.20
# --23:52
# 对竞争性优化一下，k和任务  20.08.21--12:52
#已完成