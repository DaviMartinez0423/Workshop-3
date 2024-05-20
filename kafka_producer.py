import pandas as pd
from sklearn.model_selection import train_test_split
from services.kafka import producer
import time

def normalization2015_2016(df, year):
    df = df.rename(columns={'Economy (GDP per Capita)':'GDP per Capita',
                            'Health (Life Expectancy)':'Life Expectancy',
                            'Family':'Social support',
                            'Trust (Government Corruption)':'Government Corruption'})
    df.columns = df.columns.str.lower()
    df['year'] = year
    return df

def normalization2017(df, year):
    df = df.rename(columns={'Happiness.Rank':'Happiness Rank',
                                  'Happiness.Score':'Happiness Score',
                                  'Whisker.high':'Upper Confidence Interval',
                                  'Whisker.low':'Lower Confidence Interval',
                                  'Economy..GDP.per.Capita.':'GDP per Capita',
                                  'Family':'Social support',
                                  'Health..Life.Expectancy.':'Life Expectancy',
                                  'Trust..Government.Corruption.':'Government Corruption',
                                  'Dystopia.Residual':'DystopiaResidual'})
    df.columns = df.columns.str.lower()
    df['year'] = year       
    return df

def normalization2018_2019(df, year):
    df = df.rename(columns={'Country or region':'Country',
                                    'Score':'Happiness Score',
                                    'Healthy life expectancy':'Life Expectancy',
                                    'Freedom to make life choices':'Freedom',
                                    'Perceptions of corruption':'Government Corruption'})

    df.columns = df.columns.str.lower()
    df['year'] = year
    return df

def transformations():
    # Reading
    df_2015 = pd.read_csv('notebooks/dataset/2015.csv')
    df_2016 = pd.read_csv('notebooks/dataset/2016.csv')
    df_2017 = pd.read_csv('notebooks/dataset/2017.csv')
    df_2018 = pd.read_csv('notebooks/dataset/2018.csv')
    df_2019 = pd.read_csv('notebooks/dataset/2019.csv')
    
    # Transformations
    df_2015 = normalization2015_2016(df_2015, 2015)
    df_2016 = normalization2015_2016(df_2016, 2016)
    df_2017 = normalization2017(df_2017, 2017)
    df_2018 = normalization2018_2019(df_2018, 2018)
    df_2019 = normalization2018_2019(df_2019, 2019)
    
    # Concatenation
    training_df = pd.concat([df_2015, df_2016, df_2017, df_2018, df_2019], ignore_index=True, join='inner')
    training_df = training_df.rename(columns={
        'happiness score': 'happiness_score',
        'gdp per capita': 'gdp_per_capita',
        'social support': 'social_support',
        'life expectancy': 'life_expectancy',
        'government corruption': 'government_corruption'
    })
    training_df = training_df.dropna()
    
    return training_df

def model(training_df):
    features = ['freedom','gdp_per_capita','life_expectancy','social_support']
    X = training_df[features]
    y = training_df['happiness_score']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    return training_df.loc[y_test.index]

if __name__ == "__main__":
    training_df = transformations()
    training_df = model(training_df)
    for index, row in training_df.iterrows():
        producer(row)
        time.sleep(1)