# dashboard-etl
ETL script for Google Data Studio Dashboard. The main objective of the script is to prepare the dataset for data visualization. ETL stands for "extract, transform and load". Therefore, the data pipeline will extract the dataset from various sources, transform the data using business logic and load the data into database for data visualization.
___
## 1. Extract Dataset
The data sources are stored in MySQL database. The list of sources are given below:
1. **`gds_advisory_transactions`**: This dataset contains transactional data originating from **Advisory** service module. Advisory is an income generating activity. Data gets appended everyday.
2. **`gds_expense_transactions`**: This dataset contains transactional data originating from **Expense** module. Expense is a cost incurring activity. Data gets appended everyday.
3. **`gds_machine_purchase_transactions`**: This dataset contains transactional data originating from **Machinery** module and contains *purchase transactions only*. Machine purchase is a cost incurring activity. Data gets appended everyday.
4. **`gds_machine_rent_transactions`**: This dataset contains transactional data originating from **Machinery** module and contains *rent transactions only*. Renting machine is an income generating activity. Data gets appended everyday.
5. **`gds_processing_transactions`**: This dataset contains transactional data originating from advisory service module. Processing records production footprints. Therefore, it is a cost incurring activity. Data gets appended everyday.
6. **`gds_purchase_transactions`**: This dataset contains transactional data originating from advisory service module. Purchase is a cost incurring activity. Data gets appended everyday.
7. **`gds_sale_transactions`**: This dataset contains transactional data originating from advisory service module. Sale is an income generating activity. Data gets appended everyday.
8. **`gds_stocks`**: This dataset contains transactional data originating from advisory service module. The dataset gets refreshed everyday and contains inventory level for the day. The remaining inventory can be considered asset for a business.
9. **`gds_users_information`**: This dataset contains transactional data originating from advisory service module. The dataset gets refreshed everyday and contains user information including drop-off date, start date and other relevant information.
## 2. Transform the Dataset
The dataset is transformed based on the business requirements. The business requirements are listed below:
1. **Financial Analytics**  
    * Number of Unique Countries
    * Number of Users incl. Franchisee (Network Manager) and FarmersHub
    * Number of Customers i.e. beneficiaries of the platform
    * Revenue
    * Gross Profit
    * Gross Profit Margin
    * Revenue Per Hub Per Month
    * Net Profit
    * Net Profit Margin
    * Profitability analysis
    * Revenue share from business category & product category
    * User count from each country and associated revenue
2. **Operational Analytics**
    * Number of unique farmers
    * Number of unique locations
    * Number of franchisee
    * Number of trader
    * Number of dropout i.e. churned user
    * Female ratio
    * Number of transactions
    * Program growth
    * Revenue, transaction count and region for each country
3. **Product performance**
    * Revenue for each business category
    * Category breakdown
    * Revenue trend for each category
    * Expenditure trend for each category
    * Product performance incl. revenue, gross profit & gross profit margin
4. **Data Quality**
    * Number of unique transactions
    * Number of transactions with mobile number
    * Number of transactions with phone number
    * Percentage of transactions with gender information
    * Transactions that are potentially anomalous
