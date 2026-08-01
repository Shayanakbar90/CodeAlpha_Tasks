import streamlit as st
from deep_translator import GoogleTranslator


st.set_page_config(
    page_title="Language Translation Tool",
    page_icon="🌍",
    layout="centered",
)

st.title("Language Translation Tool")
st.write("Enter some text, choose the languages, and click Translate.")


@st.cache_data
def get_languages():
    """Return the languages supported by GoogleTranslator."""
    return GoogleTranslator().get_supported_languages(as_dict=True)


languages = get_languages()

source_languages = {
    "Auto Detect": "auto",
    **{name.title(): code for name, code in languages.items()},
}

target_languages = {
    name.title(): code for name, code in languages.items()
}


source_column, target_column = st.columns(2)

with source_column:
    source_name = st.selectbox(
        "Source language",
        options=list(source_languages.keys()),
    )

with target_column:
    target_names = list(target_languages.keys())

    default_target = (
        target_names.index("English")
        if "English" in target_names
        else 0
    )

    target_name = st.selectbox(
        "Target language",
        options=target_names,
        index=default_target,
    )


input_text = st.text_area(
    "Text to translate",
    placeholder="Type or paste your text here...",
    height=180,
)


if st.button("Translate", type="primary", use_container_width=True):

    if not input_text.strip():
        st.warning("Please enter some text before translating.")

    else:
        source_code = source_languages[source_name]
        target_code = target_languages[target_name]

        if source_code == target_code:
            st.info("Please choose two different languages.")

        else:
            try:
                translated_text = GoogleTranslator(
                    source=source_code,
                    target=target_code,
                ).translate(input_text.strip())

                st.subheader("Translated text")
                st.code(translated_text, language=None)
                st.caption(
                    "Use the copy icon in the result box to copy the translation."
                )

            except Exception:
                st.error(
                    "The translation could not be completed. "
                    "Check your internet connection and try again."
                )
