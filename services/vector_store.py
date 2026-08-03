import os
from pathlib import Path


from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_nvidia_ai_endpoints import NVIDIAEmbeddings


class VectorStoreService:

    VECTOR_DB_PATH = "vector_db"
    POLICY_PATH = "data/trendly_policy.md"

    def __init__(self):



        self.embeddings = NVIDIAEmbeddings(
            model="nvidia/nv-embed-v1",
            api_key=os.getenv("NVIDIA_EMBEDDINGS_API_KEY")
        )

        self.vectorstore = None

        index_path = Path(self.VECTOR_DB_PATH)

        if (
            index_path.exists()
            and (index_path / "index.faiss").exists()
            and (index_path / "index.pkl").exists()
        ):
            self.load_vectorstore()
        else:
            self.create_vectorstore()

    def create_vectorstore(self):

        print("Creating Vector Database...")

        # Step 1 : Load markdown
        loader = TextLoader(self.POLICY_PATH, encoding="utf-8")
        documents = loader.load()

        # Step 2 : Split into chunks
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )

        chunks = splitter.split_documents(documents)

        print(f"Total Chunks : {len(chunks)}")

        # Step 3 : Create FAISS
        self.vectorstore = FAISS.from_documents(
            documents=chunks,
            embedding=self.embeddings
        )

        # Step 4 : Save
        Path(self.VECTOR_DB_PATH).mkdir(exist_ok=True)

        self.vectorstore.save_local(
            self.VECTOR_DB_PATH
        )

        print("Vector Database Created Successfully.")

    def load_vectorstore(self):

        print("Loading Existing Vector Database...")

        self.vectorstore = FAISS.load_local(
            folder_path=self.VECTOR_DB_PATH,
            embeddings=self.embeddings,
            allow_dangerous_deserialization=True
        )

        print("Vector Database Loaded.")

    def similarity_search(self, query: str, k: int = 3):

        return self.vectorstore.similarity_search(
            query=query,
            k=k
        )

    def get_retriever(self):

        return self.vectorstore.as_retriever(
            search_kwargs={
                "k": 3
            }
        )