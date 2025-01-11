import pandas as pd

# Load raw data
raw_file = "../dataset/raw_data.csv"
cleaned_file = "../dataset/cleaned_data.csv"

def clean_data():
    # Read raw data
    data = pd.read_csv(raw_file, delimiter="\t")

    # Rename columns
    data.columns = ["ID", "CallType", "Category", "SubCategory", "Feedback"]

    # Fill missing feedback
    data["Feedback"] = data["Feedback"].fillna("No feedback")

    # Save cleaned data
    data.to_csv(cleaned_file, index=False)
    print("Data cleaned and saved!")

if __name__ == "__main__":
    clean_data()
