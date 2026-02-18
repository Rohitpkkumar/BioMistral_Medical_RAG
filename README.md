# BioMistral Medical RAG 🧬

![Python](https://img.shields.io/badge/Python-3.10%2B-blue) ![LLM](https://img.shields.io/badge/LLM-BioMistral_7B-green) ![RAG](https://img.shields.io/badge/RAG-LangChain-orange) ![License](https://img.shields.io/badge/License-MIT-lightgrey)

BioMistral Medical **Retrieval Augmented Generation (RAG)** is a privacy-first, local Retrieval Augmented Generation (RAG) application tailored for the biomedical domain. Built entirely on an open-source stack, it allows users to securely chat with medical documents without internet dependency. The system leverages BioMistral 7B for accurate medical reasoning, PubMedBert for high-fidelity embeddings, and Qdrant for local vector storage, all orchestrated seamlessly via LangChain and Llama.cpp.

## Features

* **Specialized Medical LLM:** Uses **BioMistral 7B**, a model fine-tuned on PubMed Central and other medical data.
* **Privacy First:** Runs entirely **locally** on your machine. No data is sent to OpenAI or cloud APIs.
* **RAG Architecture:**
    * **Embeddings:** `PubMedBert` (optimized for medical semantic search).
    * **Vector Store:** `Qdrant` (Self-hosted/Local instance).
    * **Orchestration:** `LangChain`.

## Tech Stack

* **Frontend:** HTML5, Bootstrap 5, Custom CSS (Glassmorphism), JavaScript (Fetch API).
* **Backend:** Flask (Python).
* **AI/ML:**
    * `llama-cpp-python` (for quantized model inference).
    * `langchain` & `langchain-community`.
    * `sentence-transformers`.
    * `qdrant-client`.

## Prerequisites

Before running this project, ensure you have:

1.  **Python 3.10+** installed.
2.  **C++ Compiler** (Required for `llama-cpp-python`):
    * *Windows:* Visual Studio Community (Desktop development with C++).
    * *Mac/Linux:* GCC/Clang (`xcode-select --install` on Mac).
3.  **RAM:** At least 8GB (16GB recommended) to run the 7B model smoothly.

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/Rohitpkkumar/Medical-RAG-BioMistral.git
cd Medical-RAG-BioMistral
```
### 2. Create a Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```
### 3. Install Dependencies
```bash
pip -r requirements.txt
```
### 4. Download the Model

You need the quantized GGUF version of BioMistral.
1. Create a folder named model in the root directory.
2. Download BioMistral-7B.Q4_K_M.gguf (or a similar Quantization) from TheBloke's HuggingFace repo.
Download Link [TheBloke/BioMistral-7B-GGUF](https://huggingface.co/BioMistral/BioMistral-7B-GGUF/blob/main/ggml-model-Q4_K_M.gguf) 
3. Place the .gguf file inside the model/ folder.

### 5. Download the Embedding Model
~~~bash
git lfs install
git clone https://huggingface.co/NeuML/pubmedbert-base-embeddings
~~~

### 6. Install [Docker Desktop](https://docs.docker.com/desktop/) with optional proxy settings

### 7. Create the Qdrant container
~~~bash
docker pull qdrant/qdrant
docker run -p 6333:6333 -v .\qdrant_db\:/qdrant/storage qdrant/qdrant
~~~
Access the Dashboard using http://localhost:6333/dashboard

## How to Run
### Step 1: Ingest Your Data
Place your medical PDF documents into the `data/` directory. Then, run the ingestion script to create the vector embeddings.

```bash
python ingest.py
```
### Step 2. Start the Application
Run the Flask backend:
```
uvicorn app:app
```
### Step 3. Access the UI
Open your browser and navigate to:
```bash
http://localhost:5000
```
## Project Structure
```
├── app.py              
├── ingest.py       
├── data/                  
├── model/                 
├── templates/
│   └── index.html         
├── static/               
├── requirements.txt       
└── README.md

```
## Screenshot
<img width="1679" height="1010" alt="Screenshot 2026-02-18 at 4 55 12 PM" src="https://github.com/user-attachments/assets/80acf158-f838-45e5-bea7-2bdd6defc122" />
<img width="1680" height="961" alt="Screenshot 2026-02-18 at 4 57 11 PM" src="https://github.com/user-attachments/assets/ae19bb93-f20e-41f2-b75d-de244edf4a66" />
<img width="1680" height="961" alt="Screenshot 2026-02-18 at 5 06 22 PM" src="https://github.com/user-attachments/assets/6955844f-d3ad-4e9e-b953-9d7ecd97e04d" />
<img width="1680" height="961" alt="Screenshot 2026-02-18 at 5 06 00 PM" src="https://github.com/user-attachments/assets/dea0c2f6-3482-4699-9ab7-8dbad782e226" />

