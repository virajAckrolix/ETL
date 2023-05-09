----Basic Documentation ----
- folder name - generate fake data
    uses Faker library to generate and populate fake data via Hubspot Post API

- folder name - extract-load-data
    calls the paginated APIs to extract all data
    very basic transformation of extracting main data and removing meta data is done
    json objects are pushed into an array
    array of objects is push to the DB via insert many operation
    