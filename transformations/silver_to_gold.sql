CREATE OR REFRESH MATERIALIZED VIEW insurance_catalog.03_gold.claims_per_policy AS
SELECT
    policy_no,
    COUNT(claim_no) AS total_claims,
    SUM(total) AS total_claim_amount,
    AVG(total) AS avg_claim_amount
FROM insurance_catalog.02_silver.claim
GROUP BY policy_no;

CREATE OR REFRESH MATERIALIZED VIEW insurance_catalog.03_gold.customer_risk_score AS
SELECT
    c.CUST_ID,
    COUNT(cl.claim_no) AS total_claims,
    SUM(cl.total) AS total_loss,
    
    CASE 
        WHEN SUM(cl.total) > 10000 THEN 'HIGH'
        WHEN SUM(cl.total) BETWEEN 5000 AND 10000 THEN 'MEDIUM'
        ELSE 'LOW'
    END AS risk_level
FROM insurance_catalog.02_silver.policy c
LEFT JOIN insurance_catalog.02_silver.claim cl
    ON c.policy_no = cl.policy_no
GROUP BY c.CUST_ID;

CREATE OR REFRESH MATERIALIZED VIEW insurance_catalog.03_gold.fraud_signals AS
SELECT
    claim_no,
    policy_no,
    suspicious_activity,
    total,
    
    CASE 
        WHEN suspicious_activity = TRUE AND total > 5000 THEN 'HIGH_RISK'
        WHEN suspicious_activity = TRUE THEN 'MEDIUM_RISK'
        ELSE 'NORMAL'
    END AS fraud_flag
FROM insurance_catalog.02_silver.claim;

CREATE OR REFRESH MATERIALIZED VIEW insurance_catalog.03_gold.policy_performance AS
SELECT
    policy_no,
    COUNT(*) AS total_claims,
    SUM(total) AS total_payout,
    AVG(total) AS avg_payout
FROM insurance_catalog.02_silver.claim
GROUP BY policy_no;
