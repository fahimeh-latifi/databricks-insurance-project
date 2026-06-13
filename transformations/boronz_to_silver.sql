CREATE OR REFRESH STREAMING TABLE insurance_catalog.02_silver.policy
(
  CONSTRAINT valid_policy_no EXPECT (POLICY_NO IS NOT NULL) ON VIOLATION DROP ROW,
  CONSTRAINT valid_cust_id EXPECT (CUST_ID IS NOT NULL) ON VIOLATION DROP ROW,
  CONSTRAINT valid_policytype EXPECT (POLICYTYPE IS NOT NULL) ON VIOLATION DROP ROW
)
AS
SELECT
    POLICY_NO,
    CAST(CUST_ID AS DOUBLE) AS CUST_ID,
    TRIM(POLICYTYPE) AS POLICYTYPE,

    TRY_CAST(POL_ISSUE_DATE AS DATE) AS POL_ISSUE_DATE,
    TRY_CAST(POL_EFF_DATE AS DATE) AS POL_EFF_DATE,
    TRY_CAST(POL_EXPIRY_DATE AS DATE) AS POL_EXPIRY_DATE,

    TRIM(MAKE) AS MAKE,
    TRIM(MODEL) AS MODEL,
    CAST(MODEL_YEAR AS INT) AS MODEL_YEAR,

    TRIM(CHASSIS_NO) AS CHASSIS_NO,
    TRIM(USE_OF_VEHICLE) AS USE_OF_VEHICLE,
    TRIM(PRODUCT) AS PRODUCT,

    CAST(SUM_INSURED AS DOUBLE) AS SUM_INSURED,
    CAST(PREMIUM AS DOUBLE) AS PREMIUM,
    CAST(DEDUCTABLE AS INT) AS DEDUCTABLE,

    source_file,
    source_path,
    ingestion_time
FROM STREAM(insurance_catalog.01_bronze.policy);

CREATE OR REFRESH STREAMING TABLE insurance_catalog.02_silver.claim
(
  CONSTRAINT valid_claim_no EXPECT (claim_no IS NOT NULL) ON VIOLATION DROP ROW,
  CONSTRAINT valid_policy_no EXPECT (policy_no IS NOT NULL) ON VIOLATION DROP ROW,
  CONSTRAINT valid_total EXPECT (total >= 0) ON VIOLATION DROP ROW
)
AS
SELECT
    TRIM(claim_no) AS claim_no,
    TRIM(policy_no) AS policy_no,

    TRY_CAST(claim_date AS DATE) AS claim_date,

    CAST(months_as_customer AS INT) AS months_as_customer,

    CAST(injury AS INT) AS injury,
    CAST(property AS INT) AS property,
    CAST(vehicle AS INT) AS vehicle,

    CAST(total AS INT) AS total,

    TRIM(collision_type) AS collision_type,
    CAST(number_of_vehicles_involved AS INT) AS number_of_vehicles_involved,

    CAST(age AS DOUBLE) AS age,

    TRIM(insured_relationship) AS insured_relationship,

    TRY_CAST(license_issue_date AS DATE) AS license_issue_date,

    CAST(hour AS INT) AS hour,

    TRIM(type) AS type,
    TRIM(severity) AS severity,

    CAST(number_of_witnesses AS INT) AS number_of_witnesses,

    CAST(suspicious_activity AS BOOLEAN) AS suspicious_activity,

    _rescued_data
FROM STREAM(insurance_catalog.01_bronze.claim);

CREATE OR REFRESH STREAMING TABLE insurance_catalog.02_silver.customer
(
  CONSTRAINT valid_customer_id EXPECT (customer_id IS NOT NULL) ON VIOLATION DROP ROW,
  CONSTRAINT valid_name EXPECT (name IS NOT NULL) ON VIOLATION DROP ROW,
  CONSTRAINT valid_zip_code EXPECT (zip_code IS NOT NULL) ON VIOLATION DROP ROW
)
AS
SELECT
    CAST(customer_id AS DOUBLE) AS customer_id,

    TRY_CAST(date_of_birth AS DATE) AS date_of_birth,

    TRIM(borough) AS borough,
    TRIM(neighborhood) AS neighborhood,
    TRIM(zip_code) AS zip_code,
    TRIM(name) AS name,

    _rescued_data,

    source_file,
    source_path,
    ingestion_time

FROM STREAM(insurance_catalog.01_bronze.customer);
