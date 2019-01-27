# S 型曲线

使用文献 1 中的 Richards 模型。生长曲线如下

## $\lambda$

## 文献

1. Bentea, Lucian, Murielle A. Watzky, and Richard G. Finke. "Sigmoidal nucleation and growth curves across nature fit by the Finke–Watzky model of slow continuous nucleation and autocatalytic growth: explicit formulas for the lag and growth times plus other key insights." The Journal of Physical Chemistry C 121.9 (2017): 5302-5312.

## 种群分布

```txt
牛的密度：3.4130/平方公里
羊的密度：9.4514/平方公里
野兔的密度：2.426/平方公里
```

```txt
牛肉：125大卡/100g
羊肉：118 大卡/100g
兔肉：102 大卡/100g
```

1. It is difficult to generalize or average out the weight of all cattle because different kinds have different averages of weights. However, according to some sources, the average weight of all cattle is 753 kg (1,660 lb). Finishing steers in the feedlot average about 640 kg (1,410 lb); cows about 725 kg (1,600 lb), and bulls about 1,090 kg (2,400 lb).[44] "FAO Cattle Weights". FAO. Archived from the original on 21 April 2015. Retrieved 5 May 2015.

```
牛的质量：753kg
羊的质量：45 - 100 kg, 45 - 160 kg, 87.5 kg
兔的质量：70 kg
Antelope jackrabbit: 8.7 lbs, 3.94625 kg
```

## 耗氧量随着时间的变化情况

$m_d$ 为龙的质量，只要定了岁数就是常数，耗氧量与时间成正比。

$$
V(O_2) = m_d V_E t
$$

关键是计算 $V_E$，表示耗氧量

$$
\begin{aligned}
    V_E &= 37.5 mL/(kg \cdot min) \\
&= \frac{37.5 mL * 10^{-3}L/mL}{1 kg \cdot min \cdot \frac{1}{60} h/min} \\
&= 2.25L/(kg \cdot h)
\end{aligned}
$$

现在只考虑两天内的消耗，因此 $t = 48h$。

$$
V(O_2) = m_d \cdot 2.25 \cdot 48
$$

$$
m(O_2) = 1.429 g/L * V(O_2) = ...g
$$

摩尔质量的计算

$$
{\displaystyle n={\frac {m}{M}}}
$$

$$
M(O_2) = 32 g/mol \\
M(葡萄糖) = 180.156 g/mol
$$

其中葡萄糖得到的能量为：

$$
unit_{energy} = 1161 kJ/mol = \frac{1161 * 1000 J / (4.184 J /calories)}{mol} = 277485.66 calories / mol
$$

最后算的总能量为
$$
\frac{m_d V_E t * \rho(O_2)}{M(O_2)} * M(葡萄糖) * unit_{energy}
$$

## 生长所需的能量

先算 $dm_d$，再算 $d_S$，再算 $E_g$。

$dm_d$ 根据现在的生长率和时间段长度（定为 2 天）得来：

$$
dm_d = \mu * period
$$

然后计算出 $dS$，需要用到这几个参数：

$$
\rho_m = 1.12 kg/m^3\\
\rho_b = 1.23 kg/m^3
$$

$r_b$ 与 $r_m$ 成比例，可以认为：

$$
r_b = 4k \\
r_m = 5k
$$

$$
E_p = 17130 kJ/kg\\
E_b = 0.2 Ep
$$

## 飞行所需的能量

$$
v_d = 5.70 m_d^{0.16}
$$

$$
E_f = m_d\frac{L_d}{v_d}E_v
$$

其中：

$$
E_v = 300 J/(kg \cdot h)
$$

## 喷火所需的能量

https://www.engineeringtoolbox.com/specific-heat-capacity-food-d_295.html

$$
c_p = 
$$

$$
牛肉：1.47 kJ/(kg \cdot 度)\\
羊肉：1.5
兔肉:1.63
$$

已经确定：

$$
T_p = 80\\
T_e = 25
$$

$$
l_c = 10 r_h
$$

## 计算所需的面积

