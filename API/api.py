from fastapi import FastAPI, UploadFile
import csv
import io
import uvicorn 


app = FastAPI()

def get_key(key):
    return int(key["distance"])

@app.post("/assignWithCsv")
def upload_csv(file: UploadFile):
    if file.content_type != "text/csv":
        return {"error": "File must be a CSV"}
    
    content = file.file.read().decode("utf-8")

    reader =  csv.DictReader(io.StringIO(content))
    rows = list(reader)
    #מסדר לפי מרחק את כל הCSV
    rows.sort(key=get_key,reverse= True)
    
    

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)


