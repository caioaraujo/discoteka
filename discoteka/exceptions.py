class RegistroRedundanteException(Exception):
    """
        Excecao para quando registro ja estiver na base de dados.
    """

    def __init__(self, message=None):
        super(RegistroRedundanteException, self).__init__(message)


class ValorObrigatorioException(Exception):
    """
        Excecao para quando algum valor obrigatorio nao for informado.
    """

    def __init__(self, message=None):
        super(ValorObrigatorioException, self).__init__(message)


class RegistroNaoEncontradoException(Exception):
    """
    Excecao para quando nao encontrar registro na base de dados
    """

    def __init__(self, message=None):
        super(RegistroNaoEncontradoException, self).__init__(message)