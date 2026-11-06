# quant-journey

My 12-week python journey toward quantitative finance.

本仓库记录我从 Python 基础语法，到独立完成第一个因子回测的 12 周过程。
每个知识点对应一个 .py 文件，全部亲手敲过，不复制粘贴。

## 文件说明

| 文件 | 周次 | 内容 |
|---|---|---|
| `week01_def_practice.py` | 第 1 周 | 星座判断封装成函数（def、return、身份证日期切片、日期真实性校验） |
| `week02_file_io.py` | 第 2 周 | 读 `ids.txt` 的身份证号，批量算星座并写入 `result.txt`（`try / except / else` 三段式异常处理） |
| `week03_grade_stats.py` | 第 3 周 | 成绩统计脚本：读 `grades.csv` → 算总分/平均分 → 按平均分排名 → 写 `grades_result.csv` |
| `week03_list_practice.py` | 第 3 周 | 列表操作七项练习（索引与切片、`len`、`append`/推导式、`sum`、平均分、排序、字符串排序陷阱） |
| `week04_numpy_mc.py` | 第 4 周 | NumPy 入门：数组创建（`np.array` / 数据 vs 形状）、四个属性、dtype 提升、`reshape`、逗号索引、视图 vs 拷贝、布尔索引、花式索引、转置 `.T`、ufunc（`sqrt`/`log1p`/`maximum`）、`np.where` |
| `week04_numpy_random.py` | 第 4 周 | 伪随机数（第 2 版 Ch4.6）：`RandomState` 的可重复性（同种子同结果）、`random_sample`/`randint`/`normal`/`choice`/`permutation`、`mean`/`std` 与年化、蒙特卡洛估 π |
| `random练习.py` | 计划外 | random 库练习（randint / randrange / choice） |
| `ids.txt` | — | 第 2 周测试输入：11 条合法 + 2 条非法（长度不足、日期越界） |
| `result.txt` | — | 第 2 周输出，运行 `week02_file_io.py` 生成（生成物，已 gitignore） |
| `grades.csv` | — | 第 3 周测试输入：10 名学生 × 3 门科目（含 92.5 这类小数成绩） |
| `grades_result.csv` | — | 第 3 周输出，运行 `week03_grade_stats.py` 生成（生成物，已 gitignore） |

## 如何运行

第 1–3 周只用标准库，任意 Python 3 都能跑。**第 4 周起依赖 numpy**，必须用仓库内的虚拟环境 `.venv`（已 gitignore，不随仓库分发，克隆后需自建）。

方式一：先激活，再跑（推荐，之后的 `pip install` 也会装进这里）

```bash
cd quant-journey
source .venv/bin/activate
python week04_numpy_mc.py
```

方式二：不激活，直接用环境里的解释器

```bash
.venv/bin/python week04_numpy_mc.py
```

各脚本用途：

```bash
python week01_def_practice.py   # 单条身份证号 → 星座
python week02_file_io.py        # 批量：ids.txt → result.txt
python week03_grade_stats.py    # 成绩统计：grades.csv → grades_result.csv
python week04_numpy_mc.py       # NumPy 数组创建与属性（末行故意报错，属预期）
python week04_numpy_random.py   # 伪随机数：可重复性、分布抽样、蒙特卡洛估 π
```

克隆后重建环境（一次性）：

```bash
python3 -m venv .venv
.venv/bin/python -m pip install numpy pandas matplotlib -i https://pypi.tuna.tsinghua.edu.cn/simple
```

## 学习进度

- [x] **第 1 周**：def 函数、return 返回值、身份证日期切片、日期合法性校验（`datetime.date`）
- [x] **第 2 周**：文件读写（`with open`）、异常处理（`try / except / else`）
- [x] **第 3 周**：成绩统计脚本（读 CSV → 总分与平均分 → 按平均分排名 → 写 CSV）—— 10/28 完成，10/29 补充小数成绩支持并扩至 10 人
  - [x] Ch6 6.2 列表：索引与切片、`len`、`append` 与列表推导式、`sum` 与类型转换、平均分 `round`
  - [x] Ch6 6.2 排序：元组列表 + `reverse=True`；多级排序 `key=lambda x: (x[0], -x[1])`
  - [x] Ch6 6.3 实例9 基本统计值计算（阅读）
  - [x] Ch6 6.4 字典类型和操作（阅读；字典练习从简，正式脚本用列表即可）
  - [x] Ch7 7.4 / 7.5 CSV 读写（`csv.reader` / `csv.writer`，含表头分离与 `newline=""`）
  - [x] 正式脚本：`grades.csv` → 排名 → `grades_result.csv`

