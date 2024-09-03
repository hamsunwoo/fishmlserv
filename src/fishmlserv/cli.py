import fire
import typer
from fishmlserv.main import fish
from fishmlserv.model.manager import get_model_path

def fish_prediction():
    fire.Fire(fish)

def print_model_path():
    typer.run(get_model_path)


