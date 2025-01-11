import scripts.etl as etl
import scripts.analysis as analysis

if __name__ == "__main__":
    print("Starting ETL process...")
    etl.clean_data()

    print("Starting analysis...")
    analysis.analyze_data()
