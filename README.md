# quant-journey

My 12-week python journey toward quantitative finance.

本仓库记录我从 Python 基础语法，到独立完成第一个因子回测的 12 周过程。
每个知识点对应一个 .py 文件，全部亲手敲过，不复制粘贴。

## 文件说明

| 文件 | 周次 | 内容 |
|---|---|---|
| `week01_def_practice.py` | 第 1 周 | 星座判断封装成函数（def、return、身份证日期切片） |
| `02_file_io.py` | 第 2 周 | 读 `ids.txt` 的身份证号，批量算星座并写入 `result.txt`（含异常处理） |
| `random练习.py` | 计划外 | random 库练习（randint / randrange / choice） |
| `ids.txt` | — | 第 2 周测试输入：10 个合法 + 1 个非法样本 |
| `result.txt` | — | 第 2 周输出，运行 `02_file_io.py` 生成 |

## 如何运行

需要 Python 3。在仓库根目录下执行：

```bash
python week01_def_practice.py   # 单条身份证号 → 星座
python 02_file_io.py            # 批量：ids.txt → result.txt
```

## 学习进度

- [x] **第 1 周**：def 函数、return 返回值、身份证日期切片
- [x] **第 2 周**：文件读写（open / with）、异常处理（try-except）
- [ ] **第 3 周**：成绩统计脚本（读 CSV → 总分与平均分 → 按平均分排名 → 写 CSV），截止 10/28

## TODO

- [x] `constellation()` 加日期**范围**校验（13 月、1 月 32 日等）—— 已完成
- [ ] `constellation()` 加日期**真实性**校验（2 月 29 日、4 月 31 日等），需 calendar 模块
- [ ] random 深化留到 numpy 阶段（第 6–8 周）

## 目录约定

练习文件放仓库根目录，命名 `weekNN_主题.py`，`weekNN_` 为周次前缀（`week01_def_practice.py`、`week02_file_io.py`、`week03_grade_stats.py` …）。

用 `week` 前缀而不是纯数字，是因为数字开头的文件名无法被 `import`，以后复用函数会报 SyntaxError。

计划外练习不占编号（如 `random练习.py`）。

## 关于

作者：erin_nn（GitHub: [Erin-nn](https://github.com/Erin-nn)）
