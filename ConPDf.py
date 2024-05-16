# Traer el archivo .env
import os
from dotenv import load_dotenv
# Cargar variables de entorno
load_dotenv()
# Acceder a la variable de entorno COHERE_API_KEY
cohere_api_key = os.getenv("COHERE_API_KEY")

# Importar la clase ChatCohere
from langchain_cohere import ChatCohere
llm = ChatCohere()

from langchain_core.prompts import ChatPromptTemplate
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain

# Crear el cargador de documentos PDF
loader = PyPDFLoader("./pdf/Dialnet-AplicacionDeLaTeoriaFundamentadaGroundedTheoryAlEs-2499458.pdf")
docs = loader.load()

# Proceso de embedding
from langchain_cohere.embeddings import CohereEmbeddings
embeddings = CohereEmbeddings()

# Almacén de vectores local simple, FAISS
text_splitter = RecursiveCharacterTextSplitter()
documents = text_splitter.split_documents(docs)
vector = FAISS.from_documents(documents, embeddings)

# Crear cadena de recuperación
prompt = ChatPromptTemplate.from_template("""
                                          1-nunca te presentes. 
                                          2 - si alguien pregunta algo que no esta en el contex responde:" no puedo responder a eso por ahora, solo puedo responder sobre "  y completa la oracion hbalndo por arriba del contexto
                                          3 - si se hace una pregunta que puedes responder... solo responde con la respuesta directamente, sin anda mas que la respuesta.
                                          4 - si alquien dice hola solo  responde " Hola ¿En que puedo ayudarte?
                                          5 - si alguien dice adios solo responde "Adios. Que tengas un buen dia"
                                          6 - si alguien dice hola y una pregunta, responde "hola" y completa con al respuesta a la pregunta
                                          7- si alguien pregunta " quien eres?" responde "Soy un asistente virtual creado por estudiantes de la UTN-FRSR del equipo UTN-MMXXIII, puedo ayudarte con tus dudas sobre " y completa con informacion del contexto
<context>
{context}
</context>
Question: {input}""")

# Crear cadena de documentos
document_chain = create_stuff_documents_chain(llm, prompt)

# Convertir la base de vectores a un recuperador (retriever)
retriever = vector.as_retriever()

# Crear la cadena de recuperación
retrieval_chain = create_retrieval_chain(retriever, document_chain)

def call_api_IA(user_input):
    response = retrieval_chain.invoke({"input": user_input})
    return response
