# Build the app based on MovieGPT from CreataAI.com.


# MovieGPT - Sample Code for API Calling AI Agent
 *From CreataAI.com*

## Overview
Sample code for building an AI agent that calls themoviedb.org's API 
The structure and method can be generalized for other APIs. You can modify this code and build another agent that calls different APIs and achieve different effects.

Can ask questions about movies or TV shows, and the chatbot will retrieve and present relevant information from the the movie database.

**Note: this is a skeleton AI agent to serve the purpose of demo. It is by no means optimized or bug free. As a matter of fact, there are many areas where the agent can be improved.**

## Features

- **API Calling**: Uses the themoviedb.org's API to fetch detailed information about movies and TV shows.
- **Information Extraction**: Understands user queries and extracts relevant information.
- **Text Summarization**: Provides concise summaries of movie or TV show information.
- **Tagging**: Categorizes movies or TV shows based on user queries.
- **Interactive Interface**: Offers a conversational interface through Streamlit.

## Getting Started

### Prerequisites

- Python  3.x
- OpenAI api key
- TheMovieDB.org's API access
- Streamlit for the web application interface

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/creataai/movieGPT.git
   ```
2. Navigate to the project directory:
   ```
   cd movieGPT
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Set up your environment variables in a `.env` file:
   ```
   OPENAI_API_KEY=your_openai_api_key
   TMDB_API_TOKEN=your_tmdb_api_key
   ```

### Running the Application

1. Run the Streamlit app:
   ```
   streamlit run app.py
   ```
2. Access the chatbot in your web browser at `http://localhost:8501`.

## Possible Issues
Here is the list of possible issues:
1. *ValidationError: 1 validation error for StructuredTool
   args_schema
   subclass of BaseModel expected (type=type_error.subclass; expected_class=BaseModel)*: 

   In utils/tools.py, try to replace: 
   ```
   from pydantic import BaseModel, Field"
   ``` 
   with

   ```
   from pydantic.v1 import BaseModel, Feild
   ```
   See more info here: https://github.com/langchain-ai/langchain/issues/9441
#
