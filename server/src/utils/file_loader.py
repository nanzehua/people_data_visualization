import os


class FileLoader:

    def __init__(self):
        pass

    @staticmethod
    def get_files(path: str, types: tuple = ('.pdf', '.xls', '.xlsx')):
        """获取指定目录下的所有文件

        Args:
            path (str): 文件路径
            types (tuple, optional): 文件类型. Defaults to ('.pdf', '.xls', '.xlsx').

        Returns:
            list: 文件列表
        """
        result = []
        for root, _, files in os.walk(path):
            for f in files:
                if f.endswith(types):
                    filepath = os.path.abspath(os.path.join(root, f))
                    result.append(filepath)
        return result
