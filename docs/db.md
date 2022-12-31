# Database Utilities

## Database Router Class

### `ReadAndWriteRouter`

A database router toggles the database to connect depending on whether the SQL query is read or written.

You can use this utils, using `settings.DATABSE` and  `settings.DATABASE_ROUTERS`.

```python
# settings.py

# Database

DATABASES = {
    'default': {
        ...
    },
    'readonly': {
        ...
    },
}

DATABASE_ROUTERS = ['backend_utils.db.routers.ReadAndWriteRouter']
```

Adding to the `default` engine, please set up a `readonly` engine to use the `ReadAndWriteRouter`.

If `settings.DATABASES` has no `readonly` engine, all the query connected to the `default` engine.
