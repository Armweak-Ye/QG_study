# Pandas 数据结构 - Series

Series 是 Pandas 中的一个核心数据结构，类似于一个一维的数组，具有数据和索引。

Series 可以存储任何数据类型（整数、浮点数、字符串等），并通过标签（索引）来访问元素。

Series 的数据结构是非常有用的，因为它可以处理各种数据类型，同时保持了高效的数据操作能力，比如可以通过标签来快速访问和操作数据。

**Series 特点：**

- **一维数组：**Series 中的每个元素都有一个对应的索引值。
- **索引：** 每个数据元素都可以通过标签（索引）来访问，默认情况下索引是从 0 开始的整数，但你也可以自定义索引。
- **数据类型：** `Series` 可以容纳不同数据类型的元素，包括整数、浮点数、字符串、Python 对象等。
- **大小不变性：**Series 的大小在创建后是不变的，但可以通过某些操作（如 append 或 delete）来改变。
- **操作：**Series 支持各种操作，如数学运算、统计分析、字符串处理等。
- **缺失数据：**Series 可以包含缺失数据，Pandas 使用NaN（Not a Number）来表示缺失或无值。
- **自动对齐：**当对多个 Series 进行运算时，Pandas 会自动根据索引对齐数据，这使得数据处理更加高效。

我们可以使用 Pandas 库来创建一个 Series 对象，并且可以为其指定索引（Index）、名称（Name）以及值（Values）：

