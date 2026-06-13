# Insurance Data Pipeline - Databricks Project

A comprehensive data engineering project implementing a Bronze-Silver-Gold lakehouse architecture for insurance data processing using Databricks Lakeflow Spark Declarative Pipelines.

## 📋 Project Overview

This project processes insurance data through a medallion architecture:
- **Bronze Layer**: Raw data ingestion from CSV files
- **Silver Layer**: Data quality checks and transformations  
- **Gold Layer**: Business metrics and analytics

## 🏗️ Architecture

```
📁 databricks-insurance-project/
├── 📁 transformations/          # Pipeline transformation files
│   ├── ingestion_to_bronze.sql  # Bronze layer: Raw data ingestion
│   ├── bronze_to_silver.sql     # Silver layer: Data quality & transforms
│   └── silver_to_gold.sql       # Gold layer: Business aggregations
├── 📄 README.md                 # This file
└── 📄 .gitignore                # Git ignore patterns
```

## 📊 Data Layers

### Bronze Layer (`01_bronze`)
Ingests raw CSV data from Unity Catalog volumes:
- **customer** - Customer demographics and information
- **policy** - Insurance policy details
- **claim** - Claims and incident data

### Silver Layer (`02_silver`)
Applies data quality rules and transformations:
- **Data Quality**: NOT NULL checks, value validation
- **Transformations**: Type casting, date parsing, string trimming
- **Cleaned Data**: Ready for analytics

### Gold Layer (`03_gold`)
Business-ready aggregated tables:
- **claims_per_policy** - Claims aggregated by policy
- **customer_risk_score** - Risk scoring per customer
- **fraud_signals** - Fraud detection indicators
- **policy_performance** - Policy performance metrics

## 🗃️ Data Schema

### Customer Data
- `customer_id`: Unique customer identifier
- `date_of_birth`: Customer birth date
- `borough`, `neighborhood`, `zip_code`: Location data
- `name`: Customer name

### Policy Data
- `POLICY_NO`: Unique policy identifier
- `CUST_ID`: Customer reference
- `POLICYTYPE`: Type of insurance policy
- `POL_ISSUE_DATE`, `POL_EFF_DATE`, `POL_EXPIRY_DATE`: Policy dates
- `MAKE`, `MODEL`, `MODEL_YEAR`: Vehicle information
- `SUM_INSURED`, `PREMIUM`, `DEDUCTABLE`: Financial data

### Claim Data
- `claim_no`: Unique claim identifier
- `policy_no`: Policy reference
- `claim_date`: Date of claim
- `injury`, `property`, `vehicle`: Damage breakdown
- `total`: Total claim amount
- `collision_type`: Type of incident
- `suspicious_activity`: Fraud indicator

## 🚀 Getting Started

### Prerequisites
- Databricks workspace with Unity Catalog enabled
- Access to `insurance_catalog` catalog
- Source data in Unity Catalog volumes:
  - `/Volumes/insurance_catalog/volum_raw/volum_raw_data/customer`
  - `/Volumes/insurance_catalog/volum_raw/volum_raw_data/policy`
  - `/Volumes/insurance_catalog/volum_raw/volum_raw_data/claim`

### Deployment

1. **Clone this repository** in your Databricks workspace
2. **Create a Lakeflow Pipeline**:
   - Go to Workflows → Lakeflow → Create Pipeline
   - Set source code path: `<your-repo-path>/transformations`
   - Configure target catalog: `insurance_catalog`
   - Set target schemas: `01_bronze`, `02_silver`, `03_gold`
3. **Run the pipeline** to process data through all layers

## 🔄 Pipeline Execution

```
[CSV Files] → [Bronze Tables] → [Silver Tables] → [Gold Tables]
   (Raw)         (Ingested)       (Cleansed)      (Analytics)
```

## 📈 Analytics Use Cases

- **Risk Assessment**: Identify high-risk customers based on claim history
- **Fraud Detection**: Flag suspicious claims for investigation
- **Policy Performance**: Analyze profitability by policy type
- **Customer Segmentation**: Group customers by risk level

## 🛠️ Technologies

- **Databricks**: Cloud data platform
- **Spark SQL**: Data processing
- **Delta Lake**: Storage format
- **Unity Catalog**: Data governance
- **Lakeflow Pipelines**: ETL orchestration

## 📝 Notes

- All tables use **streaming ingestion** for real-time processing
- **Data quality expectations** enforce business rules
- **Medallion architecture** ensures data quality progression
- **Unity Catalog** provides governance and lineage

## 👤 Author

Fahimeh Latifi
- GitHub: [@fahimeh-latifi](https://github.com/fahimeh-latifi)

## 📄 License

This project is available for educational and demonstration purposes.