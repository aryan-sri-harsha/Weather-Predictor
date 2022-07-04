import pandas as pd
import os
def modifiedCsv(fileName):
    df = pd.read_csv(fileName+".csv")
    df2 = df[87650:]
    df2.to_csv(fileName+"-modified.csv",index=False);
    return

if __name__ == "__main__":
    # modifiedCsv("pune");
    data = ["pune","delhi","bombay","hyderabad","jaipur","nagpur","bengaluru","kanpur"]
    for i in data:
        modifiedCsv(i);
        os.remove(i+".csv")