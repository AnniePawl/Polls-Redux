# Models 

## Models 
- A model is a single, definitive source of truth about data
- Contains essential fields and behvaiors of data
- Goal: define data n one place, automatically derive things fromit

### Making Model Changes (3 Steps)
1. Change models in `models.py`
2. Run `$python3 manage.py makemigrations` to create migrations for those changes
3. Run`$python3 manage.py migrate` to apply changes to databse


- Each model is represented by a class that subclasses `django.db.models.Model`. 
- Each model has many class variables, each of which represents a database field in teh model 
- Instance of `Field` cass tells Django what kind of field
- Some field classes have required arguments, or optional requirements 
- **Foreign Key** tells Django each **Choice** is ralted to single questions

# Activating Models 
Small bit of model code tells Django a lot:
- Create a database schema for app (CREATETABLE statement)
- Create Python database-access API for accessing Question and Choice objects


