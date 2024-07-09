from fastapi import FastAPI


# uvicorn main:my_awesome_api 
# my_awesome_api = FastAPI()  # 这个决定了 uvicorn 启动时，会运行哪个

# uvicorn main:app  --reload     #  --reload 自动重启
app = FastAPI()  # 这个决定了 uvicorn 启动时，会运行哪个


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/cly")
async def root2():
    return {"message": "Hello cly"}

