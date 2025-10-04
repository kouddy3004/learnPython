import os
import glob
import pandas as pd
class MovieDb:
    filePath=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),"learnAi","datasets")
    # def __init__(self, title, director, year):
    #     self.title = title
    #     self.director = director
    #     self.year = year

    # def __repr__(self):
    #     return f"<MovieDb(title={self.title}, director={self.director}, year={self.year})>"
    
    def getAllMovies(self,name=""):
        all_files = glob.glob(os.path.join(self.filePath, "tmdb_5000_movies.csv"))
        df_from_each_file = (pd.read_csv(f) for f in all_files)
        concatenated_df   = pd.concat(df_from_each_file, ignore_index=True)
        concatenated_df.fillna("")
        if name!="":
            concatenated_df=concatenated_df[concatenated_df['title'].str.contains(name, case=False)]
        return concatenated_df.head(10)
        


# obj=MovieDb()
# obj.getAllMovies()