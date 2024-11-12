from dagster import define_asset_job, AssetSelection

dbt_analytics_job = define_asset_job(
    name="dbt_analytics_job", selection=AssetSelection.groups("dbt_analytics")
)
