
#########################################
# IMPORT SoftwareAI Libs 
from CoreApp._init_libs_ import *
#########################################
# IMPORT SoftwareAI Functions
from ..Functions._init_functions_ import *
#########################################

def submit_output_get_current_datetime(function_name,
                                function_arguments,
                                tool_call,
                                threead_id,
                                client,
                                run
                                ):


    if function_name == 'get_current_datetime':
        args = json.loads(function_arguments)
        result = get_current_datetime()
        tool_call_id = tool_call.id
        client.beta.threads.runs.submit_tool_outputs(
            thread_id=threead_id,
            run_id=run.id,
            tool_outputs=[
                {
                    "tool_call_id": tool_call_id,
                    "output": json.dumps(result)
                }
            ]
        )

