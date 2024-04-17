select
    {{ dbt_utils.star(from=ref('fact_sale'), relation_alias='fact_sale', except=[
        "product_key", "customer_key", "creditcard_key", "ship_address_key", "order_status_key", "order_date_key"
    ]) }},
    {{ dbt_utils.star(from=ref('dim_product'), relation_alias='dim_product', except=["product_key"]) }},
    {{ dbt_utils.star(from=ref('dim_customer'), relation_alias='dim_customer', except=["customer_key"]) }},
    {{ dbt_utils.star(from=ref('dim_credit_card'), relation_alias='dim_credit_card', except=["creditcard_key"]) }},
    {{ dbt_utils.star(from=ref('dim_address'), relation_alias='dim_address', except=["address_key"]) }},
    {{ dbt_utils.star(from=ref('dim_order_status'), relation_alias='dim_order_status', except=["order_status_key"]) }},
    {{ dbt_utils.star(from=ref('dim_date'), relation_alias='dim_date', except=["date_day"]) }}
from {{ ref('fact_sale') }} as fact_sale
left join {{ ref('dim_product') }} as dim_product on fact_sale.product_key = dim_product.product_key
left join {{ ref('dim_customer') }} as dim_customer on fact_sale.customer_key = dim_customer.customer_key
left join {{ ref('dim_credit_card') }} as dim_credit_card on fact_sale.creditcard_key = dim_credit_card.creditcard_key
left join {{ ref('dim_address') }} as dim_address on fact_sale.ship_address_key = dim_address.address_key
left join {{ ref('dim_order_status') }} as dim_order_status on fact_sale.order_status_key = dim_order_status.order_status_key
left join {{ ref('dim_date') }} as dim_date on fact_sale.orderdate = dim_date.date_day
