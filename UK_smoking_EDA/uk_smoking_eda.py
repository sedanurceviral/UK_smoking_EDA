import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 500)
pd.set_option('display.float_format', lambda x: '%.2f' % x)
pd.set_option('display.width', 100)

df = pd.read_csv(r'C:\Users\seda\Desktop\UK_Smoking_EDA\smoking.csv')


def check_df(dataframe, head=5):
    print("######### unique #########")
    print(dataframe.nunique())
    print("######### shape #########")
    print(dataframe.shape)
    print("######### types #########")
    print(dataframe.dtypes)
    print("######### head #########")
    print(dataframe.head(head))
    print("######### tail #########")
    print(dataframe.tail(head))
    print("######### NA #########")
    print(dataframe.isnull().sum())
    print('######### duplicates #########')
    print(dataframe.duplicated().sum())
    print("######### quantiles #########")
    print(dataframe.describe([0, 0.05, 0.50, 0.95, 0.99, 1]).T)
    print('######### info #########')
    print(dataframe.info())


check_df(df)
df.drop_duplicates(inplace=True)

cat_cols = [col for col in df.columns if str(df[col].dtypes) in ["category", "object", "bool"]]
num_but_cat = [col for col in df.columns if df[col].nunique() < 10 and df[col].dtypes in ["int64", "float64"]]
cat_but_car = [col for col in df.columns if df[col].nunique() > 20 and str(df[col].dtypes) in ["category", "object"]]
cat_cols = cat_cols + num_but_cat
cat_cols = [col for col in cat_cols if col not in cat_but_car]

df[cat_cols].nunique()
[col for col in df.columns if col not in cat_cols]


def cat_summary(dataframe, col_name, plot=False):
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
    print("################################################")
    if plot:
        sns.countplot(x=dataframe[col_name], data=dataframe)
        plt.xticks(rotation=45)
        plt.show(block=True)


for col in cat_cols:
    cat_summary(df, col, plot=True)

num_cols = [col for col in df.columns if df[col].dtypes in ["int64", "float64"]]
num_cols = [col for col in num_cols if col not in cat_cols]


def num_summary(dataframe, numerical_col, plot=False):
    quantiles = [0.05, 0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90, 0.95, 0.99]
    print(dataframe[numerical_col].describe(quantiles).T)
    if plot:
        dataframe[numerical_col].hist()
        plt.xlabel(numerical_col)
        plt.title(numerical_col)
        plt.xticks(rotation=45)
        plt.show(block=True)


for col in num_cols:
    num_summary(df, col, plot=True)


def target_summary_with_cat(dataframe, target, categorical_col):
    print(pd.DataFrame({"TARGET_MEAN": dataframe.groupby(categorical_col)[target].mean()}), end="\n\n\n")


for col in cat_cols:
    target_summary_with_cat(df, "amt_weekends", col)

for col in cat_cols:
    target_summary_with_cat(df, "amt_weekdays", col)


def target_summary_with_num(dataframe, target, numerical_col):
    print(dataframe.groupby(target).agg({numerical_col: "mean"}), end="\n\n\n")


for col in num_cols:
    target_summary_with_num(df, 'gender', col)

for col in num_cols:
    target_summary_with_num(df, 'highest_qualification', col)

for col in num_cols:
    target_summary_with_num(df, 'gross_income', col)

for col in num_cols:
    target_summary_with_num(df, 'region', col)

for col in num_cols:
    target_summary_with_num(df, 'type', col)

