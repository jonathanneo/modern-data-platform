from dagster import define_asset_job, AssetSelection

fivetran_job = define_asset_job(
    name="fivetran_job", selection=AssetSelection.groups("fivetran")
)

dbt_analytics_job = define_asset_job(
    name="dbt_analytics_job", selection=AssetSelection.groups("dbt_analytics")
)

dbt_reporting_job = define_asset_job(
    name="dbt_reporting_job", selection=AssetSelection.groups("dbt_reporting")
)

dbt_web_events_job = define_asset_job(
    name="dbt_web_events_job", selection=AssetSelection.groups("dbt_web_events")
)

fivetran_analytics_reporting_job = define_asset_job(
    name="fivetran_analytics_reporting_job", selection=AssetSelection.groups("fivetran", "dbt_analytics", "dbt_reporting")
)
