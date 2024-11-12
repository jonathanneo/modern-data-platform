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

If you only want to view asset lineage: 
```
cd dagster/data-platform
dagster-webserver
```

Otherwise, to run dagster web-server with the scheduler, run: 
```
cd dagster/data-platform
dagster dev
```

# Demo 

1. Inferred Asset DAG
    - Show import code for Fivetran and dbt. 
    - No need to manually generate a DAG.
    - Dependencies are inferred using dbt's graph (source/ref).
    - Asset level dependencies, and not Project level dependencies. 
    - Compare this approach to Argo/Airflow approach. You have to explicitly define your upstream dependencies, and on the Project level. 
2. Create custom assets (e.g. Census)
    - We have plenty of use-cases that we don't have built-in asset connectors for e.g. Experiments, ML Pipelines, Census, etc. 
    - We can create our own custom asset connectors that read data from APIs or code locations, and create the necessary assets. 
3. Policy based scheduling
    - Uses Policies (aka conditions) to trigger asset refresh. 
    - Policies are defined in the same place that Analytics Engineers and Data Scientist contribute code i.e. dbt projects. 
    - Policy types:
        - Eager
            - Let's see this in action. 
            - What problem does it create? Over-syncing -- perhaps we don't need that table to be SUPER fresh. It's fine to have some delays in refreshing (i.e. allow for an evaluation period of 30 minutes). 

Everything else you'd expect: 
3. Retries and continue from failed step
4. Partitions and backfills
5. Different refresh cadences 
6. Back to primitive methods for scheduling - Explicit Job Crons 
