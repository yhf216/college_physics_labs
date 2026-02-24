#import "ReportTemplate/phylab.typ": phylab

#show: phylab.with(
  name: "棱镜偏向角特性 G",
  instructor: "王宗利",
  desk-id: "18",
  class: "",
  author: "", 
  author-id: "",
  date: datetime(year: 2025, month: 11, day: 6),
  week: "第6周",
  am-pm: "下午",
)

// 此处填写正文，如：

= 预习报告（10分）
== 实验综述（5分）
（自述实验现象、实验原理和实验方法，包括必要的光路图、电路图、公式等。不超过500字。）

本实验旨在掌握最小偏向角的测量方法，学会测定棱镜玻璃对汞灯某单色光的折射率。

1.分光计的调整与三棱镜顶角的测量

该部分已在“分光计的调整与使用”实验中学习并掌握，此处不再赘述。

2.最小偏向角测量原理

如图1所示，旋转载物台使得一光学面AC与平行光管入射方向基本垂直。从平行光管发出平行光射向三棱镜光学面AB，经过三棱镜光学面AC折射出来，望远镜从毛玻璃面BC底边出发逆时针旋转，会看到汞单色系列光，说明已经找到折射的光路。

#figure(
  grid(columns: 1, rows: 1, gutter: 1em,
    image("preview/p1.png",width: 70%), 
  [图1],
))

#h(2em)再继续转动载物台，观察汞单色光偏向角的变化，如果向右移动，偏向角$delta$会变小。继续转动载物台直至汞单色光突然向左移动，使偏向角$delta$变大，此转折点即为该汞单色光最小偏向角位置。用望远镜对准此处，记录此时分光计读数游标窗口数据为$theta_(min Ⅰ)$、$theta_(min Ⅱ)$。然后移去三棱镜，用望远镜对准入射光，读取游标窗口数据为$theta_(o Ⅰ)、theta_(o Ⅱ)$，则最小偏向角为：

#h(1fr)$ delta_(min)=1/2(|theta_(min Ⅰ)-theta_(o Ⅰ)|+|theta_(min Ⅱ)-theta_(o Ⅱ)|) $#h(1fr)

3.折射率测量原理

一束平行单色光从三棱镜的一个光学面AB入射，经折射后从另一光学面AC射出，入射角$i$、出射角$i^'$、偏向角$delta$如图2所示。

#figure(
  grid(columns: 1, rows: 1, gutter: 1em,
    image("preview/p2.png",width: 75%), 
  [图2],
))

#h(2em)可知$delta=(i-r)+(i^'-r^')$，当$i=i^'$时，由折射定律有$r=r^'$，$r+r^'=2r=∠A$，得：

#h(1fr) $ r=1/2∠A,i=1/2delta_(min)+r=(∠A+delta_(min))/2 $ #h(1fr)

再由折射定律推导出三棱镜折射率：

#h(1fr) $ n = sin(i)/sin(r) = sin((∠A+delta_(min))/2)/sin(∠A/2) $ #h(1fr)

由上式可知，只需测得三棱镜顶角A和汞单色光波的入射光的最小偏向角$delta_(min)$，就可以计算出三棱镜对该汞单色光波的入射光的折射率。

== 实验重点（3分）
（简述本实验的学习重点，不超过100字。）

本实验的学习重点在于掌握最小偏向角的测量方法，学会测定棱镜玻璃对汞灯某单色光的折射率，同时进一步熟悉分光计的调整方法。

== 实验难点（2分）
（简述本实验的实现难点，不超过100字。）

本实验的难点在于正确调整分光计、准确判断最小偏向角并正确读数，同时，确保数据测量与处理的准确性也是该实验的难点。

= 原始数据（20分）
（将有老师签名的“自备数据记录草稿纸”的扫描或手机拍摄图粘贴在下方，完整保留姓名，学号，教师签字和日期。）

//#figure(supplement: auto,image("原始数据.jpg", width: 100%))

= 结果与分析（60分）

== 数据处理与结果（30分）
（列出数据表格、选择适合的数据处理方法、写出测量或计算结果。）

1.三棱镜顶角测量

