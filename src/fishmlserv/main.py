from typing import Union
from fastapi import FastAPI
import pickle
from fishmlserv.model.manager import get_model_path

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "world"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/fish")
def fish(l: float, w: float):
    """물고기 종류 판별기

    Args:
        l (float): 물고기 길이(cm)
        w (float): 물고기 무게(g)

    Returns:
        dict: 물고기 종류를 담은 딕셔너리
    """
    ### 모델 불러오기
    model_path = get_model_path()
    with open(model_path, "rb") as f:
        fish_model = pickle.load(f)

    prediction = fish_model.predict([[l, w]])

    if prediction[0] == 1:
        fish_class = "도미"
    else:
        fish_class = "빙어"
    
    print(f"length: {l}, weight: {w} = {fish_class}입니다!!")
    return {
            "prediction": fish_class,
            "length": l,
            "weight": w
            }
