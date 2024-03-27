import pandas as pd
import pickle
import tkinter as tk
from tkinter import ttk, messagebox

#1. Sistema de Recomendación Basado en popularidad
def popularity_based_recommendation(df, top_n=5):
  # Calcular el score de popularidad de cada curso
  df['popularity_score'] = 0.6 * df['num_subscribers'] + 0.4 * df['num_reviews']

  # ordenar por score de poupularidad
  df_sorted = df.sort_values(by='popularity_score', ascending=False)

  # Seleccionar las columnas titulo y score de popularidad
  recommended_courses = df_sorted[['course_title', 'popularity_score']].head(top_n)

  return recommended_courses


# 2.Sistema de recomedación Basado en similaridad
with open('similarity.pkl', 'rb') as f:
  similarity = pickle.load(f)

#funcction bases on contend
def recommed(course):
    try:
       course_index = data[data['course_title']==course].index[0]
       distances = similarity[course_index]
       courses_list = sorted(list(enumerate(distances)), reverse = True, key =lambda x:x[1])[1:6]
       recommended_courses = [data.iloc[i[0]]['course_title'] for i in courses_list]
       return recommended_courses
    except IndexError:
       messagebox.showerror('Error Course {}no found.'.format(course))


#3. Button de recomendación
def recommed_button_click():
   course_title = course_var.get()
   recommended_courses = recommed(course_title)
   if recommended_courses:
      popularity_label.pack_forget()
      result_label.config(text="Recommended Courses:\n" + '\n'.join(recommended_courses))

#4. Application
# Create the main applications window
root = tk.Tk()
root.title('Recommend System')
root.geometry('400x300')

# change fond and color
font_style = ('Arial', 12)
label_color = 'blue'
heading_color = 'red'
button_color = 'green'
result_label_color = 'black'

#5. Create and Place GUI elements
course_titles = data['couse_title'].tolist()
course_var = tk.StringVar(value = course_titles[0])
course_dropdown = ttk.Combobox(root, textvariable=course_var, values=course_titles, width=40, font=font_style)
course_dropdown.pack(pady=5)

popularity_recommendations = popularity_based_recommendation(data, top_n=5)
popularity_label = tk.Label(root, text="Popularity-based Recommendations:\n" + popularity_recommendations.to_string(index=False),
                             font=font_style, fg=label_color)
popularity_label.pack()

recommend_button = tk.Button(root, text="Recommend", command= recommend_button_click, width=20, font=font_style, fg=button_color)
recommend_button.pack(pady=10)

result_label = tk.Label(root, text="", wraplength=350, font=font_style, fg=result_label_color)
result_label.pack()

root.mainloop()

       