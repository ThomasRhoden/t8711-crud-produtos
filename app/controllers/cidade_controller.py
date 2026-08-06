from app.models.cidade import Cidade


class Cidade_Controller:

    def __init__(self, dao, estado_dao, view):
        self.dao = dao
        self.estado_dao = estado_dao
        self.view = view

    def carregar_estados(self):

        estados = self.estado_dao.get_all()

        if hasattr(self.view, "preencher_estados"):
            self.view.preencher_estados(estados)

    def new(self):

        self.view.limpar_campos()

    def save(self):

        try:

            nome, estado_id = self.view.ler_dados_cidade()

            if not nome.strip():
                self.view.exibir_mensagem(
                    "Informe o nome da cidade.",
                    False
                )
                return

            estado = self.estado_dao.get_by_id(
                int(estado_id)
            )

            if estado is None:

                self.view.exibir_mensagem(
                    "Estado não encontrado.",
                    False
                )

                return

            cidade = Cidade(
                None,
                nome,
                estado
            )

            self.dao.save(cidade)

            self.get_all()

            self.view.limpar_campos()

            self.view.exibir_mensagem(
                "Cidade cadastrada com sucesso!"
            )

        except Exception as e:

            self.view.exibir_mensagem(
                str(e),
                False
            )

    def get_all(self):

        cidades = self.dao.get_all()

        self.view.exibir_cidades(cidades)

    def selecionar_cidade(self, event):

        try:

            id_cidade = self.view.get_id_selecionado()

            cidade = self.dao.get_by_id(
                int(id_cidade)
            )

            if cidade:

                self.view.preencher_campos(
                    cidade
                )

        except Exception:
            pass

    def update(self):

        try:

            id_cidade = self.view.txt_id.get()

            if not id_cidade:

                self.view.exibir_mensagem(
                    "Selecione uma cidade.",
                    False
                )

                return

            cidade = self.dao.get_by_id(
                int(id_cidade)
            )

            if cidade is None:

                self.view.exibir_mensagem(
                    "Cidade não encontrada.",
                    False
                )

                return

            nome, estado_id = self.view.ler_dados_cidade()

            estado = self.estado_dao.get_by_id(
                int(estado_id)
            )

            if estado is None:

                self.view.exibir_mensagem(
                    "Estado não encontrado.",
                    False
                )

                return

            cidade.atualizar_dados(
                nome,
                estado
            )

            self.dao.update(cidade)

            self.get_all()

            self.view.exibir_mensagem(
                "Cidade atualizada com sucesso!"
            )

        except Exception as e:

            self.view.exibir_mensagem(
                str(e),
                False
            )

    def delete(self):

        try:

            id_cidade = self.view.txt_id.get()

            if not id_cidade:

                self.view.exibir_mensagem(
                    "Selecione uma cidade.",
                    False
                )

                return

            if not self.view.confirmar_exclusao():
                return

            sucesso = self.dao.delete(
                int(id_cidade)
            )

            if sucesso:

                self.get_all()

                self.view.limpar_campos()

                self.view.exibir_mensagem(
                    "Cidade excluída com sucesso!"
                )

            else:

                self.view.exibir_mensagem(
                    "Cidade não encontrada.",
                    False
                )

        except Exception as e:

            self.view.exibir_mensagem(
                str(e),
                False
            )