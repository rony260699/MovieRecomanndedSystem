# AI-Powered-Movie-Recommender-System

An AI-based movie recommendation system built using Python, Machine Learning, and Streamlit that suggests the top 5 similar movies based on user selection. The system also fetches real-time movie posters using the TMDB API, providing an interactive and visually appealing experience.

This project is designed as a portfolio project to demonstrate skills in machine learning, API integration, and UI development.

## 🚀 Features

- **Movie Recommendation:** Suggests top 5 similar movies based on selected movie.

- **Machine Learning Model:** Uses cosine similarity on movie feature vectors.

- **Poster Fetching:** Retrieves real-time movie posters using the TMDB API.

- **Interactive UI:** Clean and responsive interface built with Streamlit.

- **Side-by-Side Display:** Displays 5 recommended movies with posters simultaneously.

## ⚙️ Technologies Used

- **Python**

- **Streamlit**

- **Scikit-learn**

- **Pandas**

- **Pickle**

- **TMDB API**

- **Cosine Similarity**

## 🔍 How It Works

### Data Preparation
Movie data is preprocessed and converted into feature vectors based on relevant attributes.

### Model Building
A similarity matrix is created using cosine similarity, which measures how similar movies are to each other.

### Recommendation Logic
When a user selects a movie, the system finds the most similar movies from the similarity matrix and recommends the top 5.

### API Integration
The TMDB API is used to fetch movie posters dynamically for better visualization.

### User Interface
Streamlit provides an interactive UI where users can select movies and instantly view recommendations.

## 🌐 Live Demo

👉 Try it here: https://lnkd.in/gsUszMmH

Screenshots

(Add screenshots of the app interface, movie selection, and recommendations here)
<img width="1897" height="867" alt="Screenshot 2026-01-16 170936" src="https://github.com/user-attachments/assets/2fc2736b-dfda-4e9f-af17-15e4d3e7889b" />
<img width="1892" height="903" alt="Screenshot 2026-01-16 170931" src="https://github.com/user-attachments/assets/afed6308-73f9-4717-bc81-5465984cf6ec" />
<img width="1908" height="813" alt="Screenshot 2026-01-16 170948" src="https://github.com/user-attachments/assets/a339917f-cc1e-41b1-ae11-cf7be169902e" />
<img width="1886" height="882" alt="Screenshot 2026-01-16 170942" src="https://github.com/user-attachments/assets/4195c402-577e-4d44-963b-cc372eeae8bc" />

## 📌 Future Enhancements

Personalized recommendations using user ratings

Genre-based and popularity-based filtering

User login and watchlist feature

Improved recommendation accuracy with hybrid models
