Migrations are Django's way of propagating changes you make to your models (adding a field, deleting a model, etc) into database scheme. Designed to be mostly automatic, but sometimes have to make migration . 
- Specialized in updating your database live, without using data

### Making Model Changes (3 Steps)
1. Change models in `models.py`
2. Run `$python3 manage.py makemigrations` to create migrations for those changes
3. Run`$python3 manage.py migrate` to apply changes to databse


## The Commands 
- `migrate` responsible for applying and unapplying migrations. 
- `makemigrations` creatings new migratios based on changes from models 
- `sqlmigeate` displays SQ statements for migration. Takes migration names and returns their SQL

