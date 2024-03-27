import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import neattext.functions  as nfx
from sklearn.preprocessing import MinMaxScaler
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity, sigmoid_kernel
from functions import load_data,cleaning_add_new_column, popularity_based_recommendation,recommed_based_contend
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors


#settings
st.set_option('deprecation.showPyplotGlobalUse', False)


# 0=> Get Data
data = load_data('data.csv')
#clening dataset
data = cleaning_add_new_column(data)



#1. Body
st.title('Recommendation System')
tab1, tab2 = st.tabs(['Based on Popularity', 'Based on Content'])

with tab1:
  options = ['Popularity', 'Avg Weigted']
  menu = st.sidebar.selectbox('Select type Based on Popularity', options)
  if menu == 'Popularity':
     num = st.number_input('Enter a Number you want to be recommended', min_value=5)
     popularidad = popularity_based_recommendation(data, num)
     fig = px.bar(popularidad, y='course_title', x='popularity_score', title='Recomendation Base on Popularity Scores',color = 'subject',)
     st.plotly_chart(fig) 
  else:
     v = data['num_subscribers']
     R = data['num_reviews']
     C = data['num_subscribers'].mean()
     m = data['num_subscribers'].quantile(0.70)
     data['weighted_average'] = ((R*v)+ (C*m))/(v+m)
     
     #viz
     num = st.number_input('Enter a Number you want to be recommended', min_value=5)
     w = data[['course_title','subject' ,'weighted_average']].sort_values(by = 'weighted_average', ascending=False).head(num)
     fig = px.bar(w,y="course_title",x="weighted_average",title="Recomendation Base on Weigted Average Scores",  color = 'subject',)
     st.plotly_chart(fig)


#Based on Content

with tab2:
   #vetorizar los datos
   options1 = ['Cosine Similarity', 'Using k-Nearest Neighbors']
   menu1 = st.sidebar.selectbox('Select type Based on Content', options1)
   
   
   

   if menu1 == 'Cosine Similarity':
      #cv = CountVectorizer(max_features=3000)
      #vectors = cv.fit_transform(data['title_subject']).toarray() 
      #Clacular la similaridad
      #similarity = cosine_similarity(vectors) 

      #User Enter
      titulos = data['course_title'].to_list()
      selec_title = st.selectbox('Seleccione el Titulo', titulos)
      #data_select = data[data['course_title'] == selec_title]
      #st.write(selec_title)
      
      # Recommend System
      vectorizer = TfidfVectorizer()
      tfid = vectorizer.fit_transform(data['title_subject'])
      
      def search(query, vectorizer):
         query_vec = vectorizer.transform([query])
         similarity = cosine_similarity(query_vec, tfid).flatten()
         indeces = np.argpartition(similarity, -10)[-10:]
         results = data.iloc[indeces]
         results = results.sort_values('num_subscribers',ascending= False)

         return results[1:6]
      
      recommendetion = search(selec_title, vectorizer)[['course_title', 'subject']]
      st.write(recommendetion)
     
      
   else:
      df_pivot = data.pivot(index = 'course_title', columns = 'course_id', values = 'num_subscribers' ).fillna(0)
      #csc matrix
      df_pivot_matrix = csr_matrix(df_pivot.values)
      #model setup
      model = NearestNeighbors(metric='cosine', algorithm='brute')
      model.fit(df_pivot_matrix)

      titulos = df_pivot.index
      selec_title = st.selectbox('Seleccione el Titulo', titulos)
      query_index = df_pivot.loc[selec_title].values.reshape(1,-1)
      #st.write(query_index)
      
      distances, indices  = model.kneighbors(query_index)
      #st.write(indices)
      
      for i in range(0, len(distances.flatten())):
         if i == 0:
            st.write('Recommendations for: `{0}`\n'.format(selec_title))
         else:
            st.write('{0}: {1}.'.format(i, df_pivot.index[indices.flatten()[i]]))


      
      




 
      



