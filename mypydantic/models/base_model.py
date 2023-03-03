from pydantic import BaseModel as MyPydanticBaseModel


class BaseModel(MyPydanticBaseModel):
    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True

    def __init__(self, **kwargs):
        self.update_forward_refs()
        super().__init__(**kwargs)
