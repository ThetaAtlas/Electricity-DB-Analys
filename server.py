import gradio as gr
from agent import predict
from config import CONFIG

if __name__ == "__main__":
    print("Starting Texas Electricity Market Analyst...")

    demo = gr.ChatInterface(
        fn=predict,                                                             #function Created in agent
        title="Texas Electricity Market Analyst",                               #Title of the window
        description="Local AI Agent powered by LM Studio + SQLite Database",    
        examples=[
            "What was the average electricity price in 2024?",
            "Show me summer price trends in ERCOT",
            "How has volatility changed over the last 3 years?",
        ],
        chatbot=gr.Chatbot(height=720),                                         #chatbot window
    )

    print(f"Server running at http://{CONFIG["LMSTUDIO"]["server_name"]}:{CONFIG["LMSTUDIO"]["port"]}")
    demo.launch(
        server_name=CONFIG["LMSTUDIO"]["server_name"],
        server_port=CONFIG["LMSTUDIO"]["port"],
        share=False,
        debug=True
    )