from dagster import ScheduleDefinition, AssetSelection 
from data_platform.jobs import fivetran_job, dbt_analytics_job, dbt_reporting_job, dbt_web_events_job, fivetran_analytics_reporting_job

fivetran_schedule = ScheduleDefinition(
    name="fivetran_schedule",
    target=fivetran_job,
    cron_schedule="*/5 * * * *",
)

dbt_web_events_schedule = ScheduleDefinition(
    name="dbt_web_events_schedule",
    target=dbt_web_events_job,
    cron_schedule="*/30 * * * *",
)

dbt_analytics_schedule = ScheduleDefinition(
    name="dbt_analytics_schedule",
    target=dbt_analytics_job,
    cron_schedule="0 0 * * *",
)

dbt_reporting_schedule = ScheduleDefinition(
    name="dbt_reporting_schedule",
    target=dbt_reporting_job,
    cron_schedule="0 0 * * *",
)

fivetran_analytics_reporting_schedule = ScheduleDefinition(
    name="fivetran_analytics_reporting_schedule",
    target=fivetran_analytics_reporting_job,
    cron_schedule="0 0 * * *",
)

# add schedule on individual assets
dim_date_schedule = ScheduleDefinition(
    name="dim_date_schedule",
    target=AssetSelection.assets("marts/dim_date"),
    cron_schedule="0 */1 * * *",
)
