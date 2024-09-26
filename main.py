from chat_prompt.prompt import ExecuteLlm
DEFAULT_MODEL_NAME = "gpt-4o"

# template = """
#  Greet {user_name} and ask for address {address}
# """

# actual_data = {
#     "user_name": "Bob hamal", "address": "you live"
# }

# dynamic_vars = ['user_name', 'address']

# api_key = 'sk-proj-QpjFGYzInc8IeS0FEvuuT3BlbkFJV3muZkrMIWB1hLRnxP5f'


class OpenaiChatPrompt:
    def run(self, dynamic_var: list[str], data: dict, question: dict, api_key: str, template: str, model_name: str = DEFAULT_MODEL_NAME) -> None:
        prompt = ExecuteLlm(
            dynamic_var, data, question, api_key, model_name, template
        )
        response = prompt.run_prompt()
        return response


# if __name__ == '__main__':
#     prompt_response = OpenaiChatPrompt()
#     prompt_response.run(dynamic_var=dynamic_vars, data=actual_data, question=actual_data,
#                         api_key=api_key, template=template)
