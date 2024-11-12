{{ config(
    materialized="incremental", 
    incremental_strategy="append",
)}}

select
    count(*) as session_count,
    sum(orderqty) as session_clicks,
    startdate as session_date
from {{ ref('fact_web_events') }} as workorder
where startdate >= '{{ var("start_date")}}' and startdate < '{{ var("end_date")}}'
group by startdate
