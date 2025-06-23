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
            ("10", "Córtex insular"),
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
    "2.5": {
        "answers": [
            ("1", "Hipotálamo"),
            ("2", " Tálamo"),
            ("3", " Córtex cerebral"),
            ("4", " Cerebelo (colorea un lóbulo)"),
            ("5", " Médula espinal"),
            ("6", " Bulbo raquídeo"),
            ("7", " Puente"),
            ("8", " Mesencéfalo"),
            ("9", " Hipófisis"),
        ]
    },
    "2.6": {
        "answers": [
            ("1", "Bulbo y tracto olfatorios"),
            ("2", "Hipófisis"),
            ("3", "Córtex olfatorio primario (uncus)"),
            ("4", "Cuerpos mamilares"),
            ("5", "Pedúnculo cerebral"),
            ("6", "Sustancia negra"),
            ("7", "Córtex de asociación visual"),
            ("8", "Córtex visual primario"),
            ("9", "Giro parahipocampal"),
            ("10", "Córtex periamigdalino"),
        ]
    },
    "3.1": {
        "answers": [
            ("1", "Colículos superiores"),
            ("2", "Colículos inferiores"),
            ("3", "Colículo facial"),
            ("4", "Tubérculo cuneiforme"),
            ("5", "Tubérculo grácil"),
            ("6", "Raíces dorsales de la médula espinal"),
            ("7", "Pedúnculo cerebeloso inferior"),
            ("8", "Pedúnculo cerebeloso medio"),
            ("9", "Pedúnculo cerebeloso superior"),
            ("10", "Nervio trigémino (NC V)"),
            ("11", "Cuerpo (núcleo) geniculado medial del tálamo"),
            ("12", "Cuerpo (núcleo) geniculado lateral del tálamo"),
        ]
    },
    "3.2": {
        "answers": [
            ("1", "Tracto olfatorio (que se extiende desde el nervio olfatorio)"),
            (
                "2",
                "Quiasma óptico (zona donde el nervio óptico cruza antes del tracto óptico)",
            ),
            ("3", "Nervio oculomotor (NC III)"),
            ("4", "Nervio troclear (NC IV)"),
            ("5", "Nervio trigémino (NC V)"),
            ("6", "Nervio abducens (NC VI)"),
            ("7", "Nervio facial (NC VII) (con el nervio intermedio)"),
            ("8", "Nervio vestibulococlear (NC VIII)"),
            ("9", "Nervio glosofaríngeo (NC IX)"),
            ("10", "Nervio vago (NC X)"),
            ("11", "Nervio hipogloso (NC XII)"),
            ("12", "Nervio accesorio (NC XI)"),
        ]
    },
    "3.3.A": {
        "answers": [
            ("1", "Vermis (superior e inferior)"),
            ("2", "Paravermis"),
            ("3", "Hemisferios cerebelosos laterales"),
            ("4", "Lóbulo anterior"),
            ("5", "Lóbulo medio"),
        ]
    },
    "3.3.B": {
        "answers": [
            ("1", "Vermis (superior e inferior)"),
            ("3", "Hemisferios cerebelosos laterales"),
            ("4", "Lóbulo anterior"),
            ("5", "Lóbulo medio"),
            ("6", "Pedúnculo cerebeloso superior"),
            ("7", "Pedúnculo cerebeloso medio"),
            ("8", "Pedúnculo cerebeloso inferior"),
            ("9", "Lóbulo floculonodular"),
        ]
    },
    "3.3.C": {
        "answers": [
            ("1", "Vermis (superior e inferior)"),
            ("6", "Pedúnculo cerebeloso superior"),
            ("10", "Núcleo del fastigio"),
            ("11", "Núcleos globoso y emboliforme"),
            ("12", "Núcleo dentado"),
        ]
    },
    "3.4.A": {
        "answers": [
            ("1", "Intumescencia cervical (médula espinal)"),
            ("2", "Duramadre"),
            ("3", "Intumescencia lumbosacra (médula espinal)"),
            ("4", "Cono medular"),
            ("5", "Cola de caballo"),
            ("6", "Filum terminal"),
            ("7", "Foramen magno"),
            ("8", "Cisterna lumbar"),
        ]
    },
    "3.4.B": {
        "answers": [
            ("1", "Intumescencia cervical (médula espinal)"),
            ("9", "Raíz dorsal"),
            ("10", "Ligamento dentado"),
        ],
    },
    "3.5.A": {
        "answers": [
            ("1", "Cuerpo vertebral"),
            ("2", "Espacio epidural con grasa"),
            ("3", "Duramadre"),
            ("4", "Espacio subaracnoideo"),
            ("5", "Apófisis espinosa"),
            ("6", "Rama dorsal del nervio espinal"),
            ("7", "Ganglio de la raíz dorsal"),
            ("8", "Raíz dorsal"),
            ("9", "Raíz ventral"),
            ("10", "Ramos comunicantes blanco y gris"),
        ],
    },
    "3.5.B": {
        "answers": [
            ("1", "Cuerpo vertebral"),
            ("4", "Espacio subaracnoideo"),
            ("5", "Apófisis espinosa"),
            ("7", "Ganglio de la raíz dorsal"),
            ("8", "Raíz dorsal"),
            ("9", "Raíz ventral"),
            ("10", "Ramos comunicantes blanco y gris"),
            ("11", "Cola de caballo"),
            ("12", "Filum terminal"),
        ],
    },
    "3.6.A": {
        "answers": [
            ("1", "Cordones posteriores"),
            ("2", "Intumescencia cervical (sustancia gris)"),
            ("3", "Cordones laterales"),
            ("4", "Cordones anteriores"),
            ("5", "Asta posterior"),
            ("6", "Zona intermedia"),
            ("7", "Asta anterior"),
            ("8", "Intumescencia lumbosacra (sustancia gris)"),
        ],
    },
    "3.6.B": {
        "answers": [
            ("9", "Tractos espinotalámico y espinorreticular"),
            ("10", "Fascículo cuneiforme"),
            ("11", "Fascículo grácil"),
            ("12", "Tracto corticoespinal lateral"),
            ("13", "Tracto rubroespinal"),
            ("14", "Tractos reticuloespinales"),
            ("15", "Tractos vestibuloespinales"),
        ],
    },
    "4.1": {
        "answers": [
            ("1", "Asta anterior del ventrículo lateral izquierdo"),
            ("2", "Cuerpo del ventrículo lateral izquierdo"),
            ("3", "Asta temporal del ventrículo lateral izquierdo"),
            ("4", "Asta occipital del ventrículo lateral izquierdo"),
            ("5", "Acueducto cerebral (de Silvio)"),
            ("6", "Cuarto ventrículo"),
            ("7", "Orificio medio (foramen de Magendie)"),
            ("8", "Tercer ventrículo"),
            ("9", "Foramen interventricular de Monro"),
        ],
    },
    "4.2": {
        "answers": [
            ("1", "Plexo coroideo del tercer ventrículo"),
            ("2", "Foramen interventricular de Monro"),
            ("3", "Tálamo"),
            ("4", "Lámina terminal"),
            ("5", "Colículos superiores e inferiores"),
            ("6", "Puente"),
            ("7", "Cuarto ventrículo"),
            ("8", "Amígdala del cerebelo"),
            ("9", "Orificio medio de Magendie"),
            ("10", "Acueducto cerebral (de Silvio)"),
            ("11", "Plexo coroideo del cuarto ventrículo"),
        ],
    },
    "4.3": {
        "answers": [
            ("1", "Venas puente"),
            ("2", "Plexo coroideo del ventrículo lateral"),
            ("3", "Seno sagital superior"),
            ("4", "Espacio subaracnoideo"),
            ("5", "Granulaciones aracnoideas"),
            ("6", "Cisterna de la vena cerebral magna (de Galeno)"),
            ("7", "Cisterna magna"),
            ("8", "Plexo coroideo del cuarto ventrículo"),
            ("9", "Cisterna prepontina"),
            ("10", "Cisterna interpeduncular"),
            ("11", "Plexo coroideo del tercer ventrículo"),
            ("12", "Cisterna quiasmática"),
          ],
    },
    "4.4.A": {
        "answers": [
            ("1", "Arteria carótida externa derecha"),
            ("2", "Arterias cerebrales anteriores"),
            ("3", "Arteria comunicante anterior"),
            ("4", "Arterias comunicantes posteriores"),
            ("5", "Arteria meningea media"),
            ("6", "Arterias cerebrales posteriores"),
            ("7", "Arteria basilar"),
            ("8", "Arteria carótida interna derecha"),
            ("9", "Arterias vertebrales"),
            ("10", "Arteria carótida común derecha"),
            ("11", "Arterias cerebrales medias"),
          ],
    },
    "4.4.B": {
        "answers": [
            ("2", "Arterias cerebrales anteriores"),
            ("3", "Arteria comunicante anterior"),
            ("4", "Arterias comunicantes posteriores"),
            ("6", "Arterias cerebrales posteriores"),
            ("7", "Arteria basilar"),
            ("9", "Arterias vertebrales"),
            ("11", "Arterias cerebrales medias"),
            ("12", "Arteria espinal anterior"),
            ("13", "Polígono de Willis (línea de puntos)"),
          ],
    },
    "5.1": {
        "answers": [
            ("1", "Asta dorsal de la médula espinal"),
            ("2", "Raíz dorsal"),
            ("3", "Ganglio de la raíz dorsal"),
            ("4", "Corpúsculo de Pacini"),
            ("5", "Fibras musculares esqueléticas con la placa terminal motora"),
            ("6", "Terminación nerviosa libre"),
            ("7", "Raíz ventral"),
            ("8", "Asta ventral de la médula espinal"),
            ("9", "Ganglio simpático colateral"),
            ("10", "Nervio esplácnico"),
            ("11", "Ganglio de la cadena simpática"),
            ("12", "Asta lateral de la médula espinal"),
          ],
    },
    "5.2.A": {
        "answers": [
            ("1", "Vasa nervorum (vasos longitudinales)"),
            ("2", "Epineuro (capas interna y externa)"),
            ("3", "Fascículos"),
            ("4", "Haces de fibras nerviosas en un fascículo"),
            ("5", "Perineuro"),
            ("6", "Axones en los haces de fibras nerviosas en los fascículos"),
          ],
    },
    "5.2.B": {
        "answers": [
            ("7", "Axones intactos"),
            ("8", "Vaina de mielina"),
            ("9", "Axones en disolución"),
          ],
    },
    "5.2.C": {
        "answers": [
            ("2", "Epineuro (capas interna y externa)"),
            ("5", "Perineuro"),
            ("8", "Vaina de mielina"),
            ("10", "Endoneuro"),
          ],
    },
    "5.3.A": {
        "answers": [
            ("1", "Intumescencia cervical de la médula espinal",),
            ("2", "Intumescencia lumbar de la médula espinal",),
            ("3", "Cono medular",),
            ("4", "Cauda equina (cola de caballo)",),
            ("5", "Filum terminal",),
          ],
    },
    "5.3.B": {
        "answers": [
            ("6", "Núcleo pulposo del disco intervertebral",),
            ("7", "Raíz nerviosa comprimida por el núcleo pulposo herniado",),
        ],
    },
    "5.3.C": {
        "answers": [
            ("8", "Hernia de un disco intervertebral",),
            ("9", "Disco intervertebral",),
        ],
    },
    "5.3.D": {
        "answers": [
            ("6", "Núcleo pulposo del disco intervertebral",),
            ("7", "Raíz nerviosa comprimida por el núcleo pulposo herniado",),
            ("8", "Hernia de un disco intervertebral",),
            ("9", "Disco intervertebral",),
        ],
    },
    "5.3.E": {
        "answers": [
            ("6", "Núcleo pulposo del disco intervertebral",),
            ("7", "Raíz nerviosa comprimida por el núcleo pulposo herniado",),
        ],
    },
    "5.4.A": {
        "answers": [
            ("1", "Cuerpo de una célula sensitiva primaria"),
            ("2", "Axón sensitivo amielínico"),
            ("3", "Axón sensitivo mielínico"),
            ("4", "Terminación nerviosa libre"),
            ("5", "Huso muscular"),
            ("6", "Motoneurona inferior"),
            ("7", "Fibras musculares esqueléticas"),
        ],
    },
    "5.4.B": {
        "answers": [
            ("1", "Cuerpo de una célula sensitiva primaria"),
            ("3", "Axón sensitivo mielínico"),
            ("5", "Huso muscular"),
            ("8", "Tracto espinocerebeloso"),
            ("9", "Neuronas sensitivas secundarias de los sistemas espinocerebelosos"),
        ],
    },
}

todo = [
    "5.6",
    "5.10",
    "5.11",
    "6.1",
    "7.1",
    "7.5",
    "7.6",
]


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
        st.button("Show answer", on_click=show_answer)
        if st.session_state.show_answer:
            st.markdown(answer)

st.button("New question", on_click=set_question)


with st.expander("Status Láminas"):
    st.markdown("#### Available:")
    st.code(" ".join(questions.keys()))
    st.markdown("#### TODO:")
    st.code(" ".join(todo))
