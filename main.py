import streamlit as st
from streamlit_option_menu import option_menu


# Sidebar menu 
with st.sidebar:
    selected = option_menu(
        menu_title="Main Menu",
        options=["Home", "Profile","Upload Page","Recommendation Page","Voice Assitant" ,"Settings","Logout"],
        icons=["house", "person","upload","lightbulb","microphone","gear"],
        menu_icon="cast",
        default_index=0,
    )

# Page content based on selection
if selected == "Home":
    st.title("Welcome to Home Page")
    st.header('🎞️ Step-by-Step Theory.')
 
    st.write('1. Data Collection :')
    st.write('- Gather a dataset of movies including metadata: title, genre, cast, director, plot description, release year, and user ratings.')
    st.write('- Source examples: MovieLens, IMDb, TMDb API.')
    st.write('- Each movie becomes a data point with features for further analysis.')

    st.write('2. Data Preprocessing:')
    st.write('- Clean the data: remove duplicates, handle missing values, normalize genres and text.')
    st.write('- Convert categorical data (like genres and actors) into numerical format using techniques like one-hot encoding or vectorization.')

    st.write('3. Feature Extraction:')
    st.write('- For text-based features (like plot or tags), use NLP techniques such as:')
    st.write('- TF-IDF (Term Frequency–Inverse Document Frequency): captures the importance of words across descriptions.')
    st.write('- CountVectorizer: creates a word-frequency matrix.')
    st.write('- These transform text into numerical vectors for comparison.')

    st.write('4. Similarity Calculation (Content-Based Filtering):')
    st.write('- Use similarity metrics like:')
    st.write('- Cosine Similarity: compares angle between feature vectors.')
    st.write('- Euclidean Distance: compares vector distance.')
    st.write('- A similarity score is calculated between movies to find the closest matches to a selected film.')

    st.write('5. User-Item Matrix (Collaborative Filtering):')
    st.write('- Construct a matrix where:')
    st.write('- Rows = Users')
    st.write('- Columns = Movies')
    st.write('- Values = Ratings (explicit or implicit)')
    st.write('- Identify user patterns in how they rate or interact with movies.')

    st.write('6. Collaborative Filtering Algorithms:')
    st.write('- Apply models like:')
    st.write('- User-Based Filtering: find users similar to the current user and recommend movies they liked.')
    st.write('- Item-Based Filtering: find movies similar to ones the user liked, based on other users\' opinions.')
    st.write('- Matrix Factorization (e.g., SVD): reduce dimensionality to uncover hidden user/movie features.')

    st.write('7. Hybrid Recommendation System (Optional)')
    st.write('- Combine both content-based and collaborative methods to improve accuracy.')
    st.write('- Helps when data is sparse or user history is limited.')

    st.write('8. Output Generation')
    st.write('- Based on selected preferences or history, the system recommends top N movies with the highest relevance or predicted rating.')
    st.write('- Results may include metadata, posters, links to trailers, and streaming platforms.')

    st.title('🎬 Project Name: CineMatch — Personalized Movie Recommender')

    st.write('⚙️ Purpose: To recommend movies based on a users tastes, viewing history, or preferences, using either:')
    st.write('- Content-Based Filtering (matching movie features)')
    st.write('- Collaborative Filtering (matching users’ preferences)')

    st.write('🧩 Core Modules & Logic:')
    st.write('📁 1. Data Collection:')
    st.write('- Use datasets like IMDb, MovieLens, or TMDb API')
    st.write('- Key attributes: Title, Genre, Cast, Director, Ratings, Reviews, Tags')
    st.write('🧠 2. Content-Based Filtering:')
    st.write('- Use movie metadata (e.g. genre, actors, plot summary)')
    st.write('- Convert text features to numeric (using TF-IDF or CountVectorizer)')
    st.write('- Compute similarity with cosine similarity or Euclidean distance')
    st.write('- Recommend movies with closest feature match')
    st.write('🤝 3. Collaborative Filtering:')
    st.write('- User-item rating matrix')
    st.write('- Apply algorithms like:')
    st.write('- Matrix Factorization (SVD)')
    st.write('- KNN (Nearest neighbor of similar users)')
    st.write('- Predict how a user might rate unseen movies, recommend top-rated ones')
    st.write('🧪 4. Hybrid System (Optional):')
    st.write('- Combine both approaches for smarter recommendations')
    st.write('🎛️ 5. Streamlit Interface:')
    st.write('- User login/profile page')
    st.write('- Genre selection or favorite movies input')
    st.write('- Recommendation list with posters, trailers, links')
    st.write('- Sidebar filters: Language, Rating, Year, Platform')

    st.write('🔍 6. Advanced Features (Optional):')
    st.write('- Sentiment Analysis on reviews')
    st.write('- Voice input for movie search')
    st.write('- Auto-scraping movie metadata from various sources')

    st.write('🧱 Project Structure:')
    st.write('📦 movie_recommender/')
    st.write(' ┣ 📁 data/')
    st.write(' ┃ ┗ 📄 movies.csv')
    st.write(' ┣ 📁 pages/')
    st.write(' ┃ ┗ 📄 recommender.py')
    st.write(' ┣ 📁 utils/')
    st.write(' ┃ ┗ 📄 filtering.py')
    st.write(' ┣ 📄 app.py')
    st.write(' ┗ 📄 config.py')
    st.header('📚 Libraries Used:')
    st.checkbox("pandas")
    st.checkbox("numpy")
    st.checkbox("scikit-learn")
    st.checkbox("nltk")
    st.checkbox("streamlit")
    st.checkbox("beautifulsoup4")
    st.checkbox("requests")
    st.checkbox("matplotlib")
    st.checkbox("seaborn")
    if st.button("Click Me!"):
        st.success("Button clicked!")  


