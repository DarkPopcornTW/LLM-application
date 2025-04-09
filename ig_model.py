"""from pydantic import BaseModel, Field
from typing import List

#定義輸出格式
class ig(BaseModel):
    titles:List[str]=Field(description="IG的5個標題",min_items=5,max_items=5)
    content:str=Field(description="IG的正文內容")
"""
from pydantic import BaseModel, Field
from typing import List

# 定義輸出格式

class ig(BaseModel):
    titles: List[str] = Field(..., description="5個IG標題", min_items=5, max_items=5)
    content: str = Field(..., description="IG的正文內容")
"""
    # 新增Pydantic支持的 json_schema 方法
    class Config:
        # 配置以支持 LangChain 解析器
        json_schema_extra = {
            "examples": [
                {
                    "titles": ["標題1", "標題2", "標題3", "標題4", "標題5"],
                    "content": "這是正文內容，這裡有 Emoji 😄"
                }
            ]
        }

"""
