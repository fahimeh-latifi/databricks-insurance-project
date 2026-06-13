# from pyspark import pipelines as dp
# from pyspark.sql import functions as F
# 
# # Silver layer: Policy data with data quality checks
# @dp.table(name="insurance_catalog.02_silver.policy")
# @dp.expect_or_drop("valid_policy_no", "POLICY_NO IS NOT NULL")
# @dp.expect_or_drop("valid_cust_id", "CUST_ID IS NOT NULL")
# @dp.expect_or_drop("valid_policytype", "POLICYTYPE IS NOT NULL")
# def policy():
#     return (
#         spark.readStream.table("insurance_catalog.01_bronze.policy")
#         .select(
#             F.col("POLICY_NO"),
#             F.col("CUST_ID").cast("double").alias("CUST_ID"),
#             F.trim(F.col("POLICYTYPE")).alias("POLICYTYPE"),
#             
#             F.expr("TRY_CAST(POL_ISSUE_DATE AS DATE)").alias("POL_ISSUE_DATE"),
#             F.expr("TRY_CAST(POL_EFF_DATE AS DATE)").alias("POL_EFF_DATE"),
#             F.expr("TRY_CAST(POL_EXPIRY_DATE AS DATE)").alias("POL_EXPIRY_DATE"),
#             
#             F.trim(F.col("MAKE")).alias("MAKE"),
#             F.trim(F.col("MODEL")).alias("MODEL"),
#             F.col("MODEL_YEAR").cast("int").alias("MODEL_YEAR"),
#             
#             F.trim(F.col("CHASSIS_NO")).alias("CHASSIS_NO"),
#             F.trim(F.col("USE_OF_VEHICLE")).alias("USE_OF_VEHICLE"),
#             F.trim(F.col("PRODUCT")).alias("PRODUCT"),
#             
#             F.col("SUM_INSURED").cast("double").alias("SUM_INSURED"),
#             F.col("PREMIUM").cast("double").alias("PREMIUM"),
#             F.col("DEDUCTABLE").cast("int").alias("DEDUCTABLE"),
#             
#             F.col("source_file"),
#             F.col("source_path"),
#             F.col("ingestion_time")
#         )
#     )
# 
# # Silver layer: Claim data with data quality checks
# @dp.table(name="insurance_catalog.02_silver.claim")
# @dp.expect_or_drop("valid_claim_no", "claim_no IS NOT NULL")
# @dp.expect_or_drop("valid_policy_no", "policy_no IS NOT NULL")
# @dp.expect_or_drop("valid_total", "total >= 0")
# def claim():
#     return (
#         spark.readStream.table("insurance_catalog.01_bronze.claim")
#         .select(
#             F.trim(F.col("claim_no")).alias("claim_no"),
#             F.trim(F.col("policy_no")).alias("policy_no"),
#             
#             F.expr("TRY_CAST(claim_date AS DATE)").alias("claim_date"),
#             
#             F.col("months_as_customer").cast("int").alias("months_as_customer"),
#             
#             F.col("injury").cast("int").alias("injury"),
#             F.col("property").cast("int").alias("property"),
#             F.col("vehicle").cast("int").alias("vehicle"),
#             
#             F.col("total").cast("int").alias("total"),
#             
#             F.trim(F.col("collision_type")).alias("collision_type"),
#             F.col("number_of_vehicles_involved").cast("int").alias("number_of_vehicles_involved"),
#             
#             F.col("age").cast("double").alias("age"),
#             
#             F.trim(F.col("insured_relationship")).alias("insured_relationship"),
#             
#             F.expr("TRY_CAST(license_issue_date AS DATE)").alias("license_issue_date"),
#             
#             F.col("hour").cast("int").alias("hour"),
#             
#             F.trim(F.col("type")).alias("type"),
#             F.trim(F.col("severity")).alias("severity"),
#             
#             F.col("number_of_witnesses").cast("int").alias("number_of_witnesses"),
#             
#             F.col("suspicious_activity").cast("boolean").alias("suspicious_activity"),
#             
#             F.col("_rescued_data")
#         )
#     )
# 
# # Silver layer: Customer data with data quality checks
# @dp.table(name="insurance_catalog.02_silver.customer")
# @dp.expect_or_drop("valid_customer_id", "customer_id IS NOT NULL")
# @dp.expect_or_drop("valid_name", "name IS NOT NULL")
# @dp.expect_or_drop("valid_zip_code", "zip_code IS NOT NULL")
# def customer():
#     return (
#         spark.readStream.table("insurance_catalog.01_bronze.customer")
#         .select(
#             F.col("customer_id").cast("double").alias("customer_id"),
#             
#             F.expr("TRY_CAST(date_of_birth AS DATE)").alias("date_of_birth"),
#             
#             F.trim(F.col("borough")).alias("borough"),
#             F.trim(F.col("neighborhood")).alias("neighborhood"),
#             F.trim(F.col("zip_code")).alias("zip_code"),
#             F.trim(F.col("name")).alias("name"),
#             
#             F.col("_rescued_data"),
#             
#             F.col("source_file"),
#             F.col("source_path"),
#             F.col("ingestion_time")
#         )
#     )
