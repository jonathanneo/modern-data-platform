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
    - Asset tests are displayed on each asset
2. Create custom assets (e.g. Census)
    - We have plenty of use-cases that we don't have built-in asset connectors for e.g. Experiments, ML Pipelines, Census, etc. 
    - We can create our own custom asset connectors that read data from APIs or code locations, and create the necessary assets. 
3. Policy based scheduling
    - Uses Policies (aka conditions) to trigger asset refresh. 
    - Policies are defined in the same place that Analytics Engineers and Data Scientist contribute code i.e. dbt projects. 
    - Policy types:
        - Eager
            - Let's see this in action. 
                ```YML
                models:
                    +meta:
                        dagster:
                        group: dbt_reporting
                        auto_materialize_policy:
                            type: "eager"
                ```
            - What problem does it create? Over-syncing -- perhaps we don't need that table to be SUPER fresh. It's fine to have some delays in refreshing (i.e. allow for an evaluation period of 30 minutes). 
        - on_cron
        - on_missing
        - See: https://docs.dagster.io/concepts/automation/declarative-automation#automation-conditions
    - If any of the above common policy types don't suffice for your use-case, you can customise your own policies, see: https://docs.dagster.io/concepts/automation/declarative-automation/customizing-automation-conditions. These contains building blocks to create an assortment of custom automation policies. 

Everything else you'd expect from an orchestrator: 

4. Retries and continue from failed step
5. Partitions and backfills
6. Different refresh cadences 
7. Back to primitive methods for scheduling - Explicit Job Crons 
8. Monitoring and alerting (run view) - compare that to dashboards we've built in Mode
9. Asset Catalog - comparable to the Atlan data catalog
    - Column metadata
    - Owners
    - Tags
    - Lineage
    - Execution history (++) - We don't have this information in Atlan. 
        - You can drill into all historical runs for a given asset.
    - Execution runtime trend analysis (Plots) - Easily see spikes in runtime duration
