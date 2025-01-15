// Dimension Tables
Table "dim_customer" {
  customer_key int [pk]
  customer_id int
  first_name varchar
  last_name varchar
  email varchar
  age int
  gender varchar
  state varchar
  city varchar
  postal_code varchar
  country varchar
  traffic_source varchar
  created_at timestamp
}

Table "dim_product" {
  product_key int [pk]
  product_id int
  product_name varchar
  brand varchar
  category varchar
  department varchar
  retail_price decimal
  cost decimal
  sku varchar
}

Table "dim_location" {
  location_key int [pk]
  distribution_center_id int
  center_name varchar
  latitude decimal
  longitude decimal
  state varchar
  city varchar
}

Table "dim_date" {
  date_key int [pk]
  full_date date
  day_of_week int
  day_name varchar
  day_of_month int
  day_of_year int
  week_of_year int
  month_number int
  month_name varchar
  quarter int
  year int
  is_weekend boolean
  season varchar
}

// Fact Tables
Table "fact_sales" {
  sales_key int [pk]
  order_item_id int
  customer_key int [ref: > dim_customer.customer_key]
  product_key int [ref: > dim_product.product_key]
  location_key int [ref: > dim_location.location_key]
  date_key int [ref: > dim_date.date_key]
  order_id int
  quantity int
  sale_price decimal
  gross_margin decimal
  is_returned boolean
  shipping_time int
  status varchar
}

Table "fact_inventory" {
  inventory_key int [pk]
  product_key int [ref: > dim_product.product_key]
  location_key int [ref: > dim_location.location_key]
  date_key int [ref: > dim_date.date_key]
  quantity_on_hand int
  quantity_received int
  quantity_sold int
  stock_level_status varchar
}