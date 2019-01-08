#####python3+selenium+unittest web自动化测试框架##########
目录结构如下
--config                #配置文件目录
    ---config.yml       #可以将一些配置放到此处如url,发收邮件人等
--data                  #数据文件目录如测试用例用的上传图片及文档
    --logo.png
--drivers               #浏览器驱动目录
    --chromedriver.exe  #google浏览器驱动,如果版本不匹配可自行下载及替换 google：http://chromedriver.storage.googleapis.com/index.html IE：http://selenium-release.storage.googleapis.com/index.html
--horen                 #测试目录
    --case              #测试用例目录（此目录可再分项目目录的case）
        --demo.py       #测试用例Demo
        --run_case.py   #运行当前目录下所有测试用例脚本,执行此脚本可运行用例
--log                   #日志目录
    --log.txt
--report                #测试报告存放目录
    --result.html
--utils                 #可以将一些工具和公共类和方法
      --config.py       #读取config下config.yml配置及定义文件路径
      --HTMLTestRunner.py  #生成测试报告源码,已修改过中文
      --log.py          #日志类
      --mail.py         #邮件类
      --random_func.py  #随机函数



