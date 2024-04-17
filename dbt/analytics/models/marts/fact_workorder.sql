select
    {{ dbt_utils.generate_surrogate_key(['workorderid']) }} as workorder_key,
    {{ dbt_utils.generate_surrogate_key(['productid']) }} as product_key,
    workorderid,
    scrapreasonid,
    orderqty,
    scrappedqty,
    startdate,
    enddate,
    duedate,
    modifieddate
from {{ source('adventureworks_production', 'workorder') }} as workorder
