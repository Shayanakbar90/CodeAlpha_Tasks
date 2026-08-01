# FAQ Chatbot

This project was developed as part of my CodeAlpha Artificial Intelligence Internship.
It is an NLP-based chatbot designed to answer frequently asked questions about an online shopping store. Users can ask about orders, delivery, returns, refunds, payments, account access, and customer support.

## Live Demo
[Open the FAQ Chatbot](https://codealpha-faqchatbot-prcdghhmrd3peacjyvfnac.streamlit.app/)

## Project Screenshot
[View the FAQ Chatbot screenshot](chatbot-demo.png)

## Features
- Chat-style interface built with Streamlit
- Frequently asked questions stored in a separate JSON file
- Text cleaning and normalization before matching
- Stop-word removal and word stemming
- TF-IDF feature extraction
- Cosine-similarity-based question matching
- Fallback response when no reliable match is found
- Conversation history during the current session
- Clear-conversation option
- Similarity score for each response
- Error handling for missing or incorrectly formatted FAQ data

## How It Works

The chatbot uses a collection of sample questions and answers stored in `faqs.json`.
When a user submits a question, the application:
1. Converts the text to lowercase.
2. Removes unnecessary characters and common stop words.
3. Reduces words to their basic stems using the Porter Stemmer.
4. Converts the processed question into a TF-IDF vector.
5. Compares it with the stored FAQ questions using cosine similarity.
6. Returns the answer linked to the closest matching question.

If the highest similarity score is below the selected threshold, the chatbot asks the user to rephrase the question instead of returning an unreliable answer.

## Technologies Used
- Python
- Streamlit
- scikit-learn
- NLTK
- JSON
- TF-IDF
- Cosine similarity

## FAQ Topics
The current knowledge base includes questions related to:
- Order tracking
- Delivery times
- Returns and exchanges
- Order cancellation
- Payment methods
- Damaged products
- Refund processing
- Shipping addresses
- International delivery
- Password recovery
- Discount codes
- Product availability
- Customer support

## Project Structure
```text
.
├── app.py
├── faqs.json
├── requirements.txt
├── chatbot-demo.png
├── README.md
└── .gitignore
```
## Run the Project Locally

Make sure Python is installed on your computer.

### 1. Download the repository

Download the repository as a ZIP file from GitHub and extract it.

### 2. Open the project folder

Open a terminal or command prompt inside the extracted folder.

### 3. Install the required packages

```bash
pip install -r requirements.txt
```

### 4. Start the application

```bash
streamlit run app.py
```

The application will open in your web browser.

## Example Questions
You can test the chatbot with questions such as:
- How can I track my order?
- How long does delivery take?
- Can I return an item?
- Which payment methods do you accept?
- When will I receive my refund?
- I forgot my password.
- How can I contact customer support?

## Limitations

This chatbot matches questions using words and phrases found in its FAQ knowledge base. It does not generate new answers or understand every possible question like a large language model.

Its accuracy can be improved by adding more question variations and answers to `faqs.json`.

## Project Status

The application has been developed and deployed. Its response quality depends on the number and variety of questions available in the FAQ knowledge base.

## Author

**Shayan Akbar**

Developed as part of the CodeAlpha Artificial Intelligence Internship.
