# quant-journey

My 12-week python journey toward quantitative finance.

本仓库记录我从 Python 基础语法，到独立完成第一个因子回测的 12 周过程。
每个知识点对应一个 .py 文件，全部亲手敲过，不复制粘贴。

## 文件说明

| 文件 | 周次 | 内容 |
|---|---|---|
| `week01_def_practice.py` | 第 1 周 | 星座判断封装成函数（def、return、身份证日期切片） |
| `week02_file_io.py` | 第 2 周 | 读 `ids.txt` 的身份证号，批量算星座并写入 `result.txt`（含异常处理） |
| `week03_grade_stats.py` | 第 3 周 | 成绩统计脚本：读 `grades.csv` → 算总分/平均分 → 按平均分排名 → 写 `grades_result.csv` |
| `week03_list_practice.py` | 第 3 周 | 列表操作七项练习（索引与切片、`len`、`append`/推导式、`sum`、平均分、排序、字符串排序陷阱） |
| `random练习.py` | 计划外 | random 库练习（randint / randrange / choice） |
| `ids.txt` | — | 第 2 周测试输入：11 条合法 + 2 条非法（长度不足、日期越界） |
| `result.txt` | — | 第 2 周输出，运行 `week02_file_io.py` 生成（生成物，已 gitignore） |
| `grades.csv` | — | 第 3 周测试输入：3 名学生 × 3 门科目 |
| `grades_result.csv` | — | 第 3 周输出，运行 `week03_grade_stats.py` 生成（生成物，已 gitignore） |

## 如何运行

需要 Python 3。在仓库根目录下执行：

```bash
python week01_def_practice.py   # 单条身份证号 → 星座
python week02_file_io.py        # 批量：ids.txt → result.txt
python week03_grade_stats.py    # 成绩统计：grades.csv → grades_result.csv
```

## 学习进度

- [x] **第 1 周**：def 函数、return 返回值、身份证日期切片
- [x] **第 2 周**：文件读写（open / with）、异常处理（try-except）
- [x] **第 3 周**：成绩统计脚本（读 CSV → 总分与平均分 → 按平均分排名 → 写 CSV）—— 10/28 完成
  - [x] Ch6 6.2 列表：索引与切片、`len`、`append` 与列表推导式、`sum` 与类型转换、平均分 `round`
  - [x] Ch6 6.2 排序：元组列表 + `reverse=True`；多级排序 `key=lambda x: (x[0], -x[1])`
  - [x] Ch6 6.3 实例9 基本统计值计算（阅读）
  - [x] Ch6 6.4 字典类型和操作（阅读；字典练习从简，正式脚本用列表即可）
  - [x] Ch7 7.4 / 7.5 CSV 读写（`csv.reader` / `csv.writer`，含表头分离与 `newline=""`）
  - [x] 正式脚本：`grades.csv` → 排名 → `grades_result.csv`

## TODO

- [x] `constellation()` 加日期**范围**校验（13 月、1 月 32 日等）—— 已完成
- [ ] `constellation()` 加日期**真实性**校验（2 月 29 日、4 月 31 日等），需 calendar 模块
- [ ] random 深化留到 numpy 阶段（第 6–8 周）
- [x] 生成 `grades_result.csv` 后，将其加入 `.gitignore`（生成物不提交）—— 已完成

## 五个易错点备忘

1. **列表的 `+=` 是 `extend` 不是 `append`** —— `names += "张三"` 会把字符串拆成 `['张','三']`，必须用 `append()` 或 `+= ["张三"]`。
2. **二维列表两层索引** —— 第一个方括号选「行」，第二个选「字段」。表头只影响**行索引**，列索引 `0` 永远是第一列。`rows[0][1:]` 是第一个人的三科成绩，`rows[1:4]` 是第 2 行到末尾的所有行。
3. **字符串排序按字典序** —— `sorted(["92","88","100"])` 得到 `['100','88','92']`。任何比较、求和、排序前必须先 `int()`。
4. **容器与临时变量要起明显不同的名字** —— `scored` 与 `scores` 只差一个字母，极易看错并导致打印错变量。累积用 `ranking` / `result`，单轮临时用 `scores` / `row`。另外 `list.sort()` 原地修改并返回 `None`，写成 `x = x.sort()` 会把列表冲成 `None`。
5. **结果行以姓名开头时，排序必须用 `key`** —— `result.sort(reverse=True)` 会按姓名字典序排，不报错但结果错。须写 `key=lambda x: x[-1]`。

## 目录约定

练习文件放仓库根目录，命名 `weekNN_主题.py`，`weekNN_` 为周次前缀（`week01_def_practice.py`、`week02_file_io.py`、`week03_grade_stats.py` …）。

用 `week` 前缀而不是纯数字，是因为数字开头的文件名无法被 `import`，以后复用函数会报 SyntaxError。

计划外练习不占编号（如 `random练习.py`）。

**输入提交，输出忽略**：`ids.txt`、`grades.csv` 是输入，要提交；`result.txt`、`grades_result.csv` 是程序产物，已 gitignore。

## 关于

作者：erin_nn（GitHub: [Erin-nn](https://github.com/Erin-nn)）
