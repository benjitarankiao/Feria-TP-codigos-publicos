"""
codigo arreglado
"""


class Vuelos:
    def __init__(self, data):
        self.idvuelos = data["idvuelos"]
        self.pais = data["pais"]
        self.ciudad = data["ciudad"]
        self.precio = data["precio"]
        self.hora = data["hora"]
        self.continente = self.determinar_continente()

    def determinar_continente(self):
        paises_europa = [
            "Luxemburgo",
            "España",
            "Inglaterra",
            "Francia",
            "Alemania",
            "Suecia",
        ]
        paises_asia = ["Rusia", "China", "Japón"]
        if self.pais in paises_europa:
            return "Europa"
        elif self.pais in paises_asia:
            return "Asia"
        else:
            return "Otro"

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM vuelos;"
        results = connectToMySQL("27_agency").query_db(query)
        vuelos = []
        for result in results:
            vuelos.append(cls(result))
        return vuelos


"""
codigo sin arreglar
"""


class vuelos:
    def __init__(self, data):
        self.idvuelos = data["idvuelos"]
        self.pais = data["pais"]
        self.ciudad = data["ciudad"]
        self.precio = data["precio"]
        self.hora = data["hora"]

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM vuelos;"
        results = connectToMySQL("27_agency").query_db(query)
        usuarios = []
        for result in results:
            usuarios.append(cls(result))
        return usuarios

    @classmethod
    def get_all_filter(cls, search_term):
        query = f"SELECT * FROM usuarios WHERE nombre LIKE '%{search_term}%';"
        results = connectToMySQL("27_agency").query_db(query)
        usuarios = []
        for result in results:
            usuarios.append(cls(result))
        return usuarios

    @classmethod
    def get_usuario(cls, id):
        query = "SELECT * FROM usuarios WHERE id = " + id + ";"
        results = connectToMySQL("27_agency").query_db(query)
        usuarios = []
        for result in results:
            usuarios.append(cls(result))
        return usuarios
