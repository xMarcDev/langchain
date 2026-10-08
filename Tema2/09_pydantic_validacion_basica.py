"""09_pydantic_validacion_basica.py — Validar y convertir datos con un modelo Pydantic (base de los output parsers)."""

from pydantic import BaseModel

RAW_DATA = {"id": "123", "name": "Ana"}


class User(BaseModel):
    id: int
    name: str
    active: bool = True


def main() -> None:
    user = User(**RAW_DATA)

    print(user)
    print(user.model_dump_json())


if __name__ == "__main__":
    main()
