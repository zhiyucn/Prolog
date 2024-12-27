# 导入必要的模块
from prolog.handler import ConsoleHandler, FileHandler, NoHandler
from prolog.filters import NoFilters
from prolog import ProLog
from prolog.extension_handler import BeautifulColorHandler, JSONHandler, XMLHandler
class MyFilters():
    def filter(level, message):
        if '调试' in message:
            return False
        return True
# 创建 ProLog 实例
log = ProLog('main', XMLHandler(), NoFilters())

# 测试不同日志级别的消息
log.info('这是一个信息级别的日志消息')
log.debug('这是一个调试级别的日志消息')
log.warning('这是一个警告级别的日志消息')
log.error('这是一个错误级别的日志消息')
log.critical('这是一个严重级别的日志消息')
