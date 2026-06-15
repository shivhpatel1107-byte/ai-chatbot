# Task 4 – AI Chatbot with Simple NLP

A Python chatbot that uses **NLTK** for basic Natural Language Processing.

## Features
- Tokenization, stopword removal, lemmatization
- Intent detection using keyword matching
- Part-of-Speech (POS) tagging
- Rule-based sentiment analysis
- Debug mode to see NLP pipeline in action

## Tech Used
- Python 3.x
- NLTK (Natural Language Toolkit)

## Setup & Run

```bash
# 1. Install dependency
pip install nltk

# 2. Run the chatbot
python chatbot.py
```

## Example Conversation

```
You: hello
Bot: Hello! How can I help you today?

You: what is nlp
Bot: Natural Language Processing (NLP) is a branch of AI...

You: tell me a joke
Bot: Why do programmers prefer dark mode? Because light attracts bugs! 🐛

You: bye
Bot: Goodbye! Have a great day!
```

## NLP Concepts Demonstrated
| Concept | Function |
|---|---|
| Tokenization | `tokenize()` |
| Stopword removal | `remove_stopwords()` |
| Lemmatization | `lemmatize()` |
| POS Tagging | `get_pos_tags()` |
| Sentiment Analysis | `detect_sentiment()` |
| Intent Detection | `match_intent()` |

## Project Structure
```
chatbot.py   ← main file with all NLP logic and chat loop
README.md    ← this file
```
