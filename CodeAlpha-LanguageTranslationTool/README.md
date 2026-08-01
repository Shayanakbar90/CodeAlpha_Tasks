# Language Translation Tool

A web-based language translation application developed as part of my CodeAlpha Artificial Intelligence Internship.
The application allows users to enter text, select the source and target languages, and receive the translated result through a simple interface.

## Live Demo

[Open the Language Translation Tool](https://codealpha-languagetranslationtool-rpdqjcy32ksyscug6j2xvu.streamlit.app/)

## Project Screenshot

[Language Translation Tool](translation-demo.png)

## Features
- Translate text between multiple languages
- Automatically detect the source language
- Select the source and target languages
- Display the translated result clearly
- Warn the user when the text box is empty
- Prevent translation when the same language is selected twice
- Handle translation and connection errors

## Technologies Used
- Python
- Streamlit
- deep-translator (`GoogleTranslator`)

## How It Works
The user enters text and selects the source and target languages. When the **Translate** button is clicked, the application processes the text using the `GoogleTranslator` class provided by the `deep-translator` package.
The translated text is then displayed on the screen. The source language can also be set to **Auto Detect** when the original language is unknown.

## Project Structure
```text
.
├── app.py
├── requirements.txt
├── translation-demo.png
├── README.md
└── .gitignore
```
## Run Locally

Make sure Python is installed on your computer.

### 1. Download the repository

Download the repository as a ZIP file from GitHub and extract it on your computer.

### 2. Open the project folder

Open a terminal or command prompt inside the extracted project folder.

### 3. Install the required packages

```bash
pip install -r requirements.txt
```
### 4. Start the application

```bash
streamlit run app.py
```
The application will open in your web browser.

## Project Status

The main translation functionality has been completed, tested, and deployed successfully.

## Author

**Shayan Akbar**

Developed as part of the CodeAlpha Artificial Intelligence Internship.
