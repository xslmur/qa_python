from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import mapped_column, relationship, Mapped, declarative_base
from typing import List

from alchemy.models.base import Base

# https://docs.sqlalchemy.org/en/20/orm/quickstart.html

# pets=# \d cats
#                                    Table "public.cats"
#  Column |         Type          | Collation | Nullable |             Default
# --------+-----------------------+-----------+----------+----------------------------------
#  id     | integer               |           | not null | nextval('cats_id_seq'::regclass)
#  name   | character varying(50) |           |          |
#  breed  | character varying(50) |           |          |
#  age    | integer               |           |          |
#  owner  | character varying(50) |           |          |


class CatModel(Base):
    __tablename__ = "cats"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    breed: Mapped[str] = mapped_column(String(50))
    age: Mapped[int] = mapped_column(Integer)
    owner: Mapped[str] = mapped_column(String(50))

    dogs: Mapped[List["DogModel"]] = relationship(
        back_populates="owner_cat", cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return f"Cat(id:{self.id!r}, name:{self.name!r}, breed:{self.breed!r}, age:{self.age!r}, owner:{self.owner!r} )"