调整好分光计后，利用棱脊分束法测量三棱镜顶角，得到数据如下表：
#figure(
    table(
      columns:(1.06fr, 0.9fr, 0.9fr, 0.9fr, 0.9fr, 1.24fr, 1.26fr, 1.24fr),
      [实验次数], [$theta_(左 Ⅰ)$], [$theta_(左 Ⅱ)$], [$theta_(右 Ⅰ)$], [$theta_(右 Ⅱ)$], [$|theta_(左 Ⅰ)-theta_(右 Ⅰ)|$],[$|theta_(左 Ⅱ)-theta_(右 Ⅱ)|$],[∠A],
      [1],[$343degree 55acute$],[$163degree 55acute$],[$223degree 55acute$],[$43degree 53acute$],[$120degree 00acute$],[$120degree 2acute$],[$60degree 00acute 30acute.double$],
      [2],[$351degree 21acute$],[$171degree 21acute$],[$231degree 24acute$],[$51degree 23acute$],[$119degree 57acute$],[$119degree 58acute$],[$59degree 58acute 45acute.double$],
      [3],[$338degree 51acute$],[$158degree 51acute$],[$218degree 53acute$],[$38degree 52acute$],[$119degree 58acute$],[$119degree 59acute$],[$59degree 59acute 15acute.double$],
      [4],[$350degree 17acute$],[$170degree 17acute$],[$230degree 23acute$],[$50degree 19acute$],[$119degree 54acute$],[$119degree 58acute$],[$59degree 58acute 00acute.double$],
      [5],[$7degree 5acute$],[$187degree 5acute$],[$247degree 12acute$],[$67degree 9acute$],[$119degree 53acute$],[$119degree 56acute$],[$59degree 57acute 15acute.double$],
      [6],[$356degree 44acute$],[$176degree 44acute$],[$236degree 50acute$],[$56degree 47acute$],[$119degree 54acute$],[$119degree 57acute$],[$59degree 57acute 45acute.double$],
    ),
)<table_1>

#h(1fr)$phi_1=|theta_(左 Ⅰ)-theta_(右 Ⅰ)|,phi_2=|theta_(左 Ⅱ)-theta_(右 Ⅱ)|$#h(1fr)

#h(1fr)$∠A=1/2(phi_1+phi_2)=1/4(|theta_(左 Ⅰ)-theta_(右 Ⅰ)|+|theta_(左 Ⅱ)-theta_(右 Ⅱ)|)$#h(1fr)

根据上述公式计算出∠A。数据处理时已考虑“过零”情况。为避免中间数据四舍五入造成的精度损失，在计算时保留到秒，最终求出∠A平均值：

#h(1fr)$ #overline[∠A]=1/6Sigma_(i=1)^6∠A_i=59degree 59acute$#h(1fr)

2.三棱镜对汞灯绿光的最小偏向角测量及折射率计算

观察并记录最小偏向角相关数据如下表：

#figure(
    table(
      columns:(1.1fr, 1fr, 1fr, 1fr, 1fr, 1.2fr, 1.2fr, 1.2fr),
      [实验次数], [$phi_1$], [$phi_2$], [$phi_(10)$], [$phi_(20)$], [$|phi_1-phi_(10)|$],[$|phi_2-phi_(20)|$],[$delta_(min)$],
      [1],[$33degree 50acute$],[$213degree 50acute$],[$339degree 58acute$],[$159degree 58acute$],[$53degree 52acute$],[$53degree 52acute$],[$53degree 52acute $],
      [2],[$35degree 15acute$],[$215degree 15acute$],[$341degree 21acute$],[$161degree 21acute$],[$53degree 54acute$],[$53degree 54acute$],[$53degree 54acute $],
      [3],[$27degree 22acute$],[$207degree 22acute$],[$333degree 30acute$],[$153degree 30acute$],[$53degree 52acute$],[$53degree 52acute$],[$53degree 52acute $],
      [4],[$26degree 49acute$],[$206degree 49acute$],[$332degree 56acute$],[$152degree 56acute$],[$53degree 53acute$],[$53degree 53acute$],[$53degree 53acute $],
      [5],[$20degree 57acute$],[$200degree 57acute$],[$327degree 5acute$],[$147degree 3acute$],[$53degree 52acute$],[$53degree 54acute$],[$53degree 53acute $],
      [6],[$18degree 14acute$],[$198degree 14acute$],[$324degree 22acute$],[$144degree 22acute$],[$53degree 52acute$],[$53degree 52acute$],[$53degree 52acute $],
    ),
)<table_2>

#h(1fr)$delta_(min)=1/2(|phi_1-phi_(10)|+|phi_2-phi_(20)|)$#h(1fr)

根据上述公式计算出$delta_(min)$。数据处理时已经考虑“过零”情况。最终求出$delta_(min)$的平均值：

#h(1fr) $#overline[δ]_min=1/6Sigma_(i=1)^6(delta_(min))_i=53degree 53acute$#h(1fr)

将∠A与$delta_(min)$代入折射率计算公式，可以得到：

#h(1fr) $ n =  sin((∠A+delta_(min))/2)/sin(∠A/2) = 1.6765 $ #h(1fr)

3.汞灯单色光最小偏向角测量及折射率计算

同样的方法观察并记录其他汞灯单色光的最小偏向角相关数据并计算折射率$n$：
#figure(
    table(
      columns:(1.1fr, 1.8fr, 1fr, 1fr, 1fr, 1fr, 1fr, 1fr),
      [实验次数], [汞灯单色光波长],[$phi_1$], [$phi_2$], [$phi_(10)$], [$phi_(20)$], [$delta_(min)$],[$n$],
      [1],[$404.7n m$(紫)],[$26degree 45acute$],[$206degree 45acute$],[$329degree 15acute$],[$149degree 15acute$],[$57degree 15acute$],[$1.7078$],
      [2],[$435.8n m$(蓝)],[$29degree 37acute$],[$209degree 37acute$],[$333degree 20acute$],[$153degree 20acute$],[$56degree 17acute$],[$1.6990$],
      [3],[$546.0n m$(绿)],[/],[/],[/],[/],[$53degree 53acute$],[$1.6765 $],
      [4],[$577.1n m$(黄)],[$22degree 44acute$],[$202degree 46acute$],[$329degree 15acute$],[$149degree 15acute$],[$53degree 30acute$],[$1.6728$],
    ),
)<table_2>

