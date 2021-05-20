# reporter_su
**Language**

English

**Deacription**

Auto check your task if you use PBS to submit and email you when finished

**Requirements**

`> python 3`

**Installation**

Option 1:

```python
git clone git@github.com:ZeroDesigner/reporter.git
cd reporter
python setup.py install
```

Option 2:

```python
pip install reporter_su
```

**Usage**

Step 1

```python
# you need to get these informations below
receiver = 'lus***@outlook.com'
sender = '86136***@qq.com'
mail_license = '******'
smtpserver = 'smtp.qq.com'
mail_body = 'my task pdbid has been finished'
mail_title = 'task 1'
pdbid = 'change_text'
```

Step 2

```python
# the checker will check task status every 60 mins
import reporter_su.pbs_reporter as rp
if rp.auto_check(pdbid,time_scan = 3600) == 0:
   rp.auto_report(receiver,sender,mail_license,smtpserver,mail_body,mail_title)
```

![Screen Shot 2021-05-21 at 1.06.17 AM](https://gitee.com/zerodesigner/markdown-png/raw/master/uPic/Screen%20Shot%202021-05-21%20at%201.06.17%20AM.png)

#### **License**

MIT

**Email**

luskyqi@outlook.com



-------------



#### **语言**

中文

#### **描述**

自动检查你的任务是否已经完成（在使用PBS调度系统时），同时email提醒，在任务完成之后

#### 依赖

大于 python 3

#### 安装

##### 选项 1：

```python
git clone git@github.com:ZeroDesigner/reporter.git
cd reporter
python setup.py install
```

##### 选项 2：

```python
pip install reporter_su
```

#### 用法

##### 步骤 1

```python
# 你需要获取这些信息
receiver = 'lus***@outlook.com'
sender = '86136***@qq.com'
mail_license = '******'
smtpserver = 'smtp.qq.com'
mail_body = 'my task pdbid has been finished'
mail_title = 'task 1'
pdbid = 'change_text'
```

##### 步骤 2

```python
# 脚本会每隔1个小时检查一下任务是否存在
import reporter_su.pbs_reporter as rp
if rp.auto_check(pdbid,time_scan = 3600) == 0:
   rp.auto_report(receiver,sender,mail_license,smtpserver,mail_body,mail_title)
```

![Screen Shot 2021-05-21 at 1.06.17 AM](https://gitee.com/zerodesigner/markdown-png/raw/master/uPic/Screen%20Shot%202021-05-21%20at%201.06.17%20AM-1530425.png)

####  协议

MIT

#### 邮箱

luskyqi@outlook.com

