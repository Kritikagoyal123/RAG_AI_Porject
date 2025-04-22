# 🧠 Retrieval-Augmented Generation (RAG) System – Local Setup

This project marks my first hands-on experience building a fully functional **Retrieval-Augmented Generation (RAG)** system from scratch. It deepened my understanding of how **LLMs, vector databases, and embedding models** work together to power document-based question answering — combining the strengths of both retrieval and generation approaches.

**🔧 What I Built**
**
🗂️ Phase 1: Knowledge Base in Open WebUI**

I started by uploading documents into **Open WebUI**, which allowed me to experiment with knowledge collections and see how LLMs can improve responses by using external context — without requiring retraining. This showed me the importance of retrieval-based augmentation for improving model accuracy.

**🐍 Phase 2: Local RAG Pipeline with Python**

I then built a custom RAG pipeline using the following stack:
	•	**Ollama** – for running local LLMs
	•	**LlamaIndex** – to manage document queries and orchestration
	•	**ChromaDB** – as the vector database
	•	**Hugging Face embeddings** – to convert documents and queries into vector space

**🧪 Key Learnings & Challenges**

**⚙️ Technical Insights**
	•	Understood the difference between EphemeralClient vs. PersistentClient in **ChromaDB**.
	•	My initial setup lost all vectors on restart.
	•	Switching to PersistentClient enabled document reuse and made the system much faster.
	•	Learned to fix dependency issues:
	•	Faced a version error with the BAAI/bge-small-en model.
	•	Solved it by aligning versions of transformers and tokenizers.
	•	Explored different models:
	•	Tested **llama3.2, deepseek-r1**, and others via Ollama.
	•	Compared their response quality on domain-specific queries.
	•	Custom Prompt Engineering:
	•	Used PromptTemplate to tailor responses to my use case.
	•	Tuned similarity_top_k to adjust how many relevant documents are retrieved.
	•	Fixed missing dependencies (e.g., xlrd for reading Excel files).

**🔍 Concepts Reinforced**
	•	How embedding models convert text into numerical vectors for semantic search.
	•	How retrieval pipelines work:
	1.	Load and chunk documents
	2.	Create embeddings
	3.	Store vectors in ChromaDB
	4.	Query using a local LLM with contextual results


**🙌 Outcome**

This project boosted my confidence in working with open-source AI tools and Python-based architectures. I now have a clear understanding of how to build, debug, and optimize a local RAG system — from document ingestion to response generation.
