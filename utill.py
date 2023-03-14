import pandas as pd
PATH = "/Users/junyuwu/Netflix /components/netfix_cleaned.csv"
df = pd.read_csv(PATH)
df.fillna(method="ffill", inplace=True)
df["hour"] = df["duration"].str.extract(r'(\d+)h')
df["hour"].fillna("0", inplace=True)
df["hour"] = df["hour"].astype(int)
new_df = df[df["release_year"] >= 2020]
new_df = new_df[new_df["hour"]>=2]
new_df.reset_index(drop=True, inplace=True)

def get_year():
    year = new_df["release_year"].value_counts()
    list_year = sorted(list(set(year.index.tolist())))
    return list_year

def get_year_count():
    byyear = new_df["release_year"].value_counts().to_frame()
    byyear.reset_index(inplace=True)
    byyear.rename(columns = {'index':'year', "release_year":"release movies count"}, inplace=True)
    return byyear

def get_year_rate_list():
    age = new_df["maturity_rating"].value_counts()
    list_Age = list(set(age.index.tolist()))
    return list_Age

def get_year_rate():
    byrate = new_df["maturity_rating"].value_counts().to_frame()
    byrate.reset_index(inplace=True)
    byrate.rename(columns = {'index':'age_limitation'}, inplace=True)
    return byrate

def get_mood():
    bymood = new_df["mood"].value_counts().to_frame()[:15]
    return bymood

def get_genre():
    bygenre = new_df["genre"].value_counts().to_frame()[:10]
    bygenre.reset_index(inplace=True)
    bygenre.rename(columns = {'index':'genre_classification'}, inplace=True)
    return bygenre

def get_sub():
    bysub = new_df["subtitles"].value_counts()[:3].to_frame()
    bysub.reset_index(inplace=True)
    bysub.rename(columns = {'index':'subtitle_classification'}, inplace=True)
    return bysub

def get_audio():
    byaudio = new_df["audio"].value_counts()[:10].to_frame()
    byaudio.reset_index(inplace=True)
    byaudio.rename(columns = {'index':'audio_classification'}, inplace=True)
    return byaudio