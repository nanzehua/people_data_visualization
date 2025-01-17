# 读取环境变量
from dotenv import load_dotenv

load_dotenv()

# # 下载
# import nltk
#
# nltk.download('punkt_tab')
# nltk.download('averaged_perceptron_tagger_eng')

# 获取文件列表
from src.utils.file_loader import FileLoader

file_util = FileLoader()
file_path = "./docs/2000第五次"
xls_files = file_util.get_files(file_path, types=('.xls', '.xlsx'))
print(len(xls_files))

# 创建文档加载器
from langchain_community.document_loaders import UnstructuredExcelLoader, CSVLoader

xls_docs = []
for file in xls_files:
    loader = UnstructuredExcelLoader(file, mode='elements')
    docs = loader.load()
    xls_docs.extend(docs)
print(len(xls_docs))

# 创建嵌入模型
from langchain_openai import OpenAIEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings

model_name = "shibing624/text2vec-base-chinese"
model_kwargs = {
    'device': 'cpu',
    'trust_remote_code': True
}
encode_kwargs = {'normalize_embeddings': True}
hf_embeddings = HuggingFaceEmbeddings(
    model_name=model_name,
    model_kwargs=model_kwargs,
    encode_kwargs=encode_kwargs
)

# 创建向量数据库
from langchain_community.vectorstores import FAISS, DocArrayInMemorySearch

vectorStoreDB = FAISS.from_documents(xls_docs, embedding=hf_embeddings)
print(vectorStoreDB)

# 检索
results = vectorStoreDB.similarity_search("陕西人口是多少？")
print(results)

# 检索器
retriever = vectorStoreDB.as_retriever(
    search_type="mmr",
    search_kwargs={"k": 1}
)

docs = retriever.get_relevant_documents("陕西人口是多少？")
print(docs)
