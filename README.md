# CrewAI RAG Deep Dive

This repository contains a deep dive into using CrewAI with RAG (Retrieval-Augmented Generation) techniques. The project showcases how to set up and utilize various agents, tools, and tasks within CrewAI to perform specific operations, such as analyzing PDFs and YouTube channels, extracting information, and generating structured outputs.

## Table of Contents

- [Project Structure](#project-structure)
- [Setup and Installation](#setup-and-installation)
- [Agents and Tasks](#agents-and-tasks)
- [Examples](#examples)
- [YouTube API Setup](#youtube-api-setup)
- [Goal](#goal)
- [Contributing](#contributing)
- [License](#license)

## Project Structure

```markdown
crewai-rag-deep-dive/
├── .vscode/
│ └── settings.json
├── 1_pdf/
│ ├── .env
│ ├── 1_crew.py
│ ├── 2_crew_custom_model_and_embed.py
│ └── example_home_inspection.pdf
├── 2_youtube_and_web/
│ ├── tools/
│ │ ├── **init**.py
│ │ ├── AddVideoToVectorDBTool.py
│ │ └── FetchLatestVideosFromYouTubeChannelTool.py
│ ├── .env
│ ├── crew.py
│ └── main.py
├── .gitignore
├── poetry.lock
├── pyproject.toml
└── README.md
```

### Overview of Key Files and Directories

- **1_pdf/**: Contains code and environment configurations for working with PDF documents.

  - `1_crew.py`: Basic setup for processing home inspection PDFs.
  - `2_crew_custom_model_and_embed.py`: Custom configurations for processing PDFs using specific LLMs and embedders.
  - `example_home_inspection.pdf`: Sample PDF document used for testing.

- **2_youtube_and_web/**: Contains code and tools for processing YouTube channels and videos.
  - `tools/`: Directory containing custom tools.
    - `AddVideoToVectorDBTool.py`: Tool for adding YouTube videos to a vector database.
    - `FetchLatestVideosFromYouTubeChannelTool.py`: Tool for fetching the latest videos from a YouTube channel.
  - `crew.py`: Main script for setting up agents and tasks related to YouTube processing.
  - `main.py`: Entry point for running YouTube processing tasks.

## Setup and Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/bhancockio/crewai-rag-deep-dive.git
   cd crewai-rag-deep-dive
   ```

2. **Install dependencies**:
   Ensure you have [Poetry](https://python-poetry.org/docs/#installation) installed.

   ```bash
   poetry install --no-root
   ```

3. **Set up environment variables**:
   Create a `.env` file in the root directory and in relevant subdirectories (1_pdf, 2_youtube_and_web) with your API keys and other configurations.
   ```env
   YOUTUBE_API_KEY=your_youtube_api_key
   OPENAI_API_KEY=your_openai_api_key
   # Add other necessary environment variables
   ```

## Agents and Tasks

### PDF Processing Agents and Tasks

#### Agents

1. **Manager Agent**: Manages the workflow and delegates tasks.
2. **Research Agent**: Searches through the PDF to find relevant answers.
3. **Professional Writer Agent**: Writes professional emails based on the research agent's findings.

#### Tasks

1. **Answer Customer Question Task**: Searches the PDF to find answers to customer questions.
2. **Write Email Task**: Generates a professional email to contractors based on the research findings.

### YouTube Processing Agents and Tasks

#### Agents

1. **Scrape Agent**: Extracts content from YouTube videos and adds it to the vector database.
2. **Vector DB Processor**: Adds YouTube videos to the vector database.
3. **General Research Agent**: Gathers all required information from the YouTube channel.
4. **Follow-up Agent**: Performs thorough research to find any missing data.
5. **Fallback Agent**: Conducts final checks and searches the internet for any remaining information.

#### Tasks

1. **Scrape YouTube Channel Task**: Extracts information from the latest five videos of a specified YouTube channel.
2. **Process Videos Task**: Adds the extracted video URLs to the vector database.
3. **Find Initial Information Task**: Fills out the `ContentCreatorInfo` model with as much information as possible.
4. **Follow-up Task**: Searches for any missing data in the `ContentCreatorInfo` model.
5. **Fallback Task**: Performs final checks to ensure the `ContentCreatorInfo` model is fully populated.

## Examples

### Running PDF Processing

To run the PDF processing crew, navigate to the `1_pdf` directory and execute the script:

```bash
cd 1_pdf
python 1_crew.py
```

### Running YouTube Processing

To run the YouTube processing crew, navigate to the `2_youtube_and_web` directory and execute the script:

```bash
cd 2_youtube_and_web
python crew.py
```

## YouTube API Setup

To use the YouTube Data API v3 for this project, follow these steps:

1. **Enable the YouTube Data API v3**:

   - Go to the [YouTube Data API v3 page](https://console.cloud.google.com/marketplace/product/google/youtube.googleapis.com?q=search&referrer=search&project=crewai-415713) on Google Cloud Console.
   - Click on **Enable**.

2. **Create API Credentials**:
   - Go to the [API Credentials page](https://console.cloud.google.com/apis/credentials?project=crewai-415713) on Google Cloud Console.
   - Click on **Create Credentials** and select **API Key**.
   - Copy the generated API key and add it to your `.env` file as `YOUTUBE_API_KEY`.

## Goal

The primary goal of this project is to help people get comfortable with using RAG (Retrieval-Augmented Generation) techniques. This includes:

- **Scraping**: Extracting content from various sources.
- **Embedding**: Adding content to a vector database.
- **Querying**: Searching for information within the vector database.
- **Making and Using Tools**: Creating custom tools and using existing tools effectively.

### Use Cases

1. **Searching for Information in a Vector Store**: If the information is not found, look elsewhere.
   - Example: Hiring a job candidate and searching their resume.
   - Example: Sales job needing information about potential customers.
   - Example: Company looking through internal docs to answer a question before falling back to the web.

## Contributing

We welcome contributions to enhance the functionality and features of this project. Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature-name`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature/your-feature-name`).
6. Create a new Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
