from .llm.llamaCpp.infer import LlamaGGUF


llm = LlamaGGUF()


def response_user_msg(msg: str):
    generator = llm.get_llm_generator(msg)
    if not generator:
        return "AI failed to respond."

    for chunk in generator:
        response_token = llm.get_llm_stream_out(chunk)
        yield response_token
