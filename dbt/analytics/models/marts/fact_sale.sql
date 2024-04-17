with salesorderheader as (
    select
        salesorderid,
        customerid,
        creditcardid,
        shiptoaddressid,
        status as order_status,
        cast(orderdate as date) as orderdate
    from {{ source('adventureworks_sales', 'salesorderheader') }}
),

salesorderdetail as (
    select
        salesorderid,
        salesorderdetailid,
        productid,
        orderqty,
        unitprice,
        unitprice * orderqty as revenue
    from {{ source('adventureworks_sales', 'salesorderdetail') }}
)

select
    {{ dbt_utils.generate_surrogate_key(['salesorderdetail.salesorderid', 'salesorderdetailid']) }} as sales_key,
    {{ dbt_utils.generate_surrogate_key(['productid']) }} as product_key,
    {{ dbt_utils.generate_surrogate_key(['customerid']) }} as customer_key,
    {{ dbt_utils.generate_surrogate_key(['creditcardid']) }} as creditcard_key,
    {{ dbt_utils.generate_surrogate_key(['shiptoaddressid']) }} as ship_address_key,
    {{ dbt_utils.generate_surrogate_key(['order_status']) }} as order_status_key,
    orderdate,
    salesorderdetail.salesorderid,
    salesorderdetail.salesorderdetailid,
    salesorderdetail.unitprice,
    salesorderdetail.orderqty,
    salesorderdetail.revenue
from salesorderdetail
inner join salesorderheader
    on salesorderdetail.salesorderid = salesorderheader.salesorderid
