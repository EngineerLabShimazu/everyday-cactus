import os
from ask_sdk.standard import StandardSkillBuilder
from handlers.launch_request_handler import LaunchRequestHandler

table_name = 'cactus'
if os.environ.get('AWS_LAMBDA_FUNCTION_VERSION') == '$LATEST':
    table_name = 'cactus-dev'
sb = StandardSkillBuilder(table_name=table_name, auto_create_table=True)
sb.add_request_handler(LaunchRequestHandler())

handler = sb.lambda_handler()
