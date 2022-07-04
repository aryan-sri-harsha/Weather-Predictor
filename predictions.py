
def get_predictions(cityName):
    import pandas as pd
    import datetime
    import math
    x = datetime.datetime.now()
    # print(x.month,x.day)
    df = pd.read_csv(cityName+"-coef.csv")
    result = []
    #day month
    for row in df.iterrows():
        # print(row[1][0])
        result.append(math.ceil(row[1][0]+row[1][1]*x.day+row[1][2]*x.month))
    return result

if __name__ == "__main__":
    res = get_predictions("hyderabad")
    print(res)
