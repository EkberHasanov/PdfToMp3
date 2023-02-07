import pydantic

__all__ = ("BaseModel",)


class BaseModel(pydantic.BaseModel):
    
    @pydantic.root_validator(pre=True)
    def _min_properties(cls, data: dict) -> dict:
        if not data:
            raise ValueError('At least one property must be specified')
        return data

    def dict(self, include_nulls=False, **kwargs) -> dict:
        # kwargs['exclude_nulls'] = not include_nulls
        return super().dict(**kwargs)
    
    class Config:
        extra = pydantic.Extra.forbid
        anystr_strip_whitespace = True
