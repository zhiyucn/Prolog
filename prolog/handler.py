import time
import re
import strip_ansi
def clean_ansi_codes(text):

    return strip_ansi.strip_ansi(text)
class NoHandler:
    @staticmethod
    def handle(name, message, level='INFO'):
        clean_message = clean_ansi_codes(level)  # 去掉ANSI颜色码
        with open(f'{time.strftime("%Y-%m-%d")}.log', 'a', encoding='utf-8') as f:
            f.write(f'[{clean_ansi_codes(level)}] {name} - {message}\n')  # 写入纯文本消息
        print(f'[{level}] {name} - {message}')  # 控制台输出纯文本消息

class ConsoleHandler:
    @staticmethod
    def handle(name, message, level='INFO'):
        clean_message = clean_ansi_codes(message)  # 去掉ANSI颜色码
        print(f'[{level}] {name} - {message}')  # 控制台输出纯文本消息

class FileHandler:
    @staticmethod
    def handle(name, message, level='INFO'):
        with open(f'{time.strftime("%Y-%m-%d")}.log', 'a', encoding='utf-8') as f:
            f.write(f'[{strip_ansi.strip_ansi(level)}] {name} - {message}\n')  # 写入纯文本消息