import json
import re
from pathlib import Path

import streamlit as st
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS, TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


st.set_page_config(
    page_title="FAQ Chatbot",
    page_icon="💬",
    layout="centered",
)


DATA_FILE = Path(__file__).parent / "faqs.json"
MATCH_THRESHOLD = 0.20

stemmer = PorterStemmer()
stop_words = set(ENGLISH_STOP_WORDS)


def preprocess_text(text: str) -> str:
    """Clean and normalize text before similarity matching."""
    tokens = re.findall(r"[a-zA-Z0-9']+", text.lower())

    processed_tokens = [
        stemmer.stem(token)
        for token in tokens
        if token not in stop_words and len(token) > 1
    ]

    return " ".join(processed_tokens)


@st.cache_data
def load_faqs() -> list[dict]:
    """Load and validate the FAQ knowledge base."""
    with DATA_FILE.open("r", encoding="utf-8") as file:
        data = json.load(file)

    if not isinstance(data, list) or not data:
        raise ValueError("The FAQ file is empty or incorrectly formatted.")

    for item in data:
        if (
            "questions" not in item
            or "answer" not in item
            or not isinstance(item["questions"], list)
            or not item["questions"]
        ):
            raise ValueError("One or more FAQ entries are incorrectly formatted.")

    return data


@st.cache_resource
def create_search_index(faq_data_json: str):
    """Create the TF-IDF search index from all sample questions."""
    faq_data = json.loads(faq_data_json)

    sample_questions = []
    answer_indexes = []

    for answer_index, faq in enumerate(faq_data):
        for question in faq["questions"]:
            sample_questions.append(preprocess_text(question))
            answer_indexes.append(answer_index)

    vectorizer = TfidfVectorizer(
        ngram_range=(1, 2),
        sublinear_tf=True,
    )

    question_matrix = vectorizer.fit_transform(sample_questions)

    return vectorizer, question_matrix, answer_indexes


def find_answer(
    user_question: str,
    faq_data: list[dict],
    vectorizer: TfidfVectorizer,
    question_matrix,
    answer_indexes: list[int],
) -> tuple[str, float]:
    """Return the best matching FAQ answer and similarity score."""
    processed_question = preprocess_text(user_question)

    if not processed_question:
        return (
            "Please enter a clear question with a few meaningful words.",
            0.0,
        )

    user_vector = vectorizer.transform([processed_question])
    similarity_scores = cosine_similarity(
        user_vector,
        question_matrix,
    ).flatten()

    best_question_index = int(similarity_scores.argmax())
    best_score = float(similarity_scores[best_question_index])

    if best_score < MATCH_THRESHOLD:
        return (
            "I could not find a reliable answer to that question. "
            "Please rephrase it or ask about orders, delivery, returns, "
            "refunds, payments, or account support.",
            best_score,
        )

    faq_index = answer_indexes[best_question_index]
    return faq_data[faq_index]["answer"], best_score


st.title("FAQ Chatbot")
st.write(
    "Ask a question about orders, delivery, returns, payments, "
    "refunds, or customer support."
)


try:
    faqs = load_faqs()
    faqs_json = json.dumps(faqs, sort_keys=True)

    vectorizer, question_matrix, answer_indexes = create_search_index(
        faqs_json
    )

except (FileNotFoundError, json.JSONDecodeError, ValueError) as error:
    st.error(f"The FAQ knowledge base could not be loaded: {error}")
    st.stop()


if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": (
                "Hello! Ask me a question about shopping, delivery, "
                "returns, payments, or your account."
            ),
        }
    ]


with st.sidebar:
    st.subheader("Example questions")
    st.write("• How can I track my order?")
    st.write("• What is your return policy?")
    st.write("• When will I receive my refund?")
    st.write("• Which payment methods do you accept?")

    if st.button("Clear conversation", use_container_width=True):
        st.session_state.messages = [
            {
                "role": "assistant",
                "content": "Conversation cleared. What would you like to ask?",
            }
        ]
        st.rerun()


for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])


user_question = st.chat_input("Type your question here...")


if user_question:
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_question,
        }
    )

    with st.chat_message("user"):
        st.write(user_question)

    answer, confidence = find_answer(
        user_question,
        faqs,
        vectorizer,
        question_matrix,
        answer_indexes,
    )

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer,
        }
    )

    with st.chat_message("assistant"):
        st.write(answer)

        with st.expander("Match information"):
            st.write(f"Similarity score: {confidence:.2f}")
