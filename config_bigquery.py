from bigquery_management.modelo_bigquery import BigQueryConfig

# =============================================================================
# Raw data tables
# =============================================================================

RAW_TABLE_CUSTOMERS = BigQueryConfig(
    project_id="olist-funnel-analysis-494020",
    dataset="raw",
    table="customers"
)

RAW_TABLE_GEOLOCATION = BigQueryConfig(
    project_id="olist-funnel-analysis-494020",
    dataset="raw",
    table="geolocation"
)

RAW_TABLE_ORDER_ITEMS = BigQueryConfig(
    project_id="olist-funnel-analysis-494020",
    dataset="raw",
    table="order_items"
)

RAW_TABLE_ORDER_PAYMENTS = BigQueryConfig(
    project_id="olist-funnel-analysis-494020",
    dataset="raw",
    table="order_payments"
)

RAW_TABLE_ORDER_REVIEWS = BigQueryConfig(
    project_id="olist-funnel-analysis-494020",
    dataset="raw",
    table="order_reviews"
)

RAW_TABLE_ORDERS = BigQueryConfig(
    project_id="olist-funnel-analysis-494020",
    dataset="raw",
    table="orders"
)

RAW_TABLE_PRODUCTS = BigQueryConfig(
    project_id="olist-funnel-analysis-494020",
    dataset="raw",
    table="products"
)

RAW_TABLE_SELLERS = BigQueryConfig(
    project_id="olist-funnel-analysis-494020",
    dataset="raw",
    table="sellers"
)

RAW_TABLE_CATEGORY_NAME_TRANSLATION = BigQueryConfig(
    project_id="olist-funnel-analysis-494020",
    dataset="raw",
    table="category_name_translation"
)