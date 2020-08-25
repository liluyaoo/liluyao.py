def collaborativeCrowdsourcing():
    N = int(input("请输入合作数量："))     #合作数量
    x0 = 1.2    #相互协作系数
    rho = 0.1   #风险系数
    sigma = 0.1
    k = int(input("请输入努力货币化系数："))    #努力货币化系数  原数值为20
    Qbar = float(input("请输入任务总估价："))   
    a = Qbar * 0.3 / N  #固定薪资
    Sbar = 300  #接包方能接受的最低薪资
    if Sbar > a:
        print("Tips：该任务价格下，接包方数量设置过多,可能对双方收益中的一方不友好！")
    Qbar = (((Qbar - a*N)/N - 215*(k/8)**4) / (0.4*(k/8)**2))**(1/3)  #保留任务量
    Qbar = round(Qbar, 3)
    import numpy as np
    epsilon = np.random.normal(0, sigma, size=N)#随机影响
    b=k*rho*sigma**2
     #选择模型
    choice = input("请选择基于总产出激励模型或者基于个人产出激励模型，输入总产出或者个人即可：")
    if choice == "总产出": 
        #众包任务量较低时
        EOTR = N ** 2 * x0 ** 2 * (N - 1 + (N + 1) * b) / (((1 + b) ** 2 * N - 1) * k)
        EOTR = round(EOTR, 3)
        if Qbar < EOTR:
            betaTR0 = b*x0*N/((1+b)**2*N-1) / 10#基于个人产出的激励系数
            betaTR0 = round(betaTR0, 3)
            gammaTR0 = ((1+b)*N-1)/((1+b)**2*N-1) / 10#基于总产出的激励系数
            gammaTR0 = round(gammaTR0, 3)
            eTR0 = 10 * ((1+2*b)*N-1)*x0/(((1+b)**2*N-1)*k) 
            ETR0 = 10 * ((1+b)*N-1)*x0/(((1+b)**2*N-1)*k)
            paiTR0 = [0] * N #货币化收入
            ratio = 400 * 2 / (k*(eTR0**2 + (N-1)*ETR0**2))
            i = 0
            Y = 0 #总产出
            while i < N:
                Y += eTR0**2+(N-1)*ETR0**2+epsilon[i] 
                i += 1 
            c = 0
            # exa = [1]*N
            while c < N:
                paiTR0[c] = a+0.5*k*ratio*(betaTR0*(eTR0**2+(N-1)*ETR0**2+epsilon[c])+gammaTR0*x0*Y)
                # exa[c] = (betaTR0*(eTR0+(N-1)*ETR0+epsilon[c])+gammaTR0*x0*Y)*ratio #去掉固定薪资
                paiTR0[c] = round(paiTR0[c], 1)
                c += 1 
            # CMTR0 = round(N ** 2 * x0 ** 2*((1+b)**3*N**2+(1+b)*(b**2-2)*N+1-b)/(2*k*((1+b)**2*N-1)**2), 3)
            print("保留任务量相对较低,任务对接包方无约束作用： \n", "基于个人努力的激励系数：", betaTR0, "\n",  "基于总努力的激励系数：", gammaTR0, "\n", "总收入：", paiTR0)
        # 众包任务量较高时
        else:
            betaTR1 = (((1+b)*N-1)*Qbar*k-N**2*(N-1)*x0**2)/(N*x0*(2*b*N+N-1)) / 10
            betaTR1 = round(betaTR1, 3)
            gammaTR1 = (b*Qbar*k+N*(N-1)*x0**2)/(N*x0**2*(2*b*N+N-1)) / 10
            gammaTR1 = round(gammaTR1, 3)
            eTR1 = 10 * (((1+b)*N+b-1)*Qbar*k-N*(N-1)**2*x0**2)/(N*x0*(2*b*N+N-1)*k)
            ETR1 = 10 * (b*Qbar*k+N*(N-1)*x0**2)/(N*x0*(2*b*N+N-1)*k)
            ratio = 400 * 2 / (k*(eTR1**2 + (N-1)*ETR1**2))
            paiTR1 = [0] * N
            i1 = 0
            Y1 = 0
            while i1 < N:
                Y1 += eTR1**2+(N-1)*ETR1**2+epsilon[i1]
                i1 += 1
            c1 = 0
            while c1 < N:
                paiTR1[c1] = a+0.5*k*ratio*(betaTR1*(eTR1**2+(N-1)*ETR1**2+epsilon[c1])+gammaTR1*x0*Y1)
                paiTR1[c1] = round(paiTR1[c1], 1)
                c1 += 1
            # CMTR1 = round(Qbar - N * ((betaTR1 + x0 * gammaTR1)**2 + (N - 1) * x0 ** 2 * gammaTR1 ** 2 + b * (betaTR1 ** 2 + N * x0 ** 2 * gammaTR1 ** 2)) / (2*k), 3)
            print("保留任务量相对较高，任务对接包方有约束作用： \n", "基于个人努力的激励系数：", betaTR1,"\n", "基于总努力的激励系数：", gammaTR1, "\n", "总收入：", paiTR1)
    elif choice == "个人":
         EONR = N * x0 ** 2 / ((1 + b) * k)
         EONR = round(EONR, 3)
         #保留任务量较低
         if Qbar < EONR: 
            betaNR0 = x0/(1+b) / 10
            betaNR0 = round(betaNR0, 3)
            eNR0 = 10 * x0/((1+b)*k)
            ratio = 400 * 2 / (k*(eNR0**2))
            paiNR0 = [0]*N
            j = 0
            while j < N:
                paiNR0[j] = a+0.5*k*betaNR0*(eNR0**2+epsilon[j])*ratio
                paiNR0[j] = round(paiNR0[j], 1)
                j += 1
            print("保留任务量相对较低,任务对接包方无约束作用： \n", "基于个人努力的激励系数：", betaNR0, "\n", "总收入：", paiNR0)
         else: 
            betaNR1 = k*Qbar/(N*x0) / 10
            betaNR1 = round(betaNR1, 3)
            eNR1 = 10 * Qbar/(N*x0)
            paiNR1 = [0]*N
            ratio = 400 * 2 / (k*(eNR1**2))
            j1 = 0
            while j1 < N:
                paiNR1[j1] = a+0.5*k*betaNR1*(eNR1**2+epsilon[j1])*ratio
                paiNR1[j1] = round(paiNR1[j1], 1)
                j1 += 1
            print("保留任务量相对较高,任务对接包方起到约束作用：\n", "基于个人努力的激励系数：", betaNR1,  "\n", "总收入：", paiNR1)
    else:
        print("请输入总产出或个人！")