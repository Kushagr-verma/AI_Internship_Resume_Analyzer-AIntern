def retrieve_jobs(text, df):
    
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
    top_jobs = list(dict(jobs).items())[:5]

    return top_jobs

#this is the retreiver basic stuff 
#extrats the relevabt internships 