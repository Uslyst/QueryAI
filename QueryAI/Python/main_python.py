import sqlite3
import ollama
import ai_prompts as ai_prompts
import socket
import os
import database_manager
# Conectar ao banco de dados

def get_subjects():

    conn = sqlite3.connect(database_manager.db_path)
    cursor = conn.cursor()

    cursor.execute("SELECT subject FROM appdata")
    subjects = cursor.fetchall()

    subject_list = [subject[0] for subject in subjects]

    conn.close()

    return subject_list


def get_description(subject_to_search):
    conn = sqlite3.connect(database_manager.db_path)
    cursor = conn.cursor()

    # print(f"Pesquisando por: '{subject_to_search}'")

    subject_to_search = subject_to_search.strip()

    # Usar REPLACE() para ignorar espaços internos e COLLATE NOCASE para ignorar maiúsculas/minúsculas
    cursor.execute("""
        SELECT description FROM appdata 
        WHERE REPLACE(subject, ' ', '') = REPLACE(?, ' ', '') COLLATE NOCASE
    """, (subject_to_search,))

    result = cursor.fetchone()
    conn.close()

    return result[0] if result else None

def ask_model(question):
    
    resposta = ollama.chat(model="gemma3:4b", messages=[{"role": "user", "content": question}])

    # Exibir a resposta
    return resposta['message']['content']

def search_relevant_subject(userInput):
    subjects = get_subjects()
    relevantSubjectPrompt = ai_prompts.relevant_subject(subjects, userInput)
    return ask_model(relevantSubjectPrompt)

def cover_subject_not_found(subject_guess_response, user_input):
    if subject_guess_response == user_input:
        return f"Não tenho informações sobre '{user_input}' em específico"
    else:       
        return subject_guess_response
def c_sharp_bridge():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("127.0.0.1", 5000))
    server.listen(1)

    print("Aguardando conexão...")
    conn, addr = server.accept()
    print(f"Conectado a {addr}")

    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        print("Recebido: ", data)
        ai_mode, user_input = data.split("] ", 1)
        ai_mode = data + "]"

        subject_guess_response = search_relevant_subject(data)
        # direct => descrição minha
        # detailed => descrição da ia melhorada
        # free => habilitado conversação sobre qualquer assunto (busca de assunto 1)
        
        subject_description_response = get_description(subject_guess_response)

        enchance_description_prompt = ai_prompts.enchance_subject_description(subject_guess_response, subject_description_response)

        if subject_description_response:
            modelDescription = ask_model(enchance_description_prompt)
            conn.send(modelDescription.encode())
            #print(f"{modelDescription}")
        else:
            #print(relevant_subject_response)
            subject_not_found_answer = cover_subject_not_found(subject_guess_response,  )
                
            conn.send(subject_not_found_answer.encode())
        
    conn.close()

def main():   
    c_sharp_bridge()

    
    
if __name__ == "__main__":
    main()

