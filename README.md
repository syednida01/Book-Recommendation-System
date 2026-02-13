# 📚 Book Recommendation System

  A Machine Learning–based Book Recommendation System built using **Python**, **Pandas**, **Scikit-learn**, and **Streamlit**.
  This application recommends books to users based on popularity and similarity using collaborative filtering techniques.
  
--- 

## 🚀 Project Overview

  This project analyzes user ratings and book metadata to build a recommendation engine.
  It provides:
  
  - 📖 Popular books recommendation
  
  - 🤝 Similar book suggestions (based on user ratings)
  
  - 🌐 Interactive web interface using Streamlit
  
  The goal is to demonstrate how recommendation systems work using real-world datasets.
  
---
## 🛠️ Tech Stack

  - 1.Python
  
  - 2.Pandas – Data manipulation
  
  - 3.NumPy – Numerical computations
  
  - 4.Scikit-learn – Similarity calculations
  
  - 5.Pickle – Model serialization
  
  - 6.Streamlit – Web application interface
  
---
## 📂 Dataset Used

  The project uses the popular Book Recommendation dataset containing:
  
  1.Books data (Title, Author, Image URL, Year, Publisher)
  
  2.Users data
  
  3.Ratings data
  
  - Dataset files:
    - Books.csv
    - Users.csv
    - Ratings.csv
---
## ⚙️ Features
- ✅ 1. Data Preprocessing

  - Removed duplicate books
  
  - Cleaned inconsistent year values
  
  - Filtered active users (based on rating count)
  
  - Created user-item matrix

- ✅ 2. Popularity-Based Recommendation

  - Recommends top-rated and most popular books

- ✅ 3. Collaborative Filtering

  - Uses cosine similarity
  
  - Suggests books similar to the selected book

- ✅ 4. Interactive Web App

  - Built with Streamlit
  
  - Simple and user-friendly interface
  
  - Displays book title, author, and cover image
---
## 🧠 How It Works

  1.Data is cleaned and merged.
  
  2.A pivot table (user-item matrix) is created.
  
  3.Cosine similarity is computed between books.
  
  4.Pickle files are generated to store data.
  
  5.Streamlit loads these files and serves recommendations instantly.
  
--- 

## 📦 Installation & Setup
1️⃣ **Clone the Repository**

    git clone https://github.com/yourusername/book-recommendation-system.git
    cd book-recommendation-system

2️⃣**Create Virtual Environment (Recommended)**

    conda create -n bookrec python=3.10
    conda activate bookrec

3️⃣**Install Dependencies**
 
    pip install -r requirements.txt
  
  
  Or manually:
  
    pip install pandas numpy scikit-learn streamlit

4️⃣ **Run the Application**
  
    streamlit run app.py


If Streamlit is not recognized:

    python -m streamlit run app.py
---

## 📁 Project Structure
  Book-Recommendation-System/
  │
  ├── app.py
  ├── popular.pkl
  ├── pt.pkl
  ├── similarity_scores.pkl
  ├── archive/
  │   ├── Books.csv
  │   ├── Users.csv
  │   └── Ratings.csv
  ├── requirements.txt
  └── README.md
  
---

## 🎯 Future Improvements

  - Add user login system
  
  - Deploy on Streamlit Cloud / Heroku
  
  - Implement hybrid recommendation (content + collaborative)
  
  - Improve UI design
  
  - Add filtering options (genre, year, author)
---

## 🏆 Learning Outcomes

  Through this project, you learn:
  
  - Data preprocessing techniques
  
  - Pivot tables and matrix creation
  
  - Cosine similarity
  
  - Model serialization using pickle
  
  - Building ML web apps with Streamlit

---
## 📌 Conclusion

  This Book Recommendation System demonstrates how collaborative filtering can be used to generate personalized recommendations efficiently. It provides a strong foundation for building advanced recommendation engines used by platforms like Amazon and Goodreads.

**👤 Author**

Syed Nida Ali
Computer Science Graduate
Machine Learning & Data Enthusiast
