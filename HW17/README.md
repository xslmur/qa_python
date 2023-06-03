```shell
> insert json from the file 'data.json' to mongodb collection 'my_collection_3':
[{'name': 'Cheadle Yorkshire', 'email': 'cheadyork@gmail.com', 'age': '25', 'pets': [{'pet_name': 'Galaxy', 'breed': 'Siamese', 'pet_age': '2', 'about_pet': {'favourite_toy': 'minnie_mouse', 'temperament': 'calm'}}]}]

> read from mongodb collection 'my_collection_3' and parse to the model by filter: {'name': 'Cheadle Yorkshire'}
json:
 {'_id': ObjectId('647b509b749fb552c076bc03'), 'name': 'Cheadle Yorkshire', 'email': 'cheadyork@gmail.com', 'age': '25', 'pets': [{'pet_name': 'Galaxy', 'breed': 'Siamese', 'pet_age': '2', 'about_pet': {'favourite_toy': 'minnie_mouse', 'temperament': 'calm'}}]}
person:
 PersonModel(id:647b509b749fb552c076bc03, name:Cheadle Yorkshire, email:cheadyork@gmail.com, age:25, pets:[PetModel(pet_name:Galaxy, pet_age:2, about:PetAboutModel(favourite_toy:minnie_mouse, minnie_mouse:calm))]))

> remove from mongodb collection 'my_collection_3' by filter: {'name': 'Cheadle Yorkshire'}
```