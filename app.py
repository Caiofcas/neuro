import streamlit as st
import random
from pathlib import Path

images_folder = Path("images")

questions = {
  "2.1.A": {
    "answers": [
      ("1A", "Hoz del cerebro"),
      ("1B", "Capa interna de la duramadre"),
      ("1C", "Capa externa de la duramadre"),
      ("1D", "Capas fusionadas de la duramadre"),
      ("2", "Aracnoides"),
      ("3", "Piamadre (membrana pial-glial)"),
      ("4", "Granulaciones aracnoideas"),
      ("5", "Seno sagital superior"),
      ("6", "Espacio subaracnoideo"),
      ("7", "Arteria meníngea media"),
      ("8", "Vena cerebral superior"),
    ] 
  },
  "2.1.B": {
    "answers": [
      ("1A", "Hoz del cerebro"),
      ("1B", "Capa interna de la duramadre"),
      ("1C", "Capa externa de la duramadre"),
      ("1D", "Capas fusionadas de la duramadre"),
      ("2", "Aracnoides"),
      ("3", "Piamadre (membrana pial-glial)"),
      ("4", "Granulaciones aracnoideas"),
      ("5", "Seno sagital superior"),
      ("6", "Espacio subaracnoideo"),
      ("8", "Vena cerebral superior"),
    ] 
  },
  "2.2.A": {
    "answers": [
      ("1", "Surco lateral"),
      ("2", "Giro frontal inferior"),
      ("3", "Giro precentral"),
      ("4", "Surco central"),
      ("5", "Giro poscentral"),
      ("6", "Giro supramarginal"),
      ("7", "Lobulillo parietal superior"),
      ("8", "Giro angular"),
      ("9", "Giro temporal superior"),
      ("10", "Córtex insular"),
    ] 
  },
  "2.2.C": {
    "answers": [
      ("10", "Cortéx insular"),
    ] 
  },
  "2.3.A": {
    "answers": [
      ("1", "Área de Broca"),
      ("2", "Campos oculares frontales"),
      ("3", "Córtex premotor y motor suplementario"),
      ("4", "Córtex motor primario lateral"),
      ("5", "Córtex somatosensitivo primario lateral"),
      ("6", "Córtex auditivo primario"),
      ("7", "Giro temporal medio"),
      ("8", "Área de Wernicke"),
      ("9", "Lobulillo parietal superior"),
      ("10", "Córtex visual primario"),
    ] 
  },
  "2.3.B": {
    "answers": [
      ("10", "Córtex visual primario"),
    ] 
  },
  # 2.5
  # 2.6
  # 3.1
  # 3.2
  # 3.3
  # 3.4
  # 3.5
  # 3.6
  # 4.1
  # 4.2
  # 4.3
  # 4.4
  # 5.1
  # 5.2
  # 5.3
  # 5.4
  # 5.6
  # 5.10
  # 5.11
  # 6.1
  # 7.1
  # 7.5
  # 7.6
}

def set_question():
  image_key = random.choice(list(questions))
  question, answer = random.choice(questions[image_key]["answers"])
  st.session_state.question = {
    "image_url": f"{image_key}.png",
    "question": question,
    "answer": answer,
  }
  st.session_state.show_answer = False

def show_answer():
  st.session_state.show_answer = True

if "question" not in st.session_state:
  set_question()

question: str = st.session_state.question["question"]
answer: str = st.session_state.question["answer"]
image_url: str = st.session_state.question["image_url"]

st.markdown("# Neuro")
st.markdown("### Image:")
st.image(images_folder / image_url)

user_answer = st.text_input(f"{question}: ")

if user_answer:
  correct_answer = user_answer.lower().strip() == answer.lower().strip()
  if correct_answer:
    st.markdown("Correct! :white_check_mark:")
  else:
    st.markdown("Incorrect! :no_entry_sign:")

  with st.container():
    st.button("Show answer", on_click=show_answer )
    if st.session_state.show_answer:
      st.markdown(answer)

st.button("New question", on_click=set_question)