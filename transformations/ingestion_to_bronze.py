# from pyspark import pipelines as dp
# from pyspark.sql import functions as F
# 
# # Bronze layer: Customer data ingestion
# @dp.table(name="insurance_catalog.01_bronze.customer")
# def customer():
#     return (
#         spark.readStream.format("cloudFiles")
#         .option("cloudFiles.format", "csv")
#         .option("header", "true")
#         .option("cloudFiles.schemaHints", "customer_id double, date_of_birth date")
#         .load("/Volumes/insurance_catalog/volum_raw/volum_raw_data/customer")
#         .select(
#             "*",
#             F.col("_metadata.file_name").alias("source_file"),
#             F.col("_metadata.file_path").alias("source_path"),
#             F.current_timestamp().alias("ingestion_time")
#         )
#     )
# 
# # Bronze layer: Policy data ingestion
# @dp.table(name="insurance_catalog.01_bronze.policy")
# def policy():
#     return (
#         spark.readStream.format("cloudFiles")
#         .option("cloudFiles.format", "csv")
#         .option("header", "true")
#         .option("cloudFiles.schemaHints", "CUST_ID double, POL_ISSUE_DATE date, POL_EFF_DATE date, POL_EXPIRY_DATE date, SUM_INSURED double, PREMIUM double, DEDUCTABLE int, MODEL_YEAR int")
#         .load("/Volumes/insurance_catalog/volum_raw/volum_raw_data/policy")
#         .select(
#             "*",
#             F.col("_metadata.file_name").alias("source_file"),
#             F.col("_metadata.file_path").alias("source_path"),
#             F.current_timestamp().alias("ingestion_time")
#         )
#     )
# 
# # Bronze layer: Claim data ingestion
# @dp.table(name="insurance_catalog.01_bronze.claim")
# def claim():
#     return (
#         spark.readStream.format("cloudFiles")
#         .option("cloudFiles.format", "csv")
#         .option("header", "true")
#         .option("cloudFiles.schemaHints", "claim_date date, months_as_customer int, injury int, property int, vehicle int, total int, number_of_vehicles_involved int, age double, license_issue_date date, hour int, number_of_witnesses int, suspicious_activity boolean")
#         .load("/Volumes/insurance_catalog/volum_raw/volum_raw_data/claim")
#         .select(
#             "*",
#             F.col("_metadata.file_name").alias("source_file"),
#             F.col("_metadata.file_path").alias("source_path"),
#             F.current_timestamp().alias("ingestion_time")
#         )
#     )
