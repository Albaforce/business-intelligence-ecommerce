import pandas as pd
import matplotlib.pyplot as plt

cleaned_file = "../dataset/cleaned_data.csv"

def analyze_data():
    # Load cleaned data
    data = pd.read_csv(cleaned_file)

    # Analyze CallType distribution
    call_type_counts = data["CallType"].value_counts()
    print(call_type_counts)

    # Create a bar chart
    call_type_counts.plot(kind="bar", color=["blue", "orange"])
    plt.title("Call Type Distribution")
    plt.xlabel("Call Type")
    plt.ylabel("Count")
    plt.savefig("../reports/call_type_distribution.png")
    print("Visualization saved!")

if __name__ == "__main__":
    analyze_data()
