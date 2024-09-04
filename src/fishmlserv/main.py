from typing import Union
from fastapi import FastAPI, HTTPException
import pickle
from fishmlserv.model.manager import get_model_path

app = FastAPI()

#실행 시 모델을 한 번 로딩
def load_model():
    global fish_model
    model_path = get_model_path()
    with open(model_path, "rb") as f:
        fish_model = pickle.load(f)


@app.get("/fish")
def fish(l: float, w: float):
    """물고기 종류 판별기

    Args:
        l (float): 물고기 길이(cm)
        w (float): 물고기 무게(g)

    Returns:
        dict: 물고기 종류를 담은 딕셔너리
    """

    #모델 예측
    model_path = get_model_path()
    with open(model_path, "rb") as f:
        fish_model = pickle.load(f)
    
    prediction = fish_model.predict([[l, w]])

    if prediction[0] == 1:
        fish_class = "도미"

    elif prediction[0] == 0:
        fish_class = "빙어"

    else:
        raise HTTPException(status_code=500, detail="예측할 수 없는 결과입니다.")
    
    return {
            "prediction": fish_class,
            "length": l,
            "weight": w
            }
