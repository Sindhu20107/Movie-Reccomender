import streamlit as st 
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.title("Movie reccomender system")
df=pd.read_csv(r"tmdb_5000_movies.csv")


C=df['vote_average'].mean()
m=df['vote_count'].quantile(0.9)

def weighted_rating(x,m=m,C=C):
    v=x['vote_count']
    R=x['vote_average']
    return (v/(+m)*R)+(m/(v+m)*C)
    
df['score']=df.apply(weighted_rating,axis=1)

def get_top10_movies_by_score():
    return df.sort_values('score',ascending=False).head(10)
    
def get_top10_movies_by_popularity():
    return df.sort_values('popularity',ascending =False).head(10)

def create_similarity():
    df['overview']=df['overview'].fillna('')
    vectorizer=TfidfVectorizer(stop_words="english")
    tfidf_matrix=vectorizer.fit_transform(df['overview'])
    sim=cosine_similarity(tfidf_matrix,tfidf_matrix)
    return sim
    
sim=create_similarity()

indices=pd.Series(df.index,index=df['title']).drop_duplicates()

def get_personalized_recommendation(title):
    idx=indices[title]
    sim_scores=list(enumerate(sim[idx]))
    sort_sim_scores=sorted(sim_scores,key=lambda x:x[1],reverse=True)
    sort_sim_scores=sort_sim_scores[1:11]
    movie_indices=[]
    for i in sort_sim_scores:
        movie_indices.append(i[0])

    return df.iloc[movie_indices]
    

option=st.sidebar.radio(
    "Select Recommendation Type",
    ("Weighted Rating","Popularity Based","Personalized")
)

if option=="Weighted Rating":
    st.subheader("Top 10 movies by weighted rating")
    movies=get_top10_movies_by_score()
    st.dataframe(movies[['title','vote_average','vote_count','score']])
elif option=="Popularity Based":
    st.subheader("Top 10 Popular movies")
    movies=get_top10_movies_by_popularity()
    st.dataframe(movies[['title','popularity']])
elif option=="Personalized":
    st.subheader("Top 10 Personalized recommendation")
    selected_movies=st.selectbox("Select a movie",df['title'].values)

    if st.button("Recommend"):
        rec_movies=get_personalized_recommendation(selected_movies)

        st.write("### Recommend Movies:")
        st.dataframe(rec_movies[['title','overview','vote_average']])






    