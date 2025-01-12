# Business Intelligence E-Commerce Project

## Project Overview
The **Business Intelligence E-Commerce Project** is designed to process, analyze, and extract valuable insights from e-commerce data. This project covers data cleaning, transformation, and analysis, culminating in a star schema data warehouse. The insights support decision-making processes for optimizing business operations.

---

## Project Structure
```
business-intelligence-ecommerce
├── data
│   ├── processed
│   │   ├── cleaned_events_chunks
│   │   │   ├── cleaned_events_chunk_1.csv
│   │   │   ├── cleaned_events_chunk_2.csv
│   │   │   ├── cleaned_events_chunk_3.csv
│   │   │   └── cleaned_events_chunk_4.csv
│   │   ├── cleaned_distribution_centers.csv
│   │   ├── cleaned_events.csv
│   │   ├── cleaned_inventory_items.csv
│   │   ├── cleaned_order_items.csv
│   │   ├── cleaned_orders.csv
│   │   ├── cleaned_products.csv
│   │   └── cleaned_users.csv
│   └── raw
│       ├── events_chunks
│       │   ├── events_1.csv
│       │   ├── events_2.csv
│       │   ├── events_3.csv
│       │   └── events_4.csv
│       ├── distribution_centers.csv
│       ├── inventory_items.csv
│       ├── order_items.csv
│       ├── orders.csv
│       ├── products.csv
│       └── users.csv
├── src
│   ├── analysis
│   │   └── clustering.py
│   ├── ETL
│   │   ├── pipeline.ipynb
│   │   └── visualisations.ipynb
│   └── Warehouse
│       └── schema.sql
├── README.md
└── requirements.txt
```

---

## Features
1. **Data Processing**:
   - Raw data stored in `data/raw/`.
   - Cleaned and transformed data stored in `data/processed/`.

2. **ETL Pipeline**:
   - Found in `src/ETL/pipeline.ipynb`.
   - Automates data extraction, transformation, and loading into a warehouse-ready format.

3. **Data Warehouse Schema**:
   - Star schema SQL scripts available in `src/Warehouse/schema.sql`.

4. **Analysis**:
   - Clustering analysis performed in `src/analysis/clustering.py`.
   - Data visualizations in `src/ETL/visualisations.ipynb`.

---

## Requirements
The project depends on the following Python packages:
- `pandas`
- `numpy`
- `matplotlib`
- `seaborn`
- `geopandas`
- `shapely`

Install all required packages using:
```bash
pip install -r requirements.txt
```

---

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/Albaforce/business-intelligence-        ecommerce.git
   cd business-intelligence-ecommerce
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Execute the ETL pipeline:
   - Open `src/ETL/pipeline.ipynb` in Jupyter Notebook and run all cells.

4. Run the analysis scripts:
   - For clustering analysis, execute `src/analysis/clustering.py`.

5. Access the data warehouse schema:
   - SQL scripts for creating and populating the star schema are available in `src/Warehouse/schema.sql`.

---

## Data
The data directory includes:
- **Raw Data**: Unprocessed CSV files in `data/raw/`.
- **Processed Data**: Cleaned and transformed datasets in `data/processed/`.

---

## Contribution Guidelines
1. Fork the repository and create a new branch for your feature or bug fix.
2. Follow proper coding standards and comment your code.
3. Submit a pull request with detailed explanations.

---

## License
This project is licensed under the [MIT License](LICENSE).

---

## Acknowledgments
- Inspiration and support from the open-source community.
- Datasets used for analysis sourced from simulated e-commerce activities.
- dataset link : https://www.kaggle.com/datasets/mustafakeser4/looker-ecommerce-bigquery-dataset?select=users.csv

