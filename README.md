# Theme Parks

This is the seeding solution for de-pg-theme-parks.

It contains a seeding solution that creates, and inserts, data into the parks, and rides, tables.

It does not seed the Advanced Task 'stalls' and 'foods' tables, though placeholders have been left
in the seed function.

## To run the seed

Ensure that you add a `.env` file to the root of `de-pg-theme-parks`. Inside it should read as so:

```env
PG_USER=replace_with_your_psql_username
PG_PASSWORD=replace_with_your_psql_password
PG_DATABASE=theme_parks
```

Once you have set up your `.env` file you can then run the command `make all`.

This will run the Makefile and install everything you require.

## Check your local PSQL has the theme-parks database

Once you've run all of the above you can check that the data is in place by running `psql` in your CLI.

This should open a PSQL session in your CLI. From here you can run:

- \c theme_parks (connect to theme_parks database)
- \dt (to display tables, of which parks and rides should be present)
- SELECT * FROM parks; (should return a table of parks)
- SELECT * FROM rides; (should return a table of rides)
- \q (to quit the table view, and again to exit PSQL)

You should now have a seeded database ready to continue your tasks.