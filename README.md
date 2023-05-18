# 复旦自动刷锻脚本

基于原刷锻脚本 fudan-sport-automate 包装的自动刷锻脚本。~~由于原仓库似乎消失了~~(原作者提供的新仓库：https://github.com/fsy2001/fudan-sport-automator)故提供此替代方案。  


> 当前功能有效性尚未验证。

## 使用


> 当前的包装仅支持邯郸南区刷锻。如需选择其他区域请参照原脚本本地运行的说明。

- 安装依赖：`pip install -r requirements.txt`
- `py Run.py` 开启脚本。
- 刷锻计划任务在脚本启动后即就绪，时间到后将会自动执行。请确保脚本正在运行。
- 脚本中输入命令`help`可查看所有可执行指令。
- 启动后需要使用`set`系列指令来设定 USER_ID 与 token ，请参考抓包教程。

## 关于原仓库

本仓库大部分代码来源于原刷锻脚本仓库(fudan-sport-automate) Clone . 有关原仓库的说明请见 `old README.md`

## 关于贡献

首先不是原作者(~~仓库消失了我也找不到原作者了qwq~~https://github.com/fsy2001)，~~也没有多少相关知识和经验，故项目更接近自用与单纯的分享性质。如想改进更建议另外建立项目维护。~~不过也欢迎提交。

## 帮助

### 抓包教程

#### iOS 系统

抓包教程可参考 [使用 Stream 抓包](https://www.azurew.com/%e8%bf%90%e7%bb%b4%e5%b7%a5%e5%85%b7/8528.html)
，抓包软件可在 [App Store](https://apps.apple.com/cn/app/stream/id1312141691) 下载。

按照教程内的指引配置到设置证书的步骤，然后在软件内点击 Sniff Now 按钮，打开刷锻小程序刷新一下（确保小程序已经登录），再回到
Stream，点击 Stop Sniffing，然后点击 Sniff
History，选择最近的一条记录，点开后找到开头为 `GET https://sport.fudan.edu.cn/sapi` 的任意一条记录，点进去选择 Request，在
Request Line 中有 `userid=xxx&token=xxx` 的记录，记下这两段信息。

#### Windows 系统

可参考 [教程](https://juejin.cn/post/6920993581758939150/) 进行相应设置。注意：需要把 Fidder 中 HTTPS 部分设置的复选框由
from browers only 改为 from all processes。

在配置完后，微信登录，右上角齿轮进入代理，端口为 127.0.0.1，端口号为 8888（默认）
登录后进入小程序并登录，在 fiddler 里找到下图中的 ID 和 token
![image](https://user-images.githubusercontent.com/51439899/226794395-42eca333-fb65-4e29-a2cb-b8ce3fd13221.png)

**注意，目前 Token 的有效期为 3 天。**

