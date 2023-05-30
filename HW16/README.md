```shell
/home/sl/w/qa_python/HW16/.env/bin/python /home/sl/w/qa_python/HW16/main.py 
cats = cats_repo.get_all_by_lambda()
Cat(ID: 1, Name: Galaxy, Breed: Siamese, Age: 5, Owner: Simon)
   owned dog:  Dog(ID: 11, Name: Killua, Breed: Labrador Retriever, Age: 2, Owner: Zoldyck)
Cat(ID: 2, Name: Gurren, Breed: Persian, Age: 2, Owner: Kamina)
   owned dog:  Dog(ID: 12, Name: Hisoka, Breed: Poodle, Age: 1, Owner: Morow)
Cat(ID: 3, Name: Lagann, Breed: Maine Coon, Age: 9, Owner: Nia)
   owned dog:  Dog(ID: 10, Name: Gon, Breed: Golden Retriever, Age: 4, Owner: Freecss)

cats = cats_repo.get_all_by_for()
Cat(ID: 1, Name: Galaxy, Breed: Siamese, Age: 5, Owner: Simon)
   owned dog:  Dog(ID: 11, Name: Killua, Breed: Labrador Retriever, Age: 2, Owner: Zoldyck)
Cat(ID: 2, Name: Gurren, Breed: Persian, Age: 2, Owner: Kamina)
   owned dog:  Dog(ID: 12, Name: Hisoka, Breed: Poodle, Age: 1, Owner: Morow)
Cat(ID: 3, Name: Lagann, Breed: Maine Coon, Age: 9, Owner: Nia)
   owned dog:  Dog(ID: 10, Name: Gon, Breed: Golden Retriever, Age: 4, Owner: Freecss)

cat = cats_repo.get_by_id(cats[0].id)
Cat(ID: 1, Name: Galaxy, Breed: Siamese, Age: 5, Owner: Simon)

dogs = dogs_repo.get_all_by_lambda()
Dog(ID: 10, Name: Gon, Breed: Golden Retriever, Age: 4, Owner: Freecss)
  owner cat:  Cat(ID: 3, Name: Lagann, Breed: Maine Coon, Age: 9, Owner: Nia)
Dog(ID: 11, Name: Killua, Breed: Labrador Retriever, Age: 2, Owner: Zoldyck)
  owner cat:  Cat(ID: 1, Name: Galaxy, Breed: Siamese, Age: 5, Owner: Simon)
Dog(ID: 12, Name: Hisoka, Breed: Poodle, Age: 1, Owner: Morow)
  owner cat:  Cat(ID: 2, Name: Gurren, Breed: Persian, Age: 2, Owner: Kamina)

dogs = dogs_repo.get_all_by_for()
Dog(ID: 10, Name: Gon, Breed: Golden Retriever, Age: 4, Owner: Freecss)
  owner cat:  Cat(ID: 3, Name: Lagann, Breed: Maine Coon, Age: 9, Owner: Nia)
Dog(ID: 11, Name: Killua, Breed: Labrador Retriever, Age: 2, Owner: Zoldyck)
  owner cat:  Cat(ID: 1, Name: Galaxy, Breed: Siamese, Age: 5, Owner: Simon)
Dog(ID: 12, Name: Hisoka, Breed: Poodle, Age: 1, Owner: Morow)
  owner cat:  Cat(ID: 2, Name: Gurren, Breed: Persian, Age: 2, Owner: Kamina)

Process finished with exit code 0
```
