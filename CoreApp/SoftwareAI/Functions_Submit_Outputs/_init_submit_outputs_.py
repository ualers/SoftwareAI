from .create_github_repo_and_upload_submit_outputs import submit_output_create_github_repo_and_upload
from .get_current_datetime_submit_outputs import submit_output_get_current_datetime
from .improve_code_and_create_pull_request_submit_outputs import submit_output_improve_code_and_create_pull_request
from .test_software_submit_outputs import submit_output_test_software
from .add_project_map_submit_outputs import submit_output_add_projectmap_to_github

def _init_output_(function_name,
                function_arguments,
                tool_call,
                threead_id,
                client,
                run):
    
    submit_output_create_github_repo_and_upload(function_name,
                function_arguments,
                tool_call,
                threead_id,
                client,
                run)
    submit_output_get_current_datetime(function_name,
                function_arguments,
                tool_call,
                threead_id,
                client,
                run)
    submit_output_improve_code_and_create_pull_request(function_name,
                function_arguments,
                tool_call,
                threead_id,
                client,
                run)
    submit_output_test_software(function_name,
                function_arguments,
                tool_call,
                threead_id,
                client,
                run)
    submit_output_add_projectmap_to_github(function_name,
                function_arguments,
                tool_call,
                threead_id,
                client,
                run)

