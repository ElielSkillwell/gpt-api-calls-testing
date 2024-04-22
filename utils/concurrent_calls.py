import concurrent.futures

import utils._global as _global
from utils.model_funcs import invoke_model



def run_thread_pool(llms, pool_size):
    for llm in llms:
        with concurrent.futures.ThreadPoolExecutor(max_workers=pool_size) as executor:
            futures = [executor.submit(invoke_model, llm) for i in range(pool_size)]

            concurrent.futures.wait(futures)

            execution_times = [future.result() for future in futures]

            avg_call_time = sum(execution_times) / len(execution_times)
            total_time = sum(execution_times)
            print(f"Average Call Time for {llm.model_name}: {avg_call_time} s.")
            print(f"Total Pool Execution Time for {llm.model_name}: {total_time} s.")