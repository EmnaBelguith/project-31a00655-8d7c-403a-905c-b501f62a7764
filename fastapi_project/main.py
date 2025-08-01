# main.py

from fastapi import FastAPI

# Crée une instance de l'application FastAPI
app = FastAPI()

# Définit un point de terminaison (endpoint) pour la racine de l'API
@app.get("/")
async def read_root():
    """
    Point de terminaison racine qui retourne un message de bienvenue.
    """
    return {"message": "Bienvenue sur mon API FastAPI minimale !"}

# Définit un autre point de terminaison avec un paramètre de chemin
@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    """
    Point de terminaison qui retourne des informations sur un article.
    Prend un ID d'article (entier) et un paramètre de requête optionnel 'q'.
    """
    if q:
        return {"item_id": item_id, "q": q, "message": f"Voici l'article {item_id} avec la requête '{q}'"}
    return {"item_id": item_id, "message": f"Voici l'article {item_id}"}

# Un exemple de point de terminaison pour un test de santé simple
@app.get("/health")
async def health_check():
    """
    Point de terminaison pour vérifier la santé de l'application.
    """
    return {"status": "ok"}

if __name__ == "__main__":
    import uvicorn
    # Lance l'application avec Uvicorn.
    # host="0.0.0.0" permet d'écouter sur toutes les interfaces réseau.
    # port=8000 est le port par défaut pour Uvicorn.
    # reload=True est utile pour le développement (redémarre le serveur à chaque modification de fichier).
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
