from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import mapped_column, relationship, Mapped, declarative_base

from alchemy.models.base import Base

# https://docs.sqlalchemy.org/en/20/orm/quickstart.html

# pets=# \d dogs
#                                       Table "public.dogs"
#     Column    |         Type          | Collation | Nullable |             Default
# --------------+-----------------------+-----------+----------+----------------------------------
#  id           | integer               |           | not null | nextval('dogs_id_seq'::regclass)
#  name         | character varying(50) |           |          |
#  breed        | character varying(50) |           |          |
#  age          | integer               |           |          |
#  owner        | character varying(50) |           |          |
#  owner_cat_id | integer               |           |          |
# Indexes:
#     "dogs_pkey" PRIMARY KEY, btree (id)
# Foreign-key constraints:
#     "dogs_owner_cat_id_fkey" FOREIGN KEY (owner_cat_id) REFERENCES cats(id)


class DogModel(Base):
    __tablename__ = "dogs"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    breed: Mapped[str] = mapped_column(String(50))
    age: Mapped[int] = mapped_column(Integer)
    owner: Mapped[str] = mapped_column(String(50))
    owner_cat_id: Mapped[int] = mapped_column(ForeignKey("cats.id"))

    owner_cat: Mapped["CatModel"] = relationship(back_populates="dogs")

    def __repr__(self) -> str:
        return (f"Dog(id:{self.id!r}, name:{self.name!r}, breed:{self.breed!r},"
                f"age:{self.age!r}, owner:{self.owner!r}, owner_cat_id:{self.owner_cat_id!r})")