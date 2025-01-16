# 添加: 获取 docs 目录下所有的 xls 文件
import os

def get_files(directory, types=('.pdf', '.xls', '.xlsx')):
    def _get_files_recursively(dir_path):
        for root, _, files in os.walk(dir_path):
            for f in files:
                if f.endswith(types):
                    yield os.path.abspath(os.path.join(root, f))
    return list(_get_files_recursively(directory))