![img](https://www.runoob.com/wp-content/uploads/2021/04/1_fgFKkClAfRMEsUtJvDtXAQ.png)

```python
import pandas as pd

# 创建一个Series对象，指定名称为'A'，值分别为1, 2, 3, 4
# 默认索引为0, 1, 2, 3
series = pd.Series([1, 2, 3, 4], name='A')

# 显示Series对象
print(series)

# 如果你想要显式地设置索引，可以这样做：
custom_index = [1, 2, 3, 4]  # 自定义索引
series_with_index = pd.Series([1, 2, 3, 4], index=custom_index, name='A')

# 显示带有自定义索引的Series对象
print(series_with_index)

'''
0    1
1    2
2    3
3    4
Name: A, dtype: int64
1    1
2    2
3    3
4    4
Name: A, dtype: int64
'''
```

# 创建Series

可以使用 pd.Series() 构造函数创建一个 Series 对象，传递一个数据数组（可以是列表、NumPy 数组等）和一个可选的索引数组。

```
pandas.Series(data=None, index=None, dtype=None, name=None, copy=False, fastpath=False)
```

参数说明：

- `data`：Series 的数据部分，可以是列表、数组、字典、标量值等。如果不提供此参数，则创建一个空的 Series。
- `index`：Series 的索引部分，用于对数据进行标记。可以是列表、数组、索引对象等。如果不提供此参数，则创建一个默认的整数索引。
- `dtype`：指定 Series 的数据类型。可以是 NumPy 的数据类型，例如 `np.int64`、`np.float64` 等。如果不提供此参数，则根据数据自动推断数据类型。
- `name`：Series 的名称，用于标识 Series 对象。如果提供了此参数，则创建的 Series 对象将具有指定的名称。
- `copy`：是否复制数据。默认为 False，表示不复制数据。如果设置为 True，则复制输入的数据。
- `fastpath`：是否启用快速路径。默认为 False。启用快速路径可能会在某些情况下提高性能。

# Series 方法

下面是 Series 中一些常用的方法：

| **方法名称**                 | **功能描述**                                           |
| :--------------------------- | :----------------------------------------------------- |
| `index`                      | 获取 Series 的索引                                     |
| `values`                     | 获取 Series 的数据部分（返回 NumPy 数组）              |
| `head(n)`                    | 返回 Series 的前 n 行（默认为 5）                      |
| `tail(n)`                    | 返回 Series 的后 n 行（默认为 5）                      |
| `dtype`                      | 返回 Series 中数据的类型                               |
| `shape`                      | 返回 Series 的形状（行数）                             |
| `describe()`                 | 返回 Series 的统计描述（如均值、标准差、最小值等）     |
| `isnull()`                   | 返回一个布尔 Series，表示每个元素是否为 NaN            |
| `notnull()`                  | 返回一个布尔 Series，表示每个元素是否不是 NaN          |
| `unique()`                   | 返回 Series 中的唯一值（去重）                         |
| `value_counts()`             | 返回 Series 中每个唯一值的出现次数                     |
| `map(func)`                  | 将指定函数应用于 Series 中的每个元素                   |
| `apply(func)`                | 将指定函数应用于 Series 中的每个元素，常用于自定义操作 |
| `astype(dtype)`              | 将 Series 转换为指定的类型                             |
| `sort_values()`              | 对 Series 中的元素进行排序（按值排序）                 |
| `sort_index()`               | 对 Series 的索引进行排序                               |
| `dropna()`                   | 删除 Series 中的缺失值（NaN）                          |
| `fillna(value)`              | 填充 Series 中的缺失值（NaN）                          |
| `replace(to_replace, value)` | 替换 Series 中指定的值                                 |
| `cumsum()`                   | 返回 Series 的累计求和                                 |
| `cumprod()`                  | 返回 Series 的累计乘积                                 |
| `shift(periods)`             | 将 Series 中的元素按指定的步数进行位移                 |
| `rank()`                     | 返回 Series 中元素的排名                               |
| `corr(other)`                | 计算 Series 与另一个 Series 的相关性（皮尔逊相关系数） |
| `cov(other)`                 | 计算 Series 与另一个 Series 的协方差                   |
| `to_list()`                  | 将 Series 转换为 Python 列表                           |
| `to_frame()`                 | 将 Series 转换为 DataFrame                             |
| `iloc[]`                     | 通过位置索引来选择数据                                 |
| `loc[]`                      | 通过标签索引来选择数据                                 |

# Pandas 数据结构 - DataFrame

DataFrame 是 Pandas 中的另一个核心数据结构，类似于一个二维的表格或数据库中的数据表。

DataFrame 是一个表格型的数据结构，它含有一组有序的列，每列可以是不同的值类型（数值、字符串、布尔型值）。

DataFrame 既有行索引也有列索引，它可以被看做由 Series 组成的字典（共同用一个索引）。

DataFrame 提供了各种功能来进行数据访问、筛选、分割、合并、重塑、聚合以及转换等操作。

DataFrame 是一个非常灵活且强大的数据结构，广泛用于数据分析、清洗、转换、可视化等任务。

**DataFrame 特点：**

- **二维结构：** `DataFrame` 是一个二维表格，可以被看作是一个 Excel 电子表格或 SQL 表，具有行和列。可以将其视为多个 `Series` 对象组成的字典。
- **列的数据类型：** 不同的列可以包含不同的数据类型，例如整数、浮点数、字符串或 Python 对象等。
- **索引**：`DataFrame` 可以拥有行索引和列索引，类似于 Excel 中的行号和列标。
- **大小可变**：可以添加和删除列，类似于 Python 中的字典。
- **自动对齐**：在进行算术运算或数据对齐操作时，`DataFrame` 会自动对齐索引。
- **处理缺失数据**：`DataFrame` 可以包含缺失数据，Pandas 使用 `NaN`（Not a Number）来表示。
- **数据操作**：支持数据切片、索引、子集分割等操作。
- **时间序列支持**：`DataFrame` 对时间序列数据有特别的支持，可以轻松地进行时间数据的切片、索引和操作。
- **丰富的数据访问功能**：通过 `.loc`、`.iloc` 和 `.query()` 方法，可以灵活地访问和筛选数据。
- **灵活的数据处理功能**：包括数据合并、重塑、透视、分组和聚合等。
- **数据可视化**：虽然 `DataFrame` 本身不是可视化工具，但它可以与 Matplotlib 或 Seaborn 等可视化库结合使用，进行数据可视化。
- **高效的数据输入输出**：可以方便地读取和写入数据，支持多种格式，如 CSV、Excel、SQL 数据库和 HDF5 格式。
- **描述性统计**：提供了一系列方法来计算描述性统计数据，如 `.describe()`、`.mean()`、`.sum()` 等。
- **灵活的数据对齐和集成**：可以轻松地与其他 `DataFrame` 或 `Series` 对象进行合并、连接或更新操作。
- **转换功能**：可以对数据集中的值进行转换，例如使用 `.apply()` 方法应用自定义函数。
- **滚动窗口和时间序列分析**：支持对数据集进行滚动窗口统计和时间序列分析。

![img](https://www.runoob.com/wp-content/uploads/2021/04/pandas-DataStructure.png)

![img](https://www.runoob.com/wp-content/uploads/2021/04/df-dp.png)

```python
pandas.DataFrame(data=None, index=None, columns=None, dtype=None, copy=False)
```

参数说明：

- `data`：DataFrame 的数据部分，可以是字典、二维数组、Series、DataFrame 或其他可转换为 DataFrame 的对象。如果不提供此参数，则创建一个空的 DataFrame。
- `index`：DataFrame 的行索引，用于标识每行数据。可以是列表、数组、索引对象等。如果不提供此参数，则创建一个默认的整数索引。
- `columns`：DataFrame 的列索引，用于标识每列数据。可以是列表、数组、索引对象等。如果不提供此参数，则创建一个默认的整数索引。
- `dtype`：指定 DataFrame 的数据类型。可以是 NumPy 的数据类型，例如 `np.int64`、`np.float64` 等。如果不提供此参数，则根据数据自动推断数据类型。
- `copy`：是否复制数据。默认为 False，表示不复制数据。如果设置为 True，则复制输入的数据。

**使用列表创建**

```python
import pandas as pd

data = [['Google', 10], ['Runoob', 12], ['Wiki', 13]]

# 创建DataFrame
df = pd.DataFrame(data, columns=['Site', 'Age'])

# 使用astype方法设置每列的数据类型
df['Site'] = df['Site'].astype(str)
df['Age'] = df['Age'].astype(float)

print(df)
```

**使用字典创建**

```python
import pandas as pd

data = {'Site':['Google', 'Runoob', 'Wiki'], 'Age':[10, 12, 13]}

df = pd.DataFrame(data)

print (df)
```

Pandas 可以使用 **loc** 属性返回指定行的数据，如果没有设置索引，第一行索引为 **0**，第二行索引为 **1**，以此类推：

```python
import pandas as pd

data = {
 "calories": [420, 380, 390],
 "duration": [50, 40, 45]
}

# 数据载入到 DataFrame 对象
df = pd.DataFrame(data)

# 返回第一行
print(df.loc[0])
# 返回第二行
print(df.loc[1])
```

输出结果如下：

```
calories    420
duration     50
Name: 0, dtype: int64
calories    380
duration     40
Name: 1, dtype: int64
```

**注意：**返回结果其实就是一个 Pandas Series 数据。

也可以返回多行数据，使用 **[[ ... ]]** 格式，**...** 为各行的索引，以逗号隔开：

```python
import pandas as pd

data = {
 "calories": [420, 380, 390],
 "duration": [50, 40, 45]
}

# 数据载入到 DataFrame 对象
df = pd.DataFrame(data)

# 返回第一行和第二行
**print**(df.loc[[0, 1]])
```

输出结果为：

```
   calories  duration
0       420        50
1       380        40
```

**注意：**返回结果其实就是一个 Pandas DataFrame 数据。

# DataFrame 方法

DataFrame 的常用操作和方法如下表所示：

| **方法名称**        | **功能描述**                                                |
| :------------------ | :---------------------------------------------------------- |
| `head(n)`           | 返回 DataFrame 的前 n 行数据（默认前 5 行）                 |
| `tail(n)`           | 返回 DataFrame 的后 n 行数据（默认后 5 行）                 |
| `info()`            | 显示 DataFrame 的简要信息，包括列名、数据类型、非空值数量等 |
| `describe()`        | 返回 DataFrame 数值列的统计信息，如均值、标准差、最小值等   |
| `shape`             | 返回 DataFrame 的行数和列数（行数, 列数）                   |
| `columns`           | 返回 DataFrame 的所有列名                                   |
| `index`             | 返回 DataFrame 的行索引                                     |
| `dtypes`            | 返回每一列的数值数据类型                                    |
| `sort_values(by)`   | 按照指定列排序                                              |
| `sort_index()`      | 按行索引排序                                                |
| `dropna()`          | 删除含有缺失值（NaN）的行或列                               |
| `fillna(value)`     | 用指定的值填充缺失值                                        |
| `isnull()`          | 判断缺失值，返回一个布尔值 DataFrame                        |
| `notnull()`         | 判断非缺失值，返回一个布尔值 DataFrame                      |
| `loc[]`             | 按标签索引选择数据                                          |
| `iloc[]`            | 按位置索引选择数据                                          |
| `at[]`              | 访问 DataFrame 中单个元素（比 `loc[]` 更高效）              |
| `iat[]`             | 访问 DataFrame 中单个元素（比 `iloc[]` 更高效）             |
| `apply(func)`       | 对 DataFrame 或 Series 应用一个函数                         |
| `applymap(func)`    | 对 DataFrame 的每个元素应用函数（仅对 DataFrame）           |
| `groupby(by)`       | 分组操作，用于按某一列分组进行汇总统计                      |
| `pivot_table()`     | 创建透视表                                                  |
| `merge()`           | 合并多个 DataFrame（类似 SQL 的 JOIN 操作）                 |
| `concat()`          | 按行或按列连接多个 DataFrame                                |
| `to_csv()`          | 将 DataFrame 导出为 CSV 文件                                |
| `to_excel()`        | 将 DataFrame 导出为 Excel 文件                              |
| `to_json()`         | 将 DataFrame 导出为 JSON 格式                               |
| `to_sql()`          | 将 DataFrame 导出为 SQL 数据库                              |
| `query()`           | 使用 SQL 风格的语法查询 DataFrame                           |
| `duplicated()`      | 返回布尔值 DataFrame，指示每行是否是重复的                  |
| `drop_duplicates()` | 删除重复的行                                                |
| `set_index()`       | 设置 DataFrame 的索引                                       |
| `reset_index()`     | 重置 DataFrame 的索引                                       |
| `transpose()`       | 转置 DataFrame（行列交换）                                  |

# CSV文件

### pd.read_csv() - 读取 CSV 文件

read_csv() 是从 CSV 文件中读取数据的主要方法，将数据加载为一个 DataFrame。

```python
import pandas as pd

# 读取 CSV 文件，并自定义列名和分隔符
df = pd.read_csv('data.csv', sep=';', header=0, names=['A', 'B', 'C'], dtype={'A': int, 'B': float})
print(df)
```

read_csv 常用参数:

| **参数**             | **说明**                                                     | **默认值** |
| :------------------- | :----------------------------------------------------------- | :--------- |
| `filepath_or_buffer` | CSV 文件的路径或文件对象（支持 URL、文件路径、文件对象等）   | 必需参数   |
| `sep`                | 定义字段分隔符，默认是逗号（`,`），可以改为其他字符，如制表符（`\t`） | `','`      |
| `header`             | 指定行号作为列标题，默认为 0（表示第一行），或者设置为 `None` 没有标题 | `0`        |
| `names`              | 自定义列名，传入列名列表                                     | `None`     |
| `index_col`          | 用作行索引的列的列号或列名                                   | `None`     |
| `usecols`            | 读取指定的列，可以是列的名称或列的索引                       | `None`     |
| `dtype`              | 强制将列转换为指定的数据类型                                 | `None`     |
| `skiprows`           | 跳过文件开头的指定行数，或者传入一个行号的列表               | `None`     |
| `nrows`              | 读取前 N 行数据                                              | `None`     |
| `na_values`          | 指定哪些值应视为缺失值（NaN）                                | `None`     |
| `skipfooter`         | 跳过文件结尾的指定行数                                       | `0`        |
| `encoding`           | 文件的编码格式（如 `utf-8`，`latin1` 等）                    | `None`     |

## df.to_csv() - 将 DataFrame 写入 CSV 文件

to_csv() 是将 DataFrame 写入 CSV 文件的方法，支持自定义分隔符、列名、是否包含索引等设置。

```
import pandas as pd

# 假设 df 是一个已有的 DataFrame
df.to_csv('output.csv', index=False, header=True, columns=['A', 'B'])
```

to_csv 常用参数:

| **参数**          | **说明**                                                     | **默认值** |
| :---------------- | :----------------------------------------------------------- | :--------- |
| `path_or_buffer`  | CSV 文件的路径或文件对象（支持文件路径、文件对象）           | 必需参数   |
| `sep`             | 定义字段分隔符，默认是逗号（`,`），可以改为其他字符，如制表符（`\t`） | `','`      |
| `index`           | 是否写入行索引，默认 `True` 表示写入索引                     | `True`     |
| `columns`         | 指定写入的列，可以是列的名称列表                             | `None`     |
| `header`          | 是否写入列名，默认 `True` 表示写入列名，设置为 `False` 表示不写列名 | `True`     |
| `mode`            | 写入文件的模式，默认是 `w`（写模式），可以设置为 `a`（追加模式） | `'w'`      |
| `encoding`        | 文件的编码格式，如 `utf-8`，`latin1` 等                      | `None`     |
| `line_terminator` | 定义行结束符，默认为 `\n`                                    | `None`     |
| `quoting`         | 设置如何对文件中的数据进行引号处理（0-3，具体引用方式可查文档） | `None`     |
| `quotechar`       | 设置用于引用的字符，默认为双引号 `"`                         | `'"'`      |
| `date_format`     | 自定义日期格式，如果列包含日期数据，则可以使用此参数指定日期格式 | `None`     |
| `doublequote`     | 如果为 `True`，则在写入时会将包含引号的文本使用双引号括起来  | `True`     |

# Pandas 数据清洗

数据清洗是对一些没有用的数据进行处理的过程。

很多数据集存在数据缺失、数据格式错误、错误数据或重复数据的情况，如果要使数据分析更加准确，就需要对这些没有用的数据进行处理。

数据清洗与预处理的常见步骤：

1. **缺失值处理**：识别并填补缺失值，或删除含缺失值的行/列。
2. **重复数据处理**：检查并删除重复数据，确保每条数据唯一。
3. **异常值处理**：识别并处理异常值，如极端值、错误值。
4. **数据格式转换**：转换数据类型或进行单位转换，如日期格式转换。
5. **标准化与归一化**：对数值型数据进行标准化（如 Z-score）或归一化（如 Min-Max）。
6. **类别数据编码**：将类别变量转换为数值形式，常见方法包括 One-Hot 编码和标签编码。
7. **文本处理**：对文本数据进行清洗，如去除停用词、词干化、分词等。
8. **数据抽样**：从数据集中抽取样本，或通过过采样/欠采样处理类别不平衡。
9. **特征工程**：创建新特征、删除不相关特征、选择重要特征等。

## Pandas 清洗空值

如果我们要删除包含空字段的行，可以使用 **dropna()** 方法，语法格式如下：

```
DataFrame.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)
```

**参数说明：**

- axis：默认为 **0**，表示逢空值剔除整行，如果设置参数 **axis＝1** 表示逢空值去掉整列。
- how：默认为 **'any'** 如果一行（或一列）里任何一个数据有出现 NA 就去掉整行，如果设置 **how='all'** 一行（或列）都是 NA 才去掉这整行。
- thresh：设置需要多少非空值的数据才可以保留下来的。
- subset：设置想要检查的列。如果是多个列，可以使用列名的 list 作为参数。
- inplace：如果设置 True，将计算得到的值直接覆盖之前的值并返回 None，修改的是源数据。

```python
import pandas as pd

df = pd.read_csv('property-data.csv')
new_df = df.dropna()
print(new_df.to_string())
```

**注意：**默认情况下，dropna() 方法返回一个新的 DataFrame，不会修改源数据。

如果你要修改源数据 DataFrame, 可以使用 **inplace = True** 参数

**我们也可以 fillna()方法来替换一些空字段：**

使用12345代替空子段

```python
import pandas as pd

df = pd.read_csv('property-data.csv')
df.fillna(12345, inplace = True)
print(df.to_string())
```

Pandas使用 **mean()**、**median()** 和 **mode()** 方法计算列的均值（所有值加起来的平均值）、中位数值（排序后排在中间的数）和众数（出现频率最高的数）。

```python
#使用 median() 方法计算列的中位数并替换空单元格：
import pandas as pd

df = pd.read_csv('property-data.csv')
x = df["ST_NUM"].mean()
df["ST_NUM"].fillna(x, inplace = True)
print(df.to_string())
```

## Pandas 清洗格式错误数据

数据格式错误的单元格会使数据分析变得困难，甚至不可能。

我们可以通过包含空单元格的行，或者将列中的所有单元格转换为相同格式的数据。

以下实例会格式化日期：

```python
import pandas as pd

# 第三个日期格式错误
data = {
  "Date": ['2020/12/01', '2020/12/02' , '20201226'],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data, index = ["day1", "day2", "day3"])
df['Date'] = pd.to_datetime(df['Date'], format='mixed')
print(df.to_string())

#结果如下:
'''
           Date  duration
day1 2020-12-01        50
day2 2020-12-02        40
day3 2020-12-26        45
'''
```

## Pandas 清洗错误数据

数据错误也是很常见的情况，我们可以对错误的数据进行替换或移除。

以下实例会替换错误年龄的数据：

```python
import pandas as pd

person = {
 "name": ['Google', 'Runoob' , 'Taobao'],
 "age": [50, 40, 12345]   # 12345 年龄数据是错误的
}

df = pd.DataFrame(person)
df.loc[2, 'age'] = 30 # 修改数据
print(df.to_string())
```

以上实例输出结果如下：

```
     name  age
0  Google   50
1  Runoob   40
2  Taobao   30
```

也可以设置条件语句：

将 age 大于 120 的设置为 120:

```python
import pandas as pd

person = {
 "name": ['Google', 'Runoob' , 'Taobao'],
 "age": [50, 200, 12345]   
}

df = pd.DataFrame(person)

for x in df.index:
 if df.loc[x, "age"] > 120:
  df.loc[x, "age"] = 120

print(df.to_string())
```

以上实例输出结果如下：

```
     name  age
0  Google   50
1  Runoob  120
2  Taobao  120
```

也可以将错误数据的行删除：

将 age 大于 120 的删除:

```python
import pandas as pd

person = {
 "name": ['Google', 'Runoob' , 'Taobao'],
 "age": [50, 40, 12345]   # 12345 年龄数据是错误的
}

df = pd.DataFrame(person)

for x in df.index:
 if df.loc[x, "age"] > 120:
  df.drop(x, inplace = True)

print(df.to_string())
```

以上实例输出结果如下：

```
     name  age
0  Google   50
1  Runoob   40
```

------

## Pandas 清洗重复数据

如果我们要清洗重复数据，可以使用 **duplicated()** 和 **drop_duplicates()** 方法。

如果对应的数据是重复的，**duplicated()** 会返回 True，否则返回 False。

```python
import pandas as pd

person = {
 "name": ['Google', 'Runoob', 'Runoob', 'Taobao'],
 "age": [50, 40, 40, 23] 
}
df = pd.DataFrame(person)
print(df.duplicated())
```

以上实例输出结果如下：

```
0    False
1    False
2     True
3    False
dtype: bool
```

删除重复数据，可以直接使用**drop_duplicates()** 方法。

```python
import pandas as pd

persons = {
 "name": ['Google', 'Runoob', 'Runoob', 'Taobao'],
 "age": [50, 40, 40, 23] 
}

df = pd.DataFrame(persons)
df.drop_duplicates(inplace = True)
print(df)
```

以上实例输出结果如下：

```
     name  age
0  Google   50
1  Runoob   40
3  Taobao   23
```

## 常用方法及说明

数据清洗与预处理的常见方法：

| **操作**               | **方法/步骤**                | **说明**                                                     | **常用函数/方法**                                        |
| :--------------------- | :--------------------------- | :----------------------------------------------------------- | :------------------------------------------------------- |
| **缺失值处理**         | 填充缺失值                   | 使用指定的值（如均值、中位数、众数等）填充缺失值。           | `df.fillna(value)`                                       |
|                        | 删除缺失值                   | 删除包含缺失值的行或列。                                     | `df.dropna()`                                            |
| **重复数据处理**       | 删除重复数据                 | 删除 DataFrame 中的重复行。                                  | `df.drop_duplicates()`                                   |
| **异常值处理**         | 异常值检测（基于统计方法）   | 通过 Z-score 或 IQR 方法识别并处理异常值。                   | 自定义函数（如基于 Z-score 或 IQR）                      |
|                        | 替换异常值                   | 使用合适的值（如均值或中位数）替换异常值。                   | 自定义函数（如替换异常值）                               |
| **数据格式转换**       | 转换数据类型                 | 将数据类型从一个类型转换为另一个类型，如将字符串转换为日期。 | `df.astype()`                                            |
|                        | 日期时间格式转换             | 转换字符串或数字为日期时间类型。                             | `pd.to_datetime()`                                       |
| **标准化与归一化**     | 标准化                       | 将数据转换为均值为0，标准差为1的分布。                       | `StandardScaler()`                                       |
|                        | 归一化                       | 将数据缩放到指定的范围（如 [0, 1]）。                        | `MinMaxScaler()`                                         |
| **类别数据编码**       | 标签编码                     | 将类别变量转换为整数形式。                                   | `LabelEncoder()`                                         |
|                        | 独热编码（One-Hot Encoding） | 将每个类别转换为一个新的二进制特征。                         | `pd.get_dummies()`                                       |
| **文本数据处理**       | 去除停用词                   | 从文本中去除无关紧要的词，如 "the" 、 "is" 等。              | 自定义函数（基于 `nltk` 或 `spaCy`）                     |
|                        | 词干化与词形还原             | 提取词干或恢复单词的基本形式。                               | `nltk.stem.PorterStemmer()`                              |
|                        | 分词                         | 将文本分割成单词或子词。                                     | `nltk.word_tokenize()`                                   |
| **数据抽样**           | 随机抽样                     | 从数据中随机抽取一定比例的样本。                             | `df.sample()`                                            |
|                        | 上采样与下采样               | 通过过采样（复制少数类样本）或欠采样（减少多数类样本）来平衡数据集中的类别分布。 | `SMOTE()`（上采样）； `RandomUnderSampler()`（下采样）   |
| **特征工程**           | 特征选择                     | 选择对目标变量有影响的特征，去除冗余或无关特征。             | `SelectKBest()`                                          |
|                        | 特征提取                     | 从原始数据中创建新的特征，提升模型的预测能力。               | `PolynomialFeatures()`                                   |
|                        | 特征缩放                     | 对数值特征进行缩放，使其具有相同的量级。                     | `MinMaxScaler()` 、 `StandardScaler()`                   |
| **类别特征映射**       | 特征映射                     | 将类别变量映射为对应的数字编码。                             | 自定义映射函数                                           |
| **数据合并与连接**     | 合并数据                     | 将多个 DataFrame 按照某些列合并在一起，支持内连接、外连接、左连接、右连接等。 | `pd.merge()`                                             |
|                        | 连接数据                     | 将多个 DataFrame 进行行或列拼接。                            | `pd.concat()`                                            |
| **数据重塑**           | 数据透视表                   | 将数据根据某些维度进行分组并计算聚合结果。                   | `pd.pivot_table()`                                       |
|                        | 数据变形                     | 改变数据的形状，如从长格式转为宽格式或从宽格式转为长格式。   | `df.melt()` 、 `df.pivot()`                              |
| **数据类型转换与处理** | 字符串处理                   | 对字符串数据进行处理，如去除空格、转换大小写等。             | `str.replace()` 、 `str.upper()` 等                      |
|                        | 分组计算                     | 按照某个特征分组后进行聚合计算。                             | `df.groupby()`                                           |
| **缺失值预测填充**     | 使用模型预测填充缺失值       | 使用机器学习模型（如回归模型）预测缺失值，并填充缺失数据。   | 自定义模型（如 `sklearn.linear_model.LinearRegression`） |
| **时间序列处理**       | 时间序列缺失值填充           | 使用时间序列的方法（如前向填充、后向填充）填充缺失值。       | `df.fillna(method='ffill')`                              |
|                        | 滚动窗口计算                 | 使用滑动窗口进行时间序列数据的统计计算（如均值、标准差等）。 | `df.rolling(window=5).mean()`                            |
| **数据转换与映射**     | 数据映射与替换               | 将数据中的某些值替换为其他值。                               | `df.replace()`                                           |

**填充缺失值：**

```python
import pandas as pd

# 示例数据
data = {'Name': ['Alice', 'Bob', 'Charlie', None],
    'Age': [25, 30, None, 35],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']}

df = pd.DataFrame(data)

# 填充缺失的 "Age" 为均值
df['Age'].fillna(df['Age'].mean(), inplace=True)
print(df)
```

输出：

```
      Name  Age           City
0    Alice   25.0       New York
1      Bob   30.0    Los Angeles
2  Charlie   30.0        Chicago
3     None   35.0        Houston
```

独热编码：

`````python
import pandas as pd

# 示例数据
data = {'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']}

df = pd.DataFrame(data)

# 对 "City" 列进行 One-Hot 编码
df_encoded = pd.get_dummies(df, columns=['City'])
print(df_encoded)
`````

输出：

```
   City_Chicago  City_Houston  City_Los Angeles  City_New York
0             0             0                 0              1
1             0             0                 1              0
2             1             0                 0              0
3             0             1                 0              0
```

标准化：

```python
from sklearn.preprocessing import StandardScaler
import pandas *as pd

# 示例数据
data = {'Age': [25, 30, 35, 40, 45],
    'Salary': [50000, 60000, 70000, 80000, 90000]}

df = pd.DataFrame(data)

# 标准化数据
scaler = StandardScaler()
df_scaled = scaler.fit_transform(df)

print(df_scaled)
```

输出：

```
[[-1.41421356 -1.41421356]
 [-0.70710678 -0.70710678]
 [ 0.          0.        ]
 [ 0.70710678  0.70710678]
 [ 1.41421356  1.41421356]]
```