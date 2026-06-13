# from pyspark import pipelines as dp
# from pyspark.sql import functions as F
# 
# # Gold layer: Claims aggregated per policy
# @dp.materialized_view(name="insurance_catalog.03_gold.claims_per_policy")
# def claims_per_policy():
#     return (
#         spark.read.table("insurance_catalog.02_silver.claim")
#         .groupBy("policy_no")
#         .agg(
#             F.count("claim_no").alias("total_claims"),
#             F.sum("total").alias("total_claim_amount"),
#             F.avg("total").alias("avg_claim_amount")
#         )
#     )
# 
# # Gold layer: Customer risk score based on claims
# @dp.materialized_view(name="insurance_catalog.03_gold.customer_risk_score")
# def customer_risk_score():
#     policy = spark.read.table("insurance_catalog.02_silver.policy").alias("c")
#     claim = spark.read.table("insurance_catalog.02_silver.claim").alias("cl")
#     
#     return (
#         policy.join(
#             claim,
#             F.col("c.policy_no") == F.col("cl.policy_no"),
#             "left"
#         )
#         .groupBy(F.col("c.CUST_ID"))
#         .agg(
#             F.count("cl.claim_no").alias("total_claims"),
#             F.sum("cl.total").alias("total_loss"),
#             F.when(F.sum("cl.total") > 10000, "HIGH")
#              .when(F.sum("cl.total").between(5000, 10000), "MEDIUM")
#              .otherwise("LOW")
#              .alias("risk_level")
#         )
#     )
# 
# # Gold layer: Fraud signals detection
# @dp.materialized_view(name="insurance_catalog.03_gold.fraud_signals")
# def fraud_signals():
#     return (
#         spark.read.table("insurance_catalog.02_silver.claim")
#         .select(
#             "claim_no",
#             "policy_no",
#             "suspicious_activity",
#             "total",
#             F.when((F.col("suspicious_activity") == True) & (F.col("total") > 5000), "HIGH_RISK")
#              .when(F.col("suspicious_activity") == True, "MEDIUM_RISK")
#              .otherwise("NORMAL")
#              .alias("fraud_flag")
#         )
#     )
# 
# # Gold layer: Policy performance metrics
# @dp.materialized_view(name="insurance_catalog.03_gold.policy_performance")
# def policy_performance():
#     return (
#         spark.read.table("insurance_catalog.02_silver.claim")
#         .groupBy("policy_no")
#         .agg(
#             F.count("*").alias("total_claims"),
#             F.sum("total").alias("total_payout"),
#             F.avg("total").alias("avg_payout")
#         )
#     )
