BOLD = '\033[1m'
YELLOW = '\033[33m'
RESET = '\033[0m'
RED = '\033[31m'
WHITE = '\033[37m'
# ProLog 更好的日志

class ProLog:
    def __init__(self, name, handler, filters):
        self.name = name
        self.handler = handler
        self.filters = filters
    
    def info(self, message):
        if self.filters.filter(message):
            self.handler.handle(self.name, message, WHITE + 'INFO' + RESET)
        else:
            pass
    
    def debug(self, message):
        if self.filters.filter(message):
            self.handler.handle(self.name, message, YELLOW + 'DEBUG' + RESET)
        else:
            pass
    
    def error(self, message):
        if self.filters.filter(message):
            self.handler.handle(self.name, message, BOLD + RED + 'ERROR' + RESET)
        else:
            pass
    
    def warning(self, message):
        if self.filters.filter(message):
            self.handler.handle(self.name, message, BOLD + YELLOW + 'WARNING' + RESET)
        else:
            pass
    
    def critical(self, message):
        if self.filters.filter(message):
            self.handler.handle(self.name, message, BOLD + RED + 'CRITICAL' + RESET)
        else:
            pass