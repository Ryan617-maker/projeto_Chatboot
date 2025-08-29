import streamlit as st

st.set_page_config(page_title="Atendimento Escola", page_icon=" +")
st.title(" Atendimento Virtual - Escola")

# Histórico do chat
if "messages" not in st.session_state:
    st.session_state.messages = []

# Perguntas e respostas pré-definidas
faq = {
"Qual é o horário de atendimento?": "Nosso horário de atendimento é de segunda a sexta, das 08:00 às 18:00.",
"Como faço matrícula?": "Para matrícula, acesse o formulário no nosso site ou venha até a secretaria da escola.",
"Quais cursos vocês oferecem?": "Oferecemos Ensino Fundamental, Ensino Médio e cursos extracurriculares de idiomas e tecnologia.",
"Qual é o valor da mensalidade?": "O valor da mensalidade depende do curso. Entre em contato com a secretaria para mais detalhes.",
"Onde a escola está localizada?": "Estamos localizados na Rua Exemplo, nº 123, Centro.",
"Falar com atendente": "Você pode falar diretamente com um atendente pelo WhatsApp clicando no botão abaixo.",
}

# Mostrar histórico
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Campo de input com sugestões de perguntas
pergunta = st.chat_input("Digite sua pergunta ou escolha uma das sugestões abaixo:")

# Mostrar botões de perguntas
for key in faq.keys():
    if st.button(key):
        pergunta = key