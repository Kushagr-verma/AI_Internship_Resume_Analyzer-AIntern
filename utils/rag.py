from utils.retriever import retrieve_jobs   #main rag pipeline, import of retreiver ti get jobs

def run_rag(text, df):
    jobs = retrieve_jobs(text, df)

    return jobs   #returns the results 

