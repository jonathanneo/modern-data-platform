# modern-data-platform

![](./modern-data-platform.drawio.png)

## Set up 

Create the following accounts: 
- [Fivetran](https://fivetran.com/)
- [Snowflake](https://app.snowflake.com)
- [Census](https://app.getcensus.com/)

Create environment variable file `.env` in `dagster/data-platform/`

```
FIVETRAN_API_KEY=<TODO>
FIVETRAN_API_SECRET=<TODO>
SNOWFLAKE_USERNAME=<TODO>
SNOWFLAKE_PASSWORD=<TODO>
CENSUS_API_KEY=<TODO>
```

# Run the app 

To prevent frequent code repository refresh (to not over-poll Fivetran)
```
cd dagster/data-platform
dagster-webserver
```

Otherwise, 
```
cd dagster/data-platform
dagster dev
```
