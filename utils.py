from prompt_template import system_template_text,user_template_text
from langchain_openai import ChatOpenAI
from langchain.output_parsers import PydanticOutputParser
from langchain.prompts import ChatPromptTemplate
from ig_model import ig

import os

def generate_ig(theme, openai_api_key): #定義函數（參數: 主題、金鑰）
    #建立提示
    prompt=ChatPromptTemplate.from_messages([
        ("system",system_template_text), #由另一個檔案導入變量
        ("user",user_template_text) #由另一個檔案導入變量
    ])
    #定義模型
    model=ChatOpenAI(model="gpt-3.5-turbo", api_key=openai_api_key)
    #定義解析器
    output_parser=PydanticOutputParser(pydantic_object=ig) #獲得json格式輸出，將結果轉換為預期格式
    #串聯
    chain=prompt | model | output_parser #

    """result=chain.invoke({
        "parser_instructions":output_parser.get_format_instructions(),
        "theme":theme
    })"""

    raw_result = model.invoke({
        "parser_instructions": output_parser.get_format_instructions(),
        "theme": theme
    })
    print("Raw GPT Response:", raw_result)
    if "titles" not in raw_result or "content" not in raw_result:
        raise ValueError("API 回傳的 JSON 缺少必要欄位: titles 或 content")

    # 解析 JSON
    result = output_parser.parse(raw_result)
    
    return result

print(generate_ig("大模型", os.getenv("OPENAI_API_KEY")))