elif selected == "Profile":
    st.title("Your Profile")
    st.image("jpg.hacker.jpg", caption="Profile Picture")
    st.write("Name : Ritik Kumar")
    st.write("Gender : Male")
    st.write('Mobile Number : 1234567890')
    st.write("Email : ritik.kumar@example.com")
    st.write('Course : B.Tech in Computer Science')
    st.write('College : XYZ University')
    st.write("Hobbies : Reading, Coding, Traveling")
    st.write("Skills : Python, Java, C++, Data Analysis, Machine Learning")

elif selected =='Upload Page':
    st.header('Upload Your Movie Data')    
    st.file_uploader("Upload a CSV file with movie data", type=["csv",'xlsx','json','xml'])
    if st.button("Upload"):
        st.success("File uploaded successfully!")
        st.write("Now you can process the data for recommendations.")
elif selected == "Recommendation Page":
    st.title("Movie Recommendation Page")
    st.write("Select your favorite genre or movie to get personalized recommendations.")
    genre = st.selectbox("Choose a genre", ["Action", "Comedy", "Drama", "Horror", "Romance"])
    st.write(f"You selected: {genre}")
    if st.button("Get Recommendations"):
        st.success(f"Here are some {genre} movies you might like!")

elif selected == "Voice Assitant":
    st.title("🎙️ Voice Assistant")
    st.write("This feature is under development. Stay tuned for updates!")
    st.write("You can use voice commands to search for movies or get recommendations.")
    st.button("Activate Voice Assistant")


elif selected == "Introduction of The Page":
    st.title("Introduction of The Page")
    st.write("This page is designed to help you navigate through the movie recommendation system.")
    st.write("You can explore different sections like Home, Profile, Upload Page, Recommendation Page, Voice Assistant, Settings, and Logout.")
    st.write("Each section provides unique functionalities to enhance your movie discovery experience.")
    st.write("Feel free to explore and enjoy personalized movie recommendations!")


elif selected == "Settings":
    st.title("Settings")
    st.button("click here to change theme", on_click=lambda: st.session_state.update({"theme":'black' if st.session_state.get('theme', 'white') == 'white' else 'white'}))
    if 'theme' in st.session_state:
        st.session_state.theme = 'white'
        st.success("Theme changed to " + st.session_state.theme)

    st.write("Yahan app ke options ya preferences set kar sakte ho.")

elif selected == "Logout":
    st.header('')
    st.checkbox('Are you sure you want to log out?')
    st.button("Log out ")
    st.success('successfull Logout')

#st.title("🎙️ Voice Assistant")

# Initialize speech engine



