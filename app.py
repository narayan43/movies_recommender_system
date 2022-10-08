import streamlit as st
import pandas as pd
import pickle
import requests
import creds
with open("./data_dict.pkl", 'rb') as f:
    x = pickle.load(f)
with open("./similarvec.pkl", 'rb') as f:
    similarity = pickle.load(f)
data=pd.DataFrame(x)
print(data.shape)
st.title("Movies Recommender System")
sellected_movie=st.selectbox("Sellect movie",data['title'].values)

def similar_10_movies(movie):
  movies_name=[]
  movie_index=data[data['title']==movie].index[0]
  movies_tuples=sorted(enumerate(similarity[movie_index]),reverse=True,key=lambda x :x[1])[1:7]
  for i in movies_tuples:
      movies=data.iloc[i[0]]
      movies_name.append(movies[0])
  return movies_name
movies_list=similar_10_movies(sellected_movie)
def poster_links():
    posters_paths=[]
    for i in movies_list:
      try: 
        json_path=f'https://api.themoviedb.org/3/search/movie?api_key={creds.api_key}&language=en-US&query={i}&page=1&include_adult=false'  
        res =requests.get(json_path)
        json=res.json()
        pos_path= json['results'][0]['poster_path']
        posters_paths.append(f'https://image.tmdb.org/t/p/original/{pos_path}')
      except:
         posters_paths.append("/Users/narayan/Documents/python_data_science_projects/recommender_system/images.jpeg")
    return posters_paths
        
posters_paths=poster_links()
col1, col2, col3, = st.columns(3)

with col1:
   st.header(movies_list[0])
   st.image(posters_paths[0])
with col2:
   st.header(movies_list[1])
   st.image(posters_paths[1])
with col3:
   st.header(movies_list[2])
   st.image(posters_paths[2])
col4 ,col5,col6=st.columns(3)
with col4:
   st.header(movies_list[3])
   st.image(posters_paths[3])
with col5:
   st.header(movies_list[4])
   st.image(posters_paths[4])
with col6:
   st.header(movies_list[5])
   st.image(posters_paths[5])