> 第 4 周起换教材：改用 Wes McKinney《Python for Data Analysis》**第 2 版**（中文在线版 `wizardforcel.gitbooks.io/pyda-2e`，章号体系与前面的嵩天教材不同，以下一律标该书第 2 版章号）。注意第 2 版与第 3 版的 Ch4 小节编号不同：第 3 版把伪随机数从 4.6 提前到 4.2，并与 ufunc 对调。**进 Ch5（pandas）前换第 3 版**，因为第 2 版对应 pandas 0.20，`df.append`、`.ix` 在本机 pandas 3.1.0 已不存在。

- [ ] **第 4 周（进行中）**：NumPy 基础（Ch4，第 2 版编号）
  - [x] 4.1 数组创建：`np.array` 吃**数据**不吃形状；`zeros`/`ones`/`arange`/`eye` 才吃形状
  - [x] 4.1 四个属性：`shape` / `ndim` / `size` / `dtype`
  - [x] 4.1 dtype 提升：`[6, 7.5, 8, 0, 1]` 中有一个浮点，整体升为 `float64`；`zeros` 默认也是 `float64`
  - [x] 4.1 `reshape`：返回新数组、不原地改；`(6,) → (4,2)` 抛 `ValueError: cannot reshape`
  - [x] 4.1 索引与切片：`a[1:4]` / `[::-1]` / `[::2]`；二维逗号索引 `b[1]`（整行）/ `b[:, 1]`（整列）/ `b[0:2, 1:3]`
  - [x] 4.1 视图与拷贝：基本切片共享内存（改切片原数组跟着变），`.copy()` 断开；布尔索引返回拷贝
  - [x] 4.1 布尔索引：`r[r > 0]` 取值、`m[m < 0] = 0` 掩码赋值
  - [x] 4.1 花式索引：`a[[0, 2]]` 选不连续位置、可乱序、可重复；**返回拷贝**（`shares_memory` = False）
  - [x] 4.1 转置 `.T`：2×3 → 3×2，是**视图**（改 `c.T` 原数组跟着变）；一维数组 `.T` 无效，形状不变（轴对换 `swapaxes` 仅认识，量化用不到）
  - [x] 4.2 通用函数：`np.sqrt`（负数 → `nan` + RuntimeWarning）、`np.maximum`（逐元素截断，区别于聚合的 `np.max`）、`np.abs`；`np.log1p(x)` ≡ `ln(1+x)`，x 在 1e-16 量级时 `log(1+x)` 归零而 `log1p` 正确
  - [x] 4.3 将条件逻辑表述为数组运算：`np.where(ret > 0, 1, -1)`；单参数返回**元组** `(array([0, 3]),)`；非短路——两分支先完整求值再挑选，故 `1/ret` 仍触发除零 Warning
  - [x] 4.6 伪随机数生成：`RandomState(seed)` 可重复（同种子同结果，`np.array_equal` 验证）、`random_sample`/`randint`/`normal`/`choice`/`permutation`；`mean`/`std` 与年化（收益 ×252、波动 ×√252）；蒙特卡洛估 π（`4 × inside.mean()`）
  - [ ] 4.3 数学和统计方法（`mean`/`std`/`cumsum`/`cumprod` 等，`cumsum` 待补）
  - [ ] 4.4 用于数组的文件输入输出（`np.save`/`np.load`/`np.loadtxt`）
  - [ ] 4.5 线性代数（`np.dot`/`inv`/`solve`/`svd`）
  - [ ] 4.7 示例：随机漫步（依赖 `cumsum`）

## 异常处理的三条实践原则

教材只讲语法，这三条是踩坑之后总结的：

