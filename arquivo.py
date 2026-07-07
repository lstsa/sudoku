import os
import json


def salvar(board, date, celulas_imutaveis):
    os.makedirs("saves", exist_ok=True)
    with open(f"saves/save_{date}.json", "w", encoding="utf-8") as arquivo:
        json.dump(
            {
                "board": board,
                "celulas_imutaveis": celulas_imutaveis,
                "date": str(date)
            },
            arquivo,
            indent=4,
            ensure_ascii=False
        )
        
def carregar(date):
    try:
        with open(f"saves/save_{date}.json", "r", encoding="utf-8") as arquivo:
            save = json.load(arquivo)
            celulas_imutaveis = [tuple(celula) for celula in save["celulas_imutaveis"]]
            return save["board"], celulas_imutaveis, save["date"]
    except FileNotFoundError:
        print(f"Não foi encontrado um save para a data {date}.")
        return None, None, None