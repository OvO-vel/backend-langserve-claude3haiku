import boto3
from botocore.config import Config
from langchain_core.messages import SystemMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.prompts.chat import HumanMessagePromptTemplate
from langchain_core.runnables import chain, Runnable

import config
from utils.llm_utils.claude3haiku import create_chat_claude3haiku_chain


# セッションの作成
session = boto3.Session(
    region_name=config.REGION_NAME,  # 使用するリージョンを指定
)

# Bedrock クライアントの初期化
BEDROCK = session.client(
    service_name='bedrock-runtime',
    config=Config(
        retries={
            'max_attempts': 3,
            'mode': 'standard',
        },
    ),
)

@chain
def chat_claude3haiku_chain_with_client(input_: dict) -> Runnable:
    print(
        '>>> chat_claude3haiku_chain_with_client()>>>\n',
        '実行時に Runnable chain を定義しています...\n',
    )
    return create_chat_claude3haiku_chain(client=BEDROCK)

prompt = ChatPromptTemplate.from_messages([
    SystemMessage(content='You are a helpful assistant.'),
    HumanMessagePromptTemplate.from_template('{input}'),
])

chat_claude3haiku_chain = prompt \
    | chat_claude3haiku_chain_with_client \
    | StrOutputParser()
