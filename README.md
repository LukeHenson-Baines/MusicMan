# MusicMan

MusicMan is a conversational music and playlist management assistant developed as a university project during the penultimate year of my MSci Computer Science degree at the University of Nottingham.

The project explores **Human–AI Interaction (HAI)** and natural language processing using classical machine-learning techniques. Users interact with MusicMan through natural-language text, which the system interprets to answer questions, hold simple conversations, and perform playlist-management operations.

> **Note:** MusicMan was developed as an academic project and is not intended to be a production-ready music assistant. It represents my approach to conversational AI at that stage of my degree. A modern implementation would use substantially different technologies; some ideas for how I would develop the system today are outlined below.

## Features

MusicMan supports several types of interaction:

- Natural-language intent classification
- Creation and deletion of playlists
- Adding and removing songs from playlists
- Viewing playlist contents
- Dataset-based question answering
- Basic conversational responses and small talk
- User-name customisation
- Current date and time queries
- Confirmation before certain destructive or state-changing operations

Playlist and song information is stored locally using CSV files, allowing the project to demonstrate the full interaction flow without relying on an external music service.

## How It Works

MusicMan separates natural-language interpretation from the deterministic functions responsible for carrying out user requests.

```text
                         ┌─────────────────────┐
                         │     User Input      │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │   Pre-processing    │
                         │ lowercase / cleanup │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │ Question Answering  │
                         │ TF-IDF + similarity │
                         └──────────┬──────────┘
                                    │
                              No QA match
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │ Intent Classifier   │
                         │ CountVectorizer     │
                         │ + Linear SVM        │
                         └──────────┬──────────┘
                                    │
              ┌─────────────────────┼─────────────────────┐
              │                     │                     │
              ▼                     ▼                     ▼
        Small Talk             Utility Intents      Playlist Intents
        Name Handling          Date / Time          Create / Delete
                                                   Add / Remove / View
                                                         │
                                                         ▼
                                                Deterministic Python
                                                     Functions
                                                         │
                                                         ▼
                                                   CSV Storage
```

### Intent Classification

The main intent classifier is implemented using **scikit-learn**.

Training phrases representing supported user intents are combined into a labelled dataset and transformed using `CountVectorizer`. A linear Support Vector Machine (`SVC`) is then trained to classify new user input.

Supported intents include:

- `small_talk`
- `name_inquiry`
- `change_name`
- `discoverability`
- `current_time`
- `current_date`
- `add_to_playlist`
- `remove_from_playlist`
- `view_playlist`
- `make_playlist`
- `delete_playlist`

The classifier is deliberately lightweight and is trained from predefined intent examples when used.

### Question Answering

MusicMan also contains a separate question-answering pathway based on a provided CSV dataset.

Questions are represented using **TF-IDF vectors**, with cosine similarity used to compare matching questions. Answers are retrieved from the corresponding dataset entries.

This component is intentionally limited in scope and should be considered a demonstration of classical text-retrieval techniques rather than an open-domain question-answering system.

### Small Talk

Simple conversational interactions are handled separately from operational playlist commands.

TF-IDF and cosine similarity are used to select an appropriate response from a predefined collection of conversational examples, allowing MusicMan to respond to greetings and other basic interactions.

### Playlist Management

Once MusicMan identifies a playlist-management intent, the corresponding operation is handled using conventional Python functions rather than machine learning.

The application can:

- Create a playlist
- Delete a playlist
- View a playlist
- Add a song to a playlist
- Remove a song from a playlist

Playlist data is persisted locally in CSV files. A separate song dataset acts as the catalogue from which songs can be added.

Confirmation is requested before playlist creation and deletion, separating the interpretation of the user's request from execution of the operation.

## Project Structure

```text
MusicMan/
├── code/
│   ├── main.py
│   ├── classification.py
│   ├── questionAnswering.py
│   ├── smallTalk.py
│   ├── intentData.py
│   ├── playlistManagement.py
│   ├── songChanges.py
│   ├── nameManagement.py
│   ├── dateTime.py
│   └── csvUtil.py
│
├── datasets/
│   ├── qaDataset.csv
│   └── songDataset.csv
│
├── requirements.txt
├── .gitignore
└── README.md
```