#h(2em)根据柯西色散公式：

#h(1fr) $ n(lambda)=a+b/(lambda^2)+c/(lambda^4)$ #h(1fr)

用Python拟合得：

#h(1fr)$a=1.633382,b=1.39 times 10^(-14) m^2,c=-2.72 times 10^(-28) m^4$#h(1fr)

绘制色散曲线如下：

#figure(supplement: auto,image("log.png", width: 100%))


== 误差分析（20分）
（运用测量误差、相对误差或不确定度等分析实验结果，写出完整的结果表达式，并分析误差原因。）

（1）实验结果分析

已知仪器允差$Delta_(仪 器)=1 acute$

1.三棱镜顶角测量

A类不确定度：$u_A = sqrt(1/(6 times 5) times sum_(i=1)^6 (∠A_i-#overline[∠A])^2) = 29 acute.double$

B类不确定度：$u_B = Delta_(仪 器)/sqrt(3) = 35 acute.double$

合成不确定度：$u = sqrt(u_A^2+u_B^2) = 1 acute$

最终结果表达式：$∠A = 59degree 59 acute ± 1 acute$

2.三棱镜对汞灯绿光的最小偏向角测量及折射率计算

A类不确定度：$u_A = sqrt(1/(6 times 5) times sum_(i=1)^6 ((delta_(min))_i-#overline[δ]_min)^2) = 20 acute.double$

B类不确定度：$u_B = Delta_(仪 器)/sqrt(3) = 35 acute.double$

合成不确定度：$u = sqrt(u_A^2+u_B^2) = 1 acute$

最终结果表达式：$delta_(min) = 53degree 53acute ± 1 acute$

计算三棱镜对汞灯绿光折射率的不确定度：

#h(1fr) $u = sqrt(((partial n)/(partial ∠A)dot u_(∠A))^2+((partial n)/(partial delta_(min))dot u_(delta_min))^2) = 3 times 10^(-4)$#h(1fr)

最终结果表达式：$n=1.6765±0.0003$

（2）误差可能的原因

1.最小偏向角位置的确定存在一定的主观性，可能导致一定的误差

2.平行光管射出的光线具有一定的宽度，判断刻度对准时有一定的主观性，可能造成一定误差。

3.仪器的角游标刻线较细，读数时可能存在人为误差。

4.仪器可能存在误差，如仪器老化、刻度不准、仪器热胀冷缩等。

5.分光计的调整中，判断绿色十字是否对齐刻度线的操作存在一定的主观性，可能导致分光计未精确调好，导致一定的误差。
== 实验探讨（10分）
（对实验内容、现象和过程的小结，不超过100字。）

本次实验进一步熟悉了分光计的调整方法，复习了三棱镜顶角的测量方法，学习和掌握了最小偏向角的测量方法，测定了棱镜的玻璃对汞灯单色光的折射率。实验中能够观察到汞灯的色散现象，三棱镜顶角、最小偏向角测量结果的不确定度都较小，实验比较顺利。

= 思考题（10分）
（解答教材或讲义或老师布置的思考题，请先写题干，再作答。）

1.测量时如何识别最小偏向角$delta_(min)$的位置？

首先调整望远镜，直至观察到清晰的汞灯单色系列光，说明已经找到折射的光路。此时再继续转动载物台，观察汞单色光偏向角的变化，如果向右移动，偏向角$delta$会变小。继续转动载物台直至汞单色光突然向左移动，使偏向角$delta$变大，此转折点即为该汞单色光最小偏向角$delta_(min)$的位置。

2.设计一种测量三棱镜折射率的方法。

采用掠入射法测量三棱镜折射率：当一束光从三棱镜的一个光学面（如AB面）入射，经折射后射向另一个光学面（如AC面），若在AC面发生全反射，则入射角等于临界角$i_c$，满足$sin i_c = 1/n$（$n$为三棱镜折射率，空气折射率$approx$1）。测量掠入射光的偏折角$theta$，取入射角为90度，测得棱镜顶角∠A，可以通过公式$n=sin((A+theta)/2)/sin(A/2)$计算三棱镜折射率。

- 注意事项：
+ 用PDF格式上传“实验报告”，文件名：学生姓名+学号+实验名称+周次。
+ “实验报告”必须递交在“学在浙大”本课程内对应实验项目的“作业”模块内。
+ “实验报告”成绩必须在“浙江大学物理实验教学中心网站”-“选课系统”内查询。
+ 教学评价必须在“浙江大学物理实验教学中心网站”-“选课系统”内进行，学生必须进行教学评价，才能看到实验报告成绩，教学评价须在本次实验结束后3天内进行。