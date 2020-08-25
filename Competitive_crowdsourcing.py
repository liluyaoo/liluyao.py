def competitiveCrowdsourcing():
    M = int(input("请输入任务数量："))        #任务分解数
    k = int(input("请输入努力程度货币化系数："))                                   #货币化系数
    b = 1                                   #风险系数
    arr = input("请输入接包方在任务每个阶段的努力程度，用空格隔开：")
    e = [int(n) for n in arr.split()]       #努力程度假定值
    mu = [10, 0]            #随机影响参数
    sigma = [1,1]           
    x = [0]*M 
    f = [0]*M
    m = [10] + [0] * (M-1)
    pai = [0]*M             #货币化收入
    import numpy as np
    np.set_printoptions(suppress=True)
    eta = np.random.normal(mu[0], sigma[0], size=M)#研发能力数据化的正态分布
    epsilon = np.random.normal(mu[1], sigma[1], size=M)#随机影响
    i = 0
    tmp = [0]*M
    while i < M:
        #tmp是Σ t`2 的值
        tmp[i] = sigma[0] ** 2 * eta[i] ** 2 / ((i+1) * sigma[0] ** 2 + eta[i] ** 2) + eta[i] ** 2
        #接包方业绩 
        pai[i] = eta[i] + e[i] + epsilon[i]
        i += 1
    #求解m的中间值
    hope = [0] * 4 
    t = 0
    t1 = 1
    t2 = -1
    while t < M-1:
        t2 += 1
        while t < t1:
            hope[t2] += (pai[t+1] - e[t1])
            t += 1
        t1 += 1
    j = 1
    while j < M:
        m[j] = (eta[j] ** 2 * m[0] + sigma[0] ** 2 * hope[j-1]) / (eta[j] ** 2 + j*sigma[0] ** 2)
        j += 1
    #求解方差值
    vkar = 0
    vepkar = 0
    vkc = 0
    while vkc < M:
        vkar += eta[vkc] 
        vepkar += epsilon[vkc]
        vkc += 1
    vkar /= M   #研发能力平均值
    vepkar /= M #随机变量平均值
    variance = [0] * 4
    varianceep = [0] * 4
    vcon = 0
    vcon1 = 0
    while vcon < M-1:
        vcon1 = 0
        while vcon1 < vcon + 1:
            variance[vcon] +=  (eta[vcon1] - vkar) ** 2
            varianceep[vcon] += (epsilon[vcon1] - vepkar) ** 2
            vcon1 += 1
        variance[vcon]  /= vcon + 1
        varianceep[vcon] /= vcon + 1
        vcon += 1
    #求解(x, f)
    x[M-1] = 1/(1+2 * b * k * (variance[M-2] + varianceep[M-2]**2))
    f[M-1] = (1/2 - x[M-1])*(m[M-1] + e[M -1]) + 1/2 * k * e[M-1] ** 2
    xc=M-2
    b1=0
    while xc >= 0:
        b1 = xc
        tmp2=0
        while b1 < M - 1:
            tmp2 += x[b1+1]
            b1 += 1
            #获取契约(x(b),f(b))
        x[xc] = (1 - 2 * b * k * variance[xc-1]**2 * tmp2) /(1+2* b * k * (variance[xc-1]+varianceep[xc-1]**2)) 
        if(x[xc] < 0):
            x[xc] = 0
        f[xc] = (1/2 - x[xc])*(m[xc]+e[xc])+1/2*k*e[xc]**2
        xc -= 1
    import numpy 
    result = numpy.zeros((M,2))
    c1=0
    c3=0
    while c1 < M:
        c2=0
        while c2 < 2:
            if c2 == 0:
                result[c1][c2] = round(x[c3], 3)
            else:
                result[c1][c2] = round(f[c3], 3)
            c2 += 1
        c1 += 1
        c3 += 1 
    S = [0] * M #最终收入
    s = 0
    while s < M:
        #货币化
        S[s] = round(f[s] + x[s] * 0.5 * k * pai[s] ** 2, 1)
        s += 1
    print("第一列为激励系数、第二列为固定薪资: \n", result, "\n", "总薪资：", S)