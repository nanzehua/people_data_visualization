from dotenv import load_dotenv

load_dotenv()

from utils.file import get_files  # 添加: 导入 get_files 函数

# 获取文件列表
file_path= "../docs/2010第六次"
xls_files = get_files(file_path, types=('.xls', '.xlsx'))
print(xls_files)

# 加载xls文件
from langchain_community.document_loaders.excel import UnstructuredExcelLoader

# 如果 xls_files 是列表，需要遍历处理
xls_loaders = []
for file in xls_files:
    loader = UnstructuredExcelLoader(file)
    xls_loaders.extend(loader.load())
print(xls_loaders)


from langchain_community.vectorstores import FAISS
from langchain_community.embeddings.huggingface import HuggingFaceEmbeddings

# 设置向量数据库路径
embeddings_path = "./embeddings"
embeddings = HuggingFaceEmbeddings(model_name=embeddings_path)

# 创建向量数据库
vectorStoreDB = FAISS.from_documents(xls_loaders, embedding=embeddings)
print(vectorStoreDB)

results = vectorStoreDB.similarity_search("陕西人口是多少？")
print(results)

retriever = vectorStoreDB.as_retriever(
    search_type="mmr",
    search_kwargs={"k": 1}
)

docs = retriever.get_relevant_documents("陕西人口是多少？")
print(docs)



