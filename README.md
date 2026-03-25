A simple movie recommendation web app built using Streamlit, Pandas, and Scikit-learn. 
This app suggests movies based on weighted ratings, popularity, and personalized content similarity.

The weighted rating system ranks movies by considering both the average rating and the number of votes, making the results more reliable than using ratings alone. 
The popularity-based option shows the most trending movies based on their popularity score.

The personalized recommendation system uses natural language processing techniques. 
It converts movie overviews into numerical data using TF-IDF vectorization and then calculates similarity between movies using cosine similarity. 
Based on this, it recommends movies that are most similar to the one selected by the user.

The dataset used in this project is the TMDB 5000 movies dataset, which includes information such as movie titles, ratings, vote counts, popularity, and plot summaries.

To run this project, you need to install the required libraries including Streamlit, Pandas, and Scikit-learn.
After installing these libraries, you can run the application using the Streamlit command, and it will open in your browser.

