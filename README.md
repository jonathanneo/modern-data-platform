# modern-data-platform

![](./images/modern-data-platform.drawio.png)

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

Run dagster locally
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
2. Policy based scheduling
    - Uses Policies (aka conditions) to trigger asset refresh. 
    - Policies can be defined in the same place that Analytics Engineers and Data Scientist contribute code i.e. dbt projects. 
    - Built-in policy types:
        - Eager
            - Let's see this in action. !! Make sure to turn on `default_automation_condition_sensor`! 
                ```YML
                models:
                    +meta:
                        dagster:
                        group: dbt_reporting
                        auto_materialize_policy:
                            type: "eager"
                ```
            - What problem does it create? Over-syncing -- perhaps we don't need that table to be SUPER fresh. It's fine to have some delays in refreshing (i.e. allow for an evaluation period of 30 minutes). 
        - on_cron: Different schedule cadences e.g. monthly, weekly, daily, hourly
        - on_missing
        - See: https://docs.dagster.io/concepts/automation/declarative-automation#automation-conditions
    - If any of the above built-in policy types don't suffice for your use-case, you can create your own custom policies, see: https://docs.dagster.io/concepts/automation/declarative-automation/customizing-automation-conditions. The link contains building blocks to create an assortment of custom automation policies based on different conditions.
3. Asset Catalog - comparable to the Atlan data catalog
    - Column metadata
    - Owners (search catalog by owners)
    - Tags (search catalog by tags)
    - Lineage
    - Execution history (++) - We don't have this information in Atlan. 
        - You can drill into all historical runs for a given asset.
        - (We don't need to build this in Mode!)
    - Execution runtime trend analysis (Plots) - Easily see spikes in runtime duration
        - (We don't need to build this in Mode!)
4. Partitions and backfills
    - Tracks partition state in an dagster internal database (postgresql).
    - Fires of either sequential or parallel sub-processes (or pods in k8s) for each partition. 
        - Sequential (single-run): If your SQL logic is using `upsert` or `merge` or `delete+insert` statements with an incremental predicate using the target table's max date, then you'd want to sequentially process data. 
        - Parallel (multi-run): If your SQL logic is using `insert` statements without an incremental predicate, then you can insert data in parallel.

5. Combination of automation_condition and primitive methods for scheduling - Explicit Jobs and Job Schedule per dbt project (similar to Cronjobs, Airflow and Argo). They can both work together. 
    - Different schedule cadences e.g. monthly, weekly, daily, hourly

6. Create custom assets (e.g. Census)
    - We have plenty of use-cases that we don't have built-in asset connectors for e.g. Experiments, ML Pipelines, Census, etc. 
    - We can create our own custom asset connectors that read data from APIs or code locations, and create the necessary assets. 

Everything else you'd expect from an orchestrator: 

7. Automatic retries and continue from failed step: https://docs.dagster.io/deployment/run-retries
8. Monitoring and slack alerting (run view) - compare that to dashboards we've built in Mode (already went through this)
    ![slack-alert](./images/slack-alert.png)
