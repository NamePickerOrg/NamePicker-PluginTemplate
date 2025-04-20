from .NamePickerPluginBase import PluginBase,SettingBase
from qfluentwidgets import *
from loguru import logger

class Plugin(PluginBase):
    def __init__(self):
        super().__init__()
        self.filters = [self.customFilter]# 在这里填入筛选函数
        self.filtersName = ["自定义筛选器"]# 在这里填入筛选器名字
        self.customKey = ["test"]# 在这里填入要求用户添加的字段
        self.customKeyTitle = ["测试用额外字段"]# 在这里填入字段标题

    def customFilter(self,name):
        return name["test"] != "9191"

    def beforePick(self):
        # 在这编写抽选按钮按下后，抽选结果产生前执行的操作
        logger.info("Before Pick")

    def afterPick(self,name):
        # 在这编写抽选按钮按下后，抽选结果产生后执行的操作
        logger.info("After Pick")
        logger.info(name)

    def onStartup(self):
        # 在这编写插件被加载时执行的操作
        logger.info("Startup")

class Settings(SettingBase):
    def __init__(self):
        super().__init__()
        # 在这编写设置界面
        self.testCard = SettingCard(
            icon=FluentIcon.INFO,
            title="测试配置项",
            content="这是一个配置项"
        )
        self.vbox = VBoxLayout(self)
        self.vbox.addWidget(self.testCard)