1. **优先捕获具体类型，不要用 `except Exception` 一把兜**。宽捕获会把「代码里的 bug」伪装成「数据有问题」——实测：`int(x) / 0` 抛 `ZeroDivisionError`，窄捕获让它穿透、立刻暴露 bug；宽捕获返回「输入不是数字」，把 bug 藏起来。
2. **一个 `try` 只放「逻辑上不可分割的一步」**。判断标准：这几句是否要么全成功、要么全失败；失败后我是否知道下一步做什么；`try` 里有没有不会抛目标异常的语句。
3. **成功路径放 `else`，不要堆在 `try` 末尾**。`else` 只在 `try` 未抛异常时执行，这样 `try` 里只剩真正可能出错的那一句，定位零成本。

`week02_file_io.py` 就是这三条的应用：长度校验用 `if ... continue` 提前拦掉（不依赖异常），`try` 里只有 `con = constellation(sid)` 一句，成功走 `else`，失败走 `except`。

## TODO

- [x] `constellation()` 加日期**范围**校验（13 月、1 月 32 日等）—— 已完成
- [x] `constellation()` 加日期**真实性**校验（2 月 29 日、4 月 31 日等）—— 已完成，实际用 `datetime.date(year, month, day)`，比 calendar 更简洁
- [ ] random 深化留到 numpy 阶段（第 6–8 周）
- [x] 生成 `grades_result.csv` 后，将其加入 `.gitignore`（生成物不提交）—— 已完成
- [ ] `week03_grade_stats.py` 加字段数校验（`len(r) != len(header)` 时跳过该行），防止 CSV 缺列导致整行静默错位

## 七个易错点备忘

1. **列表的 `+=` 是 `extend` 不是 `append`** —— `names += "张三"` 会把字符串拆成 `['张','三']`，必须用 `append()` 或 `+= ["张三"]`。
2. **二维列表两层索引** —— 第一个方括号选「行」，第二个选「字段」。表头只影响**行索引**，列索引 `0` 永远是第一列。`rows[0][1:]` 是第一个人的三科成绩，`rows[1:4]` 是第 2 行到末尾的所有行。
3. **字符串排序按字典序** —— `sorted(["92","88","100"])` 得到 `['100','88','92']`。任何比较、求和、排序前必须先 `int()` 或 `float()`。
4. **容器与临时变量要起明显不同的名字** —— `scored` 与 `scores` 只差一个字母，极易看错并导致打印错变量。累积用 `ranking` / `result`，单轮临时用 `scores` / `row`。另外 `list.sort()` 原地修改并返回 `None`，写成 `x = x.sort()` 会把列表冲成 `None`。
5. **结果行以姓名开头时，排序必须用 `key`** —— `result.sort(reverse=True)` 会按姓名字典序排，不报错但结果错。须写 `key=lambda x: x[-1]`。
6. **`TypeError` 与 `ValueError` 是并列类型，互不继承** —— `except ValueError` 抓不到 `TypeError`（如参数个数不对、类型不匹配），会导致程序直接崩溃。调用库函数前先确认参数个数：`datetime.date` 需要 3 个参数 `(year, month, day)`。
7. **CSV 少一列会导致整行静默错位** —— `csv.writer` 不做列数校验，某行字段数比表头少时，该行后续列全部左移，不报错。读 CSV 后应先校验 `len(r) == len(header)`。

## NumPy 的十二条易错点（第 4 周）

1. **`np.array()` 的参数是数据，不是形状** —— `np.array((2, 3))` 得到一维 `[2 3]`，不是 2×3 矩阵。要 2×3 得传嵌套列表 `np.array([[1,2,3],[4,5,6]])`；只有 `zeros`/`ones`/`empty`/`random.randn` 才接收形状元组。
2. **`reshape` 返回新数组，不修改原数组** —— `a.reshape(2,3)` 单独一行等于空转，必须 `print(...)` 或赋值接住。注意方向相反的例子：列表的 `.sort()` 原地改并返回 `None`，numpy 的 `.sort()` 原地改、`np.sort()` 返回副本，两套语义不要混。
3. **0 维 ≠ 1 维** —— `np.array(10)` 是 0 维标量数组，打印为 `10`（无方括号）；`np.array([10])` 才是长度为 1 的一维数组，打印为 `[10]`。
4. **不要用内置名当变量名** —— `list = np.array(10)` 之后，内置 `list` 类型被覆盖，后续 `list(...)` 全部失效。同理别用 `sum`、`max`、`dict`、`id`、`type`。
5. **三类索引的「视图 / 拷贝」语义不同，必须分开记** —— `np.shares_memory` 实测：

   | 写法 | 返回 | 改它会不会动原数组 |
   |---|---|---|
   | `a[1:4]` 基本切片 | 视图 | **会** |
   | `a[a > 5]` 布尔索引 | 拷贝 | 不会 |
   | `a[[0, 2]]` 花式索引 | 拷贝 | 不会 |

   要断开视图一律 `.copy()`。`.T` 也是视图，属同一类问题。

