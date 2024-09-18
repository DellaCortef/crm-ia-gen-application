# crm-ia-gen-application

""""
This Repo has the main objective of creating the integration of our CRM with CHatGPT's AI Gen. With integration and development, we will be able to ask ChatGPT via variables in Python, and get the answers also stored in variables in Python.
""""

### CRM Analytics Development Series ###

The CRM development series has three stages:

**data-pipeline-pocket-reference:**

-  Repository focused on Data Engineering. We will build a front-end integration with Postgre. Based on the sales input data, this data will automatically be stored in the DB. We will apply *contract data* rules to ensure data consistency.

**crm-dbt-datawarehouse-etl:**

- repository focused on applying the necessary transformations to the data, using **DBT** as a tool. We will create our *medallion* layers, such as bronze, silver and gold, and apply the business rules to create the necessary tables or views for Business.

** :**

- 