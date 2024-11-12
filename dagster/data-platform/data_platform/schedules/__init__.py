from dagster import ScheduleDefinition, AssetSelection 
from data_platform.jobs import dbt_analytics_job

dim_date_schedule = ScheduleDefinition(
    name="dim_date_schedule",
    target=AssetSelection.assets("marts/dim_date"),
    cron_schedule="* * * * *",
)

dbt_analytics_schedule = ScheduleDefinition(
    name="dbt_analytics_schedule",
    target=dbt_analytics_job,
    cron_schedule="* * * * *",
)
