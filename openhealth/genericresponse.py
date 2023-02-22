from typing import Any, TypeVar, Type, cast

# New File Added GenericREsponse

T = TypeVar("T")


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


class GenericResponse:
    Message: str
    Result: str
    HasError: bool
    Status: int

    def __init__(self, message: str, result: str, has_error: bool, status: int) -> None:
        self.Message = message
        self.Result = result
        self.HasError = has_error
        self.Status = status

    @staticmethod
    def from_dict(obj: Any) -> 'GenericResponse':
        assert isinstance(obj, dict)
        message = from_str(obj.get("Message"))
        result = from_str(obj.get("Result"))
        has_error = from_bool(obj.get("HasError"))
        status = from_int(obj.get("Status"))
        return GenericResponse(message, result, has_error, status)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Message"] = from_str(self.Message)
        result["Result"] = from_str(self.Result)
        result["HasError"] = from_bool(self.HasError)
        result["Status"] = from_int(self.Status)
        return result


def generic_response_from_dict(s: Any) -> GenericResponse:
    return GenericResponse.from_dict(s)


def generic_response_to_dict(x: GenericResponse) -> Any:
    return to_class(GenericResponse, x)