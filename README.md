# URL-Summarizer-API
This project is a high-performance **FastAPI** orchestrator that automates the pipeline of scraping web content and generating text summaries. 
It serves as the entry point for clients to request summaries of specific URLs.

# URL Summarizer API

This project is a high-performance **FastAPI** orchestrator that automates the pipeline of scraping web content and generating text summaries.
It serves as the entry point for clients to request summaries of specific URLs.

## Features

* **FastAPI Powered:** Built on a modern, high-performance web framework.
* **Asynchronous Processing:** Utilizes `async/await` for the crawling step to ensure non-blocking I/O.
* **Threaded Summarization:** Offloads the CPU-intensive summarization task using `asyncio.to_thread` to maintain server responsiveness.
* **Performance Metrics:** Returns the processing duration and length statistics in the API response.

## Project Structure

This file acts as the controller. Ensure your directory contains the following helper modules (as imported in the code):

* `orchestrator_fastapi.py` (Main entry point)
* `crawler_simple.py` (Contains logic to scrape text from a URL)
* `summarizer_simple.py` (Contains logic to summarize the text)

## Prerequisites

* Python 3.8+
* FastAPI
* Uvicorn

## Installation

1.  **Clone the repository** (or navigate to your project folder).
2.  **Install the required dependencies**:

    ```bash
    pip install fastapi uvicorn pydantic
    ```
    *(Note: You may also need to install dependencies required by your `crawler_simple` and `summarizer_simple` modules, such as `requests`, `beautifulsoup4`, or `transformers`).*

## Usage

### 1. Run the Server
Use the command provided in the file to start the uvicorn server:

```bash
uvicorn orchestrator_fastapi:app --host 0.0.0.0 --port 8000
