from flask import Flask, request, jsonify

app = Flask(__name__)

musicas = [
    {
        "id": 1,
        "titulo": "Astronomia",
        "artista": "Tony Igy",
        "duracao": 236,
        "url": "https://example.com/tony-igy-astronomia"
    }
]

@app.route("/tracks", methods=["GET"])
def buscar_musica():
    return jsonify(musicas)

@app.route("/tracks/<id>", methods=["GET"])
def buscar_musica(id):
    musica = next((m for m in musica if m["id"] == id), None)
    if not musica:
        return jsonify({"erro": "musica não encontrada!"}), 404

    return jsonify(musica)

@app.route("/tracks", methods=["POST"])
def add_musica():
    dados = request.get_json()
    nova_musica = {
        "id": len(musicas) + 1,
        "titulo": dados["titulo"],
        "artista": dados["artista"],
        "duracao": dados["duracao"],
        "url": dados["url"]
    }
    musicas.append(nova_musica)
    return jsonify(nova_musica), 201

@app.route("/tracks/<id>", methods=["PUT"])
def atualizar_musica(id):
    musica = next((m for m in musica if m["id"] == id), None)
    if not musica:
        return jsonify({"erro": "musica não encontrada!"}), 404

    dados = request.get_json()
    musica["titulo"] = dados.get('titulo', musica["titulo"])
    musica["artista"] = dados.get('artista', musica["artista"])
    musica["duracao"] = dados.get('duracao', musica["duracao"])
    musica["url"] = dados.get('url', musica["url"])

    return jsonify(musica)

@app.route("/tracks/<id>", methods=["DELETE"])
def atualizar_musica(id):
    global musicas
    musica = next((m for m in musica if m["id"] == id), None)
    if not musica:
        return jsonify({"erro": "musica não encontrada!"}), 404

    musicas = [m for m in musica if m["id"] != id]

    return jsonify({"mensagem": "musica excluida com sucesso!"})

if __name__ == "__main__":
    app.run(debug=True)