CONFIG ={
    "LMSTUDIO":{
        "model": "openai/gemma-4-e4b",          #lm studio is requires (openai/(whatever model))
        "base_url": "http://localhost:1234/v1",
        "api_key": "########",                  #not needed for lm studio but there in case
        "port":5630,
        "server_name": "127.0.0.1"
    },
    "AGENT":{
        "verbosity_level": 1,
        "max_steps": 12,
        "Prompt":
            """You are an expert Texas Electricity Market Analyst.

            You have a local database tool called `query_energy_market_db`.

            IMPORTANT RULES:
            - ALWAYS try to use the database tool first for any question about prices, trends, historical data, volatility, etc.
            - Only use web search if the database tool fails or returns no data.
            - For greetings like "hello", reply normally without tools.
            Output tool calls in clean JSON format.""",
        "History": 10,
    }
    
}


