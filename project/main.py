import uvicorn

if __name__ == "__main__":
    print("Main Hello")
    uvicorn.run("app.api:app", host="0.0.0.0", port=80 , reload=True)