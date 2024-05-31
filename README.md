# Gemini Dynamo

## Index
1. [Overview](#overview)
2. [Key Features](#key-features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Tasks](#tasks)
6. [License](#license)
7. [Contact](#contact)

## Overview
**Gemini Dynamo** is a full-stack project designed to generate flashcards of key concepts from YouTube videos. Utilizing batches of documents, optimization processes, and a scalable and robust approach, this project seamlessly integrates state-of-the-art technologies to provide a comprehensive learning tool.

## Key Features
- **Generation of Flashcards:** Extract key concepts from YouTube videos and turn them into flashcards.
- **Summarizations:** Create concise summaries of YouTube video content.
- **Batch Document Loading:** Efficiently process large volumes of YouTube video content.
- **Chain Implementation:** Utilize LCEL with Langchain and VertexAI for enhanced processing.
- **Prompt Design:** Extract key concepts with optimized prompts.
- **Intuitive and Interactive UI:** Implemented using Vite + React for a seamless user experience.

## Installation
### Prerequisites
Ensure you have the following prerequisites installed:
- npm v9.0.0 or higher
- node.js v20.0.0 or higher
- Python 3.10 or higher
- axios
- langchain
- langchain-community
- langchain-google-vertexai
- pypdf
- youtube-transcript-api
- pytube
- tiktoken
- fastapi
- uvicorn
- tqdm
- Google Cloud access for VertexAI

### Step-by-Step Installation Guide
1. **Clone the Repository:**
    ```bash
    git clone https://github.com/AaronSosaRamos/mission-dynamo.git
    cd mission-dynamo
    ```

2. **Create the Virtual Environment:**
    ```bash
    cd backend
    virtualenv venv
    source venv/bin/activate
    ```

3. **Install Dependencies:**
    - Backend:
      ```bash
      pip install -r requirements.txt
      ```
    - Frontend:
      ```bash
      cd frontend/dynamocards
      yarn install
      ```

4. **Start the Project:**
    - Frontend:
      ```bash
      yarn dev
      ```
    - Backend:
      ```bash
      uvicorn main:app --reload
      ```

5. **Access the UI:**
    Open your browser and navigate to `http://localhost:5173/`.

## Usage
1. **Load a YouTube URL:** Enter a YouTube video URL to process and extract key concepts.
2. **Generate Flashcards:** Automatically create flashcards containing key concepts and their explanations.
3. **Manage Flashcards:** Easily remove any unnecessary key concepts from your flashcard set.

## Tasks
### Task 1: Set up a Google Cloud Account
- Create and configure your Google Cloud account to access VertexAI.

### Task 2: Create a GitHub Repository
- Initialize a new GitHub repository to manage your project code and collaborate.

### Task 3: Develop a FastAPI App
- Set up a FastAPI application to handle backend processes and API endpoints.

### Task 4: Allow Cross-Origin Requests Using CORSMiddleware
- Configure CORS settings to enable secure cross-origin requests from the frontend.

### Task 5: Organize Tools and Functions
- Create a `genai.py` file to encapsulate tools and functions, including logging configurations.

### Task 6: Import Generative AI Classes
- Import and instantiate VertexAI LLM classes within the `GeminiProcessor` class for advanced AI functionalities.

### Task 7: Enhance the YouTube Processing Class
- Develop a `YoutubeProcessor` class to handle the extraction of key concepts from YouTube videos.

### Task 8: Billing Character Calculation Enhancement
- Optimize billing calculations based on character usage to manage costs effectively.

### Task 9: Key Concept Refactoring and Output Formatting
- Refactor JSON string outputs for improved processing and integration.

### Task 10: Frontend Integration and Flashcard Handling
- Implement the process flow:
  - UI Request
  - FastAPI POST Method (`/analyze_video`)
  - `YoutubeProcessor` (retrieve YouTube documents)
  - `GeminiProcessor` (LLM model Vertex AI)
  - `YoutubeProcessor` (find key concepts)
  - Retrieve data and present as flashcards in the UI.

## License
[MIT License](LICENSE)

## Contact
For further information, please contact:
Aaron Sosa Ramos - [GitHub Profile](https://github.com/AaronSosaRamos)
