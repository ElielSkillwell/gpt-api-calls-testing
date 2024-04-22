import time
import os

from langchain_openai import AzureChatOpenAI
import utils._global as _global

def get_openai_model(model: str, 
                     temperature: float, 
                     max_tokens: int):
    # model_name is just ignored because it helps with all of this being functional.
    # Look at run_prompts.py function get_summaries and how llm_func is ran.

    api_key = os.getenv("AZURE_API_KEY")
    azure_endpoint = os.getenv("AZURE_ENDPOINT")
    llm = AzureChatOpenAI(
        api_version=_global.AZURE_API_VERSION,
        azure_endpoint=azure_endpoint,
        model=model,
        openai_api_key=api_key,
        temperature=temperature,
        max_tokens=max_tokens
    )
    return llm


def invoke_model(llm):
    start_time = time.time()
    response = llm.invoke('Who are you?')
    return time.time() - start_time