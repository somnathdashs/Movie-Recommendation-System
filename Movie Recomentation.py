import joblib

similarity=joblib.load("Model.pkl")
movies=joblib.load("Movies.pkl")

def Get_RMovie(text,size):
    try:
        M_Movies=[]
        index=movies[movies['title']==text].index[0]
        distance=similarity[index]
        R_Movies=sorted(list(enumerate(distance)),key=lambda x:x[1],reverse=True)
        for r in R_Movies:
            title=movies['title'][r[0]]
            if len(M_Movies)<size and title!=text:
                M_Movies.append(title)
            elif len(M_Movies)>=size:
                break
        return M_Movies
    except Exception as e:
        print(f"No movie found of {text} name.") 
        print(e)
        return []

while True:
    inp=input("Enter movie name: ")
    size=5
    movis=Get_RMovie(inp,size)
    print("\nPredicted Movies Are followed :")
    for i,m in enumerate(movis):
        print(f'{i+1} ) {m}')

    print('\n')
