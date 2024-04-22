import concurrent.futures
import time
import asyncio
import os

from dotenv import load_dotenv
import utils._global as _global

from utils.model_funcs import get_openai_model
from utils.concurrent_calls import run_thread_pool



def main():
    load_dotenv()
    llm_4 = get_openai_model('gpt-4', 0.2, 512)
    llm_35 = get_openai_model("gpt-35-turbo", 0.2, 512)

    run_thread_pool([llm_4, llm_35], 30)


if __name__ == '__main__':
    main()