CREATE OR REFRESH STREAMING TABLE insurance_catalog.01_bronze.customer
AS
SELECT
    *,
    _metadata.file_name AS source_file,
    _metadata.file_path AS source_path,
    current_timestamp() AS ingestion_time
FROM STREAM(
    read_files(
        '/Volumes/insurance_catalog/volum_raw/volum_raw_data/customer',
        format => 'csv',
        header => true
    )
);
CREATE OR REFRESH STREAMING TABLE insurance_catalog.01_bronze.policy
AS
SELECT
    *,
    _metadata.file_name AS source_file,
    _metadata.file_path AS source_path,
    current_timestamp() AS ingestion_time
FROM STREAM(
    read_files(
        '/Volumes/insurance_catalog/volum_raw/volum_raw_data/policy',
        format => 'csv',
        header => true
    )
);
CREATE OR REFRESH STREAMING TABLE insurance_catalog.01_bronze.claim
AS
SELECT
    *,
    _metadata.file_name AS source_file,
    _metadata.file_path AS source_path,
    current_timestamp() AS ingestion_time
FROM STREAM(
    read_files(
        '/Volumes/insurance_catalog/volum_raw/volum_raw_data/claim',
        format => 'csv',
        header => true
    )
);