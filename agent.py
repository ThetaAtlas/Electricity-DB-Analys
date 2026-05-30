from smolagents import ToolCallingAgent, LiteLLMModel
from smolagents.gradio_ui import stream_to_gradio
from dotenv import load_dotenv
from tools.db_tool import DatabaseQueryTool
from pathlib import Path
from config import CONFIG

#load enviroment variables from the venv
load_dotenv()

#sets up the llm model using lite llm more optimized and better that "openai" libray
model = LiteLLMModel(
    model_id=CONFIG["LMSTUDIO"]["model"],         #platfrom/model name so lm studio is (openai/model)
    api_base=CONFIG["LMSTUDIO"]["base_url"],   #location or streaming of the lm model or loaction
    api_key=CONFIG["LMSTUDIO"]["api_key"],                   #lm studio has no api key so you can put whatever 
)

db_tool = DatabaseQueryTool()              #setting up and allowing tool to query database

agent = ToolCallingAgent(                  #define agent we are making
    model=model,                           #model which we defined above
    tools=[db_tool],                       #tools it can use or acess
    add_base_tools=True,                   # Keep this for web search fallback
    verbosity_level=CONFIG["AGENT"]["verbosity_level"],                     #how much debug info it gives lower is less higer is more 
    max_steps=CONFIG["AGENT"]["max_steps"]                          #loops and times it can think through
)

#prompt or purpouse helps control what data we get and reponse types make sure to use """ """
agent.prompt_templates["system_prompt"] = CONFIG["AGENT"]["Prompt"]
print("Agent ready - Database tool initialized")

#controls entire message and communication system
def predict(message: str, history):
    if not message or not str(message).strip(): #if no first message say hello into the chat
        message = "Hello! I'm your Texas Electricity Market Analyst."

    messages = []       #keeps track of our messages
    yield messages      # Required first yield for Gradio streaming
    
#Trimming
    try:
        # Optional: Limit history sent to the model (recommended)
        if history and len(history) > CONFIG["AGENT"]["History"]:           # Keep amount specified in config
            trimmed_history = history[CONFIG["AGENT"]["History"]:]         # Trims history
        else:
            trimmed_history = history               #just passes the history
            
#Agent execution
        for step in stream_to_gradio(               # stream_to_gradio runs the agent and yields each step (thinking + tool calls + final answer)
            agent, 
            task=message,
            reset_agent_memory=False                # Keeps conversation memory across turns
        ):
            content = getattr(step, "content", str(step))                  #gose through and gets the content for that step if it is not a string we make it one and convert that to message
            messages.append({"role": "assistant", "content": content})
            
            history = trimmed_history, 
            yield messages                                                 # Yield so Gradio can show it live (streaming effect)I

#Error handling
    except Exception as e:                                                #error handling
        error_msg = f"Error: {str(e)}"                                 #if stuff happens create error as string
        print(error_msg)                                                  #print error
        messages.append({"role": "assistant", "content": error_msg})     #append AI error
        yield messages                                                  #yeild messages