## Technologies

- **Python**
- **scikit-learn**
  - Support Vector Machines
  - CountVectorizer
  - TF-IDF
  - Cosine similarity
- **NLTK**
  - Tokenisation
  - N-grams
- **CSV-based local persistence**

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd <repository-name>
```

Create and activate a virtual environment.

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

MusicMan uses NLTK's tokenizer data. If it is not already installed, run:

```python
import nltk
nltk.download("punkt")
```

Depending on the installed NLTK version, additional tokenizer resources may also be requested when the application is first run.

## Running MusicMan

The project currently uses relative paths between the `code` and `datasets` directories, so run the application from the `code` directory:

```bash
cd code
python main.py
```

MusicMan will introduce itself and then accept natural-language input through the terminal.

For example:

```text
You: create a new playlist
MusicMan: Sure! What would you like to name your new playlist?

You: Favourites
MusicMan: You want to create a playlist named 'Favourites'. Is that correct? (Yes/No)

You: Yes
MusicMan: Great! I've created a new playlist named 'Favourites'.
```

Enter:

```text
bye
```

to exit the application.

## Limitations

This project was developed for an academic Human–AI Interaction assignment rather than as a production system, and consequently has several deliberate or practical limitations.

The intent classifier is trained from a small set of manually defined example phrases, limiting its ability to generalise to significantly different language. Question answering operates over a fixed dataset rather than external or real-time knowledge, while music and playlist data are stored locally using CSV files.

There is also no integration with a real music-streaming service, meaning that MusicMan manages representations of songs and playlists rather than controlling actual playback.

These limitations reflect both the scope of the original assignment and the NLP techniques explored during its development.

## How I Would Build It Today

If I were developing MusicMan as a production-oriented application today, I would retain the basic principle of separating **natural-language understanding from deterministic application logic**, while replacing much of the classical NLP pipeline with modern AI and API tooling.

A possible architecture would be:

```text
Voice Input
    │
    ▼
Speech-to-Text
    │
    ▼
LLM
Intent recognition + entity extraction
    │
    ▼
Structured Action
    │
    ▼
User Confirmation
(for relevant state-changing operations)
    │
    ▼
Application / Tool Layer
    │
    ▼
Music Streaming API
    │
    ▼
Playback / Playlist Operation
    │
    ▼
Natural-Language Response
```

Rather than classifying a request into one of a small number of predefined intents, an LLM could interpret conversational requests and produce constrained structured outputs representing permitted application actions.

For example:

```text
User:
"Add Bohemian Rhapsody to my driving playlist."

MusicMan:
"You'd like me to add 'Bohemian Rhapsody' to your 'Driving'
playlist. Is that correct?"

User:
"Yes."

MusicMan:
"Done — I've added it to your Driving playlist."
```

Following confirmation, deterministic application code could execute the operation through a music service API such as the **Spotify Web API**.

The same architecture could support:

- Searching for artists, albums and tracks
- Creating and deleting real playlists
- Adding and removing tracks
- Controlling playback
- Context-aware conversational requests
- Speech-to-text input
- Text-to-speech responses
- Conversation history and user preferences
- Structured LLM tool/function calling
- Authentication and per-user music libraries

Crucially, I would not allow the language model itself to directly mutate playlist state. The model would interpret the user's request and generate a constrained action; application code would validate and execute that action through the external API. Confirmation could additionally be required for destructive or ambiguous requests.

This would preserve one of the useful architectural ideas in the original project — **separating probabilistic natural-language interpretation from deterministic operations** — while replacing the constrained NLP components with technologies better suited to a modern conversational assistant.

## Background

MusicMan was created during the penultimate year of my **MSci Computer Science degree at the University of Nottingham** as part of a Human–AI Interaction module.

The aim was to explore techniques for interpreting natural-language input and designing interactions between a user and an AI-driven system.

The project therefore represents an academic exploration of conversational AI and classical NLP rather than a finished consumer application.