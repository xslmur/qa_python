execution log:
```shell
db data:
Cat(id:1, name:'Galaxy', breed:'Siamese', age:5, owner:'Simon' )
.. Dog(id:11, name:'Killua', breed:'Labrador Retriever',age:2, owner:'Zoldyck', owner_cat_id:1)
Cat(id:2, name:'Gurren', breed:'Persian', age:2, owner:'Kamina' )
.. Dog(id:12, name:'Hisoka', breed:'Poodle',age:1, owner:'Morow', owner_cat_id:2)
Cat(id:3, name:'Lagann', breed:'Maine Coon', age:9, owner:'Nia' )
.. Dog(id:10, name:'Gon', breed:'Golden Retriever',age:4, owner:'Freecss', owner_cat_id:3)

cats.get_all():
Cat(id:1, name:'Galaxy', breed:'Siamese', age:5, owner:'Simon' )
Cat(id:2, name:'Gurren', breed:'Persian', age:2, owner:'Kamina' )
Cat(id:3, name:'Lagann', breed:'Maine Coon', age:9, owner:'Nia' )

cats.get_item_by_id(1):
Cat(id:1, name:'Galaxy', breed:'Siamese', age:5, owner:'Simon' )

cat = cats.add_item(name='test', breed='test', age=42, owner='test')
Cat(id:13, name:'test', breed:'test', age:42, owner:'test' )

cats.update_item(cat)

cats.remove_item(cat)

cat = cats.add_item(name='test2', breed='test2', age=42, owner='test2')
Cat(id:14, name:'test2', breed:'test2', age:42, owner:'test2' )

cats.remove_item_by_id(cat.id)

Process finished with exit code 0
```

related postgresql log:
```sql
2023-05-29 00:05:04.813 EEST [1434808] test@pets LOG:  duration: 0.036 ms  statement: BEGIN
2023-05-29 00:05:04.814 EEST [1434808] test@pets LOG:  duration: 0.574 ms  statement: SELECT t.oid, typarray
        FROM pg_type t JOIN pg_namespace ns
            ON typnamespace = ns.oid
        WHERE typname = 'hstore';

2023-05-29 00:05:04.814 EEST [1434808] test@pets LOG:  duration: 0.014 ms  statement: ROLLBACK
2023-05-29 00:05:04.814 EEST [1434808] test@pets LOG:  duration: 0.005 ms  statement: BEGIN
2023-05-29 00:05:04.814 EEST [1434808] test@pets LOG:  duration: 0.048 ms  statement: select pg_catalog.version()
2023-05-29 00:05:04.815 EEST [1434808] test@pets LOG:  duration: 0.031 ms  statement: select current_schema()
2023-05-29 00:05:04.815 EEST [1434808] test@pets LOG:  duration: 0.011 ms  statement: show transaction isolation level
2023-05-29 00:05:04.815 EEST [1434808] test@pets LOG:  duration: 0.008 ms  statement: show standard_conforming_strings
2023-05-29 00:05:04.815 EEST [1434808] test@pets LOG:  duration: 0.007 ms  statement: ROLLBACK
2023-05-29 00:05:04.820 EEST [1434808] test@pets LOG:  duration: 0.204 ms  statement: SELECT cats.id, cats.name, cats.breed, cats.age, cats.owner 
        FROM cats
2023-05-29 00:05:04.830 EEST [1434808] test@pets LOG:  duration: 0.210 ms  statement: SELECT dogs.id AS dogs_id, dogs.name AS dogs_name, dogs.breed AS dogs_breed, dogs.age AS dogs_age, dogs.owner AS dogs_owner, dogs.owner_cat_id AS dogs_owner_cat_id 
        FROM dogs 
        WHERE 1 = dogs.owner_cat_id
2023-05-29 00:05:04.831 EEST [1434808] test@pets LOG:  duration: 0.053 ms  statement: SELECT dogs.id AS dogs_id, dogs.name AS dogs_name, dogs.breed AS dogs_breed, dogs.age AS dogs_age, dogs.owner AS dogs_owner, dogs.owner_cat_id AS dogs_owner_cat_id 
        FROM dogs 
        WHERE 2 = dogs.owner_cat_id
2023-05-29 00:05:04.832 EEST [1434808] test@pets LOG:  duration: 0.054 ms  statement: SELECT dogs.id AS dogs_id, dogs.name AS dogs_name, dogs.breed AS dogs_breed, dogs.age AS dogs_age, dogs.owner AS dogs_owner, dogs.owner_cat_id AS dogs_owner_cat_id 
        FROM dogs 
        WHERE 3 = dogs.owner_cat_id
2023-05-29 00:05:04.833 EEST [1434808] test@pets LOG:  duration: 0.055 ms  statement: SELECT cats.id AS cats_id, cats.name AS cats_name, cats.breed AS cats_breed, cats.age AS cats_age, cats.owner AS cats_owner 
        FROM cats
2023-05-29 00:05:04.835 EEST [1434808] test@pets LOG:  duration: 0.134 ms  statement: SELECT cats.id AS cats_id, cats.name AS cats_name, cats.breed AS cats_breed, cats.age AS cats_age, cats.owner AS cats_owner 
        FROM cats 
        WHERE cats.id = 1
2023-05-29 00:05:04.842 EEST [1434808] test@pets LOG:  duration: 5.436 ms  statement: INSERT INTO cats (name, breed, age, owner) VALUES ('test', 'test', 42, 'test') RETURNING cats.id, cats.name, cats.breed, cats.age, cats.owner
2023-05-29 00:05:04.844 EEST [1434808] test@pets LOG:  duration: 1.196 ms  statement: UPDATE cats SET age=43 WHERE cats.id = 13
2023-05-29 00:05:04.845 EEST [1434808] test@pets LOG:  duration: 0.056 ms  statement: SELECT cats.id AS cats_id, cats.name AS cats_name, cats.breed AS cats_breed, cats.age AS cats_age, cats.owner AS cats_owner 
        FROM cats 
        WHERE cats.id = 13
2023-05-29 00:05:04.846 EEST [1434808] test@pets LOG:  duration: 0.046 ms  statement: SELECT dogs.id AS dogs_id, dogs.name AS dogs_name, dogs.breed AS dogs_breed, dogs.age AS dogs_age, dogs.owner AS dogs_owner, dogs.owner_cat_id AS dogs_owner_cat_id 
        FROM dogs 
        WHERE 13 = dogs.owner_cat_id
2023-05-29 00:05:04.848 EEST [1434808] test@pets LOG:  duration: 1.093 ms  statement: DELETE FROM cats WHERE cats.id = 13
2023-05-29 00:05:04.848 EEST [1434808] test@pets LOG:  duration: 0.014 ms  statement: SET default_transaction_isolation TO DEFAULT
2023-05-29 00:05:04.849 EEST [1434808] test@pets LOG:  duration: 0.903 ms  statement: INSERT INTO cats (name, breed, age, owner) VALUES ('test2', 'test2', 42, 'test2') RETURNING cats.id, cats.name, cats.breed, cats.age, cats.owner
2023-05-29 00:05:04.851 EEST [1434808] test@pets LOG:  duration: 0.991 ms  statement: DELETE FROM cats WHERE cats.id = 14
2023-05-29 00:05:04.869 EEST [1434808] test@pets LOG:  duration: 0.027 ms  statement: SET default_transaction_isolation TO DEFAULT
```