# Presentation on Django migrations

## The Problems That Migrations Solve


### Making Database Changes Without SQL
```
Without migrations, you would have to connect to your database and type in a bunch of SQL commands.
```
### Avoiding Repetition

```
Creating a model and then writing SQL to create the database tables for it would be repetitive but by  help of Migrations tables are generated from your models
```

## Creating Migrations

With the model created, the first thing you need to do is create a migration for it. You can do this with the following commands:

```
python3 manage.py makemigrations <app name>

python3 manage.py makemigrations
```
## Applying Migrations
exit
You have now created the migration, but to actually make any changes in the database, you have to apply it with the management command migrate:

```
python manage.py migrate

python3 manage.py migrate <appname>

```
## Changing Models

When you change the definition of a model, the database tables used to store these models have to be changed too.

## Listing Out Migrations

If you want to know what migrations exist in a Django project, you don’t have to dig trough the migrations directories of your installed apps. You can use the showmigrations command:

```
./manage.py showmigrations
```
## Unapplying Migrations

At some point, you might want to undo changes and switch back to an earlier database schema .

```
python3 manage.py migrate <app name> 0001_initial
```
**Note :-**

Don’t confuse unapplying migrations with the undo operation you are used to from your favorite text editor.

Not all database operations can be completely reverted. If you remove a field from a model, create a migration, and apply it, Django will remove the respective column from the database.

Unapplying that migration will re-create the column, but it won’t bring back the data that was stored in that column!


## How Django Knows Which Migrations to Apply

What happens if you run python.manage.py migrate command again? Let’s try it out:

## Migration Dependencies

The dependencies list in a migration class contains any migrations that must be applied before this migration can be applied.

# Thank You
