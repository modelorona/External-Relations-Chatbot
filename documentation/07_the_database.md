# The database

The database that we use is MySQL. This is because we all know it and feel comfortable with it, and also because Django
works with it out of the box.

Currently there is just one table to represent the data, with no proper relations. This is because we did not have time
to define relations. This is definitely something that can be improved.

The current database is hosted as an RDS instance on AWS but it most certainly can be exported and reproduced on a local database elsewhere.

Please note, the database information is unfortunately hardcoded into the settings file instead of using environmental variables. Please fix it. We did not have enough time.