6. **取整列会降维，`(3,)` 不是 `(3, 1)`** —— `b[:, 1]` 形状是 `(3,)`（1 维，长度 3），`b[:, 1:2]` 才是 `(3, 1)`（2 维，3 行 1 列）。后果实测：`(3,1) + (3,)` 会广播成 `(3, 3)` 矩阵，本来只想加一列却得到一个外积表。要保持二维身份就用切片 `b[:, 1:2]`。

7. **ufunc 对非法输入返回 `nan`，只发 Warning 不抛异常** —— `np.sqrt(-1)` → `nan` + `RuntimeWarning: invalid value encountered in sqrt`；`np.log(0)` → `-inf`（除以零 Warning）、`np.log(-1)` → `nan`。`try/except` 抓不到任何东西，程序继续跑，结果被 `nan`/`-inf` 污染（求均值、排序、净值曲线全崩）。**唯一有效的防线是不让非法值进数组。**

8. **`np.where` 不是 `if`，两个分支都会先算完** —— `np.where(ret != 0, 1/ret, 0)` 里 `1/ret` 会先对整个数组求值（含 0），所以结果虽对，`RuntimeWarning: divide by zero` 照样出。要真防除零，必须先把分母的 0 换掉。另：单参数 `np.where(cond)` 返回**元组** `(array([...]),)`，不是数组，一维取下标要写 `[0]`。

9. **`log1p(x)` 是 `ln(1+x)`，不是 `ln(x)`** —— 比较两种算法必须写成 `np.log(1 + x)` vs `np.log1p(x)`。实测 x=1e-16 时：`np.log(1 + 1e-16)` = `0.0`（`1+1e-16` 被舍入成 `1.0`），`np.log1p(1e-16)` = `1e-16`，相对误差 100%。x=0.05 这种常规量级两者只差在第 16 位小数，看不出差别。

10. **生成器和抽样结果必须是两个变量** —— `rng = np.random.RandomState(42).normal(0, 0.01, 1000)` 之后 `rng` 已经是**数组**，再写 `rng.randint(...)` 报 `'numpy.ndarray' object has no attribute 'randint'`。正确写法：`rng = np.random.RandomState(42)` 留作生成器，`returns = rng.normal(...)` 存结果。这是「变量名被复用去装别的东西」的第三次（前两次：`list = np.array(10)`、`rng1` 装数组）。

11. **同一个生成器连续抽样，结果必然不同（状态会推进）** —— 想复现书上/参考的输出，必须**新建**生成器从初始状态出发。实测 `RandomState(0)`：直接 `randint` 得 `[44 47 64 67 67 …]`，先抽过 1000 个 normal 再 `randint` 得 `[96 38 31 22 91 …]`。种子只决定起点，不决定第几次调用。

12. **numpy 和 pandas 的 `std()` 分母不同** —— numpy 默认除以 `n`（总体标准差），pandas 默认除以 `n-1`（样本标准差，`ddof=1`）。实测同一组 5 个数：`np.std` = 0.027276，`pd.Series.std()` = 0.030496，差 12%。numpy 要样本标准差写 `std(ddof=1)`。

## 目录约定

练习文件放仓库根目录，命名 `weekNN_主题.py`，`weekNN_` 为周次前缀（`week01_def_practice.py`、`week02_file_io.py`、`week03_grade_stats.py` …）。

用 `week` 前缀而不是纯数字，是因为数字开头的文件名无法被 `import`，以后复用函数会报 SyntaxError。

计划外练习不占编号（如 `random练习.py`）。

**输入提交，输出忽略**：`ids.txt`、`grades.csv` 是输入，要提交；`result.txt`、`grades_result.csv` 是程序产物，已 gitignore。

## 关于

作者：erin_nn（GitHub: [Erin-nn](https://github.com/Erin-nn)）
