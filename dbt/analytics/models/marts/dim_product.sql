select
    {{ dbt_utils.generate_surrogate_key(['product.productid']) }} as product_key,
    product.productid,
    product.name as product_name,
    product.productnumber,
    product.color,
    product.class,
    productsubcategory.name as product_subcategory_name,
    productcategory.name as product_category_name
from {{ source('adventureworks_production', 'product') }} as product
inner join {{ source('adventureworks_production', 'productsubcategory') }} as productsubcategory
    on product.productsubcategoryid = productsubcategory.productsubcategoryid
inner join {{ source('adventureworks_production', 'productcategory') }} as productcategory
    on productsubcategory.productcategoryid = productcategory.productcategoryid
