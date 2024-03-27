import pandas as pd
import numpy as np
import neattext.functions  as nfx
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity, sigmoid_kernel



def load_data(filename):
    df = pd.read_csv(filename)
    return df

# #function to clean title
def cleaning_add_new_column(data):
    data = data.drop_duplicates()
    data['course_title'] = data['course_title'].apply(nfx.remove_shortwords)
    data['title_subject'] = data['course_title'] + ' ' +  data['subject']
    return data

#function to calculate remommed system by popularity
def popularity_based_recommendation(df, top_n=5):
  # Calcular el score de popularidad de cada curso
  df['popularity_score'] = 0.6 * df['num_subscribers'] + 0.4 * df['num_reviews']
  # ordenar por score de poupularidad
  df_sorted = df.sort_values(by='popularity_score', ascending=False)
  # Seleccionar las columnas titulo y score de popularidad
  recommended_courses = df_sorted[['course_title', 'popularity_score', 'subject']].head(top_n)

  return recommended_courses

#funcion based on contend
def recommed_based_contend(course):
    course_index = data[data['course_title']==course].index[0]
    distances = similarity[course_index]
    courses_list = sorted(list(enumerate(distances)), reverse = True, key =lambda x:x[1])[1:6]
    for i in courses_list:
        print(data.iloc[i[0]]['course_title'])

def search(query, vectorizer):
    query_vec = vectorizer.transform([query])

    similarity = cosine_similarity(query_vec, tfid).flatten()
    indices = np.argpartition(similarity, -10)[-10:]
    results = data.iloc[indices]
    results = results.sort_values('num_subscribers',ascending= False)

    return results.head(5)



