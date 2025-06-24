# Langchain-project-series
AI-Powered Product &amp; Social Marketing Content Generator

AI-Powered Product & Social Marketing Content Generator

This Streamlit application utilizes the power of Langchain, Ollama, and Langsmith to automate the generation of engaging marketing content for your products. It creates compelling product titles, descriptions, and social media captions from a product name and its key features, saving you time and ensuring a consistent brand message. With Langsmith integration, you can monitor, debug, and improve the performance of your AI-powered content generation pipeline.

## Features

Automated Content Generation: Generates product titles, descriptions, and social media captions using a local language model.
SEO Optimization: Allows you to incorporate a specified SEO keyword or tone modifier into the generated content for improved search engine visibility.
Dark Mode/Light Mode: Offers a user-friendly interface with customizable light and dark mode themes.
Local LLM Processing: Leverages Ollama, enabling local, offline processing without requiring API keys for large language models.
Langsmith Integration: Provides a robust backend for tracing, monitoring, and debugging your AI-powered content generation, enhancing performance and reliability.

## Use Cases

This project is ideal for:

E-commerce Businesses: Speed up the creation of compelling and informative product descriptions for large inventories while maintaining a consistent brand voice.
Social Media Managers: Create captivating social media captions quickly, driving engagement and directing traffic to online stores.
Marketing Teams: Generate ideas and variations for product marketing copy, facilitating A/B testing and campaign optimization.
Small Businesses: Produce high-quality marketing materials efficiently without the need for extensive copywriting resources.

## Technologies Used

Streamlit: To build the interactive and visually appealing web interface.
Langchain: As a powerful framework for orchestrating language model interactions and building complex applications.
Ollama: A tool for running large language models locally, providing a cost-effective and privacy-focused solution.
Python: The primary programming language.
CSS: For providing custom UI styling to create an attractive user experience.
Langsmith: For tracing, monitoring, and debugging Langchain applications.

## Setup Instructions

1. Install Python Dependencies:

    pip install streamlit langchain langchain_community python-dotenv

2. Install Ollama: Follow the instructions on the Ollama website (https://ollama.com/) to download and install Ollama.

3. Download a Language Model: Use Ollama to download a language model (e.g., TinyLlama) for the app to use:

    ollama pull tinyllama

    If you encounter memory issues, choose a smaller model.

4. Set up Langsmith:

    Create a Langsmith Account: Sign up for a free Langsmith account at https://smith.langchain.com/.
    Generate an API Key: Follow the instructions on the Langsmith website to generate an API key.
    Set Environment Variables: Create a .env file in your project directory and add your Langsmith API key and a project name:

        LANGCHAIN_TRACING_V2=true
        LANGCHAIN_API_KEY=YOUR_LANGSMITH_API_KEY
        LANGCHAIN_PROJECT=Product-Social-Marketing-Generator

        Remember to replace `YOUR_LANGSMITH_API_KEY` with your actual Langsmith API key. Add .env to your .gitignore to protect your API key.

5. Run the Streamlit Application:

    streamlit run your_script_name.py

## Usage

1. Ensure Ollama is Running: Make sure the Ollama server is running in the background before running this Streamlit app.
2. Open the Streamlit App: The Streamlit app will open in your web browser.
3. Enter Product Information: Enter the product name, features (comma-separated), and an optional SEO keyword or tone modifier in the input fields.
4. Generate Content: Click the "Generate" button.
5. View Results: The generated product title, description, and social media caption will be displayed below the input fields.
6. Toggle Dark Mode: Switch between light and dark mode using the toggle button.
7. Monitor Performance with Langsmith: Log into your Langsmith account and navigate to your project ("Product-Social-Marketing-Generator"). You can view traces, monitor performance metrics, and debug issues with your Langchain application.

## Langsmith Integration Details

This project is integrated with Langsmith to provide:

Tracing: Langsmith automatically tracks the execution flow of your Langchain application, allowing you to visualize the steps involved in generating the content.
Monitoring: Langsmith collects performance metrics such as latency, token usage, and success rates, enabling you to identify bottlenecks and areas for improvement.
Debugging: With detailed trace information, you can easily identify and debug issues such as prompt errors, LLM failures, and incorrect chain execution.
Feedback Collection: Langsmith allows you to collect feedback from users or evaluators on the quality of the generated content, enabling you to continuously improve the performance of your application.
Dataset Management: You can create and manage datasets to evaluate the performance of your application on different inputs and scenarios.

By leveraging Langsmith, you can gain valuable insights into the behavior of your AI-powered content generation pipeline and continuously optimize its performance for better results.

## Important Notes

Ollama Must Be Running: Ensure Ollama is running in the background before running this Streamlit app.
Model Downloaded: Make sure the specified model (tinyllama or a similar small model) is downloaded using `ollama pull <model_name>`.
Memory Limits: This app can be memory-intensive, especially with larger language models. Close other applications to free up memory if you encounter errors. If a small model still doesn't work, there may not be adequate free memory.
Model Selection: The best results will come from models that meet your performance requirements while fitting your memory constraints. Experiment accordingly.
Langsmith API Key: Ensure that you have correctly set up the `LANGCHAIN_API_KEY` environment variable with your Langsmith API key.
