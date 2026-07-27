from utils.pdf_reader import read_pdf  #to read the imported pdf
from flask import Flask, render_template, request   #importing the flask
import os
import pandas as pd                                  #for the csv reading of the data
from dotenv import load_dotenv                       #for gemini api key reading

load_dotenv()

app = Flask(__name__)

API_KEY = os.getenv("GEMINI_API_KEY")                #to get the key from the env file

DATA_PATH = "data/job_title_des.csv"

df = pd.read_csv(DATA_PATH)

if "Unnamed: 0" in df.columns:
    df = df.drop(columns=["Unnamed: 0"])            #loading the data in mem

print("Dataset Loaded Successfully")
print(df.head())


@app.route("/")
def home():
    return render_template("index.html")


##############################################################
# I created as i manipulataed the code

@app.route("/upload", methods=["POST"])
def upload():

    file = request.files["resume"]

    if file.filename == "":
        return "No file selected."

    save_path = os.path.join("uploads", file.filename)

    file.save(save_path)

    #reading the uploaded resume
    text = read_pdf(save_path)

    #matching the resume with internship dataset
    jobs = []

    for _, row in df.iterrows():

        title = row["Job Title"]

        desc = str(row["Job Description"])

        score = 0

        for word in text.lower().split():

            if word in desc.lower():

                score += 1

        jobs.append((title, score))

    jobs.sort(key=lambda x: x[1], reverse=True)

    top_jobs = list(dict(sorted(jobs, key=lambda x: x[1], reverse=True)).items())[:5]

    html = """
    <h2>Top Internship Matches</h2>
    <hr>
    """

    for job, score in top_jobs:

        html += f"""
        <h3>{job}</h3>
        <p>Match Score : {score}</p>
        <hr>
        """

    return html


if __name__ == "__main__":
    app.run(debug=True)     #earlier this was just choosinf the files so now I created the upload flask so as to upload and save the resumes as well.