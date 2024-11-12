{{ config(
    materialized="incremental", 
    incremental_strategy="append",
    unique_key="workorder_key"
)}}

select
    {{ dbt_utils.generate_surrogate_key(['workorderid']) }} as workorder_key,
    {{ dbt_utils.generate_surrogate_key(['productid']) }} as product_key,
    workorderid,
    scrapreasonid,
    orderqty,
    scrappedqty,
    startdate,
    enddate,
    duedate
from {{ source('production', 'workorder') }} as workorder
where startdate >= '{{ var("start_date")}}' and startdate < '{{ var("end_date")}}'
