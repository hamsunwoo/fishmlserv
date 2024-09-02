import os

def get_model_path():

    my_path = __file__

    #이 함수 파일의 절대 경로를 받아온다.
    dir_name =  os.path.dirname(my_path)

    #절대 경로를 이용해 model.pkl 의 경로를 조합
    model_path = os.path.join(dir_name, "model.pkl")
    
    #조합된 경로를 리턴 = 끝
    return model_path

    #사용 fastapi main.py 에서 아래와 같이 사용
    #from fishmlserv.model.manager import get_model_path

