Texas Electricity Market Analyst
A local AI-powered assistant that helps analyze the Texas electricity market (ERCOT) using a SQLite database and a local LLM.

Project Goal
This project was created to let a language model safely interact with a local SQLite database. The goal is to explore trends, prices, and insights about the Texas electricity market in a simple chat interface.

How It Works
The AI runs on a local server and uses a custom tool that only allows safe SELECT queries on the database. This lets the AI pull real data and help form observations and conclusions.

Data Sources
All data used in this project comes from the Federal Reserve Economic Data (FRED) website: https://fred.stlouisfed.org
Specific series used:

10-Year Breakeven Inflation Rate: https://fred.stlouisfed.org/series/T10YIE
Average Price: Electricity per Kilowatt-Hour (U.S. City Average): https://fred.stlouisfed.org/series/APU000072610
Equity Market Volatility Tracker: Energy And Environmental Regulation: https://fred.stlouisfed.org/series/EMVENRGYENVREG

NOTE: All data and credit belong to fred.stlouisfed.org. This project uses the data for learning, research, and demonstration purposes only.

Database
The energy_market.db file is included in this repository so anyone can clone and run the project immediately.

All data originates from the Federal Reserve Economic Data (FRED) website: https://fred.stlouisfed.org
Full credit and thanks to FRED for making this data publicly available.

Features
Friendly real-time chat interface powered by Gradio
Runs completely locally using LM Studio
Secure read-only access to the energy market database
Streaming responses so you can see the AI thinking step by step
Focused on Texas electricity prices, volatility, and trends

Quick Start Checklist

Activate your virtual environment:
source venv/bin/activate          (Linux / Mac)
venv\Scripts\activate             (Windows)
Make sure LM Studio is running with the OpenAI-compatible server active
Check that the model name in config.py matches what you have loaded in LM Studio
Verify all file paths (especially the database)
Install dependencies: pip install -r requirements.txt

Note: This project was built using Python 3.12.11. Other versions might cause issues.

Development Note
This project was built by me. I used AI assistance to help debug problems, explain concepts, improve the code, and write documentation.

Recommended Tools
VS Code Extension: SQLite Viewer (great for easily browsing the database)
Use the built-in "query_energy_market_db" tool inside the chat for safe querying

Common Issues & Fixes

Path errors: Check the target_path in db_tool.py
Model not found: Make sure the model name in config.py matches LM Studio
Connection issues: Confirm LM Studio server is running on the correct port
No data returned: Check if the database has data for the dates you're asking about
Import errors: Double-check you're in the right virtual environment

How to Run

Activate the virtual environment
source venv/bin/activate
Start the app
python server.py

The interface should open at http://localhost:7860 (or the port you set in your config).
Tech Stack

Agent Framework: smolagents
Chat UI: Gradio
Local LLM: LM Studio
Database: SQLite
Environment Management: python-dotenv
