from pydantic import BaseModel
from typing import Literal

class llm_schema(BaseModel):
    classifier:Literal["normal","illegal","harrasment","data extraction attempt","prompt injection"]
llm_structured_output = llm.with_structured_output(llm_schema)