def relevant_subject(subjects, userInput):
    
    return (f"Analise a frase fornecida e determine qual assunto listado é o mais relevante **com base no contexto completo da frase**, "
    f"não apenas nas palavras individuais.\n\n"
    
    f"Leia a frase com atenção e escolha o assunto que melhor representa o tema central da frase. "
    f"Se houver mais de um assunto similar, escolha o mais específico e diretamente relacionado.\n\n"
    
    f"Assuntos disponíveis (com descrição):\n"
    f"{subjects}\n\n"
    
    f"Frase: {userInput}\n\n"

    f"Retorne apenas o nome exato do assunto mais adequado. Caso esteja na lista de assuntos disponíveis.\n"
    
    f"Se nenhum dos assuntos for adequado ou não encontrado, responda exatamente neste formato: "
    f"'Não tenho informações sobre (breve resumo do que o usuário disse, sem parenteses)'.\n\n"

    f"**ATENÇÃO:** Não escolha um assunto apenas porque contém palavras semelhantes. "
    f"**ATENÇÃO:** Analise a intenção e o contexto completo da frase."
    f"**ATENÇÃO:** Em qualquer hipotese de não conseguir fazer alguma operação de forma certeira diga algo neste formato: 'Não tenho informações sobre (breve resumo do que o usuário disse, sem parenteses)', ")

def enchance_subject_description(relevant_subject_response, subject_description_response):
    return("Analise cuidadosamente a descrição e o assunto fornecidos abaixo. "
    "Gere um resumo conciso baseado **exclusivamente** nas informações presentes na descrição. "
    "**Não invente, extrapole ou adicione detalhes externos**. "
    "Sua resposta deve conter **apenas** o resumo, sem comentários adicionais.\n\n"
    f"🔹 **Assunto:** {relevant_subject_response}\n"
    f"🔹 **Descrição:** {subject_description_response}")