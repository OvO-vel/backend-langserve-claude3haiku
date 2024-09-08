from langchain_aws import ChatBedrock


def create_chat_claude3haiku_chain(client=None):
    print(
        '>>> create_chat_claude3haiku_chain() >>>\n',
        '以下のクライアント設定を用いて、ChatBedrock を初期化します:\n',
        f'{client=}\n',
    )
    return ChatBedrock(
        client=client,
        model_id='anthropic.claude-3-haiku-20240307-v1:0',
        model_kwargs=dict(temperature=0),
    )
