# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AgendaAgendamentos(models.Model):
    nome = models.CharField(db_column='Nome', max_length=50)  # Field name made lowercase.
    dataagendamento = models.DateTimeField(db_column='DataAgendamento')  # Field name made lowercase.
    situacao = models.IntegerField(db_column='Situacao', blank=True, null=True)  # Field name made lowercase.
    funcionarioabre = models.IntegerField(db_column='FuncionarioAbre', blank=True, null=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=50, blank=True, null=True)  # Field name made lowercase.
    detalhes = models.TextField(db_column='Detalhes', blank=True, null=True)  # Field name made lowercase.
    tel1 = models.CharField(db_column='Tel1', max_length=14, blank=True, null=True)  # Field name made lowercase.
    tel2 = models.CharField(db_column='Tel2', max_length=14, blank=True, null=True)  # Field name made lowercase.
    end = models.CharField(db_column='End', max_length=100, blank=True, null=True)  # Field name made lowercase.
    numero = models.IntegerField(db_column='Numero', blank=True, null=True)  # Field name made lowercase.
    bairro = models.CharField(db_column='Bairro', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cidade = models.CharField(db_column='Cidade', max_length=100, blank=True, null=True)  # Field name made lowercase.
    uf = models.CharField(db_column='UF', max_length=2, blank=True, null=True)  # Field name made lowercase.
    funcionariofinal = models.IntegerField(db_column='FuncionarioFinal', blank=True, null=True)  # Field name made lowercase.
    datafinal = models.DateTimeField(db_column='DataFinal', blank=True, null=True)  # Field name made lowercase.
    observacao = models.TextField(db_column='Observacao', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'agenda_agendamentos'


class AgendaRessuprimento(models.Model):
    fabricante = models.IntegerField(blank=True, null=True)
    data_agendada = models.DateField(blank=True, null=True)
    data_agendamento = models.DateField(blank=True, null=True)
    periodo_inicial = models.DateField(blank=True, null=True)
    periodo_final = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'agenda_ressuprimento'


class Aliquotas(models.Model):
    codigo = models.AutoField(db_column='Codigo', primary_key=True)  # Field name made lowercase.
    estadoorigem = models.CharField(db_column='EstadoOrigem', max_length=2, blank=True, null=True)  # Field name made lowercase.
    aliquotaf = models.FloatField(db_column='AliquotaF', blank=True, null=True)  # Field name made lowercase.
    aliquotaj = models.FloatField(db_column='AliquotaJ', blank=True, null=True)  # Field name made lowercase.
    estado = models.CharField(db_column='Estado', max_length=2, blank=True, null=True)  # Field name made lowercase.
    empresa = models.IntegerField(db_column='Empresa', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'aliquotas'


class AlteracaoPreco(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    idproduto = models.IntegerField(db_column='IdProduto', blank=True, null=True)  # Field name made lowercase.
    produto = models.CharField(db_column='Produto', max_length=30, blank=True, null=True)  # Field name made lowercase.
    vendaanterior = models.FloatField(db_column='VendaAnterior', blank=True, null=True)  # Field name made lowercase.
    venda = models.FloatField(db_column='Venda', blank=True, null=True)  # Field name made lowercase.
    data = models.DateTimeField(db_column='Data', blank=True, null=True)  # Field name made lowercase.
    usuario = models.IntegerField(db_column='Usuario', blank=True, null=True)  # Field name made lowercase.
    maquina = models.CharField(db_column='Maquina', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'alteracao_preco'


class Antecipacao(models.Model):
    tipo = models.CharField(max_length=9, blank=True, null=True)
    valor = models.FloatField(blank=True, null=True)
    data = models.DateField(blank=True, null=True)
    id_conta = models.IntegerField(blank=True, null=True)
    usuario = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'antecipacao'


class Auditoria(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    operacao = models.CharField(db_column='Operacao', max_length=255, blank=True, null=True)  # Field name made lowercase.
    maquina = models.CharField(db_column='Maquina', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ip = models.CharField(db_column='IP', max_length=255, blank=True, null=True)  # Field name made lowercase.
    data = models.DateField(db_column='Data', blank=True, null=True)  # Field name made lowercase.
    hora = models.CharField(db_column='Hora', max_length=255, blank=True, null=True)  # Field name made lowercase.
    usuario = models.CharField(db_column='Usuario', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tsql = models.TextField(db_column='Tsql', blank=True, null=True)  # Field name made lowercase.
    empresa = models.IntegerField(db_column='Empresa', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'auditoria'


class Auxiliar(models.Model):
    tabela = models.CharField(db_column='Tabela', max_length=30, blank=True, null=True)  # Field name made lowercase.
    codigo = models.CharField(db_column='Codigo', max_length=30, blank=True, null=True)  # Field name made lowercase.
    maquina = models.CharField(db_column='Maquina', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ip = models.CharField(db_column='IP', max_length=30, blank=True, null=True)  # Field name made lowercase.
    usuario = models.IntegerField(db_column='Usuario', blank=True, null=True)  # Field name made lowercase.
    empresa = models.IntegerField(db_column='Empresa', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'auxiliar'


class Bairros(models.Model):
    codigo = models.AutoField(db_column='Codigo', primary_key=True)  # Field name made lowercase.
    regiao = models.IntegerField(db_column='Regiao', blank=True, null=True)  # Field name made lowercase.
    regiaodesc = models.CharField(db_column='Regiaodesc', max_length=60, blank=True, null=True)  # Field name made lowercase.
    bairro = models.CharField(db_column='Bairro', max_length=60, blank=True, null=True)  # Field name made lowercase.
    cadastro = models.DateField(db_column='Cadastro', blank=True, null=True)  # Field name made lowercase.
    empresa = models.IntegerField(db_column='Empresa', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bairros'


class Balanco(models.Model):
    data = models.DateField(blank=True, null=True)
    mes = models.DateField(blank=True, null=True)
    estoque = models.FloatField(blank=True, null=True)
    estoque_custo = models.FloatField(blank=True, null=True)
    estoque_medio = models.FloatField(blank=True, null=True)
    areceber_atrasado = models.FloatField(blank=True, null=True)
    areceber_avencer = models.FloatField(blank=True, null=True)
    recebido = models.FloatField(blank=True, null=True)
    apagar = models.FloatField(blank=True, null=True)
    pago = models.FloatField(blank=True, null=True)
    venda_balcao_quant = models.FloatField(blank=True, null=True)
    venda_balcao_valor = models.FloatField(blank=True, null=True)
    venda_balcao_lucro = models.FloatField(blank=True, null=True)
    venda_balcao_lucro_medio = models.FloatField(blank=True, null=True)
    venda_os_quant = models.FloatField(blank=True, null=True)
    venda_os_valor = models.FloatField(blank=True, null=True)
    venda_os_lucro = models.FloatField(blank=True, null=True)
    venda_os_lucro_medio = models.FloatField(blank=True, null=True)
    compra_quant = models.FloatField(blank=True, null=True)
    compra_valor = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'balanco'


class Balcao(models.Model):
    codigo = models.AutoField(db_column='Codigo', primary_key=True)  # Field name made lowercase.
    cliente = models.IntegerField(db_column='Cliente', blank=True, null=True)  # Field name made lowercase.
    data = models.DateField(db_column='Data', blank=True, null=True)  # Field name made lowercase.
    hora = models.TimeField(db_column='Hora', blank=True, null=True)  # Field name made lowercase.
    situacao = models.IntegerField(db_column='Situacao', blank=True, null=True)  # Field name made lowercase.
    vendedor = models.IntegerField(db_column='Vendedor', blank=True, null=True)  # Field name made lowercase.
    requisicao = models.IntegerField(db_column='Requisicao', blank=True, null=True)  # Field name made lowercase.
    empresa = models.IntegerField(db_column='Empresa', blank=True, null=True)  # Field name made lowercase.
    mecanico = models.IntegerField(db_column='Mecanico', blank=True, null=True)  # Field name made lowercase.
    observacao = models.TextField(db_column='Observacao', blank=True, null=True)  # Field name made lowercase.
    portador = models.CharField(db_column='Portador', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'balcao'


class BancoBoleto(models.Model):
    codigo = models.AutoField(primary_key=True)
    ativo = models.IntegerField(blank=True, null=True)
    id_conta_bancaria = models.IntegerField(blank=True, null=True)
    codigo_cedente = models.CharField(max_length=20, blank=True, null=True)
    digito_codigo_cedente = models.CharField(max_length=1, blank=True, null=True)
    agencia = models.CharField(max_length=10, blank=True, null=True)
    digito_agencia = models.CharField(max_length=2, blank=True, null=True)
    conta = models.CharField(max_length=15, blank=True, null=True)
    digito_conta = models.CharField(max_length=1, blank=True, null=True)
    convenio = models.CharField(max_length=30, blank=True, null=True)
    cedente = models.CharField(max_length=60, blank=True, null=True)
    banco = models.IntegerField(blank=True, null=True)
    carteira = models.CharField(max_length=15, blank=True, null=True)
    tipo_carteira = models.IntegerField(blank=True, null=True)
    modalidade = models.CharField(max_length=5, blank=True, null=True)
    tipo_convenio = models.IntegerField(blank=True, null=True)
    codigo_transmissao = models.CharField(max_length=30, blank=True, null=True)
    descricao_carteira = models.CharField(max_length=40, blank=True, null=True)
    codigo_automatico = models.IntegerField(blank=True, null=True)
    protestar = models.IntegerField(blank=True, null=True)
    dias_protesto = models.IntegerField(blank=True, null=True)
    conceder_desconto = models.IntegerField(blank=True, null=True)
    desconto_total = models.FloatField(blank=True, null=True)
    cobrar_juros = models.IntegerField(blank=True, null=True)
    juros_dia = models.FloatField(blank=True, null=True)
    dias_vencimento = models.IntegerField(blank=True, null=True)
    cobrar_multa = models.IntegerField(blank=True, null=True)
    multa = models.FloatField(blank=True, null=True)
    instrucao = models.TextField(blank=True, null=True)
    local_pagamento = models.CharField(max_length=120, blank=True, null=True)
    endereco_boleto = models.IntegerField(blank=True, null=True)
    arquivo_remessa = models.CharField(max_length=200, blank=True, null=True)
    pessoa = models.IntegerField(blank=True, null=True)
    cpf = models.CharField(max_length=20, blank=True, null=True)
    remessa = models.IntegerField(blank=True, null=True)
    aceite = models.IntegerField(blank=True, null=True)
    cnab = models.IntegerField(blank=True, null=True)
    especie_documento = models.IntegerField(blank=True, null=True)
    quem_emite = models.IntegerField(blank=True, null=True)
    endereco = models.CharField(max_length=50, blank=True, null=True)
    numero_endereco = models.CharField(max_length=10, blank=True, null=True)
    bairro = models.CharField(max_length=30, blank=True, null=True)
    cep = models.CharField(max_length=9, blank=True, null=True)
    cidade = models.CharField(max_length=50, blank=True, null=True)
    uf = models.CharField(max_length=2, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    modelo_boleto = models.IntegerField(blank=True, null=True)
    layout = models.IntegerField(blank=True, null=True)
    cor_logo = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'banco_boleto'


class Bancos(models.Model):
    codigo = models.IntegerField(db_column='Codigo', blank=True, null=True)  # Field name made lowercase.
    banco = models.CharField(db_column='Banco', max_length=60, blank=True, null=True)  # Field name made lowercase.
    cadastro = models.DateField(db_column='Cadastro', blank=True, null=True)  # Field name made lowercase.
    mora = models.FloatField(db_column='Mora', blank=True, null=True)  # Field name made lowercase.
    despesas = models.FloatField(db_column='Despesas', blank=True, null=True)  # Field name made lowercase.
    desconto = models.FloatField(blank=True, null=True)
    instrucao1 = models.CharField(db_column='Instrucao1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    instrucao2 = models.CharField(db_column='Instrucao2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    instrucao3 = models.CharField(db_column='Instrucao3', max_length=100, blank=True, null=True)  # Field name made lowercase.
    printmora = models.IntegerField(db_column='PrintMora', blank=True, null=True)  # Field name made lowercase.
    printdesp = models.IntegerField(db_column='PrintDesp', blank=True, null=True)  # Field name made lowercase.
    printdesc = models.IntegerField(db_column='PrintDesc', blank=True, null=True)  # Field name made lowercase.
    imprimi = models.IntegerField(db_column='Imprimi', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bancos'


class Boleto(models.Model):
    id_titulo = models.IntegerField(blank=True, null=True)
    id_banco_boleto = models.IntegerField(blank=True, null=True)
    numero_banco = models.IntegerField(blank=True, null=True)
    protestar = models.IntegerField(blank=True, null=True)
    dias_protesto = models.IntegerField(blank=True, null=True)
    conceder_desconto = models.IntegerField(blank=True, null=True)
    desconto_total = models.FloatField(blank=True, null=True)
    cobrar_juros = models.IntegerField(blank=True, null=True)
    juros_dia = models.FloatField(blank=True, null=True)
    dias_vencimento = models.IntegerField(blank=True, null=True)
    desconto = models.IntegerField(blank=True, null=True)
    valor_desconto = models.FloatField(blank=True, null=True)
    data_desconto = models.DateField(blank=True, null=True)
    cobrar_multa = models.IntegerField(blank=True, null=True)
    multa = models.FloatField(blank=True, null=True, db_comment='percentual')
    instrucao = models.TextField(blank=True, null=True)
    data_processamento = models.DateField(blank=True, null=True)
    aceite = models.CharField(max_length=1, blank=True, null=True)
    especie_documento = models.IntegerField(blank=True, null=True)
    impresso = models.CharField(max_length=1, blank=True, null=True)
    remessa = models.CharField(max_length=1, blank=True, null=True)
    endereco = models.IntegerField(blank=True, null=True)
    tipo_carteira = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'boleto'


class Brindes(models.Model):
    codigo = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=50, blank=True, null=True)
    estoque = models.FloatField(blank=True, null=True)
    ativo = models.IntegerField(blank=True, null=True)
    pontos = models.FloatField(blank=True, null=True)
    custo = models.FloatField(blank=True, null=True)
    data_entrada = models.DateField(blank=True, null=True)
    data_saida = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'brindes'


class Caixa(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    saldo = models.FloatField(db_column='Saldo', blank=True, null=True)  # Field name made lowercase.
    aberto = models.IntegerField(db_column='Aberto', blank=True, null=True)  # Field name made lowercase.
    pdv = models.CharField(db_column='PDV', max_length=20, blank=True, null=True)  # Field name made lowercase.
    empresa = models.IntegerField(db_column='Empresa', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'caixa'


class CaixaDiario(models.Model):
    caixa = models.IntegerField(blank=True, null=True)
    data_abre = models.DateField(blank=True, null=True)
    hora_abre = models.TimeField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    valor_inicial = models.FloatField(blank=True, null=True)
    valor_final = models.FloatField(blank=True, null=True)
    usuario_abre = models.IntegerField(blank=True, null=True)
    usuario_fecha = models.IntegerField(blank=True, null=True)
    data_fecha = models.DateField(blank=True, null=True)
    hora_fecha = models.TimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'caixa_diario'


class CaixaDiarioLanc(models.Model):
    id_caixa = models.IntegerField(blank=True, null=True)
    caixa = models.IntegerField(blank=True, null=True)
    documento = models.IntegerField(blank=True, null=True)
    parcela = models.IntegerField(blank=True, null=True)
    nome = models.CharField(max_length=60, blank=True, null=True)
    tipo = models.CharField(max_length=7, blank=True, null=True)
    valor = models.FloatField(blank=True, null=True)
    saldo = models.FloatField(blank=True, null=True)
    historico = models.CharField(max_length=80, blank=True, null=True)
    historico_1 = models.CharField(max_length=80, blank=True, null=True)
    pago_com = models.CharField(max_length=10, blank=True, null=True)
    data_lancamento = models.DateField(blank=True, null=True)
    hora = models.TimeField(blank=True, null=True)
    funcionario = models.IntegerField(blank=True, null=True)
    maquina = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'caixa_diario_lanc'


class CaixaDinheiro(models.Model):
    documento = models.IntegerField(blank=True, null=True)
    tipo = models.CharField(max_length=7, blank=True, null=True)
    valor = models.FloatField(blank=True, null=True)
    saldo = models.FloatField(blank=True, null=True)
    historico = models.CharField(max_length=80, blank=True, null=True)
    data_lancamento = models.DateField(blank=True, null=True)
    hora = models.TimeField(blank=True, null=True)
    data_processo = models.DateField(blank=True, null=True)
    funcionario = models.IntegerField(blank=True, null=True)
    forma_saida = models.CharField(max_length=13, blank=True, null=True)
    conferido = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'caixa_dinheiro'


class CaixaTransferencia(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    especie = models.CharField(db_column='Especie', max_length=13, blank=True, null=True)  # Field name made lowercase.
    data = models.DateField(db_column='Data', blank=True, null=True)  # Field name made lowercase.
    hora = models.TimeField(db_column='Hora', blank=True, null=True)  # Field name made lowercase.
    usuario = models.IntegerField(db_column='Usuario', blank=True, null=True)  # Field name made lowercase.
    caixa = models.IntegerField(db_column='Caixa', blank=True, null=True)  # Field name made lowercase.
    caixaid = models.IntegerField(db_column='CaixaID', blank=True, null=True)  # Field name made lowercase.
    entradasaida = models.CharField(db_column='EntradaSaida', max_length=7, blank=True, null=True)  # Field name made lowercase.
    tipo = models.CharField(db_column='Tipo', max_length=9, blank=True, null=True)  # Field name made lowercase.
    valor = models.FloatField(db_column='Valor', blank=True, null=True)  # Field name made lowercase.
    cheque = models.IntegerField(db_column='CHEQUE', blank=True, null=True)  # Field name made lowercase.
    chequevista = models.FloatField(db_column='CHEQUEVISTA', blank=True, null=True)  # Field name made lowercase.
    chequeprazo = models.FloatField(db_column='CHEQUEPRAZO', blank=True, null=True)  # Field name made lowercase.
    observacao = models.CharField(db_column='Observacao', max_length=60, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'caixa_transferencia'


class Cargos(models.Model):
    codigo = models.AutoField(primary_key=True)
    cargo = models.CharField(max_length=30, blank=True, null=True)
    salario = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cargos'


class Cartao(models.Model):
    codigo = models.AutoField(primary_key=True)
    tipo_cartao = models.IntegerField(blank=True, null=True, db_comment='1-debito 2-credito')
    cartao = models.CharField(max_length=30, blank=True, null=True)
    prazo = models.IntegerField(blank=True, null=True)
    taxa = models.FloatField(blank=True, null=True)
    tarifa = models.FloatField(blank=True, null=True)
    maquineta = models.CharField(max_length=15, blank=True, null=True)
    id_admin_cartao = models.IntegerField(blank=True, null=True)
    id_bandeira = models.IntegerField(blank=True, null=True)
    administradora = models.CharField(max_length=19, blank=True, null=True)
    id_conta = models.IntegerField(blank=True, null=True)
    fornecedor = models.IntegerField(blank=True, null=True)
    desconto_recebimento = models.FloatField(blank=True, null=True)
    limite_parcela = models.IntegerField(blank=True, null=True)
    limite_parcela_venda = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cartao'


class CartaoAdministradora(models.Model):
    codigo = models.IntegerField(db_column='CODIGO', primary_key=True)  # Field name made lowercase.
    empresa = models.CharField(db_column='EMPRESA', max_length=60, blank=True, null=True)  # Field name made lowercase.
    cnpj = models.CharField(db_column='CNPJ', max_length=18, blank=True, null=True)  # Field name made lowercase.
    ativo = models.IntegerField(db_column='ATIVO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cartao_administradora'


class CartaoBandeira(models.Model):
    codigo = models.IntegerField(db_column='Codigo', primary_key=True)  # Field name made lowercase.
    bandeira = models.CharField(db_column='Bandeira', max_length=40, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cartao_bandeira'


class CartaoFidelidade(models.Model):
    cliente = models.IntegerField(blank=True, null=True)
    tipo_cliente = models.CharField(max_length=12, blank=True, null=True)
    emissao_cartao = models.DateField(blank=True, null=True)
    cartao = models.CharField(max_length=30, blank=True, null=True)
    pontos = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cartao_fidelidade'


class CartaoFidelidadeExtrato(models.Model):
    cliente = models.IntegerField(blank=True, null=True)
    tipo_cliente = models.CharField(max_length=12, blank=True, null=True)
    data = models.DateField(blank=True, null=True)
    pedido = models.IntegerField(blank=True, null=True)
    tipo_pedido = models.CharField(max_length=3, blank=True, null=True)
    valor_compra = models.FloatField(blank=True, null=True)
    pontos = models.FloatField(blank=True, null=True)
    saldo = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cartao_fidelidade_extrato'


class CartaoFidelidadeParametro(models.Model):
    modo_gerar_pontos = models.IntegerField(blank=True, null=True)
    pontos_por_real = models.FloatField(blank=True, null=True)
    pontos_produto = models.FloatField(blank=True, null=True)
    pontos_servico = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cartao_fidelidade_parametro'


class CartaoFidelidadeResgate(models.Model):
    cliente = models.IntegerField(blank=True, null=True)
    tipo_cliente = models.CharField(max_length=12, blank=True, null=True)
    data = models.DateField(blank=True, null=True)
    hora = models.TimeField(blank=True, null=True)
    brinde = models.IntegerField(blank=True, null=True)
    nome_brinde = models.CharField(max_length=50, blank=True, null=True)
    quantidade = models.FloatField(blank=True, null=True)
    pontos = models.FloatField(blank=True, null=True)
    total_pontos = models.FloatField(blank=True, null=True)
    saldo_pontos = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cartao_fidelidade_resgate'


class CartaoLancamento(models.Model):
    id_cartao = models.IntegerField(blank=True, null=True)
    id_recebimento = models.IntegerField(blank=True, null=True)
    id_caixa = models.IntegerField(blank=True, null=True)
    id_transferencia = models.IntegerField(blank=True, null=True)
    doc = models.IntegerField(blank=True, null=True)
    emissao = models.DateField(blank=True, null=True)
    vencimento = models.DateField(blank=True, null=True)
    parcela_total = models.IntegerField(blank=True, null=True)
    parcela = models.IntegerField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    valor_parcela = models.FloatField(blank=True, null=True)
    diferenca = models.FloatField(blank=True, null=True)
    valor_final = models.FloatField(blank=True, null=True)
    situacao = models.CharField(max_length=1, blank=True, null=True)
    data_baixa = models.DateField(blank=True, null=True)
    forma_baixa = models.CharField(max_length=11, blank=True, null=True)
    lote = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cartao_lancamento'


class CentroCusto(models.Model):
    codigo = models.AutoField(db_column='Codigo', primary_key=True)  # Field name made lowercase.
    centro_custo = models.CharField(db_column='Centro_Custo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    despesa_limite = models.FloatField(db_column='Despesa_Limite', blank=True, null=True)  # Field name made lowercase.
    conta_despesa = models.IntegerField(db_column='Conta_Despesa', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'centro_custo'


class Ceps(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    cep = models.CharField(db_column='Cep', max_length=9, blank=True, null=True)  # Field name made lowercase.
    cidade = models.CharField(db_column='Cidade', max_length=80, blank=True, null=True)  # Field name made lowercase.
    uf = models.CharField(db_column='UF', max_length=2, blank=True, null=True)  # Field name made lowercase.
    empresa = models.IntegerField(db_column='Empresa', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ceps'


class Cfop(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    cfop = models.CharField(db_column='CFOP', max_length=12, blank=True, null=True)  # Field name made lowercase.
    natureza = models.CharField(db_column='Natureza', max_length=60, blank=True, null=True)  # Field name made lowercase.
    artigo = models.CharField(db_column='Artigo', max_length=100, blank=True, null=True)  # Field name made lowercase.
    icm = models.IntegerField(db_column='ICM', blank=True, null=True)  # Field name made lowercase.
    tipo = models.IntegerField(db_column='Tipo', blank=True, null=True)  # Field name made lowercase.
    entradasaida = models.CharField(db_column='EntradaSaida', max_length=1, blank=True, null=True)  # Field name made lowercase.
    empresa = models.IntegerField(db_column='Empresa', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cfop'


class CfopNcms(models.Model):
    ncms = models.CharField(max_length=8, blank=True, null=True)
    cfop = models.CharField(max_length=4, blank=True, null=True)
    anp_simp = models.CharField(max_length=9, blank=True, null=True)
    descricao_anp = models.CharField(max_length=100, blank=True, null=True)
    adremicms = models.FloatField(db_column='adRemICMS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cfop_ncms'


class Checarsenha(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    cliente = models.CharField(db_column='Cliente', max_length=4, blank=True, null=True)  # Field name made lowercase.
    fornecedor = models.CharField(db_column='Fornecedor', max_length=4, blank=True, null=True)  # Field name made lowercase.
    funcionario = models.CharField(db_column='Funcionario', max_length=4, blank=True, null=True)  # Field name made lowercase.
    transportador = models.CharField(db_column='Transportador', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cep = models.CharField(db_column='Cep', max_length=4, blank=True, null=True)  # Field name made lowercase.
    envelope = models.CharField(db_column='Envelope', max_length=4, blank=True, null=True)  # Field name made lowercase.
    produto = models.CharField(db_column='Produto', max_length=4, blank=True, null=True)  # Field name made lowercase.
    fabricante = models.CharField(db_column='Fabricante', max_length=4, blank=True, null=True)  # Field name made lowercase.
    grupo = models.CharField(db_column='Grupo', max_length=4, blank=True, null=True)  # Field name made lowercase.
    linha = models.CharField(db_column='Linha', max_length=4, blank=True, null=True)  # Field name made lowercase.
    kardex = models.CharField(db_column='Kardex', max_length=4, blank=True, null=True)  # Field name made lowercase.
    acerto = models.CharField(db_column='Acerto', max_length=4, blank=True, null=True)  # Field name made lowercase.
    trocacodigo = models.CharField(db_column='TrocaCodigo', max_length=4, blank=True, null=True)  # Field name made lowercase.
    consultapreco = models.CharField(db_column='ConsultaPreco', max_length=4, blank=True, null=True)  # Field name made lowercase.
    alterapreco = models.CharField(db_column='AlteraPreco', max_length=4, blank=True, null=True)  # Field name made lowercase.
    inventario = models.CharField(db_column='Inventario', max_length=4, blank=True, null=True)  # Field name made lowercase.
    observacaofiscal = models.CharField(db_column='ObservacaoFiscal', max_length=4, blank=True, null=True)  # Field name made lowercase.
    relatorioproduto = models.CharField(db_column='RelatorioProduto', max_length=4, blank=True, null=True)  # Field name made lowercase.
    servico = models.CharField(db_column='Servico', max_length=4, blank=True, null=True)  # Field name made lowercase.
    declaracao = models.CharField(db_column='Declaracao', max_length=4, blank=True, null=True)  # Field name made lowercase.
    discriminacao = models.CharField(db_column='Discriminacao', max_length=4, blank=True, null=True)  # Field name made lowercase.
    relatorioservico = models.CharField(db_column='RelatorioServico', max_length=4, blank=True, null=True)  # Field name made lowercase.
    contaspagar = models.CharField(db_column='ContasPagar', max_length=4, blank=True, null=True)  # Field name made lowercase.
    contasreceber = models.CharField(db_column='Contasreceber', max_length=4, blank=True, null=True)  # Field name made lowercase.
    pagamento = models.CharField(db_column='Pagamento', max_length=4, blank=True, null=True)  # Field name made lowercase.
    recebimento = models.CharField(db_column='Recebimento', max_length=4, blank=True, null=True)  # Field name made lowercase.
    condicoes = models.CharField(db_column='Condicoes', max_length=4, blank=True, null=True)  # Field name made lowercase.
    planoconta = models.CharField(db_column='PlanoConta', max_length=4, blank=True, null=True)  # Field name made lowercase.
    relatoriopagar = models.CharField(db_column='RelatorioPagar', max_length=4, blank=True, null=True)  # Field name made lowercase.
    relatorioreceber = models.CharField(db_column='RelatorioReceber', max_length=4, blank=True, null=True)  # Field name made lowercase.
    ordemservico = models.CharField(db_column='OrdemServico', max_length=4, blank=True, null=True)  # Field name made lowercase.
    fechaordem = models.CharField(db_column='FechaOrdem', max_length=4, blank=True, null=True)  # Field name made lowercase.
    consultaordem = models.CharField(db_column='ConsultaOrdem', max_length=4, blank=True, null=True)  # Field name made lowercase.
    reabreordem = models.CharField(db_column='ReabreOrdem', max_length=4, blank=True, null=True)  # Field name made lowercase.
    balcao = models.CharField(db_column='Balcao', max_length=4, blank=True, null=True)  # Field name made lowercase.
    notafiscal = models.CharField(db_column='NotaFiscal', max_length=4, blank=True, null=True)  # Field name made lowercase.
    orcamento = models.CharField(db_column='Orcamento', max_length=4, blank=True, null=True)  # Field name made lowercase.
    icms = models.CharField(db_column='ICMS', max_length=4, blank=True, null=True)  # Field name made lowercase.
    relatoriovenda = models.CharField(db_column='RelatorioVenda', max_length=4, blank=True, null=True)  # Field name made lowercase.
    entrada = models.CharField(db_column='Entrada', max_length=4, blank=True, null=True)  # Field name made lowercase.
    consultaentrada = models.CharField(db_column='ConsultaEntrada', max_length=4, blank=True, null=True)  # Field name made lowercase.
    analise = models.CharField(db_column='Analise', max_length=4, blank=True, null=True)  # Field name made lowercase.
    garantia = models.CharField(db_column='Garantia', max_length=4, blank=True, null=True)  # Field name made lowercase.
    banco = models.CharField(db_column='Banco', max_length=4, blank=True, null=True)  # Field name made lowercase.
    veiculo = models.CharField(db_column='Veiculo', max_length=4, blank=True, null=True)  # Field name made lowercase.
    relatorioveiculo = models.CharField(db_column='RelatorioVeiculo', max_length=4, blank=True, null=True)  # Field name made lowercase.
    manutencao = models.CharField(db_column='Manutencao', max_length=4, blank=True, null=True)  # Field name made lowercase.
    parametro = models.CharField(db_column='Parametro', max_length=4, blank=True, null=True)  # Field name made lowercase.
    confignota = models.CharField(db_column='ConfigNota', max_length=4, blank=True, null=True)  # Field name made lowercase.
    configduplicata = models.CharField(db_column='ConfigDuplicata', max_length=4, blank=True, null=True)  # Field name made lowercase.
    usuario = models.CharField(db_column='Usuario', max_length=4, blank=True, null=True)  # Field name made lowercase.
    permissao = models.CharField(db_column='Permissao', max_length=4, blank=True, null=True)  # Field name made lowercase.
    senhaeddesos = models.CharField(db_column='SenhaEdDesOs', max_length=4, blank=True, null=True)  # Field name made lowercase.
    senhaedvalos = models.CharField(db_column='SenhaEdValOs', max_length=4, blank=True, null=True)  # Field name made lowercase.
    senhaesdesos = models.CharField(db_column='SenhaEsDesOs', max_length=4, blank=True, null=True)  # Field name made lowercase.
    senhaesvalos = models.CharField(db_column='SenhaEsValOs', max_length=4, blank=True, null=True)  # Field name made lowercase.
    editaros = models.CharField(db_column='EditarOs', max_length=4, blank=True, null=True)  # Field name made lowercase.
    excluiprodseos = models.CharField(db_column='ExcluiProdSeOs', max_length=4, blank=True, null=True)  # Field name made lowercase.
    empresa = models.IntegerField(db_column='Empresa', blank=True, null=True)  # Field name made lowercase.
    leituracaixa = models.CharField(db_column='LeituraCaixa', max_length=4, blank=True, null=True)  # Field name made lowercase.
    movicaixa = models.CharField(db_column='MoviCaixa', max_length=4, blank=True, null=True)  # Field name made lowercase.
    baixacontaspagar = models.CharField(db_column='BaixaContasPagar', max_length=4, blank=True, null=True)  # Field name made lowercase.
    posicaopagar = models.CharField(db_column='PosicaoPagar', max_length=4, blank=True, null=True)  # Field name made lowercase.
    editapagar = models.CharField(db_column='EditaPagar', max_length=4, blank=True, null=True)  # Field name made lowercase.
    baixacontasreceber = models.CharField(db_column='BaixaContasReceber', max_length=4, blank=True, null=True)  # Field name made lowercase.
    reciboreceber = models.CharField(db_column='ReciboReceber', max_length=4, blank=True, null=True)  # Field name made lowercase.
    boletoreceber = models.CharField(db_column='BoletoReceber', max_length=4, blank=True, null=True)  # Field name made lowercase.
    posicaoreceber = models.CharField(db_column='PosicaoReceber', max_length=4, blank=True, null=True)  # Field name made lowercase.
    osrecreceber = models.CharField(db_column='OsRecReceber', max_length=4, blank=True, null=True)  # Field name made lowercase.
    editareceber = models.CharField(db_column='EditaReceber', max_length=4, blank=True, null=True)  # Field name made lowercase.
    notareceber = models.CharField(db_column='NotaReceber', max_length=4, blank=True, null=True)  # Field name made lowercase.
    pneu = models.CharField(db_column='Pneu', max_length=4, blank=True, null=True)  # Field name made lowercase.
    roda = models.CharField(db_column='Roda', max_length=4, blank=True, null=True)  # Field name made lowercase.
    auditoria = models.CharField(db_column='Auditoria', max_length=4, blank=True, null=True)  # Field name made lowercase.
    empresas = models.CharField(db_column='Empresas', max_length=4, blank=True, null=True)  # Field name made lowercase.
    mecanicos = models.CharField(db_column='Mecanicos', max_length=4, blank=True, null=True)  # Field name made lowercase.
    abrecaixadiario = models.CharField(max_length=4, blank=True, null=True)
    fechacaixadiario = models.CharField(max_length=4, blank=True, null=True)
    lancacaixadiario = models.CharField(max_length=4, blank=True, null=True)
    consultacaixadiario = models.CharField(max_length=4, blank=True, null=True)
    cargacaixadiario = models.CharField(max_length=4, blank=True, null=True)
    pagamentocaixadiario = models.CharField(max_length=4, blank=True, null=True)
    transferenciacaixadiario = models.CharField(max_length=4, blank=True, null=True)
    devolucaobalcao = models.CharField(max_length=4, blank=True, null=True)
    cancelavendabalcao = models.CharField(max_length=4, blank=True, null=True)
    pdvcancvendaaberta = models.CharField(db_column='PDVCancVendaAberta', max_length=4, blank=True, null=True)  # Field name made lowercase.
    pdvcancitemvenda = models.CharField(db_column='PDVCancItemVenda', max_length=4, blank=True, null=True)  # Field name made lowercase.
    pdvbaixarecebimento = models.CharField(db_column='PDVBaixaRecebimento', max_length=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'checarsenha'


class Chequeemitido(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    banco = models.IntegerField(db_column='Banco', blank=True, null=True)  # Field name made lowercase.
    agencia = models.CharField(db_column='Agencia', max_length=10, blank=True, null=True)  # Field name made lowercase.
    chequen = models.CharField(db_column='ChequeN', max_length=20, blank=True, null=True)  # Field name made lowercase.
    contan = models.CharField(db_column='ContaN', max_length=20, blank=True, null=True)  # Field name made lowercase.
    valor = models.FloatField(db_column='Valor', blank=True, null=True)  # Field name made lowercase.
    ordem = models.CharField(db_column='Ordem', max_length=60, blank=True, null=True)  # Field name made lowercase.
    cidade = models.CharField(db_column='Cidade', max_length=60, blank=True, null=True)  # Field name made lowercase.
    data = models.DateField(db_column='Data', blank=True, null=True)  # Field name made lowercase.
    dia = models.IntegerField(db_column='Dia', blank=True, null=True)  # Field name made lowercase.
    mes = models.IntegerField(db_column='Mes', blank=True, null=True)  # Field name made lowercase.
    ano = models.IntegerField(db_column='Ano', blank=True, null=True)  # Field name made lowercase.
    bompara = models.DateField(db_column='BomPara', blank=True, null=True)  # Field name made lowercase.
    situacao = models.IntegerField(db_column='Situacao', blank=True, null=True)  # Field name made lowercase.
    empresa = models.IntegerField(db_column='Empresa', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'chequeemitido'


class Chequerecebido(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    data = models.DateField(db_column='Data', blank=True, null=True)  # Field name made lowercase.
    banco = models.IntegerField(db_column='Banco', blank=True, null=True)  # Field name made lowercase.
    numero = models.CharField(db_column='Numero', max_length=8, blank=True, null=True)  # Field name made lowercase.
    fone = models.CharField(db_column='Fone', max_length=13, blank=True, null=True)  # Field name made lowercase.
    cpf = models.CharField(db_column='CPF', max_length=18, blank=True, null=True)  # Field name made lowercase.
    rg = models.CharField(db_column='RG', max_length=18, blank=True, null=True)  # Field name made lowercase.
    vencimento = models.DateField(db_column='Vencimento', blank=True, null=True)  # Field name made lowercase.
    valor = models.FloatField(db_column='Valor', blank=True, null=True)  # Field name made lowercase.
    situacao = models.IntegerField(db_column='Situacao', blank=True, null=True)  # Field name made lowercase.
    empresa = models.IntegerField(db_column='Empresa', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'chequerecebido'


class ChequesEmitidos(models.Model):
    id_conta = models.IntegerField(blank=True, null=True)
    nome = models.CharField(max_length=50, blank=True, null=True)
    banco = models.IntegerField(blank=True, null=True)
    agencia = models.CharField(max_length=8, blank=True, null=True)
    cheque_numero = models.IntegerField(blank=True, null=True)
    valor = models.FloatField(blank=True, null=True)
    data_emissao = models.DateField(blank=True, null=True)
    data_pre = models.DateField(blank=True, null=True)
    situacao = models.CharField(max_length=1, blank=True, null=True)
    compensado = models.CharField(max_length=1, blank=True, null=True)
    data_compensacao = models.DateField(blank=True, null=True)
    funcionario = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cheques_emitidos'


class ChequesRecebidos(models.Model):
    id_recebimento = models.IntegerField(blank=True, null=True)
    id_detalhe_recebimento = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    situacao = models.CharField(max_length=1, blank=True, null=True)
    codcli = models.IntegerField(blank=True, null=True)
    cliente = models.CharField(max_length=80, blank=True, null=True)
    banco = models.IntegerField(blank=True, null=True)
    agencia = models.IntegerField(blank=True, null=True)
    cheque_numero = models.IntegerField(blank=True, null=True)
    valor = models.FloatField(blank=True, null=True)
    data_inclusao = models.DateField(blank=True, null=True)
    data_pre = models.DateField(blank=True, null=True)
    cheque_nome = models.CharField(max_length=80, blank=True, null=True)
    funcionario = models.IntegerField(blank=True, null=True)
    id_caixa = models.IntegerField(blank=True, null=True)
    id_transferencia = models.IntegerField(blank=True, null=True)
    lote = models.IntegerField(blank=True, null=True)
    data_baixa = models.DateField(blank=True, null=True)
    usuario_baixa = models.IntegerField(blank=True, null=True)
    forma_baixa = models.CharField(max_length=11, blank=True, null=True)
    devolvido = models.IntegerField(blank=True, null=True)
    data_inclusao_devolucao = models.DateField(blank=True, null=True)
    motivo_devolucao = models.CharField(max_length=40, blank=True, null=True)
    situacao_devolucao = models.CharField(max_length=1, blank=True, null=True)
    id_cc_devolucao = models.IntegerField(blank=True, null=True)
    data_baixa_devolucao = models.DateField(blank=True, null=True)
    debito_parcial = models.FloatField(blank=True, null=True)
    id_recebimento_devolucao = models.IntegerField(blank=True, null=True)
    situacao_devolucao_forn = models.CharField(max_length=1, blank=True, null=True)
    data_baixa_devolucao_forn = models.DateField(blank=True, null=True)
    id_pagamento = models.IntegerField(blank=True, null=True)
    observacao = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cheques_recebidos'


class Classificacao(models.Model):
    codigo = models.AutoField(primary_key=True)
    classificacao = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'classificacao'


class Classtr(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    classtr = models.CharField(db_column='ClassTr', max_length=3, blank=True, null=True)  # Field name made lowercase.
    obsnf = models.CharField(db_column='ObsNf', max_length=100, blank=True, null=True)  # Field name made lowercase.
    empresa = models.IntegerField(db_column='Empresa', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'classtr'


class Clientes(models.Model):
    codigo = models.AutoField(db_column='Codigo', primary_key=True)  # Field name made lowercase.
    codant = models.IntegerField(blank=True, null=True)
    tipo = models.IntegerField(db_column='Tipo', blank=True, null=True)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=60, blank=True, null=True)  # Field name made lowercase.
    apelido = models.CharField(db_column='Apelido', max_length=60, blank=True, null=True)  # Field name made lowercase.
    orgao = models.CharField(db_column='Orgao', max_length=5, blank=True, null=True)  # Field name made lowercase.
    caixapostal = models.CharField(db_column='CaixaPostal', max_length=5, blank=True, null=True)  # Field name made lowercase.
    nascimento = models.DateField(db_column='Nascimento', blank=True, null=True)  # Field name made lowercase.
    endereco = models.CharField(db_column='Endereco', max_length=60, blank=True, null=True)  # Field name made lowercase.
    end = models.CharField(db_column='End', max_length=60, blank=True, null=True)  # Field name made lowercase.
    numero = models.CharField(max_length=15, blank=True, null=True)
    complemento = models.CharField(db_column='Complemento', max_length=60, blank=True, null=True)  # Field name made lowercase.
    bairro = models.CharField(db_column='Bairro', max_length=60, blank=True, null=True)  # Field name made lowercase.
    cep = models.CharField(db_column='Cep', max_length=9, blank=True, null=True)  # Field name made lowercase.
    cidade = models.CharField(db_column='Cidade', max_length=50, blank=True, null=True)  # Field name made lowercase.
    uf = models.CharField(db_column='UF', max_length=2, blank=True, null=True)  # Field name made lowercase.
    codigocidade = models.CharField(db_column='CodigoCidade', max_length=7, blank=True, null=True)  # Field name made lowercase.
    codigoestado = models.CharField(db_column='CodigoEstado', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cpf = models.CharField(db_column='CPF', max_length=20, blank=True, null=True)  # Field name made lowercase.
    rg = models.CharField(db_column='RG', max_length=20, blank=True, null=True)  # Field name made lowercase.
    estadocivil = models.IntegerField(db_column='EstadoCivil', blank=True, null=True)  # Field name made lowercase.
    fone1 = models.CharField(db_column='Fone1', max_length=14, blank=True, null=True)  # Field name made lowercase.
    ramal1 = models.CharField(db_column='Ramal1', max_length=5, blank=True, null=True)  # Field name made lowercase.
    contato1 = models.CharField(db_column='Contato1', max_length=60, blank=True, null=True)  # Field name made lowercase.
    fone2 = models.CharField(db_column='Fone2', max_length=14, blank=True, null=True)  # Field name made lowercase.
    ramal2 = models.CharField(db_column='Ramal2', max_length=5, blank=True, null=True)  # Field name made lowercase.
    contato2 = models.CharField(db_column='Contato2', max_length=60, blank=True, null=True)  # Field name made lowercase.
    fone3 = models.CharField(db_column='Fone3', max_length=14, blank=True, null=True)  # Field name made lowercase.
    ramal3 = models.CharField(db_column='Ramal3', max_length=5, blank=True, null=True)  # Field name made lowercase.
    contato3 = models.CharField(db_column='Contato3', max_length=60, blank=True, null=True)  # Field name made lowercase.
    whatsapp = models.CharField(db_column='WhatsApp', max_length=14, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=100, blank=True, null=True)  # Field name made lowercase.
    email2 = models.CharField(db_column='Email2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    home = models.CharField(db_column='Home', max_length=100, blank=True, null=True)  # Field name made lowercase.
    trabalho1 = models.CharField(db_column='Trabalho1', max_length=60, blank=True, null=True)  # Field name made lowercase.
    funcao1 = models.CharField(db_column='Funcao1', max_length=60, blank=True, null=True)  # Field name made lowercase.
    admissao1 = models.DateField(db_column='Admissao1', blank=True, null=True)  # Field name made lowercase.
    trabfone1 = models.CharField(db_column='TrabFone1', max_length=14, blank=True, null=True)  # Field name made lowercase.
    trabfax1 = models.CharField(db_column='TrabFax1', max_length=14, blank=True, null=True)  # Field name made lowercase.
    trabramal1 = models.CharField(db_column='TrabRamal1', max_length=5, blank=True, null=True)  # Field name made lowercase.
    trabsalario1 = models.FloatField(db_column='TrabSalario1', blank=True, null=True)  # Field name made lowercase.
    trabalho2 = models.CharField(db_column='Trabalho2', max_length=60, blank=True, null=True)  # Field name made lowercase.
    funcao2 = models.CharField(db_column='Funcao2', max_length=60, blank=True, null=True)  # Field name made lowercase.
    admissao2 = models.DateField(db_column='Admissao2', blank=True, null=True)  # Field name made lowercase.
    trabfone2 = models.CharField(db_column='TrabFone2', max_length=14, blank=True, null=True)  # Field name made lowercase.
    trabfax2 = models.CharField(db_column='TrabFax2', max_length=14, blank=True, null=True)  # Field name made lowercase.
    trabramal2 = models.CharField(db_column='TrabRamal2', max_length=5, blank=True, null=True)  # Field name made lowercase.
    trabsalario2 = models.FloatField(db_column='TrabSalario2', blank=True, null=True)  # Field name made lowercase.
    enderecocob = models.CharField(db_column='EnderecoCob', max_length=60, blank=True, null=True)  # Field name made lowercase.
    endcob = models.CharField(db_column='EndCob', max_length=60, blank=True, null=True)  # Field name made lowercase.
    numerocob = models.CharField(db_column='NumeroCob', max_length=15, blank=True, null=True)  # Field name made lowercase.
    complementocob = models.CharField(db_column='ComplementoCob', max_length=60, blank=True, null=True)  # Field name made lowercase.
    bairrocob = models.CharField(db_column='BairroCob', max_length=60, blank=True, null=True)  # Field name made lowercase.
    cepcob = models.CharField(db_column='CepCob', max_length=9, blank=True, null=True)  # Field name made lowercase.
    cidadecob = models.CharField(db_column='CidadeCob', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ufcob = models.CharField(db_column='UFCob', max_length=2, blank=True, null=True)  # Field name made lowercase.
    pai = models.CharField(db_column='Pai', max_length=60, blank=True, null=True)  # Field name made lowercase.
    mae = models.CharField(db_column='Mae', max_length=60, blank=True, null=True)  # Field name made lowercase.
    nomecon = models.CharField(db_column='NomeCon', max_length=60, blank=True, null=True)  # Field name made lowercase.
    trabcon = models.CharField(db_column='TrabCon', max_length=60, blank=True, null=True)  # Field name made lowercase.
    funcaocon = models.CharField(db_column='FuncaoCon', max_length=60, blank=True, null=True)  # Field name made lowercase.
    admissaocon = models.DateField(db_column='AdmissaoCon', blank=True, null=True)  # Field name made lowercase.
    fonecon = models.CharField(db_column='FoneCon', max_length=14, blank=True, null=True)  # Field name made lowercase.
    faxcon = models.CharField(db_column='FaxCon', max_length=14, blank=True, null=True)  # Field name made lowercase.
    ramalcon = models.CharField(db_column='RamalCon', max_length=5, blank=True, null=True)  # Field name made lowercase.
    salariocon = models.FloatField(db_column='SalarioCon', blank=True, null=True)  # Field name made lowercase.
    desconto = models.FloatField(db_column='Desconto', blank=True, null=True)  # Field name made lowercase.
    prazo = models.IntegerField(db_column='Prazo', blank=True, null=True)  # Field name made lowercase.
    carteira = models.IntegerField(db_column='Carteira', blank=True, null=True)  # Field name made lowercase.
    cheque = models.IntegerField(db_column='Cheque', blank=True, null=True)  # Field name made lowercase.
    duplicata = models.IntegerField(db_column='Duplicata', blank=True, null=True)  # Field name made lowercase.
    limite = models.FloatField(db_column='Limite', blank=True, null=True)  # Field name made lowercase.
    limitar = models.CharField(db_column='Limitar', max_length=3, blank=True, null=True)  # Field name made lowercase.
    observacao = models.TextField(db_column='Observacao', blank=True, null=True)  # Field name made lowercase.
    cadastro = models.DateField(db_column='Cadastro', blank=True, null=True)  # Field name made lowercase.
    empresa = models.IntegerField(db_column='Empresa', blank=True, null=True)  # Field name made lowercase.
    situacao = models.IntegerField(db_column='Situacao', blank=True, null=True)  # Field name made lowercase.
    data_exclusao = models.DateField(db_column='Data_exclusao', blank=True, null=True)  # Field name made lowercase.
    usuario_exclusao = models.IntegerField(db_column='Usuario_exclusao', blank=True, null=True)  # Field name made lowercase.
    porcento = models.FloatField(db_column='Porcento', blank=True, null=True)  # Field name made lowercase.
    renda = models.FloatField(db_column='Renda', blank=True, null=True)  # Field name made lowercase.
    ativo = models.IntegerField(db_column='Ativo', blank=True, null=True)  # Field name made lowercase.
    cls1 = models.IntegerField(blank=True, null=True)
    cls2 = models.IntegerField(blank=True, null=True)
    cls3 = models.IntegerField(blank=True, null=True)
    cls4 = models.IntegerField(blank=True, null=True)
    cls5 = models.IntegerField(blank=True, null=True)
    tabela = models.IntegerField(blank=True, null=True)
    credito = models.FloatField(blank=True, null=True)
    ref1 = models.CharField(max_length=40, blank=True, null=True)
    telref1 = models.CharField(max_length=14, blank=True, null=True)
    ref2 = models.CharField(max_length=40, blank=True, null=True)
    telref2 = models.CharField(max_length=14, blank=True, null=True)
    ref3 = models.CharField(max_length=40, blank=True, null=True)
    telref3 = models.CharField(max_length=14, blank=True, null=True)
    obsref = models.TextField(blank=True, null=True)
    creditorestrito = models.CharField(max_length=3, blank=True, null=True)
    tipofat = models.CharField(max_length=19, blank=True, null=True)
    fat05 = models.CharField(max_length=3, blank=True, null=True)
    fat10 = models.CharField(max_length=3, blank=True, null=True)
    fat15 = models.CharField(max_length=3, blank=True, null=True)
    fat20 = models.CharField(max_length=3, blank=True, null=True)
    fat25 = models.CharField(max_length=3, blank=True, null=True)
    fat30 = models.CharField(max_length=3, blank=True, null=True)
    cond_esp = models.CharField(max_length=3, blank=True, null=True)
    cond_esp_msg = models.TextField(blank=True, null=True)
    restrito_automatico = models.IntegerField(blank=True, null=True)
    cond_recebimento = models.IntegerField(blank=True, null=True)
    ultima_compra = models.DateField(blank=True, null=True)
    usuario_alteracao_restricao = models.IntegerField(blank=True, null=True)
    aproveita_credito_icms = models.IntegerField(blank=True, null=True)
    monitorar = models.IntegerField(blank=True, null=True)
    tabela_venda = models.IntegerField(blank=True, null=True)
    tabela_desconto = models.CharField(max_length=1, blank=True, null=True)
    especie_cliente = models.IntegerField(blank=True, null=True)
    representante = models.IntegerField(blank=True, null=True)
    cartaocredito = models.CharField(db_column='CartaoCredito', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'clientes'


class ClientesAlteracaoCredito(models.Model):
    cliente = models.IntegerField(db_column='Cliente', blank=True, null=True)  # Field name made lowercase.
    usuario = models.IntegerField(db_column='Usuario', blank=True, null=True)  # Field name made lowercase.
    data = models.DateField(db_column='Data', blank=True, null=True)  # Field name made lowercase.
    hora = models.TimeField(db_column='Hora', blank=True, null=True)  # Field name made lowercase.
    maquina = models.CharField(db_column='Maquina', max_length=60, blank=True, null=True)  # Field name made lowercase.
    ip = models.CharField(db_column='IP', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'clientes_alteracao_credito'


class ClientesEspecie(models.Model):
    codigo = models.AutoField(db_column='Codigo', primary_key=True)  # Field name made lowercase.
    especie = models.CharField(db_column='Especie', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'clientes_especie'


class Cobranca(models.Model):
    id_receb = models.IntegerField(blank=True, null=True)
    data = models.DateField(blank=True, null=True)
    codigo = models.IntegerField(blank=True, null=True)
    sequencia = models.IntegerField(blank=True, null=True)
    portador = models.IntegerField(blank=True, null=True)
    tipo = models.CharField(max_length=1, blank=True, null=True)
    cliente = models.IntegerField(blank=True, null=True)
    nomecliente = models.CharField(max_length=60, blank=True, null=True)
    valor = models.FloatField(blank=True, null=True)
    vencimento = models.DateField(blank=True, null=True)
    funcionario = models.IntegerField(blank=True, null=True)
    pago = models.CharField(max_length=3, blank=True, null=True)
    datapagto = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cobranca'


class CobrancaCliente(models.Model):
    id_receb = models.IntegerField(blank=True, null=True)
    cliente = models.IntegerField(blank=True, null=True)
    data = models.DateField(blank=True, null=True)
    codigo = models.IntegerField(blank=True, null=True)
    sequencia = models.IntegerField(blank=True, null=True)
    portador = models.IntegerField(blank=True, null=True)
    tipo = models.CharField(max_length=1, blank=True, null=True)
    valor = models.FloatField(blank=True, null=True)
    vencimento = models.DateField(blank=True, null=True)
    juros = models.FloatField(blank=True, null=True)
    valorfinal = models.FloatField(blank=True, null=True)
    funcionario = models.IntegerField(blank=True, null=True)
    atraso = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cobranca_cliente'


class Codigofornecedor(models.Model):
    id_prod = models.IntegerField(blank=True, null=True)
    codigo_produto = models.CharField(max_length=50, blank=True, null=True)
    reduzido_produto = models.CharField(max_length=50, blank=True, null=True)
    fornecedor = models.IntegerField(blank=True, null=True)
    codigofornecedor = models.CharField(max_length=30, blank=True, null=True)
    reduzido = models.CharField(max_length=30, blank=True, null=True)
    confirmado = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'codigofornecedor'


class Comanda(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    livre = models.IntegerField(db_column='Livre', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'comanda'


class Comandaitens(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    seleciona = models.CharField(db_column='Seleciona', max_length=1, blank=True, null=True)  # Field name made lowercase.
    controle = models.PositiveIntegerField(db_column='Controle', blank=True, null=True)  # Field name made lowercase.
    comanda = models.PositiveIntegerField(db_column='Comanda', blank=True, null=True)  # Field name made lowercase.
    mesa = models.IntegerField(db_column='Mesa', blank=True, null=True)  # Field name made lowercase.
    data = models.DateField(db_column='Data', blank=True, null=True)  # Field name made lowercase.
    hora = models.TimeField(db_column='Hora', blank=True, null=True)  # Field name made lowercase.
    funcionario = models.IntegerField(db_column='Funcionario', blank=True, null=True)  # Field name made lowercase.
    usuario = models.IntegerField(db_column='Usuario', blank=True, null=True)  # Field name made lowercase.
    codigo = models.CharField(db_column='Codigo', max_length=30, blank=True, null=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=60, blank=True, null=True)  # Field name made lowercase.
    quantidade = models.FloatField(db_column='Quantidade', blank=True, null=True)  # Field name made lowercase.
    unitario = models.FloatField(db_column='Unitario', blank=True, null=True)  # Field name made lowercase.
    total = models.FloatField(db_column='Total', blank=True, null=True)  # Field name made lowercase.
    finalizado = models.IntegerField(db_column='Finalizado', blank=True, null=True)  # Field name made lowercase.
    venda = models.PositiveIntegerField(db_column='Venda', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'comandaitens'


class Comandavenda(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    comanda = models.IntegerField(db_column='Comanda', blank=True, null=True)  # Field name made lowercase.
    mesa = models.IntegerField(db_column='Mesa', blank=True, null=True)  # Field name made lowercase.
    finalizada = models.IntegerField(db_column='Finalizada', blank=True, null=True)  # Field name made lowercase.
    data = models.DateField(db_column='Data', blank=True, null=True)  # Field name made lowercase.
    hora = models.TimeField(db_column='Hora', blank=True, null=True)  # Field name made lowercase.
    datafim = models.DateField(db_column='DataFim', blank=True, null=True)  # Field name made lowercase.
    horafim = models.TimeField(db_column='HoraFim', blank=True, null=True)  # Field name made lowercase.
    funcionario = models.IntegerField(db_column='Funcionario', blank=True, null=True)  # Field name made lowercase.
    usuario = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='Usuario', blank=True, null=True)  # Field name made lowercase.
    numeroaleatorio = models.IntegerField(db_column='NumeroAleatorio', blank=True, null=True)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=60, blank=True, null=True)  # Field name made lowercase.
    fone = models.CharField(db_column='Fone', max_length=14, blank=True, null=True)  # Field name made lowercase.
    endereco = models.CharField(db_column='Endereco', max_length=100, blank=True, null=True)  # Field name made lowercase.
    bairro = models.CharField(db_column='Bairro', max_length=60, blank=True, null=True)  # Field name made lowercase.
    observacao = models.CharField(db_column='Observacao', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'comandavenda'


class Compratemp(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    campo1 = models.CharField(db_column='CAMPO1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    campo2 = models.FloatField(db_column='CAMPO2', blank=True, null=True)  # Field name made lowercase.
    campo3 = models.FloatField(db_column='CAMPO3', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'compratemp'


class Condicional(models.Model):
    codigo = models.AutoField(primary_key=True)
    cliente = models.IntegerField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    vendedor = models.IntegerField(blank=True, null=True)
    data = models.DateField(blank=True, null=True)
    hora = models.TimeField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    portador = models.CharField(max_length=40, blank=True, null=True)
    observacao = models.CharField(max_length=70, blank=True, null=True)
    datadevolucao = models.DateField(blank=True, null=True)
    horadevolucao = models.TimeField(blank=True, null=True)
    usuariodevolucao = models.IntegerField(blank=True, null=True)
    maquinadevolucao = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'condicional'


class Condicoesp(models.Model):
    codigo = models.AutoField(db_column='Codigo', primary_key=True)  # Field name made lowercase.
    titulo = models.CharField(db_column='Titulo', max_length=60, blank=True, null=True)  # Field name made lowercase.
    prestacoes = models.IntegerField(db_column='Prestacoes', blank=True, null=True)  # Field name made lowercase.
    valido = models.FloatField(db_column='Valido', blank=True, null=True)  # Field name made lowercase.
    prazo1 = models.IntegerField(db_column='Prazo1', blank=True, null=True)  # Field name made lowercase.
    prazo2 = models.IntegerField(db_column='Prazo2', blank=True, null=True)  # Field name made lowercase.
    prazo3 = models.IntegerField(db_column='Prazo3', blank=True, null=True)  # Field name made lowercase.
    prazo4 = models.IntegerField(db_column='Prazo4', blank=True, null=True)  # Field name made lowercase.
    prazo5 = models.IntegerField(db_column='Prazo5', blank=True, null=True)  # Field name made lowercase.
    prazo6 = models.IntegerField(db_column='Prazo6', blank=True, null=True)  # Field name made lowercase.
    prazo7 = models.IntegerField(db_column='Prazo7', blank=True, null=True)  # Field name made lowercase.
    prazo8 = models.IntegerField(db_column='Prazo8', blank=True, null=True)  # Field name made lowercase.
    prazo9 = models.IntegerField(db_column='Prazo9', blank=True, null=True)  # Field name made lowercase.
    prazo10 = models.IntegerField(db_column='Prazo10', blank=True, null=True)  # Field name made lowercase.
    prazo11 = models.IntegerField(db_column='Prazo11', blank=True, null=True)  # Field name made lowercase.
    prazo12 = models.IntegerField(db_column='Prazo12', blank=True, null=True)  # Field name made lowercase.
    chequeprazo = models.FloatField(db_column='ChequePrazo', blank=True, null=True)  # Field name made lowercase.
    chequevista = models.FloatField(db_column='ChequeVista', blank=True, null=True)  # Field name made lowercase.
    cartao = models.FloatField(db_column='Cartao', blank=True, null=True)  # Field name made lowercase.
    duplicata = models.FloatField(db_column='Duplicata', blank=True, null=True)  # Field name made lowercase.
    cadastro = models.DateField(db_column='Cadastro', blank=True, null=True)  # Field name made lowercase.
    empresa = models.IntegerField(db_column='Empresa', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'condicoesp'


class Condicoespp(models.Model):
    codigo = models.AutoField(db_column='Codigo', primary_key=True)  # Field name made lowercase.
    titulo = models.CharField(db_column='Titulo', max_length=60, blank=True, null=True)  # Field name made lowercase.
    prestacoes = models.IntegerField(db_column='Prestacoes', blank=True, null=True)  # Field name made lowercase.
    valido = models.FloatField(db_column='Valido', blank=True, null=True)  # Field name made lowercase.
    prazo1 = models.IntegerField(db_column='Prazo1', blank=True, null=True)  # Field name made lowercase.
    prazo2 = models.IntegerField(db_column='Prazo2', blank=True, null=True)  # Field name made lowercase.
    prazo3 = models.IntegerField(db_column='Prazo3', blank=True, null=True)  # Field name made lowercase.
    prazo4 = models.IntegerField(db_column='Prazo4', blank=True, null=True)  # Field name made lowercase.
    prazo5 = models.IntegerField(db_column='Prazo5', blank=True, null=True)  # Field name made lowercase.
    prazo6 = models.IntegerField(db_column='Prazo6', blank=True, null=True)  # Field name made lowercase.
    prazo7 = models.IntegerField(db_column='Prazo7', blank=True, null=True)  # Field name made lowercase.
    prazo8 = models.IntegerField(db_column='Prazo8', blank=True, null=True)  # Field name made lowercase.
    prazo9 = models.IntegerField(db_column='Prazo9', blank=True, null=True)  # Field name made lowercase.
    prazo10 = models.IntegerField(db_column='Prazo10', blank=True, null=True)  # Field name made lowercase.
    prazo11 = models.IntegerField(db_column='Prazo11', blank=True, null=True)  # Field name made lowercase.
    prazo12 = models.IntegerField(db_column='Prazo12', blank=True, null=True)  # Field name made lowercase.
    chequeprazo = models.FloatField(db_column='ChequePrazo', blank=True, null=True)  # Field name made lowercase.
    chequevista = models.FloatField(db_column='ChequeVista', blank=True, null=True)  # Field name made lowercase.
    cartao = models.FloatField(db_column='Cartao', blank=True, null=True)  # Field name made lowercase.
    duplicata = models.FloatField(db_column='Duplicata', blank=True, null=True)  # Field name made lowercase.
    cadastro = models.DateField(db_column='Cadastro', blank=True, null=True)  # Field name made lowercase.
    empresa = models.IntegerField(db_column='Empresa', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'condicoespp'


class Conexao(models.Model):
    hostname = models.CharField(db_column='HostName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    port = models.CharField(db_column='Port', max_length=200, blank=True, null=True)  # Field name made lowercase.
    user = models.CharField(db_column='User', max_length=200, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=200, blank=True, null=True)  # Field name made lowercase.
    protocol = models.CharField(db_column='Protocol', max_length=200, blank=True, null=True)  # Field name made lowercase.
    bd = models.CharField(db_column='BD', max_length=200, blank=True, null=True)  # Field name made lowercase.
    tabela = models.CharField(db_column='Tabela', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'conexao'


class Confbordero(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    width = models.IntegerField(db_column='Width', blank=True, null=True)  # Field name made lowercase.
    height = models.IntegerField(db_column='Height', blank=True, null=True)  # Field name made lowercase.
    parc1 = models.IntegerField(db_column='Parc1', blank=True, null=True)  # Field name made lowercase.
    parc2 = models.IntegerField(db_column='Parc2', blank=True, null=True)  # Field name made lowercase.
    venc1 = models.IntegerField(db_column='Venc1', blank=True, null=True)  # Field name made lowercase.
    venc2 = models.IntegerField(db_column='Venc2', blank=True, null=True)  # Field name made lowercase.
    date1 = models.IntegerField(db_column='Date1', blank=True, null=True)  # Field name made lowercase.
    date2 = models.IntegerField(db_column='Date2', blank=True, null=True)  # Field name made lowercase.
    titulo1 = models.IntegerField(db_column='Titulo1', blank=True, null=True)  # Field name made lowercase.
    titulo2 = models.IntegerField(db_column='Titulo2', blank=True, null=True)  # Field name made lowercase.
    titulo3 = models.IntegerField(db_column='Titulo3', blank=True, null=True)  # Field name made lowercase.
    titulo4 = models.IntegerField(db_column='Titulo4', blank=True, null=True)  # Field name made lowercase.
    especie1 = models.IntegerField(db_column='Especie1', blank=True, null=True)  # Field name made lowercase.
    especie2 = models.IntegerField(db_column='Especie2', blank=True, null=True)  # Field name made lowercase.
    aceite1 = models.IntegerField(db_column='Aceite1', blank=True, null=True)  # Field name made lowercase.
    aceite2 = models.IntegerField(db_column='Aceite2', blank=True, null=True)  # Field name made lowercase.
    date3 = models.IntegerField(db_column='Date3', blank=True, null=True)  # Field name made lowercase.
    date31 = models.IntegerField(db_column='Date31', blank=True, null=True)  # Field name made lowercase.
    date4 = models.IntegerField(db_column='Date4', blank=True, null=True)  # Field name made lowercase.
    valor1 = models.IntegerField(db_column='Valor1', blank=True, null=True)  # Field name made lowercase.
    valor2 = models.IntegerField(db_column='Valor2', blank=True, null=True)  # Field name made lowercase.
    venc3 = models.IntegerField(db_column='Venc3', blank=True, null=True)  # Field name made lowercase.
    venc4 = models.IntegerField(db_column='Venc4', blank=True, null=True)  # Field name made lowercase.
    desc1 = models.IntegerField(blank=True, null=True)
    desc2 = models.IntegerField(blank=True, null=True)
    acres1 = models.IntegerField(db_column='Acres1', blank=True, null=True)  # Field name made lowercase.
    acres2 = models.IntegerField(db_column='Acres2', blank=True, null=True)  # Field name made lowercase.
    inst1 = models.IntegerField(db_column='Inst1', blank=True, null=True)  # Field name made lowercase.
    inst2 = models.IntegerField(db_column='Inst2', blank=True, null=True)  # Field name made lowercase.
    inst3 = models.IntegerField(db_column='Inst3', blank=True, null=True)  # Field name made lowercase.
    inst4 = models.IntegerField(db_column='Inst4', blank=True, null=True)  # Field name made lowercase.
    inst5 = models.IntegerField(db_column='Inst5', blank=True, null=True)  # Field name made lowercase.
    inst6 = models.IntegerField(db_column='Inst6', blank=True, null=True)  # Field name made lowercase.
    inst7 = models.IntegerField(db_column='Inst7', blank=True, null=True)  # Field name made lowercase.
    inst8 = models.IntegerField(db_column='Inst8', blank=True, null=True)  # Field name made lowercase.
    nomecli1 = models.IntegerField(db_column='NomeCli1', blank=True, null=True)  # Field name made lowercase.
    nomecli2 = models.IntegerField(db_column='NomeCli2', blank=True, null=True)  # Field name made lowercase.
    codcli1 = models.IntegerField(db_column='CodCli1', blank=True, null=True)  # Field name made lowercase.
    codcli2 = models.IntegerField(db_column='CodCli2', blank=True, null=True)  # Field name made lowercase.
    endcli1 = models.IntegerField(db_column='EndCli1', blank=True, null=True)  # Field name made lowercase.
    endcli2 = models.IntegerField(db_column='EndCli2', blank=True, null=True)  # Field name made lowercase.
    cepcli1 = models.IntegerField(db_column='CepCli1', blank=True, null=True)  # Field name made lowercase.
    cepcli2 = models.IntegerField(db_column='CepCli2', blank=True, null=True)  # Field name made lowercase.
    cidcli1 = models.IntegerField(db_column='CidCli1', blank=True, null=True)  # Field name made lowercase.
    cidcli2 = models.IntegerField(db_column='CidCli2', blank=True, null=True)  # Field name made lowercase.
    cidcli3 = models.IntegerField(db_column='CidCli3', blank=True, null=True)  # Field name made lowercase.
    cidcli4 = models.IntegerField(db_column='CidCli4', blank=True, null=True)  # Field name made lowercase.
    uf1 = models.IntegerField(db_column='UF1', blank=True, null=True)  # Field name made lowercase.
    uf2 = models.IntegerField(db_column='UF2', blank=True, null=True)  # Field name made lowercase.
    cpfcli1 = models.IntegerField(db_column='CPFCli1', blank=True, null=True)  # Field name made lowercase.
    cpfcli2 = models.IntegerField(db_column='CPFCli2', blank=True, null=True)  # Field name made lowercase.
    rgcli1 = models.IntegerField(db_column='RgCli1', blank=True, null=True)  # Field name made lowercase.
    rgcli2 = models.IntegerField(db_column='RgCli2', blank=True, null=True)  # Field name made lowercase.
    extenso1 = models.IntegerField(db_column='Extenso1', blank=True, null=True)  # Field name made lowercase.
    extenso2 = models.IntegerField(db_column='Extenso2', blank=True, null=True)  # Field name made lowercase.
    dateaceite1 = models.IntegerField(db_column='DateAceite1', blank=True, null=True)  # Field name made lowercase.
    dateaceite2 = models.IntegerField(db_column='DateAceite2', blank=True, null=True)  # Field name made lowercase.
    fonte = models.CharField(db_column='Fonte', max_length=30, blank=True, null=True)  # Field name made lowercase.
    size = models.IntegerField(db_column='Size', blank=True, null=True)  # Field name made lowercase.
    maquina = models.CharField(db_column='Maquina', max_length=50, blank=True, null=True)  # Field name made lowercase.
    impressora = models.IntegerField(db_column='Impressora', blank=True, null=True)  # Field name made lowercase.
    banco = models.IntegerField(db_column='Banco', blank=True, null=True)  # Field name made lowercase.
    imprimir_endereco = models.IntegerField(db_column='Imprimir_endereco', blank=True, null=True)  # Field name made lowercase.
    empresa = models.IntegerField(db_column='Empresa', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'confbordero'


class Confnota(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    width = models.IntegerField(db_column='Width', blank=True, null=True)  # Field name made lowercase.
    height = models.IntegerField(db_column='Height', blank=True, null=True)  # Field name made lowercase.
    x1 = models.IntegerField(db_column='X1', blank=True, null=True)  # Field name made lowercase.
    x2 = models.IntegerField(db_column='X2', blank=True, null=True)  # Field name made lowercase.
    x3 = models.IntegerField(db_column='X3', blank=True, null=True)  # Field name made lowercase.
    x4 = models.IntegerField(db_column='X4', blank=True, null=True)  # Field name made lowercase.
    numero1 = models.IntegerField(db_column='Numero1', blank=True, null=True)  # Field name made lowercase.
    numero2 = models.IntegerField(db_column='Numero2', blank=True, null=True)  # Field name made lowercase.
    natureza1 = models.IntegerField(db_column='Natureza1', blank=True, null=True)  # Field name made lowercase.
    natureza2 = models.IntegerField(db_column='Natureza2', blank=True, null=True)  # Field name made lowercase.
    cfop1 = models.IntegerField(db_column='CFOP1', blank=True, null=True)  # Field name made lowercase.
    cfop2 = models.IntegerField(db_column='CFOP2', blank=True, null=True)  # Field name made lowercase.
    nomecli1 = models.IntegerField(db_column='NomeCli1', blank=True, null=True)  # Field name made lowercase.
    nomecli2 = models.IntegerField(db_column='NomeCli2', blank=True, null=True)  # Field name made lowercase.
    codcli1 = models.IntegerField(db_column='CodCli1', blank=True, null=True)  # Field name made lowercase.
    codcli2 = models.IntegerField(db_column='CodCli2', blank=True, null=True)  # Field name made lowercase.
    cpfcli1 = models.IntegerField(db_column='CpfCli1', blank=True, null=True)  # Field name made lowercase.
    cpfcli2 = models.IntegerField(db_column='CpfCli2', blank=True, null=True)  # Field name made lowercase.
    date1 = models.IntegerField(db_column='Date1', blank=True, null=True)  # Field name made lowercase.
    date2 = models.IntegerField(db_column='Date2', blank=True, null=True)  # Field name made lowercase.
    endcli1 = models.IntegerField(db_column='EndCli1', blank=True, null=True)  # Field name made lowercase.
    endcli2 = models.IntegerField(db_column='EndCli2', blank=True, null=True)  # Field name made lowercase.
    bairrocli1 = models.IntegerField(db_column='BairroCli1', blank=True, null=True)  # Field name made lowercase.
    bairrocli2 = models.IntegerField(db_column='BairroCli2', blank=True, null=True)  # Field name made lowercase.
    cepcli1 = models.IntegerField(db_column='CepCli1', blank=True, null=True)  # Field name made lowercase.
    cepcli2 = models.IntegerField(db_column='CepCli2', blank=True, null=True)  # Field name made lowercase.
    date3 = models.IntegerField(db_column='Date3', blank=True, null=True)  # Field name made lowercase.
    date4 = models.IntegerField(db_column='Date4', blank=True, null=True)  # Field name made lowercase.
    cidcli1 = models.IntegerField(db_column='CidCli1', blank=True, null=True)  # Field name made lowercase.
    cidcli2 = models.IntegerField(db_column='CidCli2', blank=True, null=True)  # Field name made lowercase.
    fonecli1 = models.IntegerField(db_column='FoneCli1', blank=True, null=True)  # Field name made lowercase.
    fonecli2 = models.IntegerField(db_column='FoneCli2', blank=True, null=True)  # Field name made lowercase.
    ufcli1 = models.IntegerField(db_column='UfCli1', blank=True, null=True)  # Field name made lowercase.
    ufcli2 = models.IntegerField(db_column='UfCli2', blank=True, null=True)  # Field name made lowercase.
    rgcli1 = models.IntegerField(db_column='RGCli1', blank=True, null=True)  # Field name made lowercase.
    rgcli2 = models.IntegerField(db_column='RGCli2', blank=True, null=True)  # Field name made lowercase.
    time1 = models.IntegerField(db_column='Time1', blank=True, null=True)  # Field name made lowercase.
    time2 = models.IntegerField(db_column='Time2', blank=True, null=True)  # Field name made lowercase.
    fatura1 = models.IntegerField(db_column='Fatura1', blank=True, null=True)  # Field name made lowercase.
    fatura2 = models.IntegerField(db_column='Fatura2', blank=True, null=True)  # Field name made lowercase.
    duplicata1 = models.IntegerField(db_column='Duplicata1', blank=True, null=True)  # Field name made lowercase.
    duplicata2 = models.IntegerField(db_column='Duplicata2', blank=True, null=True)  # Field name made lowercase.
    vencimento1 = models.IntegerField(db_column='Vencimento1', blank=True, null=True)  # Field name made lowercase.
    vencimento2 = models.IntegerField(db_column='Vencimento2', blank=True, null=True)  # Field name made lowercase.
    valor1 = models.IntegerField(db_column='Valor1', blank=True, null=True)  # Field name made lowercase.
    valor2 = models.IntegerField(db_column='Valor2', blank=True, null=True)  # Field name made lowercase.
    duplicata3 = models.IntegerField(db_column='Duplicata3', blank=True, null=True)  # Field name made lowercase.
    duplicata4 = models.IntegerField(db_column='Duplicata4', blank=True, null=True)  # Field name made lowercase.
    vencimento3 = models.IntegerField(db_column='Vencimento3', blank=True, null=True)  # Field name made lowercase.
    vencimento4 = models.IntegerField(db_column='Vencimento4', blank=True, null=True)  # Field name made lowercase.
    valor3 = models.IntegerField(db_column='Valor3', blank=True, null=True)  # Field name made lowercase.
    valor4 = models.IntegerField(db_column='Valor4', blank=True, null=True)  # Field name made lowercase.
    duplicata5 = models.IntegerField(db_column='Duplicata5', blank=True, null=True)  # Field name made lowercase.
    duplicata6 = models.IntegerField(db_column='Duplicata6', blank=True, null=True)  # Field name made lowercase.
    vencimento5 = models.IntegerField(db_column='Vencimento5', blank=True, null=True)  # Field name made lowercase.
    vencimento6 = models.IntegerField(db_column='Vencimento6', blank=True, null=True)  # Field name made lowercase.
    valor5 = models.IntegerField(db_column='Valor5', blank=True, null=True)  # Field name made lowercase.
    valor6 = models.IntegerField(db_column='Valor6', blank=True, null=True)  # Field name made lowercase.
    duplicata7 = models.IntegerField(db_column='Duplicata7', blank=True, null=True)  # Field name made lowercase.
    duplicata8 = models.IntegerField(db_column='Duplicata8', blank=True, null=True)  # Field name made lowercase.
    vencimento7 = models.IntegerField(db_column='Vencimento7', blank=True, null=True)  # Field name made lowercase.
    vencimento8 = models.IntegerField(db_column='Vencimento8', blank=True, null=True)  # Field name made lowercase.
    valor7 = models.IntegerField(db_column='Valor7', blank=True, null=True)  # Field name made lowercase.
    valor8 = models.IntegerField(db_column='Valor8', blank=True, null=True)  # Field name made lowercase.
    duplicata9 = models.IntegerField(db_column='Duplicata9', blank=True, null=True)  # Field name made lowercase.
    duplicata10 = models.IntegerField(db_column='Duplicata10', blank=True, null=True)  # Field name made lowercase.
    vencimento9 = models.IntegerField(db_column='Vencimento9', blank=True, null=True)  # Field name made lowercase.
    vencimento10 = models.IntegerField(db_column='Vencimento10', blank=True, null=True)  # Field name made lowercase.
    valor9 = models.IntegerField(db_column='Valor9', blank=True, null=True)  # Field name made lowercase.
    valor10 = models.IntegerField(db_column='Valor10', blank=True, null=True)  # Field name made lowercase.
    duplicata11 = models.IntegerField(db_column='Duplicata11', blank=True, null=True)  # Field name made lowercase.
    duplicata12 = models.IntegerField(db_column='Duplicata12', blank=True, null=True)  # Field name made lowercase.
    vencimento11 = models.IntegerField(db_column='Vencimento11', blank=True, null=True)  # Field name made lowercase.
    vencimento12 = models.IntegerField(db_column='Vencimento12', blank=True, null=True)  # Field name made lowercase.
    valor11 = models.IntegerField(db_column='Valor11', blank=True, null=True)  # Field name made lowercase.
    valor12 = models.IntegerField(db_column='Valor12', blank=True, null=True)  # Field name made lowercase.
    duplicata13 = models.IntegerField(db_column='Duplicata13', blank=True, null=True)  # Field name made lowercase.
    duplicata14 = models.IntegerField(db_column='Duplicata14', blank=True, null=True)  # Field name made lowercase.
    vencimento13 = models.IntegerField(db_column='Vencimento13', blank=True, null=True)  # Field name made lowercase.
    vencimento14 = models.IntegerField(db_column='Vencimento14', blank=True, null=True)  # Field name made lowercase.
    valor13 = models.IntegerField(db_column='Valor13', blank=True, null=True)  # Field name made lowercase.
    valor14 = models.IntegerField(db_column='Valor14', blank=True, null=True)  # Field name made lowercase.
    duplicata15 = models.IntegerField(db_column='Duplicata15', blank=True, null=True)  # Field name made lowercase.
    duplicata16 = models.IntegerField(db_column='Duplicata16', blank=True, null=True)  # Field name made lowercase.
    vencimento15 = models.IntegerField(db_column='Vencimento15', blank=True, null=True)  # Field name made lowercase.
    vencimento16 = models.IntegerField(db_column='Vencimento16', blank=True, null=True)  # Field name made lowercase.
    valor15 = models.IntegerField(db_column='Valor15', blank=True, null=True)  # Field name made lowercase.
    valor16 = models.IntegerField(db_column='Valor16', blank=True, null=True)  # Field name made lowercase.
    duplicata17 = models.IntegerField(db_column='Duplicata17', blank=True, null=True)  # Field name made lowercase.
    duplicata18 = models.IntegerField(db_column='Duplicata18', blank=True, null=True)  # Field name made lowercase.
    vencimento17 = models.IntegerField(db_column='Vencimento17', blank=True, null=True)  # Field name made lowercase.
    vencimento18 = models.IntegerField(db_column='Vencimento18', blank=True, null=True)  # Field name made lowercase.
    valor17 = models.IntegerField(db_column='Valor17', blank=True, null=True)  # Field name made lowercase.
    valor18 = models.IntegerField(db_column='Valor18', blank=True, null=True)  # Field name made lowercase.
    duplicata19 = models.IntegerField(db_column='Duplicata19', blank=True, null=True)  # Field name made lowercase.
    duplicata20 = models.IntegerField(db_column='Duplicata20', blank=True, null=True)  # Field name made lowercase.
    vencimento19 = models.IntegerField(db_column='Vencimento19', blank=True, null=True)  # Field name made lowercase.
    vencimento20 = models.IntegerField(db_column='Vencimento20', blank=True, null=True)  # Field name made lowercase.
    valor19 = models.IntegerField(db_column='Valor19', blank=True, null=True)  # Field name made lowercase.
    valor20 = models.IntegerField(db_column='Valor20', blank=True, null=True)  # Field name made lowercase.
    duplicata21 = models.IntegerField(db_column='Duplicata21', blank=True, null=True)  # Field name made lowercase.
    duplicata22 = models.IntegerField(db_column='Duplicata22', blank=True, null=True)  # Field name made lowercase.
    vencimento21 = models.IntegerField(db_column='Vencimento21', blank=True, null=True)  # Field name made lowercase.
    vencimento22 = models.IntegerField(db_column='Vencimento22', blank=True, null=True)  # Field name made lowercase.
    valor21 = models.IntegerField(db_column='Valor21', blank=True, null=True)  # Field name made lowercase.
    valor22 = models.IntegerField(db_column='Valor22', blank=True, null=True)  # Field name made lowercase.
    duplicata23 = models.IntegerField(db_column='Duplicata23', blank=True, null=True)  # Field name made lowercase.
    duplicata24 = models.IntegerField(db_column='Duplicata24', blank=True, null=True)  # Field name made lowercase.
    vencimento23 = models.IntegerField(db_column='Vencimento23', blank=True, null=True)  # Field name made lowercase.
    vencimento24 = models.IntegerField(db_column='Vencimento24', blank=True, null=True)  # Field name made lowercase.
    valor23 = models.IntegerField(db_column='Valor23', blank=True, null=True)  # Field name made lowercase.
    valor24 = models.IntegerField(db_column='Valor24', blank=True, null=True)  # Field name made lowercase.
    codprod1 = models.IntegerField(db_column='CodProd1', blank=True, null=True)  # Field name made lowercase.
    codprod2 = models.IntegerField(db_column='CodProd2', blank=True, null=True)  # Field name made lowercase.
    descprod1 = models.IntegerField(db_column='DescProd1', blank=True, null=True)  # Field name made lowercase.
    descprod2 = models.IntegerField(db_column='DescProd2', blank=True, null=True)  # Field name made lowercase.
    cfop_prod1 = models.IntegerField(db_column='Cfop_prod1', blank=True, null=True)  # Field name made lowercase.
    cfop_prod2 = models.IntegerField(db_column='Cfop_prod2', blank=True, null=True)  # Field name made lowercase.
    ncms1 = models.IntegerField(db_column='Ncms1', blank=True, null=True)  # Field name made lowercase.
    ncms2 = models.IntegerField(db_column='Ncms2', blank=True, null=True)  # Field name made lowercase.
    sitprod1 = models.IntegerField(db_column='SitProd1', blank=True, null=True)  # Field name made lowercase.
    sitprod2 = models.IntegerField(db_column='SitProd2', blank=True, null=True)  # Field name made lowercase.
    unidprod1 = models.IntegerField(db_column='UnidProd1', blank=True, null=True)  # Field name made lowercase.
    unidprod2 = models.IntegerField(db_column='UnidProd2', blank=True, null=True)  # Field name made lowercase.
    quantprod1 = models.IntegerField(db_column='QuantProd1', blank=True, null=True)  # Field name made lowercase.
    quantprod2 = models.IntegerField(db_column='QuantProd2', blank=True, null=True)  # Field name made lowercase.
    unitprod1 = models.IntegerField(db_column='UnitProd1', blank=True, null=True)  # Field name made lowercase.
    unitprod2 = models.IntegerField(db_column='UnitProd2', blank=True, null=True)  # Field name made lowercase.
    totprod1 = models.IntegerField(db_column='TotProd1', blank=True, null=True)  # Field name made lowercase.
    totprod2 = models.IntegerField(db_column='TotProd2', blank=True, null=True)  # Field name made lowercase.
    aliquota1 = models.IntegerField(db_column='Aliquota1', blank=True, null=True)  # Field name made lowercase.
    aliquota2 = models.IntegerField(db_column='Aliquota2', blank=True, null=True)  # Field name made lowercase.
    quantprod = models.IntegerField(db_column='QuantProd', blank=True, null=True)  # Field name made lowercase.
    espassoprod = models.IntegerField(db_column='EspassoProd', blank=True, null=True)  # Field name made lowercase.
    descserv1 = models.IntegerField(db_column='DescServ1', blank=True, null=True)  # Field name made lowercase.
    descserv2 = models.IntegerField(db_column='DescServ2', blank=True, null=True)  # Field name made lowercase.
    unidserv1 = models.IntegerField(db_column='UnidServ1', blank=True, null=True)  # Field name made lowercase.
    unidserv2 = models.IntegerField(db_column='UnidServ2', blank=True, null=True)  # Field name made lowercase.
    quantserv1 = models.IntegerField(db_column='QuantServ1', blank=True, null=True)  # Field name made lowercase.
    quantserv2 = models.IntegerField(db_column='QuantServ2', blank=True, null=True)  # Field name made lowercase.
    unitserv1 = models.IntegerField(db_column='UnitServ1', blank=True, null=True)  # Field name made lowercase.
    unitserv2 = models.IntegerField(db_column='UnitServ2', blank=True, null=True)  # Field name made lowercase.
    totserv1 = models.IntegerField(db_column='TotServ1', blank=True, null=True)  # Field name made lowercase.
    totserv2 = models.IntegerField(db_column='TotServ2', blank=True, null=True)  # Field name made lowercase.
    quantserv = models.IntegerField(db_column='QuantServ', blank=True, null=True)  # Field name made lowercase.
    espassoserv = models.IntegerField(db_column='EspassoServ', blank=True, null=True)  # Field name made lowercase.
    valiss1 = models.IntegerField(db_column='ValIss1', blank=True, null=True)  # Field name made lowercase.
    valiss2 = models.IntegerField(db_column='ValIss2', blank=True, null=True)  # Field name made lowercase.
    valserv1 = models.IntegerField(db_column='ValServ1', blank=True, null=True)  # Field name made lowercase.
    valserv2 = models.IntegerField(db_column='ValServ2', blank=True, null=True)  # Field name made lowercase.
    base1 = models.IntegerField(db_column='Base1', blank=True, null=True)  # Field name made lowercase.
    base2 = models.IntegerField(db_column='Base2', blank=True, null=True)  # Field name made lowercase.
    icms1 = models.IntegerField(db_column='Icms1', blank=True, null=True)  # Field name made lowercase.
    icms2 = models.IntegerField(db_column='Icms2', blank=True, null=True)  # Field name made lowercase.
    frete1 = models.IntegerField(db_column='Frete1', blank=True, null=True)  # Field name made lowercase.
    frete2 = models.IntegerField(db_column='Frete2', blank=True, null=True)  # Field name made lowercase.
    despesas1 = models.IntegerField(db_column='Despesas1', blank=True, null=True)  # Field name made lowercase.
    despesas2 = models.IntegerField(db_column='Despesas2', blank=True, null=True)  # Field name made lowercase.
    totprod3 = models.IntegerField(db_column='TotProd3', blank=True, null=True)  # Field name made lowercase.
    totprod4 = models.IntegerField(db_column='TotProd4', blank=True, null=True)  # Field name made lowercase.
    totnota1 = models.IntegerField(db_column='TotNota1', blank=True, null=True)  # Field name made lowercase.
    totnota2 = models.IntegerField(db_column='TotNota2', blank=True, null=True)  # Field name made lowercase.
    freteconta1 = models.IntegerField(db_column='FreteConta1', blank=True, null=True)  # Field name made lowercase.
    freteconta2 = models.IntegerField(db_column='FreteConta2', blank=True, null=True)  # Field name made lowercase.
    nometrans1 = models.IntegerField(db_column='NomeTrans1', blank=True, null=True)  # Field name made lowercase.
    nometrans2 = models.IntegerField(db_column='NomeTrans2', blank=True, null=True)  # Field name made lowercase.
    endtrans1 = models.IntegerField(db_column='EndTrans1', blank=True, null=True)  # Field name made lowercase.
    endtrans2 = models.IntegerField(db_column='EndTrans2', blank=True, null=True)  # Field name made lowercase.
    cidtrans1 = models.IntegerField(db_column='CidTrans1', blank=True, null=True)  # Field name made lowercase.
    cidtrans2 = models.IntegerField(db_column='CidTrans2', blank=True, null=True)  # Field name made lowercase.
    uftrans1 = models.IntegerField(db_column='UFTrans1', blank=True, null=True)  # Field name made lowercase.
    uftrans2 = models.IntegerField(db_column='UFTrans2', blank=True, null=True)  # Field name made lowercase.
    cnpjtrans1 = models.IntegerField(db_column='CNPJTrans1', blank=True, null=True)  # Field name made lowercase.
    cnpjtrans2 = models.IntegerField(db_column='CNPJTrans2', blank=True, null=True)  # Field name made lowercase.
    ietrans1 = models.IntegerField(db_column='IETrans1', blank=True, null=True)  # Field name made lowercase.
    ietrans2 = models.IntegerField(db_column='IETrans2', blank=True, null=True)  # Field name made lowercase.
    dados1 = models.IntegerField(db_column='Dados1', blank=True, null=True)  # Field name made lowercase.
    dados2 = models.IntegerField(db_column='Dados2', blank=True, null=True)  # Field name made lowercase.
    dados3 = models.IntegerField(db_column='Dados3', blank=True, null=True)  # Field name made lowercase.
    dados4 = models.IntegerField(db_column='Dados4', blank=True, null=True)  # Field name made lowercase.
    dados5 = models.IntegerField(db_column='Dados5', blank=True, null=True)  # Field name made lowercase.
    dados6 = models.IntegerField(db_column='Dados6', blank=True, null=True)  # Field name made lowercase.
    dados7 = models.IntegerField(db_column='Dados7', blank=True, null=True)  # Field name made lowercase.
    dados8 = models.IntegerField(db_column='Dados8', blank=True, null=True)  # Field name made lowercase.
    dados9 = models.IntegerField(db_column='Dados9', blank=True, null=True)  # Field name made lowercase.
    dados10 = models.IntegerField(db_column='Dados10', blank=True, null=True)  # Field name made lowercase.
    dados11 = models.IntegerField(db_column='Dados11', blank=True, null=True)  # Field name made lowercase.
    dados12 = models.IntegerField(db_column='Dados12', blank=True, null=True)  # Field name made lowercase.
    numero3 = models.IntegerField(db_column='Numero3', blank=True, null=True)  # Field name made lowercase.
    numero4 = models.IntegerField(db_column='Numero4', blank=True, null=True)  # Field name made lowercase.
    carentsai = models.CharField(db_column='CarEntSai', max_length=5, blank=True, null=True)  # Field name made lowercase.
    fonteentsai = models.CharField(db_column='FonteEntSai', max_length=30, blank=True, null=True)  # Field name made lowercase.
    sizeentsai = models.IntegerField(db_column='SizeEntSai', blank=True, null=True)  # Field name made lowercase.
    fonteoutro = models.CharField(db_column='FonteOutro', max_length=30, blank=True, null=True)  # Field name made lowercase.
    sizeoutro = models.IntegerField(db_column='SizeOutro', blank=True, null=True)  # Field name made lowercase.
    fontenumerof = models.CharField(db_column='FonteNumeroF', max_length=30, blank=True, null=True)  # Field name made lowercase.
    sizenumerof = models.IntegerField(db_column='SizeNumeroF', blank=True, null=True)  # Field name made lowercase.
    maquina = models.CharField(db_column='Maquina', max_length=50, blank=True, null=True)  # Field name made lowercase.
    impressora = models.IntegerField(db_column='Impressora', blank=True, null=True)  # Field name made lowercase.
    empresa = models.IntegerField(db_column='Empresa', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'confnota'


class ConsumoId(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    numeroaleatorio = models.IntegerField(db_column='NumeroAleatorio', blank=True, null=True)  # Field name made lowercase.
    data = models.DateField(db_column='Data', blank=True, null=True)  # Field name made lowercase.
    hora = models.TimeField(db_column='Hora', blank=True, null=True)  # Field name made lowercase.
    usuario = models.IntegerField(db_column='Usuario', blank=True, null=True)  # Field name made lowercase.
    total = models.FloatField(db_column='Total', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'consumo_id'


class ConsumoProd(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    controle = models.IntegerField(db_column='Controle', blank=True, null=True)  # Field name made lowercase.
    data = models.DateField(db_column='Data', blank=True, null=True)  # Field name made lowercase.
    hora = models.TimeField(db_column='Hora', blank=True, null=True)  # Field name made lowercase.
    usuario = models.IntegerField(db_column='Usuario', blank=True, null=True)  # Field name made lowercase.
    funcionario = models.IntegerField(db_column='Funcionario', blank=True, null=True)  # Field name made lowercase.
    codigo = models.CharField(db_column='Codigo', max_length=30, blank=True, null=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=50, blank=True, null=True)  # Field name made lowercase.
    utilizacao = models.CharField(db_column='Utilizacao', max_length=50, blank=True, null=True)  # Field name made lowercase.
    quantidade = models.FloatField(db_column='Quantidade', blank=True, null=True)  # Field name made lowercase.
    custounitario = models.FloatField(db_column='CustoUnitario', blank=True, null=True)  # Field name made lowercase.
    custototal = models.FloatField(db_column='CustoTotal', blank=True, null=True)  # Field name made lowercase.
    precovenda = models.FloatField(db_column='PrecoVenda', blank=True, null=True)  # Field name made lowercase.
    observacao = models.CharField(db_column='Observacao', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'consumo_prod'


class Conta(models.Model):
    codigo = models.AutoField(db_column='Codigo', primary_key=True)  # Field name made lowercase.
    conta = models.CharField(db_column='Conta', max_length=60, blank=True, null=True)  # Field name made lowercase.
    empresa = models.IntegerField(db_column='Empresa', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'conta'


class ContaBancaria(models.Model):
    ativo = models.IntegerField(blank=True, null=True)
    banco = models.IntegerField(blank=True, null=True)
    agencia = models.CharField(max_length=10, blank=True, null=True)
    conta = models.CharField(max_length=15, blank=True, null=True)
    titular = models.CharField(max_length=40, blank=True, null=True)
    limite = models.FloatField(blank=True, null=True)
    fornecedor = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'conta_bancaria'


class ContaCorrente(models.Model):
    id_conta = models.IntegerField(blank=True, null=True)
    tipo = models.CharField(max_length=1, blank=True, null=True)
    doc = models.IntegerField(blank=True, null=True)
    especie_doc = models.CharField(max_length=17, blank=True, null=True)
    historico = models.CharField(max_length=50, blank=True, null=True)
    data = models.DateField(blank=True, null=True)
    valor = models.FloatField(blank=True, null=True)
    id_cheque = models.IntegerField(blank=True, null=True)
    compensado = models.CharField(max_length=1, blank=True, null=True)
    data_compensacao = models.DateField(blank=True, null=True)
    usuario = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'conta_corrente'


class ContaDespesa(models.Model):
    codigo = models.AutoField(db_column='Codigo', primary_key=True)  # Field name made lowercase.
    conta_despesa = models.CharField(db_column='Conta_Despesa', max_length=60, blank=True, null=True)  # Field name made lowercase.
    despesa_limite = models.FloatField(db_column='Despesa_Limite', blank=True, null=True)  # Field name made lowercase.
    empresa = models.IntegerField(db_column='Empresa', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'conta_despesa'


class ContaDespesas(models.Model):
    iof = models.IntegerField(primary_key=True)
    forn_iof = models.IntegerField(blank=True, null=True)
    tac = models.IntegerField(blank=True, null=True)
    despesa_cartao = models.IntegerField(blank=True, null=True)
    juro_desconto_cheque = models.IntegerField(blank=True, null=True)
    juro_desconto_duplicata = models.IntegerField(blank=True, null=True)
    juro_desconto_cartao = models.IntegerField(blank=True, null=True)
    tarifa_recebiveis = models.IntegerField(blank=True, null=True)
    despesa_cobranca_boleto = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'conta_despesas'


class Contabilista(models.Model):
    nome = models.CharField(db_column='Nome', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cpf = models.CharField(db_column='CPF', max_length=14, blank=True, null=True)  # Field name made lowercase.
    crc = models.CharField(db_column='CRC', max_length=15, blank=True, null=True)  # Field name made lowercase.
    cnpj = models.CharField(db_column='CNPJ', max_length=18, blank=True, null=True)  # Field name made lowercase.
    cep = models.CharField(db_column='CEP', max_length=9, blank=True, null=True)  # Field name made lowercase.
    endereco = models.CharField(db_column='Endereco', max_length=60, blank=True, null=True)  # Field name made lowercase.
    numero = models.CharField(db_column='Numero', max_length=10, blank=True, null=True)  # Field name made lowercase.
    complemento = models.CharField(db_column='Complemento', max_length=60, blank=True, null=True)  # Field name made lowercase.
    bairro = models.CharField(db_column='Bairro', max_length=60, blank=True, null=True)  # Field name made lowercase.
    fone = models.CharField(db_column='Fone', max_length=14, blank=True, null=True)  # Field name made lowercase.
    fax = models.CharField(db_column='Fax', max_length=14, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=50, blank=True, null=True)  # Field name made lowercase.
    codigomunicipioibge = models.CharField(db_column='CodigoMunicipioIBGE', max_length=7, blank=True, null=True)  # Field name made lowercase.
    xmlnfe = models.IntegerField(db_column='XMLNFe', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'contabilista'


class Contagem(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    codigo = models.CharField(db_column='Codigo', max_length=30, blank=True, null=True)  # Field name made lowercase.
    data = models.DateField(db_column='Data', blank=True, null=True)  # Field name made lowercase.
    hora = models.TimeField(db_column='Hora', blank=True, null=True)  # Field name made lowercase.
    estoque = models.FloatField(db_column='Estoque', blank=True, null=True)  # Field name made lowercase.
    contagem = models.FloatField(db_column='Contagem', blank=True, null=True)  # Field name made lowercase.
    saldo = models.FloatField(db_column='Saldo', blank=True, null=True)  # Field name made lowercase.
    saldovalor = models.FloatField(db_column='SaldoValor', blank=True, null=True)  # Field name made lowercase.
    usuario = models.IntegerField(db_column='Usuario', blank=True, null=True)  # Field name made lowercase.
    funccontagem = models.IntegerField(db_column='FuncContagem', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'contagem'


class CopiaCheque(models.Model):
    conta = models.CharField(max_length=15, blank=True, null=True)
    agencia = models.CharField(max_length=10, blank=True, null=True)
    banco = models.IntegerField(blank=True, null=True)
    titular = models.CharField(max_length=40, blank=True, null=True)
    numero_cheque = models.IntegerField(blank=True, null=True)
    valor = models.FloatField(blank=True, null=True)
    data = models.DateField(blank=True, null=True)
    nome = models.CharField(max_length=40, blank=True, null=True)
    historico = models.CharField(max_length=150, blank=True, null=True)
    historico1 = models.CharField(max_length=150, blank=True, null=True)
    historico2 = models.CharField(max_length=150, blank=True, null=True)
    historico3 = models.CharField(max_length=150, blank=True, null=True)
    historico4 = models.CharField(max_length=150, blank=True, null=True)
    extenso = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'copia_cheque'


class CstCofins(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    codigo = models.CharField(db_column='Codigo', max_length=2, blank=True, null=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tipo = models.CharField(db_column='Tipo', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cst_cofins'


class CstIcms(models.Model):
    codigo = models.CharField(db_column='Codigo', primary_key=True, max_length=5)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=255, blank=True, null=True)  # Field name made lowercase.
    regime = models.CharField(db_column='Regime', max_length=16, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cst_icms'


class CstIcmsOrigem(models.Model):
    codigo = models.CharField(primary_key=True, max_length=1)
    origem = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cst_icms_origem'


class CstIpi(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    codigo = models.CharField(db_column='Codigo', max_length=2, blank=True, null=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tipo = models.CharField(db_column='Tipo', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cst_ipi'


class CstPis(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    codigo = models.CharField(db_column='Codigo', max_length=2, blank=True, null=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=255, blank=True, null=True)  # Field name made lowercase.
    aaaa = models.IntegerField(blank=True, null=True)
    tipo = models.CharField(db_column='Tipo', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cst_pis'


class Cupomfiscal(models.Model):
    cupom = models.IntegerField(blank=True, null=True)
    nota = models.IntegerField(blank=True, null=True)
    notaeletronica = models.IntegerField(blank=True, null=True)
    serie = models.IntegerField(blank=True, null=True)
    modelo = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    data = models.DateField(blank=True, null=True)
    hora = models.TimeField(blank=True, null=True)
    cliente = models.IntegerField(blank=True, null=True)
    vendedor = models.IntegerField(blank=True, null=True)
    icms = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cupomfiscal'


class CupomfiscalParametros(models.Model):
    marca = models.CharField(db_column='Marca', max_length=20, blank=True, null=True)  # Field name made lowercase.
    modelo = models.CharField(db_column='Modelo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tipo = models.CharField(db_column='Tipo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    numero_serie = models.CharField(db_column='Numero_Serie', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cupomfiscal_parametros'


class CupomfiscalProdutos(models.Model):
    id = models.BigAutoField(primary_key=True)
    cupom = models.IntegerField(blank=True, null=True)
    marca = models.CharField(max_length=20, blank=True, null=True)
    modelo = models.CharField(max_length=20, blank=True, null=True)
    numero_serie = models.CharField(max_length=20, blank=True, null=True)
    data = models.DateField(blank=True, null=True)
    cliente = models.IntegerField(blank=True, null=True)
    codigo = models.CharField(max_length=40, blank=True, null=True)
    descricao = models.CharField(max_length=60, blank=True, null=True)
    ncm = models.CharField(max_length=8, blank=True, null=True)
    unidade = models.CharField(max_length=2, blank=True, null=True)
    monofasico = models.IntegerField(blank=True, null=True)
    quantidade = models.FloatField(blank=True, null=True)
    unitario = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    vendaunitario = models.FloatField(blank=True, null=True)
    vendatotal = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cupomfiscal_produtos'


class Dadosnf(models.Model):
    serie = models.CharField(max_length=10, blank=True, null=True)
    servico = models.CharField(max_length=3, blank=True, null=True)
    icms = models.CharField(max_length=3, blank=True, null=True)
    fatura = models.CharField(max_length=3, blank=True, null=True)
    imunicipal = models.CharField(max_length=15, blank=True, null=True)
    retencao_iss = models.IntegerField(blank=True, null=True)
    cidade_retencao = models.CharField(max_length=50, blank=True, null=True)
    cep_retencao = models.CharField(max_length=9, blank=True, null=True)
    estado_emissao = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dadosnf'


class Despesas(models.Model):
    numero = models.IntegerField(blank=True, null=True)
    emissao = models.DateField(blank=True, null=True)
    nome = models.CharField(max_length=50, blank=True, null=True)
    vencimento = models.DateField(blank=True, null=True)
    valor = models.FloatField(blank=True, null=True)
    datapagto = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'despesas'


class Devolucao(models.Model):
    codigo = models.AutoField(primary_key=True)
    cliente = models.IntegerField(blank=True, null=True)
    situacao = models.IntegerField(blank=True, null=True)
    data = models.DateField(blank=True, null=True)
    hora = models.TimeField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    vendedor = models.IntegerField(blank=True, null=True)
    peso = models.FloatField(blank=True, null=True)
    justificativa = models.CharField(max_length=200, blank=True, null=True)
    data_agrupamento_devolucao = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'devolucao'


class DevolucaoOrdem(models.Model):
    status = models.IntegerField(blank=True, null=True)
    emissao = models.DateField(blank=True, null=True)
    cliente = models.IntegerField(blank=True, null=True)
    funcionario = models.IntegerField(blank=True, null=True)
    devolucao = models.TextField(blank=True, null=True)
    motivo = models.TextField(blank=True, null=True)
    endereco = models.CharField(max_length=60, blank=True, null=True)
    bairro = models.CharField(max_length=50, blank=True, null=True)
    observacao = models.CharField(max_length=90, blank=True, null=True)
    data = models.DateField(blank=True, null=True)
    hora = models.TimeField(blank=True, null=True)
    fone = models.CharField(max_length=14, blank=True, null=True)
    id_devolucao = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'devolucao_ordem'


class EcfFormaPagamento(models.Model):
    codigo = models.CharField(db_column='Codigo', max_length=3, blank=True, null=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=30, blank=True, null=True)  # Field name made lowercase.
    permite_vinculado = models.CharField(db_column='Permite_Vinculado', max_length=3, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ecf_forma_pagamento'


class EcfParametros(models.Model):
    codigo_consumidor = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ecf_parametros'


class Email(models.Model):
    smtp = models.CharField(db_column='SMTP', max_length=60, blank=True, null=True)  # Field name made lowercase.
    porta = models.IntegerField(db_column='Porta', blank=True, null=True)  # Field name made lowercase.
    usuario = models.CharField(db_column='Usuario', max_length=60, blank=True, null=True)  # Field name made lowercase.
    senha = models.CharField(db_column='Senha', max_length=60, blank=True, null=True)  # Field name made lowercase.
    ssl = models.IntegerField(db_column='SSL', blank=True, null=True)  # Field name made lowercase.
    tls = models.IntegerField(db_column='TLS', blank=True, null=True)  # Field name made lowercase.
    prioridade = models.IntegerField(db_column='Prioridade', blank=True, null=True, db_comment='0-baixa 1-normal 2-alta')  # Field name made lowercase.
    confirmaleitura = models.IntegerField(db_column='ConfirmaLeitura', blank=True, null=True)  # Field name made lowercase.
    emailporhora = models.IntegerField(db_column='EmailPorHora', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'email'


class EmailBoleto(models.Model):
    smpt = models.CharField(db_column='SMPT', max_length=60, blank=True, null=True)  # Field name made lowercase.
    porta = models.IntegerField(db_column='Porta', blank=True, null=True)  # Field name made lowercase.
    usuario = models.CharField(db_column='Usuario', max_length=60, blank=True, null=True)  # Field name made lowercase.
    senha = models.CharField(db_column='Senha', max_length=60, blank=True, null=True)  # Field name made lowercase.
    ssl = models.IntegerField(db_column='SSL', blank=True, null=True)  # Field name made lowercase.
    tls = models.IntegerField(db_column='TLS', blank=True, null=True)  # Field name made lowercase.
    prioridade = models.IntegerField(db_column='Prioridade', blank=True, null=True)  # Field name made lowercase.
    confirmaleitura = models.IntegerField(db_column='ConfirmaLeitura', blank=True, null=True)  # Field name made lowercase.
    assunto = models.CharField(db_column='Assunto', max_length=60, blank=True, null=True)  # Field name made lowercase.
    mensagem = models.TextField(db_column='Mensagem', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'email_boleto'


class EmailContato(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    grupo = models.IntegerField(db_column='Grupo', blank=True, null=True)  # Field name made lowercase.
    cadastro = models.DateField(db_column='Cadastro', blank=True, null=True)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=60, blank=True, null=True)  # Field name made lowercase.
    endereco = models.CharField(db_column='Endereco', max_length=60, blank=True, null=True)  # Field name made lowercase.
    numero = models.CharField(db_column='Numero', max_length=20, blank=True, null=True)  # Field name made lowercase.
    bairro = models.CharField(db_column='Bairro', max_length=60, blank=True, null=True)  # Field name made lowercase.
    codigoibge = models.IntegerField(db_column='CodigoIBGE', blank=True, null=True)  # Field name made lowercase.
    cidade = models.CharField(db_column='Cidade', max_length=60, blank=True, null=True)  # Field name made lowercase.
    uf = models.CharField(db_column='UF', max_length=2, blank=True, null=True)  # Field name made lowercase.
    fone1 = models.CharField(db_column='Fone1', max_length=14, blank=True, null=True)  # Field name made lowercase.
    fone2 = models.CharField(db_column='Fone2', max_length=14, blank=True, null=True)  # Field name made lowercase.
    contato = models.CharField(db_column='Contato', max_length=60, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=60, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'email_contato'


class EmailGrupoContato(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    cadastro = models.DateField(db_column='Cadastro', blank=True, null=True)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=60, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'email_grupo_contato'


class EmailMensagem(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_modulo = models.IntegerField(db_column='ID_Modulo', blank=True, null=True)  # Field name made lowercase.
    assunto = models.CharField(db_column='Assunto', max_length=100, blank=True, null=True)  # Field name made lowercase.
    mensagemcabecalho = models.TextField(db_column='MensagemCabecalho', blank=True, null=True)  # Field name made lowercase.
    mensagemrodape = models.TextField(db_column='MensagemRodape', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'email_mensagem'


class EmailModulo(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    modulo = models.CharField(db_column='Modulo', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'email_modulo'


class EmailPrioridade(models.Model):
    id = models.IntegerField(primary_key=True)
    prioridade = models.CharField(max_length=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'email_prioridade'


class Entrega(models.Model):
    id_prodreq = models.IntegerField(blank=True, null=True)
    pedido = models.IntegerField(blank=True, null=True)
    data = models.DateField(blank=True, null=True)
    cliente = models.IntegerField(blank=True, null=True)
    codigo = models.CharField(max_length=25, blank=True, null=True)
    descricao = models.CharField(max_length=50, blank=True, null=True)
    quantidade = models.FloatField(blank=True, null=True)
    entregue = models.FloatField(blank=True, null=True)
    saldo = models.FloatField(blank=True, null=True)
    unitario = models.FloatField(blank=True, null=True)
    reduzido = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'entrega'


class Entregacontrole(models.Model):
    codigo = models.AutoField(primary_key=True)
    data = models.DateField(blank=True, null=True)
    hora = models.TimeField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    cliente = models.IntegerField(blank=True, null=True)
    vendedor = models.IntegerField(blank=True, null=True)
    numeroaleatorio = models.IntegerField(blank=True, null=True)
    maquina = models.CharField(max_length=150, blank=True, null=True)
    data_cancelamento = models.DateTimeField(blank=True, null=True)
    hora_cancelamento = models.TimeField(blank=True, null=True)
    usuario_cancelamento = models.IntegerField(blank=True, null=True)
    maquina_cancelamento = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'entregacontrole'


class Entregaextrato(models.Model):
    id_prodreq = models.IntegerField(blank=True, null=True)
    pedido = models.IntegerField(blank=True, null=True)
    controle = models.IntegerField(blank=True, null=True)
    data = models.DateField(blank=True, null=True)
    hora = models.TimeField(blank=True, null=True)
    cliente = models.IntegerField(blank=True, null=True)
    codigo = models.CharField(max_length=25, blank=True, null=True)
    descricao = models.CharField(max_length=50, blank=True, null=True)
    entregue = models.FloatField(blank=True, null=True)
    saldo = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'entregaextrato'


class Equipamentos(models.Model):
    equipamento = models.CharField(max_length=60, blank=True, null=True)
    modelo = models.CharField(max_length=30, blank=True, null=True)
    marca = models.CharField(max_length=30, blank=True, null=True)
    numero_serie = models.CharField(max_length=30, blank=True, null=True)
    valor_equipamento = models.FloatField(blank=True, null=True)
    valor_diario = models.FloatField(blank=True, null=True)
    valor_semanal = models.FloatField(blank=True, null=True)
    valor_quinzenal = models.FloatField(blank=True, null=True)
    valor_mensal = models.FloatField(blank=True, null=True)
    situacao = models.IntegerField(blank=True, null=True)
    cadastro = models.DateField(blank=True, null=True)
    controla_estoque = models.IntegerField(blank=True, null=True)
    estoque = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'equipamentos'


class Equipes(models.Model):
    codigo = models.AutoField(primary_key=True)
    equipe = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'equipes'


class Erro(models.Model):
    codigo = models.CharField(max_length=30, blank=True, null=True)
    descricao = models.CharField(max_length=40, blank=True, null=True)
    estoque_anterior = models.FloatField(blank=True, null=True)
    venda = models.FloatField(blank=True, null=True)
    estoque_atual = models.FloatField(blank=True, null=True)
    modulo = models.CharField(max_length=30, blank=True, null=True)
    n_venda = models.IntegerField(blank=True, null=True)
    data = models.DateField(blank=True, null=True)
    falha = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'erro'


class Etiqueta(models.Model):
    codigo = models.CharField(max_length=25, blank=True, null=True)
    descricao = models.CharField(max_length=100, blank=True, null=True)
    utilizacao = models.CharField(max_length=100, blank=True, null=True)
    localizacao = models.CharField(max_length=50, blank=True, null=True)
    original = models.CharField(max_length=50, blank=True, null=True)
    valor = models.CharField(max_length=25, blank=True, null=True)
    valor1 = models.CharField(max_length=30, blank=True, null=True)
    valor2 = models.CharField(max_length=30, blank=True, null=True)
    parcelas = models.CharField(max_length=3, blank=True, null=True)
    codigobarra = models.CharField(max_length=50, blank=True, null=True)
    fabricante = models.CharField(max_length=50, blank=True, null=True)
    codigo_fabricante = models.CharField(max_length=30, blank=True, null=True)
    pontos = models.CharField(max_length=30, blank=True, null=True)
    conversao = models.CharField(max_length=30, blank=True, null=True)
    desconto = models.CharField(max_length=30, blank=True, null=True)
    descontomensal = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'etiqueta'


class Expedicao(models.Model):
    id_controle_expedicao = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    seleciona = models.CharField(max_length=1, blank=True, null=True)
    data = models.DateField(blank=True, null=True)
    hora_emissao = models.TimeField(blank=True, null=True)
    data_entrega = models.DateField(blank=True, null=True)
    hora = models.TimeField(blank=True, null=True)
    data_saida = models.DateField(blank=True, null=True)
    hora_saida = models.TimeField(blank=True, null=True)
    data_retorno = models.DateField(blank=True, null=True)
    hora_retorno = models.TimeField(blank=True, null=True)
    tipo = models.CharField(max_length=3, blank=True, null=True)
    tipo_produto = models.CharField(max_length=9, blank=True, null=True)
    pedido = models.IntegerField(blank=True, null=True)
    agrupado = models.IntegerField(blank=True, null=True)
    funcionario = models.IntegerField(blank=True, null=True)
    cliente = models.IntegerField(blank=True, null=True)
    endereco = models.CharField(max_length=60, blank=True, null=True)
    numero = models.CharField(max_length=30, blank=True, null=True)
    bairronome = models.CharField(max_length=60, blank=True, null=True)
    bairro = models.IntegerField(blank=True, null=True)
    fone = models.CharField(max_length=14, blank=True, null=True)
    cidade = models.CharField(max_length=60, blank=True, null=True)
    uf = models.CharField(max_length=2, blank=True, null=True)
    observacao = models.CharField(max_length=100, blank=True, null=True)
    obs_expedicao = models.CharField(max_length=200, blank=True, null=True)
    aguardar_entrega = models.IntegerField(blank=True, null=True)
    impresso = models.IntegerField(blank=True, null=True)
    dataimpressao = models.DateField(blank=True, null=True)
    horaimpressao = models.TimeField(blank=True, null=True)
    maquina = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'expedicao'


class ExpedicaoControle(models.Model):
    data = models.DateField(blank=True, null=True)
    hora = models.TimeField(blank=True, null=True)
    funcionario = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'expedicao_controle'


class ExpedicaoLista(models.Model):
    data = models.DateField(blank=True, null=True)
    hora = models.TimeField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    funcionario = models.IntegerField(blank=True, null=True)
    expedicao_data = models.DateField(blank=True, null=True)
    expedicao_hora = models.TimeField(blank=True, null=True)
    expedicao_finalizada_data = models.DateField(blank=True, null=True)
    expedicao_finalizada_hora = models.TimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'expedicao_lista'


class ExpedicaoListaDetalhe(models.Model):
    id_expedicao_lista = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    pedido = models.IntegerField(blank=True, null=True)
    peso = models.FloatField(blank=True, null=True)
    cliente = models.IntegerField(blank=True, null=True)
    ordem = models.IntegerField(blank=True, null=True)
    data = models.DateField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    data_entrega = models.DateField(blank=True, null=True)
    hora_entrega = models.TimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'expedicao_lista_detalhe'


class ExpedicaoParametros(models.Model):
    minutosatrasoseparacao = models.IntegerField(db_column='MinutosAtrasoSeparacao', blank=True, null=True)  # Field name made lowercase.
    minutosatrasoentrega = models.IntegerField(db_column='MinutosAtrasoEntrega', blank=True, null=True)  # Field name made lowercase.
    segundosatualizacao = models.IntegerField(db_column='SegundosAtualizacao', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'expedicao_parametros'


class Expedicaop(models.Model):
    id_controle_expedicao = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    seleciona = models.CharField(max_length=1, blank=True, null=True)
    data = models.DateTimeField(blank=True, null=True)
    data_entrega = models.DateTimeField(blank=True, null=True)
    data_saida = models.DateTimeField(blank=True, null=True)
    data_retorno = models.DateTimeField(blank=True, null=True)
    tipo = models.CharField(max_length=3, blank=True, null=True)
    pedido = models.IntegerField(blank=True, null=True)
    agrupado = models.IntegerField(blank=True, null=True)
    funcionario = models.IntegerField(blank=True, null=True)
    funcionario_entrega = models.IntegerField(blank=True, null=True)
    cliente = models.IntegerField(blank=True, null=True)
    endereco = models.CharField(max_length=60, blank=True, null=True)
    numero = models.CharField(max_length=30, blank=True, null=True)
    bairro = models.CharField(max_length=60, blank=True, null=True)
    fone = models.CharField(max_length=14, blank=True, null=True)
    cidade = models.CharField(max_length=60, blank=True, null=True)
    uf = models.CharField(max_length=2, blank=True, null=True)
    observacao = models.CharField(max_length=100, blank=True, null=True)
    obs_expedicao = models.CharField(max_length=200, blank=True, null=True)
    aguardar_entrega = models.IntegerField(blank=True, null=True, db_comment='0-false 1-true')
    latitude = models.CharField(max_length=20, blank=True, null=True)
    longitude = models.CharField(max_length=20, blank=True, null=True)
    recebedor = models.CharField(max_length=50, blank=True, null=True)
    impresso = models.IntegerField(blank=True, null=True)
    dataimpressao = models.DateField(blank=True, null=True)
    horaimpressao = models.TimeField(blank=True, null=True)
    maquina = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'expedicaop'


class Fabricantes(models.Model):
    codigo = models.AutoField(db_column='Codigo', primary_key=True)  # Field name made lowercase.
    codant = models.IntegerField(blank=True, null=True)
    fabricante = models.CharField(db_column='Fabricante', max_length=100, blank=True, null=True)  # Field name made lowercase.
    dias_ressuprimento = models.IntegerField(db_column='Dias_ressuprimento', blank=True, null=True)  # Field name made lowercase.
    cadastro = models.DateField(db_column='Cadastro', blank=True, null=True)  # Field name made lowercase.
    empresa = models.IntegerField(db_column='Empresa', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'fabricantes'


class Fatura(models.Model):
    codigo = models.IntegerField(blank=True, null=True)
    cliente = models.IntegerField(blank=True, null=True)
    data = models.DateField(blank=True, null=True)
    valor = models.FloatField(blank=True, null=True)
    valortotal = models.FloatField(blank=True, null=True)
    desconto = models.FloatField(blank=True, null=True)
    portador = models.IntegerField(blank=True, null=True)
    issqn = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fatura'


class FaturaCarta(models.Model):
    codigo = models.IntegerField(blank=True, null=True)
    cliente = models.IntegerField(blank=True, null=True)
    data = models.DateField(blank=True, null=True)
    valor = models.FloatField(blank=True, null=True)
    id_recebimento = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fatura_carta'


class FaturaCartaDetalhes(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_fatura = models.IntegerField(db_column='ID_Fatura', blank=True, null=True)  # Field name made lowercase.
    codigo = models.IntegerField(db_column='Codigo', blank=True, null=True)  # Field name made lowercase.
    emissao = models.DateField(db_column='Emissao', blank=True, null=True)  # Field name made lowercase.
    tipo = models.CharField(db_column='Tipo', max_length=1, blank=True, null=True)  # Field name made lowercase.
    portador = models.IntegerField(db_column='Portador', blank=True, null=True)  # Field name made lowercase.
    cliente = models.IntegerField(db_column='Cliente', blank=True, null=True)  # Field name made lowercase.
    vencimento = models.DateField(db_column='Vencimento', blank=True, null=True)  # Field name made lowercase.
    valorprestacao = models.FloatField(db_column='ValorPrestacao', blank=True, null=True)  # Field name made lowercase.
    valordocumento = models.FloatField(db_column='ValorDocumento', blank=True, null=True)  # Field name made lowercase.
    observacao = models.CharField(db_column='Observacao', max_length=100, blank=True, null=True)  # Field name made lowercase.
    sequencia = models.IntegerField(db_column='Sequencia', blank=True, null=True)  # Field name made lowercase.
    esp = models.CharField(db_column='ESP', max_length=2, blank=True, null=True)  # Field name made lowercase.
    empresa = models.IntegerField(db_column='Empresa', blank=True, null=True)  # Field name made lowercase.
    sequencia2 = models.IntegerField(db_column='Sequencia2', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'fatura_carta_detalhes'


class Feriados(models.Model):
    data = models.DateField(primary_key=True)
    dia = models.CharField(max_length=15, blank=True, null=True)
    comemoracao = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'feriados'


class FornFabricante(models.Model):
    fornecedor = models.IntegerField(blank=True, null=True)
    fabricante = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'forn_fabricante'


class Fornecedores(models.Model):
    codigo = models.AutoField(db_column='Codigo', primary_key=True)  # Field name made lowercase.
    codant = models.IntegerField(blank=True, null=True)
    tipo = models.IntegerField(db_column='Tipo', blank=True, null=True)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=60, blank=True, null=True)  # Field name made lowercase.
    apelido = models.CharField(db_column='Apelido', max_length=60, blank=True, null=True)  # Field name made lowercase.
    orgao = models.CharField(db_column='Orgao', max_length=5, blank=True, null=True)  # Field name made lowercase.
    caixapostal = models.CharField(db_column='CaixaPostal', max_length=5, blank=True, null=True)  # Field name made lowercase.
    nascimento = models.DateField(db_column='Nascimento', blank=True, null=True)  # Field name made lowercase.
    endereco = models.CharField(db_column='Endereco', max_length=60, blank=True, null=True)  # Field name made lowercase.
    end = models.CharField(db_column='End', max_length=60, blank=True, null=True)  # Field name made lowercase.
    numero = models.CharField(max_length=15, blank=True, null=True)
    bairro = models.CharField(db_column='Bairro', max_length=60, blank=True, null=True)  # Field name made lowercase.
    cep = models.CharField(db_column='Cep', max_length=9, blank=True, null=True)  # Field name made lowercase.
    cidade = models.CharField(db_column='Cidade', max_length=30, blank=True, null=True)  # Field name made lowercase.
    uf = models.CharField(db_column='UF', max_length=2, blank=True, null=True)  # Field name made lowercase.
    codigocidade = models.CharField(db_column='CodigoCidade', max_length=7, blank=True, null=True)  # Field name made lowercase.
    codigoestado = models.CharField(db_column='CodigoEstado', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cpf = models.CharField(db_column='CPF', max_length=20, blank=True, null=True)  # Field name made lowercase.
    rg = models.CharField(db_column='RG', max_length=20, blank=True, null=True)  # Field name made lowercase.
    estadocivil = models.IntegerField(db_column='EstadoCivil', blank=True, null=True)  # Field name made lowercase.
    fone1 = models.CharField(db_column='Fone1', max_length=14, blank=True, null=True)  # Field name made lowercase.
    ramal1 = models.IntegerField(db_column='Ramal1', blank=True, null=True)  # Field name made lowercase.
    contato1 = models.CharField(db_column='Contato1', max_length=60, blank=True, null=True)  # Field name made lowercase.
    fone2 = models.CharField(db_column='Fone2', max_length=14, blank=True, null=True)  # Field name made lowercase.
    ramal2 = models.IntegerField(db_column='Ramal2', blank=True, null=True)  # Field name made lowercase.
    contato2 = models.CharField(db_column='Contato2', max_length=60, blank=True, null=True)  # Field name made lowercase.
    fone3 = models.CharField(db_column='Fone3', max_length=14, blank=True, null=True)  # Field name made lowercase.
    ramal3 = models.IntegerField(db_column='Ramal3', blank=True, null=True)  # Field name made lowercase.
    contato3 = models.CharField(db_column='Contato3', max_length=60, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=100, blank=True, null=True)  # Field name made lowercase.
    email2 = models.CharField(db_column='Email2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    home = models.CharField(db_column='Home', max_length=100, blank=True, null=True)  # Field name made lowercase.
    enddep = models.CharField(db_column='EndDep', max_length=60, blank=True, null=True)  # Field name made lowercase.
    bairrodep = models.CharField(db_column='BairroDep', max_length=60, blank=True, null=True)  # Field name made lowercase.
    cepdep = models.CharField(db_column='CepDep', max_length=9, blank=True, null=True)  # Field name made lowercase.
    caixadep = models.CharField(db_column='CaixaDep', max_length=5, blank=True, null=True)  # Field name made lowercase.
    fonedep1 = models.CharField(db_column='FoneDep1', max_length=14, blank=True, null=True)  # Field name made lowercase.
    ramaldep1 = models.IntegerField(db_column='RamalDep1', blank=True, null=True)  # Field name made lowercase.
    contatodep1 = models.CharField(db_column='ContatoDep1', max_length=60, blank=True, null=True)  # Field name made lowercase.
    fonedep2 = models.CharField(db_column='FoneDep2', max_length=14, blank=True, null=True)  # Field name made lowercase.
    ramaldep2 = models.IntegerField(db_column='RamalDep2', blank=True, null=True)  # Field name made lowercase.
    contatodep2 = models.CharField(db_column='ContatoDep2', max_length=60, blank=True, null=True)  # Field name made lowercase.
    fonedep3 = models.CharField(db_column='FoneDep3', max_length=14, blank=True, null=True)  # Field name made lowercase.
    ramaldep3 = models.IntegerField(db_column='RamalDep3', blank=True, null=True)  # Field name made lowercase.
    contatodep3 = models.CharField(db_column='ContatoDep3', max_length=60, blank=True, null=True)  # Field name made lowercase.
    observacao = models.TextField(db_column='Observacao', blank=True, null=True)  # Field name made lowercase.
    cadastro = models.DateField(db_column='Cadastro', blank=True, null=True)  # Field name made lowercase.
    repr = models.CharField(db_column='Repr', max_length=60, blank=True, null=True)  # Field name made lowercase.
    empresa = models.IntegerField(db_column='Empresa', blank=True, null=True)  # Field name made lowercase.
    cargo = models.IntegerField(db_column='Cargo', blank=True, null=True)  # Field name made lowercase.
    dataadmissao = models.DateField(db_column='DataAdmissao', blank=True, null=True)  # Field name made lowercase.
    datademissao = models.DateField(db_column='DataDemissao', blank=True, null=True)  # Field name made lowercase.
    equipe = models.IntegerField(db_column='Equipe', blank=True, null=True)  # Field name made lowercase.
    dataaso = models.DateField(db_column='DataASO', blank=True, null=True)  # Field name made lowercase.
    dataintegracao = models.DateField(db_column='DataIntegracao', blank=True, null=True)  # Field name made lowercase.
    datanr10 = models.DateField(db_column='DataNR10', blank=True, null=True)  # Field name made lowercase.
    datanr33 = models.DateField(db_column='DataNR33', blank=True, null=True)  # Field name made lowercase.
    datanr35 = models.DateField(db_column='DataNR35', blank=True, null=True)  # Field name made lowercase.
    banco = models.IntegerField(db_column='Banco', blank=True, null=True)  # Field name made lowercase.
    agencia = models.CharField(db_column='Agencia', max_length=15, blank=True, null=True)  # Field name made lowercase.
    conta = models.CharField(db_column='Conta', max_length=30, blank=True, null=True)  # Field name made lowercase.
    numerobota = models.CharField(db_column='NumeroBota', max_length=20, blank=True, null=True)  # Field name made lowercase.
    numerocalca = models.CharField(db_column='NumeroCalca', max_length=20, blank=True, null=True)  # Field name made lowercase.
    numerocamisa = models.CharField(db_column='NumeroCamisa', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'fornecedores'


class FreteConta(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    conta = models.CharField(db_column='CONTA', max_length=60, blank=True, null=True)  # Field name made lowercase.
    tipo = models.CharField(db_column='TIPO', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'frete_conta'


class FreteContaTipo(models.Model):
    id = models.CharField(primary_key=True, max_length=1)
    tipo = models.CharField(db_column='Tipo', max_length=7, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'frete_conta_tipo'


class FreteLancamento(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    data = models.DateField(db_column='Data', blank=True, null=True)  # Field name made lowercase.
    id_veiculo = models.IntegerField(db_column='ID_Veiculo', blank=True, null=True)  # Field name made lowercase.
    id_conta = models.IntegerField(db_column='ID_Conta', blank=True, null=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=60, blank=True, null=True)  # Field name made lowercase.
    tipo = models.CharField(db_column='Tipo', max_length=1, blank=True, null=True)  # Field name made lowercase.
    valor = models.FloatField(db_column='Valor', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'frete_lancamento'


class FreteVeiculo(models.Model):
    veiculo = models.CharField(db_column='Veiculo', max_length=30, blank=True, null=True)  # Field name made lowercase.
    placa = models.CharField(db_column='Placa', max_length=8, blank=True, null=True)  # Field name made lowercase.
    ano = models.CharField(db_column='Ano', max_length=9, blank=True, null=True)  # Field name made lowercase.
    cor = models.CharField(db_column='Cor', max_length=30, blank=True, null=True)  # Field name made lowercase.
    chassi = models.CharField(db_column='Chassi', max_length=30, blank=True, null=True)  # Field name made lowercase.
    renavan = models.CharField(db_column='Renavan', max_length=30, blank=True, null=True)  # Field name made lowercase.
    kmcompra = models.IntegerField(db_column='KmCompra', blank=True, null=True)  # Field name made lowercase.
    kmvenda = models.IntegerField(db_column='KmVenda', blank=True, null=True)  # Field name made lowercase.
    datacompra = models.DateField(db_column='DataCompra', blank=True, null=True)  # Field name made lowercase.
    datavenda = models.DateField(db_column='DataVenda', blank=True, null=True)  # Field name made lowercase.
    observacao = models.TextField(db_column='Observacao', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'frete_veiculo'


class Funcionarios(models.Model):
    codigo = models.AutoField(db_column='Codigo', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=60, blank=True, null=True)  # Field name made lowercase.
    ramal = models.CharField(db_column='Ramal', max_length=5, blank=True, null=True)  # Field name made lowercase.
    funcao = models.CharField(db_column='Funcao', max_length=30, blank=True, null=True)  # Field name made lowercase.
    cadastro = models.DateField(db_column='Cadastro', blank=True, null=True)  # Field name made lowercase.
    ativo = models.IntegerField(db_column='Ativo', blank=True, null=True)  # Field name made lowercase.
    empresa = models.IntegerField(db_column='Empresa', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'funcionarios'


class Garantia(models.Model):
    codigo = models.AutoField(primary_key=True)
    cliente = models.IntegerField(blank=True, null=True)
    vendedor = models.IntegerField(blank=True, null=True)
    val_entrada = models.FloatField(blank=True, null=True)
    val_saida = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    data = models.DateField(blank=True, null=True)
    hora = models.TimeField(blank=True, null=True)
    observacao = models.CharField(max_length=30, blank=True, null=True)
    transportadora = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'garantia'


class Garantias(models.Model):
    codigo = models.AutoField(db_column='Codigo', primary_key=True)  # Field name made lowercase.
    produto = models.CharField(db_column='Produto', max_length=30, blank=True, null=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=100, blank=True, null=True)  # Field name made lowercase.
    quantidade = models.FloatField(db_column='Quantidade', blank=True, null=True)  # Field name made lowercase.
    cliente = models.IntegerField(db_column='Cliente', blank=True, null=True)  # Field name made lowercase.
    grupo = models.IntegerField(db_column='Grupo', blank=True, null=True)  # Field name made lowercase.
    documento = models.IntegerField(db_column='Documento', blank=True, null=True)  # Field name made lowercase.
    datavenda = models.DateField(db_column='DataVenda', blank=True, null=True)  # Field name made lowercase.
    os = models.IntegerField(db_column='OS', blank=True, null=True)  # Field name made lowercase.
    certificado = models.IntegerField(db_column='Certificado', blank=True, null=True)  # Field name made lowercase.
    datagarantia = models.DateField(db_column='DataGarantia', blank=True, null=True)  # Field name made lowercase.
    defeito = models.CharField(db_column='Defeito', max_length=100, blank=True, null=True)  # Field name made lowercase.
    fornecedor = models.IntegerField(db_column='Fornecedor', blank=True, null=True)  # Field name made lowercase.
    nfcompra = models.IntegerField(db_column='NFCompra', blank=True, null=True)  # Field name made lowercase.
    datacompra = models.DateField(db_column='DataCompra', blank=True, null=True)  # Field name made lowercase.
    custocompra = models.FloatField(db_column='CustoCompra', blank=True, null=True)  # Field name made lowercase.
    cfop = models.CharField(db_column='CFOP', max_length=5, blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    fornenvio = models.IntegerField(db_column='FornEnvio', blank=True, null=True)  # Field name made lowercase.
    nfenvio = models.IntegerField(db_column='NFEnvio', blank=True, null=True)  # Field name made lowercase.
    dataenvio = models.DateField(db_column='DataEnvio', blank=True, null=True)  # Field name made lowercase.
    custoenvio = models.FloatField(db_column='CustoEnvio', blank=True, null=True)  # Field name made lowercase.
    cfopenvio = models.CharField(db_column='CFOPEnvio', max_length=5, blank=True, null=True)  # Field name made lowercase.
    fornrece = models.IntegerField(db_column='FornRece', blank=True, null=True)  # Field name made lowercase.
    nfrece = models.IntegerField(db_column='NFRece', blank=True, null=True)  # Field name made lowercase.
    datarece = models.DateField(db_column='DataRece', blank=True, null=True)  # Field name made lowercase.
    custorece = models.FloatField(db_column='CustoRece', blank=True, null=True)  # Field name made lowercase.
    cfoprece = models.CharField(db_column='CFOPRece', max_length=5, blank=True, null=True)  # Field name made lowercase.
    obsrece = models.CharField(db_column='ObsRece', max_length=150, blank=True, null=True)  # Field name made lowercase.
    empresa = models.IntegerField(db_column='Empresa', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'garantias'


class Grupos(models.Model):
    codigo = models.AutoField(db_column='Codigo', primary_key=True)  # Field name made lowercase.
    codant = models.IntegerField(blank=True, null=True)
    grupo = models.CharField(db_column='Grupo', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cadastro = models.DateField(db_column='Cadastro', blank=True, null=True)  # Field name made lowercase.
    empresa = models.IntegerField(db_column='Empresa', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'grupos'


class HistoricoOs(models.Model):
    data = models.DateField(blank=True, null=True)
    hora = models.TimeField(blank=True, null=True)
    codigo_a = models.CharField(max_length=30, blank=True, null=True)
    descricao_a = models.CharField(max_length=80, blank=True, null=True)
    quantidade_a = models.FloatField(blank=True, null=True)
    unitario_a = models.FloatField(blank=True, null=True)
    total_a = models.FloatField(blank=True, null=True)
    func_a = models.IntegerField(blank=True, null=True)
    usuario_a = models.IntegerField(blank=True, null=True)
    codigo_p = models.CharField(max_length=30, blank=True, null=True)
    descricao_p = models.CharField(max_length=80, blank=True, null=True)
    quantidade_p = models.FloatField(blank=True, null=True)
    unitario_p = models.FloatField(blank=True, null=True)
    total_p = models.FloatField(blank=True, null=True)
    func_p = models.IntegerField(blank=True, null=True)
    usuario_p = models.IntegerField(blank=True, null=True)
    os = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'historico_os'


class Indice(models.Model):
    tab1 = models.FloatField(blank=True, null=True)
    tab2 = models.FloatField(blank=True, null=True)
    tab3 = models.FloatField(blank=True, null=True)
    tab4 = models.FloatField(blank=True, null=True)
    tab5 = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'indice'


class Integracao(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    data = models.DateField(db_column='Data', blank=True, null=True)  # Field name made lowercase.
    hora = models.TimeField(db_column='Hora', blank=True, null=True)  # Field name made lowercase.
    usuario = models.IntegerField(db_column='Usuario', blank=True, null=True)  # Field name made lowercase.
    maquina = models.CharField(db_column='Maquina', max_length=200, blank=True, null=True)  # Field name made lowercase.
    tabela = models.CharField(db_column='Tabela', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tipo = models.CharField(db_column='Tipo', max_length=9, blank=True, null=True)  # Field name made lowercase.
    textosql = models.TextField(db_column='TextoSQL', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'integracao'


class IntegracaoCliente(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    data = models.DateField(db_column='Data', blank=True, null=True)  # Field name made lowercase.
    hora = models.TimeField(db_column='Hora', blank=True, null=True)  # Field name made lowercase.
    controle = models.PositiveIntegerField(db_column='Controle', blank=True, null=True)  # Field name made lowercase.
    tipo = models.CharField(db_column='Tipo', max_length=9, blank=True, null=True)  # Field name made lowercase.
    textosql = models.TextField(db_column='TextoSQL', blank=True, null=True)  # Field name made lowercase.
    atualizacaook = models.IntegerField(db_column='AtualizacaoOK', blank=True, null=True)  # Field name made lowercase.
    msgerro = models.TextField(db_column='MsgErro', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'integracao_cliente'


class IntegracaoParametros(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    ultimocontrole = models.PositiveIntegerField(db_column='UltimoControle', blank=True, null=True)  # Field name made lowercase.
    dataatualizacao = models.DateField(db_column='DataAtualizacao', blank=True, null=True)  # Field name made lowercase.
    horaatualizacao = models.TimeField(db_column='HoraAtualizacao', blank=True, null=True)  # Field name made lowercase.
    replicardados = models.IntegerField(db_column='ReplicarDados', blank=True, null=True)  # Field name made lowercase.
    clienteintegracao = models.IntegerField(db_column='ClienteIntegracao', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'integracao_parametros'


class IntegracaoServidor(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    empresa = models.CharField(db_column='Empresa', max_length=50, blank=True, null=True)  # Field name made lowercase.
    baseurl = models.CharField(db_column='BaseURL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    baseurlexterna = models.CharField(db_column='BaseURLExterna', max_length=100, blank=True, null=True)  # Field name made lowercase.
    porta = models.IntegerField(db_column='Porta', blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'integracao_servidor'


class Kardex(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    numero = models.IntegerField(db_column='Numero', blank=True, null=True)  # Field name made lowercase.
    cfop = models.CharField(db_column='CFOP', max_length=5, blank=True, null=True)  # Field name made lowercase.
    serie = models.CharField(db_column='Serie', max_length=2, blank=True, null=True)  # Field name made lowercase.
    data = models.DateField(db_column='Data', blank=True, null=True)  # Field name made lowercase.
    hora = models.TimeField(db_column='Hora', blank=True, null=True)  # Field name made lowercase.
    entrada = models.FloatField(db_column='Entrada', blank=True, null=True)  # Field name made lowercase.
    saida = models.FloatField(db_column='Saida', blank=True, null=True)  # Field name made lowercase.
    valor = models.FloatField(db_column='Valor', blank=True, null=True)  # Field name made lowercase.
    valor_final = models.FloatField(db_column='Valor_final', blank=True, null=True)  # Field name made lowercase.
    clifor = models.IntegerField(db_column='CliFor', blank=True, null=True)  # Field name made lowercase.
    observacao = models.CharField(db_column='Observacao', max_length=100, blank=True, null=True)  # Field name made lowercase.
    produto = models.CharField(db_column='Produto', max_length=30, blank=True, null=True)  # Field name made lowercase.
    estoque = models.FloatField(db_column='Estoque', blank=True, null=True)  # Field name made lowercase.
    estoque_1 = models.FloatField(db_column='Estoque_1', blank=True, null=True)  # Field name made lowercase.
    quen = models.IntegerField(db_column='Quen', blank=True, null=True)  # Field name made lowercase.
    tipo = models.IntegerField(db_column='Tipo', blank=True, null=True)  # Field name made lowercase.
    usuario = models.IntegerField(db_column='Usuario', blank=True, null=True)  # Field name made lowercase.
    maquina = models.CharField(db_column='Maquina', max_length=100, blank=True, null=True)  # Field name made lowercase.
    grupo = models.IntegerField(db_column='Grupo', blank=True, null=True)  # Field name made lowercase.
    grupodesc = models.CharField(db_column='GrupoDesc', max_length=60, blank=True, null=True)  # Field name made lowercase.
    linha = models.IntegerField(db_column='Linha', blank=True, null=True)  # Field name made lowercase.
    linhadesc = models.CharField(db_column='LinhaDesc', max_length=60, blank=True, null=True)  # Field name made lowercase.
    fabricante = models.IntegerField(db_column='Fabricante', blank=True, null=True)  # Field name made lowercase.
    fabricantedesc = models.CharField(db_column='FabricanteDesc', max_length=60, blank=True, null=True)  # Field name made lowercase.
    empresa = models.IntegerField(db_column='Empresa', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'kardex'


class KardexLote(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    numero = models.IntegerField(db_column='Numero', blank=True, null=True)  # Field name made lowercase.
    data = models.DateField(db_column='Data', blank=True, null=True)  # Field name made lowercase.
    hora = models.TimeField(db_column='Hora', blank=True, null=True)  # Field name made lowercase.
    produto = models.CharField(db_column='Produto', max_length=30, blank=True, null=True)  # Field name made lowercase.
    idlote = models.IntegerField(db_column='IdLote', blank=True, null=True)  # Field name made lowercase.
    nomelote = models.CharField(db_column='NomeLote', max_length=30, blank=True, null=True)  # Field name made lowercase.
    entrada = models.FloatField(db_column='Entrada', blank=True, null=True)  # Field name made lowercase.
    saida = models.FloatField(db_column='Saida', blank=True, null=True)  # Field name made lowercase.
    estoque = models.FloatField(db_column='Estoque', blank=True, null=True)  # Field name made lowercase.
    usuario = models.IntegerField(db_column='Usuario', blank=True, null=True)  # Field name made lowercase.
    funcionario = models.IntegerField(db_column='Funcionario', blank=True, null=True)  # Field name made lowercase.
    observacao = models.CharField(db_column='Observacao', max_length=100, blank=True, null=True)  # Field name made lowercase.
    maquina = models.CharField(db_column='Maquina', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'kardex_lote'


class LancamentosCaixa(models.Model):
    documento = models.IntegerField(blank=True, null=True)
    nome = models.CharField(max_length=60, blank=True, null=True)
    tipo = models.CharField(max_length=7, blank=True, null=True)
    valor = models.FloatField(blank=True, null=True)
    saldo = models.FloatField(blank=True, null=True)
    historico = models.CharField(max_length=80, blank=True, null=True)
    pago_com = models.CharField(max_length=10, blank=True, null=True)
    data_lancamento = models.DateField(blank=True, null=True)
    funcionario = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lancamentos_caixa'


class LancamentosCaixaDetalhes(models.Model):
    id_caixa = models.IntegerField(blank=True, null=True)
    titulo = models.IntegerField(blank=True, null=True)
    parcela = models.IntegerField(blank=True, null=True)
    vencimento = models.DateField(blank=True, null=True)
    valor = models.FloatField(blank=True, null=True)
    descacre = models.FloatField(blank=True, null=True)
    valorpago = models.FloatField(blank=True, null=True)
    fornecedor = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lancamentos_caixa_detalhes'


class Linhas(models.Model):
    codigo = models.AutoField(db_column='Codigo', primary_key=True)  # Field name made lowercase.
    codant = models.IntegerField(blank=True, null=True)
    grupo = models.IntegerField(db_column='Grupo', blank=True, null=True)  # Field name made lowercase.
    grupodesc = models.CharField(db_column='GrupoDesc', max_length=60, blank=True, null=True)  # Field name made lowercase.
    linha = models.CharField(db_column='Linha', max_length=60, blank=True, null=True)  # Field name made lowercase.
    margem = models.FloatField(db_column='Margem', blank=True, null=True)  # Field name made lowercase.
    comissao = models.FloatField(db_column='Comissao', blank=True, null=True)  # Field name made lowercase.
    promocao = models.FloatField(db_column='Promocao', blank=True, null=True)  # Field name made lowercase.
    descontotabelacliente = models.IntegerField(db_column='DescontoTabelaCliente', blank=True, null=True, db_comment='0-false 1-true')  # Field name made lowercase.
    sequencia = models.IntegerField(blank=True, null=True)
    lista = models.IntegerField(db_column='Lista', blank=True, null=True)  # Field name made lowercase.
    cadastro = models.DateField(db_column='Cadastro', blank=True, null=True)  # Field name made lowercase.
    pontos_cartao = models.FloatField(blank=True, null=True)
    mensagemvenda = models.CharField(db_column='MensagemVenda', max_length=250, blank=True, null=True)  # Field name made lowercase.
    empresa = models.IntegerField(db_column='Empresa', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'linhas'


class Locacao(models.Model):
    codigo = models.AutoField(primary_key=True)
    data_locacao = models.DateField(blank=True, null=True)
    data_entrega = models.DateField(blank=True, null=True)
    data_fechamento = models.DateField(blank=True, null=True)
    hora_locacao = models.TimeField(blank=True, null=True)
    hora_entrega = models.TimeField(blank=True, null=True)
    hora_fechamento = models.TimeField(blank=True, null=True)
    dias_locacao = models.IntegerField(blank=True, null=True)
    valor_locacao = models.FloatField(blank=True, null=True)
    valor_diario = models.FloatField(blank=True, null=True)
    dias_atraso = models.IntegerField(blank=True, null=True)
    multa_dia_atraso = models.FloatField(blank=True, null=True)
    valor_locacao_final = models.FloatField(blank=True, null=True)
    descacre = models.FloatField(blank=True, null=True)
    total_geral = models.FloatField(blank=True, null=True)
    cliente = models.IntegerField(blank=True, null=True)
    funcionario = models.IntegerField(blank=True, null=True)
    portador = models.CharField(max_length=50, blank=True, null=True)
    observacao = models.CharField(max_length=200, blank=True, null=True)
    situacao = models.IntegerField(blank=True, null=True)
    condicao = models.IntegerField(blank=True, null=True)
    nota = models.IntegerField(blank=True, null=True)
    renovacao = models.IntegerField(blank=True, null=True)
    fatura = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'locacao'


class LocacaoDetalhes(models.Model):
    id_locacao = models.IntegerField(blank=True, null=True)
    data = models.DateField(blank=True, null=True)
    codigo = models.IntegerField(blank=True, null=True)
    equipamento = models.CharField(max_length=50, blank=True, null=True)
    modelo = models.CharField(max_length=50, blank=True, null=True)
    marca = models.CharField(max_length=50, blank=True, null=True)
    numero_serie = models.CharField(max_length=50, blank=True, null=True)
    quantidade = models.FloatField(blank=True, null=True)
    unitario = models.FloatField(blank=True, null=True)
    valor = models.FloatField(blank=True, null=True)
    unitario_final = models.FloatField(blank=True, null=True)
    valor_final = models.FloatField(blank=True, null=True)
    dias_locacao = models.IntegerField(blank=True, null=True)
    valor_dia_locacao = models.FloatField(blank=True, null=True)
    nota = models.IntegerField(blank=True, null=True)
    nota_old = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'locacao_detalhes'


class LocacaoFatura(models.Model):
    codigo = models.IntegerField(blank=True, null=True)
    cliente = models.IntegerField(blank=True, null=True)
    emissao = models.DateField(blank=True, null=True)
    valor = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'locacao_fatura'


class Logomarcas(models.Model):
    logo2x8 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'logomarcas'


class Maquinas(models.Model):
    maquina = models.CharField(max_length=30, blank=True, null=True)
    impr_sep = models.CharField(max_length=1, blank=True, null=True)
    impr_venda_impressora_sep = models.IntegerField(blank=True, null=True)
    papel_sep = models.CharField(max_length=6, blank=True, null=True)
    porta_sep = models.CharField(max_length=10, blank=True, null=True)
    sobe_papel_sep = models.IntegerField(blank=True, null=True)
    impressora_sep = models.IntegerField(blank=True, null=True)
    impressora_req = models.IntegerField(blank=True, null=True)
    impressora_expedicao = models.IntegerField(blank=True, null=True)
    imprimir_codigo_produto = models.IntegerField(blank=True, null=True, db_comment='0-false 1-true')
    saida = models.IntegerField(blank=True, null=True)
    vias = models.IntegerField(blank=True, null=True)
    impressora_fecha = models.IntegerField(blank=True, null=True)
    imprimir_codigo_prod_fechamento = models.IntegerField(blank=True, null=True)
    fechamento = models.CharField(max_length=6, blank=True, null=True)
    porta = models.CharField(max_length=10, blank=True, null=True)
    imprimi_recibo = models.CharField(max_length=3, blank=True, null=True)
    tipo_papel = models.CharField(max_length=6, blank=True, null=True)
    sobe_papel = models.IntegerField(blank=True, null=True)
    entrega = models.CharField(max_length=6, blank=True, null=True)
    impr_lanc_caixa = models.CharField(max_length=3, blank=True, null=True)
    skin = models.CharField(max_length=200, blank=True, null=True)
    mudar_cor_foco = models.IntegerField(blank=True, null=True)
    formulario_razao = models.IntegerField(blank=True, null=True)
    fonte_carne = models.IntegerField(blank=True, null=True)
    usartabeladescontocliente = models.IntegerField(db_column='UsarTabelaDescontoCliente', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'maquinas'


class Mecanicos(models.Model):
    codigo = models.AutoField(primary_key=True)
    empresa = models.CharField(max_length=60, blank=True, null=True)
    observacao = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mecanicos'


class MeioPagamento(models.Model):
    codigo = models.CharField(db_column='Codigo', primary_key=True, max_length=2)  # Field name made lowercase.
    meiopagamento = models.CharField(db_column='MeioPagamento', max_length=25, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'meio_pagamento'


class MensagemVenda(models.Model):
    mensagem = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mensagem_venda'


class Ncm(models.Model):
    ncm = models.CharField(primary_key=True, max_length=8)
    descricao = models.CharField(max_length=255, blank=True, null=True)
    inicio = models.DateField(db_column='Inicio', blank=True, null=True)  # Field name made lowercase.
    fim = models.DateField(db_column='Fim', blank=True, null=True)  # Field name made lowercase.
    untrib = models.CharField(db_column='UnTrib', max_length=15, blank=True, null=True)  # Field name made lowercase.
    descuntrib = models.CharField(db_column='DescUnTrib', max_length=25, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ncm'


class NcmTributacao(models.Model):
    ncm = models.CharField(primary_key=True, max_length=8)
    cst_icms_tributacao = models.CharField(max_length=2, blank=True, null=True)
    reducao_base_calculo_icms_interestadual = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ncm_tributacao'


class Ncms(models.Model):
    ncms = models.CharField(max_length=8, blank=True, null=True)
    descricao = models.CharField(max_length=255, blank=True, null=True)
    setor = models.IntegerField(blank=True, null=True, db_comment='1-Auto Pecas 2-Supermercado')
    cst_icms = models.CharField(max_length=3, blank=True, null=True)
    cst_ipi = models.CharField(max_length=2, blank=True, null=True)
    cst_pis = models.CharField(max_length=2, blank=True, null=True)
    cst_cofins = models.CharField(max_length=2, blank=True, null=True)
    iva = models.FloatField(blank=True, null=True)
    icms = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ncms'


class NfeCce(models.Model):
    numeronota = models.IntegerField(db_column='Numeronota', blank=True, null=True)  # Field name made lowercase.
    correcao = models.TextField(db_column='Correcao', blank=True, null=True)  # Field name made lowercase.
    protocolo = models.CharField(db_column='Protocolo', max_length=100, blank=True, null=True)  # Field name made lowercase.
    xml = models.TextField(db_column='XML', blank=True, null=True)  # Field name made lowercase.
    cstat = models.CharField(db_column='cStat', max_length=5, blank=True, null=True)  # Field name made lowercase.
    evento = models.IntegerField(db_column='Evento', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'nfe_cce'


class NfeCodigoCidadeIbge(models.Model):
    iduf = models.IntegerField(blank=True, null=True)
    nome = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nfe_codigo_cidade_ibge'


class NfeCodigoEstadoIbge(models.Model):
    codigo = models.AutoField(primary_key=True)
    sigla = models.CharField(max_length=2, blank=True, null=True)
    nome = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nfe_codigo_estado_ibge'


class NfeDestinada(models.Model):
    idnf_dest = models.AutoField(db_column='IdNF_Dest', primary_key=True)  # Field name made lowercase.
    codigo_nota = models.IntegerField(db_column='Codigo_NOTA', blank=True, null=True)  # Field name made lowercase.
    nome_razaosocial = models.CharField(db_column='Nome_RazaoSocial', max_length=500, blank=True, null=True)  # Field name made lowercase.
    status_nfe = models.CharField(db_column='Status_NFe', max_length=100, blank=True, null=True)  # Field name made lowercase.
    chave_nfe = models.CharField(db_column='Chave_NFe', max_length=255, blank=True, null=True)  # Field name made lowercase.
    data_emissao = models.DateField(db_column='Data_Emissao', blank=True, null=True)  # Field name made lowercase.
    xml = models.TextField(db_column='XML', blank=True, null=True)  # Field name made lowercase.
    valor = models.DecimalField(db_column='Valor', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ja_manifestada = models.CharField(db_column='Ja_Manifestada', max_length=150, blank=True, null=True)  # Field name made lowercase.
    ja_baixada = models.CharField(db_column='Ja_Baixada', max_length=100, blank=True, null=True)  # Field name made lowercase.
    situacao = models.CharField(db_column='Situacao', max_length=12, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'nfe_destinada'


class NfeDocReferenciado(models.Model):
    numeronota = models.IntegerField(db_column='NumeroNota', blank=True, null=True)  # Field name made lowercase.
    serie = models.IntegerField(db_column='Serie', blank=True, null=True)  # Field name made lowercase.
    modelonf = models.IntegerField(db_column='ModeloNF', blank=True, null=True)  # Field name made lowercase.
    chave = models.CharField(db_column='Chave', max_length=44, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'nfe_doc_referenciado'


class NfeEcfReferenciado(models.Model):
    numeronota = models.IntegerField(db_column='NumeroNota', blank=True, null=True)  # Field name made lowercase.
    serie = models.IntegerField(db_column='Serie', blank=True, null=True)  # Field name made lowercase.
    modelonf = models.IntegerField(db_column='ModeloNF', blank=True, null=True)  # Field name made lowercase.
    necf = models.IntegerField(db_column='nECF', blank=True, null=True)  # Field name made lowercase.
    ncoo = models.IntegerField(db_column='nCOO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'nfe_ecf_referenciado'


class NfeEnderecoEntrega(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    numeronota = models.IntegerField(db_column='NumeroNota', blank=True, null=True)  # Field name made lowercase.
    serie = models.IntegerField(db_column='Serie', blank=True, null=True)  # Field name made lowercase.
    modelo = models.IntegerField(db_column='Modelo', blank=True, null=True)  # Field name made lowercase.
    cnpjcpf = models.CharField(db_column='CNPJCPF', max_length=14, blank=True, null=True)  # Field name made lowercase.
    ie = models.CharField(db_column='IE', max_length=14, blank=True, null=True)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=60, blank=True, null=True)  # Field name made lowercase.
    endereco = models.CharField(db_column='Endereco', max_length=60, blank=True, null=True)  # Field name made lowercase.
    numero = models.CharField(db_column='Numero', max_length=30, blank=True, null=True)  # Field name made lowercase.
    complemento = models.CharField(db_column='Complemento', max_length=30, blank=True, null=True)  # Field name made lowercase.
    bairro = models.CharField(db_column='Bairro', max_length=30, blank=True, null=True)  # Field name made lowercase.
    codigocidadeibge = models.IntegerField(db_column='CodigoCidadeIBGE', blank=True, null=True)  # Field name made lowercase.
    cidade = models.CharField(db_column='Cidade', max_length=60, blank=True, null=True)  # Field name made lowercase.
    uf = models.CharField(db_column='UF', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cep = models.CharField(db_column='CEP', max_length=9, blank=True, null=True)  # Field name made lowercase.
    fone = models.CharField(db_column='Fone', max_length=14, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=60, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'nfe_endereco_entrega'


class NfeEnvioLote(models.Model):
    situacao = models.IntegerField(db_column='Situacao', blank=True, null=True)  # Field name made lowercase.
    lote = models.IntegerField(db_column='Lote', blank=True, null=True)  # Field name made lowercase.
    data = models.DateTimeField(db_column='Data', blank=True, null=True)  # Field name made lowercase.
    recibolote = models.CharField(db_column='ReciboLote', max_length=30, blank=True, null=True)  # Field name made lowercase.
    protocolo = models.CharField(db_column='Protocolo', max_length=30, blank=True, null=True)  # Field name made lowercase.
    cstat = models.IntegerField(db_column='cStat', blank=True, null=True)  # Field name made lowercase.
    xmotivo = models.CharField(db_column='xMotivo', max_length=100, blank=True, null=True)  # Field name made lowercase.
    nfe = models.IntegerField(db_column='NFe', blank=True, null=True)  # Field name made lowercase.
    chavenfe = models.CharField(db_column='ChaveNFe', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xml = models.TextField(db_column='XML', blank=True, null=True)  # Field name made lowercase.
    acbr_msg = models.TextField(db_column='ACBR_msg', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'nfe_envio_lote'


class NfeFatura(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    numeronota = models.IntegerField(db_column='NumeroNota', blank=True, null=True)  # Field name made lowercase.
    serie = models.IntegerField(db_column='Serie', blank=True, null=True)  # Field name made lowercase.
    modelonf = models.IntegerField(db_column='ModeloNF', blank=True, null=True)  # Field name made lowercase.
    codigo = models.IntegerField(db_column='Codigo', blank=True, null=True)  # Field name made lowercase.
    parcela = models.IntegerField(db_column='Parcela', blank=True, null=True)  # Field name made lowercase.
    vencimento = models.DateField(db_column='Vencimento', blank=True, null=True)  # Field name made lowercase.
    valor = models.FloatField(db_column='Valor', blank=True, null=True)  # Field name made lowercase.
    valordiferenca = models.FloatField(db_column='ValorDiferenca', blank=True, null=True)  # Field name made lowercase.
    codigomp = models.CharField(db_column='CodigoMP', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cnpjcredcartao = models.CharField(db_column='CNPJCredCartao', max_length=14, blank=True, null=True)  # Field name made lowercase.
    bandeiracartao = models.CharField(db_column='BandeiraCartao', max_length=2, blank=True, null=True)  # Field name made lowercase.
    autorizacaocartao = models.CharField(db_column='AutorizacaoCartao', max_length=20, blank=True, null=True)  # Field name made lowercase.
    indpag = models.CharField(db_column='IndPag', max_length=2, blank=True, null=True, db_comment='0=A Vista 1= A Prazo')  # Field name made lowercase.
    descricaooutrosmeios = models.CharField(db_column='DescricaoOutrosMeios', max_length=60, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'nfe_fatura'


class NfeIntermediador(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=60, blank=True, null=True)  # Field name made lowercase.
    cnpj = models.CharField(db_column='CNPJ', max_length=18, blank=True, null=True)  # Field name made lowercase.
    identificacao = models.CharField(db_column='Identificacao', max_length=60, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'nfe_intermediador'


class NfeNaturezaOperacao(models.Model):
    tipo = models.IntegerField(blank=True, null=True)
    venda = models.IntegerField(blank=True, null=True)
    naturezaoperacao = models.CharField(db_column='NaturezaOperacao', max_length=60, blank=True, null=True)  # Field name made lowercase.
    cfop = models.CharField(max_length=4, blank=True, null=True)
    mensagem = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nfe_natureza_operacao'


class NfeNotaFiscal(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    situacao = models.IntegerField(db_column='Situacao', blank=True, null=True)  # Field name made lowercase.
    email = models.IntegerField(db_column='Email', blank=True, null=True)  # Field name made lowercase.
    impresso = models.IntegerField(db_column='Impresso', blank=True, null=True)  # Field name made lowercase.
    venda = models.IntegerField(db_column='Venda', blank=True, null=True)  # Field name made lowercase.
    emissor = models.IntegerField(db_column='Emissor', blank=True, null=True)  # Field name made lowercase.
    recebimento = models.IntegerField(db_column='Recebimento', blank=True, null=True)  # Field name made lowercase.
    loteenvio = models.IntegerField(db_column='LoteEnvio', blank=True, null=True)  # Field name made lowercase.
    datahorarecebto = models.DateTimeField(db_column='DataHoraRecebto', blank=True, null=True)  # Field name made lowercase.
    protocolo = models.CharField(db_column='Protocolo', max_length=200, blank=True, null=True)  # Field name made lowercase.
    numerorecibo = models.CharField(db_column='NumeroRecibo', max_length=200, blank=True, null=True)  # Field name made lowercase.
    cstat = models.IntegerField(db_column='cStat', blank=True, null=True)  # Field name made lowercase.
    xmotivo = models.CharField(db_column='xMotivo', max_length=150, blank=True, null=True)  # Field name made lowercase.
    chaveacessonfe = models.CharField(db_column='ChaveAcessoNFe', max_length=200, blank=True, null=True)  # Field name made lowercase.
    datacancelamento = models.DateTimeField(db_column='DataCancelamento', blank=True, null=True)  # Field name made lowercase.
    protocolocancelamento = models.CharField(db_column='ProtocoloCancelamento', max_length=200, blank=True, null=True)  # Field name made lowercase.
    justificativacancelamento = models.CharField(db_column='JustificativaCancelamento', max_length=240, blank=True, null=True)  # Field name made lowercase.
    cstatcancelamento = models.CharField(db_column='cStatCancelamento', max_length=3, blank=True, null=True)  # Field name made lowercase.
    xmotivocancelamento = models.CharField(db_column='xMotivoCancelamento', max_length=200, blank=True, null=True)  # Field name made lowercase.
    datacartacorrecao = models.DateTimeField(db_column='DataCartaCorrecao', blank=True, null=True)  # Field name made lowercase.
    protocolocartacorrecao = models.CharField(db_column='ProtocoloCartaCorrecao', max_length=20, blank=True, null=True)  # Field name made lowercase.
    duplicata = models.IntegerField(db_column='Duplicata', blank=True, null=True)  # Field name made lowercase.
    modelonf = models.IntegerField(db_column='ModeloNF', blank=True, null=True)  # Field name made lowercase.
    serie = models.IntegerField(db_column='Serie', blank=True, null=True)  # Field name made lowercase.
    numeronota = models.IntegerField(db_column='NumeroNota', blank=True, null=True)  # Field name made lowercase.
    numeroaleatorio = models.CharField(db_column='NumeroAleatorio', max_length=10, blank=True, null=True)  # Field name made lowercase.
    id_natureza = models.IntegerField(db_column='ID_Natureza', blank=True, null=True)  # Field name made lowercase.
    natureza = models.CharField(db_column='Natureza', max_length=60, blank=True, null=True)  # Field name made lowercase.
    tipopagamento = models.IntegerField(db_column='TipoPagamento', blank=True, null=True)  # Field name made lowercase.
    emissao = models.DateField(db_column='Emissao', blank=True, null=True)  # Field name made lowercase.
    saida = models.DateField(db_column='Saida', blank=True, null=True)  # Field name made lowercase.
    horasaida = models.TimeField(db_column='HoraSaida', blank=True, null=True)  # Field name made lowercase.
    tiponf = models.IntegerField(db_column='TipoNF', blank=True, null=True)  # Field name made lowercase.
    tipoemissao = models.IntegerField(db_column='TipoEmissao', blank=True, null=True)  # Field name made lowercase.
    finalidadeemissao = models.IntegerField(db_column='FinalidadeEmissao', blank=True, null=True)  # Field name made lowercase.
    iddestinooperacao = models.IntegerField(db_column='IdDestinoOperacao', blank=True, null=True)  # Field name made lowercase.
    indconsumidorfinal = models.IntegerField(db_column='IndConsumidorFinal', blank=True, null=True)  # Field name made lowercase.
    indpresenca = models.IntegerField(db_column='IndPresenca', blank=True, null=True)  # Field name made lowercase.
    indicadorintermediario = models.IntegerField(db_column='IndicadorIntermediario', blank=True, null=True)  # Field name made lowercase.
    idintermediador = models.IntegerField(db_column='IdIntermediador', blank=True, null=True)  # Field name made lowercase.
    cnpjintermediador = models.CharField(db_column='CnpjIntermediador', max_length=18, blank=True, null=True)  # Field name made lowercase.
    identifnointermediador = models.CharField(db_column='IdentifNoIntermediador', max_length=60, blank=True, null=True)  # Field name made lowercase.
    indiedestinatario = models.IntegerField(db_column='indIEDestinatario', blank=True, null=True)  # Field name made lowercase.
    informaenderecoentrega = models.IntegerField(db_column='InformaEnderecoEntrega', blank=True, null=True, db_comment='Informar endereco de entrega')  # Field name made lowercase.
    clifor = models.IntegerField(db_column='CliFor', blank=True, null=True)  # Field name made lowercase.
    tipoclifor = models.IntegerField(db_column='TipoCliFor', blank=True, null=True)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=60, blank=True, null=True)  # Field name made lowercase.
    basecalculoirrf = models.FloatField(db_column='BaseCalculoIRRF', blank=True, null=True)  # Field name made lowercase.
    percentualirrf = models.FloatField(db_column='PercentualIRRF', blank=True, null=True)  # Field name made lowercase.
    valorirrf = models.FloatField(db_column='ValorIRRF', blank=True, null=True)  # Field name made lowercase.
    basecalculoicms = models.FloatField(db_column='BaseCalculoICMS', blank=True, null=True)  # Field name made lowercase.
    basecalculoicmsst = models.FloatField(db_column='BaseCalculoIcmsST', blank=True, null=True)  # Field name made lowercase.
    valoricmsst = models.FloatField(db_column='ValorICMSST', blank=True, null=True)  # Field name made lowercase.
    valoricms = models.FloatField(db_column='ValorICMS', blank=True, null=True)  # Field name made lowercase.
    vfcp = models.FloatField(db_column='vFCP', blank=True, null=True)  # Field name made lowercase.
    vfcpst = models.FloatField(db_column='vFCPST', blank=True, null=True)  # Field name made lowercase.
    vfcpstret = models.FloatField(db_column='vFCPSTRet', blank=True, null=True)  # Field name made lowercase.
    vfcpufdest = models.FloatField(db_column='vFCPUFDest', blank=True, null=True)  # Field name made lowercase.
    vicmsufdest = models.FloatField(db_column='vICMSUFDest', blank=True, null=True)  # Field name made lowercase.
    vicmsufremet = models.FloatField(db_column='vICMSUFRemet', blank=True, null=True)  # Field name made lowercase.
    valorprodutos = models.FloatField(db_column='ValorProdutos', blank=True, null=True)  # Field name made lowercase.
    valorfrete = models.FloatField(db_column='ValorFrete', blank=True, null=True)  # Field name made lowercase.
    valorseguro = models.FloatField(db_column='ValorSeguro', blank=True, null=True)  # Field name made lowercase.
    valordesconto = models.FloatField(db_column='ValorDesconto', blank=True, null=True)  # Field name made lowercase.
    valoripi = models.FloatField(db_column='ValorIPI', blank=True, null=True)  # Field name made lowercase.
    valoripidevolvido = models.FloatField(db_column='ValorIPIDevolvido', blank=True, null=True)  # Field name made lowercase.
    valorpis = models.FloatField(db_column='ValorPis', blank=True, null=True)  # Field name made lowercase.
    valorcofins = models.FloatField(db_column='ValorCofins', blank=True, null=True)  # Field name made lowercase.
    valoroutros = models.FloatField(db_column='ValorOutros', blank=True, null=True)  # Field name made lowercase.
    valortributos = models.FloatField(db_column='ValorTributos', blank=True, null=True)  # Field name made lowercase.
    valornotafiscal = models.FloatField(db_column='ValorNotaFiscal', blank=True, null=True)  # Field name made lowercase.
    valortroco = models.FloatField(db_column='ValorTroco', blank=True, null=True)  # Field name made lowercase.
    qbcmonoret = models.FloatField(db_column='qBCMonoRet', blank=True, null=True)  # Field name made lowercase.
    vicmsmonoret = models.FloatField(db_column='vICMSMonoRet', blank=True, null=True)  # Field name made lowercase.
    frete = models.IntegerField(db_column='Frete', blank=True, null=True)  # Field name made lowercase.
    transportadora = models.IntegerField(db_column='Transportadora', blank=True, null=True)  # Field name made lowercase.
    placaveiculo = models.CharField(db_column='PlacaVeiculo', max_length=8, blank=True, null=True)  # Field name made lowercase.
    ufplacaveiculo = models.CharField(db_column='UFPlacaVeiculo', max_length=2, blank=True, null=True)  # Field name made lowercase.
    rntc = models.CharField(db_column='RNTC', max_length=10, blank=True, null=True)  # Field name made lowercase.
    volumequantidade = models.FloatField(db_column='VolumeQuantidade', blank=True, null=True)  # Field name made lowercase.
    volumeespecie = models.CharField(db_column='VolumeEspecie', max_length=30, blank=True, null=True)  # Field name made lowercase.
    volumemarca = models.CharField(db_column='VolumeMarca', max_length=30, blank=True, null=True)  # Field name made lowercase.
    volumenumeracao = models.CharField(db_column='VolumeNumeracao', max_length=30, blank=True, null=True)  # Field name made lowercase.
    volumepesoliquido = models.FloatField(db_column='VolumePesoLiquido', blank=True, null=True)  # Field name made lowercase.
    volumepesobruto = models.FloatField(db_column='VolumePesoBruto', blank=True, null=True)  # Field name made lowercase.
    imprimifatura = models.IntegerField(db_column='ImprimiFatura', blank=True, null=True)  # Field name made lowercase.
    numerofatura = models.CharField(db_column='NumeroFatura', max_length=20, blank=True, null=True)  # Field name made lowercase.
    valorfatura = models.FloatField(db_column='ValorFatura', blank=True, null=True)  # Field name made lowercase.
    descontofatura = models.FloatField(db_column='DescontoFatura', blank=True, null=True)  # Field name made lowercase.
    valorliquidofatura = models.FloatField(db_column='ValorLiquidoFatura', blank=True, null=True)  # Field name made lowercase.
    informacoesfisco = models.TextField(db_column='InformacoesFisco', blank=True, null=True)  # Field name made lowercase.
    informacoescontribuinte = models.TextField(db_column='InformacoesContribuinte', blank=True, null=True)  # Field name made lowercase.
    informacoestributos = models.TextField(db_column='InformacoesTributos', blank=True, null=True)  # Field name made lowercase.
    nfrefuf = models.CharField(db_column='NfRefUF', max_length=2, blank=True, null=True)  # Field name made lowercase.
    nfrefanomes = models.CharField(db_column='NfRefAnoMes', max_length=4, blank=True, null=True)  # Field name made lowercase.
    nfrefcnpj = models.CharField(db_column='NfRefCNPJ', max_length=14, blank=True, null=True)  # Field name made lowercase.
    nfrefnumeronota = models.IntegerField(db_column='NfRefNumeroNota', blank=True, null=True)  # Field name made lowercase.
    nfrefserie = models.CharField(db_column='NfRefSerie', max_length=10, blank=True, null=True)  # Field name made lowercase.
    nfrefmodelo = models.CharField(db_column='NfRefModelo', max_length=10, blank=True, null=True)  # Field name made lowercase.
    nfrefnfexml = models.CharField(db_column='NfRefNFeXML', max_length=44, blank=True, null=True)  # Field name made lowercase.
    notaempenho = models.CharField(db_column='NotaEmpenho', max_length=22, blank=True, null=True)  # Field name made lowercase.
    pedido = models.CharField(db_column='Pedido', max_length=60, blank=True, null=True)  # Field name made lowercase.
    contrato = models.CharField(db_column='Contrato', max_length=60, blank=True, null=True)  # Field name made lowercase.
    xml = models.TextField(db_column='XML', blank=True, null=True)  # Field name made lowercase.
    xmlcancelamento = models.TextField(db_column='XMLCancelamento', blank=True, null=True)  # Field name made lowercase.
    xmlcartacorrecao = models.TextField(db_column='XMLCartaCorrecao', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'nfe_nota_fiscal'


class NfeNumeroaleatorio(models.Model):
    numeronota = models.IntegerField(db_column='NumeroNota', blank=True, null=True)  # Field name made lowercase.
    serie = models.IntegerField(db_column='Serie', blank=True, null=True)  # Field name made lowercase.
    modelo = models.IntegerField(db_column='Modelo', blank=True, null=True)  # Field name made lowercase.
    numeroaleatorio = models.CharField(db_column='NumeroAleatorio', max_length=7, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'nfe_numeroaleatorio'


class NfeNumeronota(models.Model):
    numeronota = models.IntegerField(blank=True, null=True)
    serie = models.IntegerField(blank=True, null=True)
    modelo = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nfe_numeronota'


class NfeOrigem(models.Model):
    situacao = models.IntegerField(blank=True, null=True)
    nftemp = models.IntegerField(db_column='NFtemp', blank=True, null=True)  # Field name made lowercase.
    numeronota = models.IntegerField(db_column='NumeroNota', blank=True, null=True)  # Field name made lowercase.
    serie = models.IntegerField(db_column='Serie', blank=True, null=True)  # Field name made lowercase.
    modelo = models.IntegerField(db_column='Modelo', blank=True, null=True)  # Field name made lowercase.
    tabelavenda = models.CharField(db_column='TabelaVenda', max_length=40, blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    cliente = models.IntegerField(db_column='Cliente', blank=True, null=True)  # Field name made lowercase.
    tabelaproduto = models.CharField(db_column='TabelaProduto', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tipo = models.CharField(db_column='Tipo', max_length=10, blank=True, null=True)  # Field name made lowercase.
    descontoproduto = models.FloatField(db_column='DescontoProduto', blank=True, null=True)  # Field name made lowercase.
    excluirrecebimento = models.IntegerField(db_column='ExcluirRecebimento', blank=True, null=True)  # Field name made lowercase.
    baixastf = models.IntegerField(db_column='BaixaSTF', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'nfe_origem'


class NfeParametros(models.Model):
    aliquota_icms_simples = models.FloatField(blank=True, null=True)
    numeronota = models.IntegerField(blank=True, null=True)
    serie = models.CharField(max_length=3, blank=True, null=True)
    lote = models.IntegerField(blank=True, null=True)
    lotecce = models.IntegerField(db_column='loteCCe', blank=True, null=True)  # Field name made lowercase.
    ambiente_sefaz = models.IntegerField(blank=True, null=True)
    numero_serie_certificado = models.CharField(db_column='Numero_serie_certificado', max_length=50, blank=True, null=True)  # Field name made lowercase.
    path_arquivos = models.CharField(max_length=255, blank=True, null=True)
    path_logo = models.CharField(max_length=255, blank=True, null=True)
    path_logo_jpg = models.CharField(max_length=255, blank=True, null=True)
    email_smtp = models.CharField(max_length=50, blank=True, null=True)
    email_porta = models.IntegerField(blank=True, null=True)
    email_usuario = models.CharField(max_length=50, blank=True, null=True)
    email_senha = models.CharField(max_length=50, blank=True, null=True)
    email_assunto = models.CharField(max_length=100, blank=True, null=True)
    email_mensagem = models.TextField(blank=True, null=True)
    email_conexao_segura = models.IntegerField(blank=True, null=True)
    email_tls = models.IntegerField(db_column='email_TLS', blank=True, null=True)  # Field name made lowercase.
    email_confirma_leitura = models.IntegerField(blank=True, null=True)
    enviar_email = models.IntegerField(blank=True, null=True)
    agrupa_produtos_nf = models.IntegerField(blank=True, null=True)
    arruma_nfe_duplicidade = models.IntegerField(blank=True, null=True)
    desmembrar_kit_produto = models.IntegerField(blank=True, null=True)
    nftemp = models.IntegerField(blank=True, null=True)
    calcula_partilha_icms = models.IntegerField(blank=True, null=True)
    ssllib = models.IntegerField(db_column='SSLLib', blank=True, null=True)  # Field name made lowercase.
    sslcryptlib = models.IntegerField(db_column='SSLCryptLib', blank=True, null=True)  # Field name made lowercase.
    sslhttplib = models.IntegerField(db_column='SSLHttpLib', blank=True, null=True)  # Field name made lowercase.
    sslxmlsignlib = models.IntegerField(db_column='SSLXmlSignLib', blank=True, null=True)  # Field name made lowercase.
    ssltype = models.IntegerField(db_column='SSLType', blank=True, null=True)  # Field name made lowercase.
    tipoimpressao = models.IntegerField(db_column='TipoImpressao', blank=True, null=True)  # Field name made lowercase.
    informarcodigobarras = models.IntegerField(db_column='InformarCodigoBarras', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'nfe_parametros'


class NfeProdutoFiscal(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    situacao = models.IntegerField(db_column='Situacao', blank=True, null=True)  # Field name made lowercase.
    cstat = models.IntegerField(db_column='cStat', blank=True, null=True)  # Field name made lowercase.
    venda = models.IntegerField(db_column='Venda', blank=True, null=True)  # Field name made lowercase.
    emissao = models.DateField(db_column='Emissao', blank=True, null=True)  # Field name made lowercase.
    numeronota = models.IntegerField(db_column='NumeroNota', blank=True, null=True)  # Field name made lowercase.
    serie = models.IntegerField(db_column='Serie', blank=True, null=True)  # Field name made lowercase.
    modelonf = models.IntegerField(db_column='ModeloNF', blank=True, null=True)  # Field name made lowercase.
    codigo = models.CharField(db_column='Codigo', max_length=30, blank=True, null=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=100, blank=True, null=True)  # Field name made lowercase.
    aplicacao = models.CharField(db_column='Aplicacao', max_length=100, blank=True, null=True)  # Field name made lowercase.
    codigobarra = models.CharField(db_column='CodigoBarra', max_length=20, blank=True, null=True)  # Field name made lowercase.
    codigobarratrib = models.CharField(db_column='CodigoBarraTrib', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ncm = models.CharField(db_column='NCM', max_length=8, blank=True, null=True)  # Field name made lowercase.
    cest = models.CharField(db_column='CEST', max_length=7, blank=True, null=True)  # Field name made lowercase.
    anp_simp = models.CharField(max_length=9, blank=True, null=True)
    descricaoanp = models.CharField(db_column='DescricaoANP', max_length=95, blank=True, null=True)  # Field name made lowercase.
    cfop = models.CharField(db_column='CFOP', max_length=8, blank=True, null=True)  # Field name made lowercase.
    unidade = models.CharField(db_column='Unidade', max_length=2, blank=True, null=True)  # Field name made lowercase.
    quantidade = models.FloatField(db_column='Quantidade', blank=True, null=True)  # Field name made lowercase.
    valorunitario = models.FloatField(db_column='ValorUnitario', blank=True, null=True)  # Field name made lowercase.
    valortotal = models.FloatField(db_column='ValorTotal', blank=True, null=True)  # Field name made lowercase.
    descontototal = models.FloatField(db_column='DescontoTotal', blank=True, null=True)  # Field name made lowercase.
    outrasdespesas = models.FloatField(db_column='OutrasDespesas', blank=True, null=True)  # Field name made lowercase.
    valorfrete = models.FloatField(db_column='ValorFrete', blank=True, null=True)  # Field name made lowercase.
    valortributos = models.FloatField(db_column='ValorTributos', blank=True, null=True)  # Field name made lowercase.
    tributofederal = models.FloatField(db_column='TributoFederal', blank=True, null=True)  # Field name made lowercase.
    tributoestadual = models.FloatField(db_column='TributoEstadual', blank=True, null=True)  # Field name made lowercase.
    cstipi = models.CharField(db_column='CstIpi', max_length=3, blank=True, null=True)  # Field name made lowercase.
    basecalculoipi = models.FloatField(db_column='BaseCalculoIPI', blank=True, null=True)  # Field name made lowercase.
    percentualipi = models.FloatField(db_column='PercentualIpi', blank=True, null=True)  # Field name made lowercase.
    valoripi = models.FloatField(db_column='ValorIPI', blank=True, null=True)  # Field name made lowercase.
    percmercdevolvipi = models.FloatField(db_column='PercMercDevolvIPI', blank=True, null=True)  # Field name made lowercase.
    valoripidevolvido = models.FloatField(db_column='ValorIPIDevolvido', blank=True, null=True)  # Field name made lowercase.
    origemmercadoria = models.IntegerField(db_column='OrigemMercadoria', blank=True, null=True)  # Field name made lowercase.
    csticms = models.CharField(db_column='CSTICMS', max_length=3, blank=True, null=True)  # Field name made lowercase.
    modbcicms = models.IntegerField(db_column='ModBCICMS', blank=True, null=True)  # Field name made lowercase.
    baseicms = models.FloatField(db_column='BaseICMS', blank=True, null=True)  # Field name made lowercase.
    predbc = models.FloatField(db_column='pRedBC', blank=True, null=True)  # Field name made lowercase.
    percentualicms = models.FloatField(db_column='PercentualICMS', blank=True, null=True)  # Field name made lowercase.
    valoricms = models.FloatField(db_column='ValorICMS', blank=True, null=True)  # Field name made lowercase.
    modbasecalculost = models.IntegerField(db_column='ModBaseCalculoST', blank=True, null=True)  # Field name made lowercase.
    percentualmvast = models.FloatField(db_column='PercentualMVAST', blank=True, null=True)  # Field name made lowercase.
    predbcst = models.FloatField(db_column='pREDBCST', blank=True, null=True)  # Field name made lowercase.
    basecalculoicmsst = models.FloatField(db_column='BaseCalculoICMSST', blank=True, null=True)  # Field name made lowercase.
    percentualicmsst = models.FloatField(db_column='PercentualICMSST', blank=True, null=True)  # Field name made lowercase.
    valoricmsst = models.FloatField(db_column='ValorICMSST', blank=True, null=True)  # Field name made lowercase.
    basecalculoicmsstretido = models.FloatField(db_column='BaseCalculoICMSSTRetido', blank=True, null=True)  # Field name made lowercase.
    valoricmsstretido = models.FloatField(db_column='ValorICMSSTRetido', blank=True, null=True)  # Field name made lowercase.
    vbcfcp = models.FloatField(db_column='vBCFCP', blank=True, null=True)  # Field name made lowercase.
    pfcp = models.FloatField(db_column='pFCP', blank=True, null=True)  # Field name made lowercase.
    vfcp = models.FloatField(db_column='vFCP', blank=True, null=True)  # Field name made lowercase.
    vbcfcpst = models.FloatField(db_column='vBCFCPST', blank=True, null=True)  # Field name made lowercase.
    pfcpst = models.FloatField(db_column='pFCPST', blank=True, null=True)  # Field name made lowercase.
    vfcpst = models.FloatField(db_column='vFCPST', blank=True, null=True)  # Field name made lowercase.
    pst = models.FloatField(db_column='pST', blank=True, null=True)  # Field name made lowercase.
    vbcfcpstret = models.FloatField(db_column='vBCFCPSTRet', blank=True, null=True)  # Field name made lowercase.
    pfcpstret = models.FloatField(db_column='pFCPSTRet', blank=True, null=True)  # Field name made lowercase.
    vfcpstret = models.FloatField(db_column='vFCPSTRet', blank=True, null=True)  # Field name made lowercase.
    cstpis = models.CharField(db_column='CSTPis', max_length=3, blank=True, null=True)  # Field name made lowercase.
    basepis = models.FloatField(db_column='BasePis', blank=True, null=True)  # Field name made lowercase.
    percentualpis = models.FloatField(db_column='PercentualPis', blank=True, null=True)  # Field name made lowercase.
    valorpis = models.FloatField(db_column='ValorPis', blank=True, null=True)  # Field name made lowercase.
    basepisquantidade = models.FloatField(db_column='BasePisQuantidade', blank=True, null=True)  # Field name made lowercase.
    percentualpisvalor = models.FloatField(db_column='PercentualPisValor', blank=True, null=True)  # Field name made lowercase.
    cstcofins = models.CharField(db_column='CSTCofins', max_length=3, blank=True, null=True)  # Field name made lowercase.
    basecofins = models.FloatField(db_column='BaseCofins', blank=True, null=True)  # Field name made lowercase.
    percentualcofins = models.FloatField(db_column='PercentualCofins', blank=True, null=True)  # Field name made lowercase.
    valorcofins = models.FloatField(db_column='ValorCofins', blank=True, null=True)  # Field name made lowercase.
    basecofinsquantidade = models.FloatField(db_column='BaseCofinsQuantidade', blank=True, null=True)  # Field name made lowercase.
    percentualcofinsvalor = models.FloatField(db_column='PercentualCofinsValor', blank=True, null=True)  # Field name made lowercase.
    percentualicmssimples = models.FloatField(db_column='PercentualIcmsSimples', blank=True, null=True)  # Field name made lowercase.
    valoricmssimples = models.FloatField(db_column='ValorIcmsSimples', blank=True, null=True)  # Field name made lowercase.
    vbcufdest = models.FloatField(db_column='vBCUFDest', blank=True, null=True)  # Field name made lowercase.
    pfcpufdest = models.FloatField(db_column='pFCPUFDest', blank=True, null=True)  # Field name made lowercase.
    picmsufdest = models.FloatField(db_column='pICMSUFDest', blank=True, null=True)  # Field name made lowercase.
    picmsinter = models.FloatField(db_column='pICMSInter', blank=True, null=True)  # Field name made lowercase.
    picmsinterpart = models.FloatField(db_column='pICMSInterPart', blank=True, null=True)  # Field name made lowercase.
    vfcpufdest = models.FloatField(db_column='vFCPUFDest', blank=True, null=True)  # Field name made lowercase.
    vicmsufdest = models.FloatField(db_column='vICMSUFDest', blank=True, null=True)  # Field name made lowercase.
    vicmsufremet = models.FloatField(db_column='vICMSUFRemet', blank=True, null=True)  # Field name made lowercase.
    pglp = models.FloatField(db_column='pGLP', blank=True, null=True)  # Field name made lowercase.
    pgnn = models.FloatField(db_column='pGNn', blank=True, null=True)  # Field name made lowercase.
    pgni = models.FloatField(db_column='pGNi', blank=True, null=True)  # Field name made lowercase.
    vpart = models.FloatField(db_column='vPart', blank=True, null=True)  # Field name made lowercase.
    qbcmonoret = models.FloatField(db_column='qBCMonoRet', blank=True, null=True)  # Field name made lowercase.
    adremicmsret = models.FloatField(db_column='adRemICMSRet', blank=True, null=True)  # Field name made lowercase.
    vicmsmonoret = models.FloatField(db_column='vICMSMonoRet', blank=True, null=True)  # Field name made lowercase.
    numeropedidocompra = models.CharField(db_column='NumeroPedidoCompra', max_length=15, blank=True, null=True)  # Field name made lowercase.
    numeroitempedidocompra = models.IntegerField(db_column='NumeroItemPedidoCompra', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'nfe_produto_fiscal'


class NfseNotaFiscal(models.Model):
    situacao = models.IntegerField(db_column='Situacao', blank=True, null=True)  # Field name made lowercase.
    email = models.IntegerField(db_column='Email', blank=True, null=True)  # Field name made lowercase.
    lote = models.IntegerField(db_column='Lote', blank=True, null=True)  # Field name made lowercase.
    cliente = models.IntegerField(db_column='Cliente', blank=True, null=True)  # Field name made lowercase.
    numerorps = models.IntegerField(db_column='NumeroRPS', blank=True, null=True)  # Field name made lowercase.
    numeronota = models.IntegerField(db_column='NumeroNota', blank=True, null=True)  # Field name made lowercase.
    protocolo = models.CharField(db_column='Protocolo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    codigoverificacao = models.CharField(db_column='CodigoVerificacao', max_length=9, blank=True, null=True)  # Field name made lowercase.
    codigosituacao = models.CharField(db_column='CodigoSituacao', max_length=5, blank=True, null=True)  # Field name made lowercase.
    serie = models.CharField(db_column='Serie', max_length=15, blank=True, null=True)  # Field name made lowercase.
    emissao = models.DateField(db_column='Emissao', blank=True, null=True)  # Field name made lowercase.
    naturezaoperacao = models.IntegerField(db_column='NaturezaOperacao', blank=True, null=True)  # Field name made lowercase.
    regimetributacao = models.IntegerField(db_column='RegimeTributacao', blank=True, null=True)  # Field name made lowercase.
    servico = models.TextField(db_column='Servico', blank=True, null=True)  # Field name made lowercase.
    valorservicos = models.FloatField(db_column='ValorServicos', blank=True, null=True)  # Field name made lowercase.
    valordeducoes = models.FloatField(db_column='ValorDeducoes', blank=True, null=True)  # Field name made lowercase.
    valorpis = models.FloatField(db_column='ValorPis', blank=True, null=True)  # Field name made lowercase.
    valorcofins = models.FloatField(db_column='ValorCofins', blank=True, null=True)  # Field name made lowercase.
    valorinss = models.FloatField(db_column='ValorInss', blank=True, null=True)  # Field name made lowercase.
    valorir = models.FloatField(db_column='ValorIr', blank=True, null=True)  # Field name made lowercase.
    valorcsll = models.FloatField(db_column='ValorCsll', blank=True, null=True)  # Field name made lowercase.
    issretido = models.IntegerField(db_column='IssRetido', blank=True, null=True)  # Field name made lowercase.
    outrasretencoes = models.FloatField(db_column='OutrasRetencoes', blank=True, null=True)  # Field name made lowercase.
    descontoincondicionado = models.FloatField(db_column='DescontoIncondicionado', blank=True, null=True)  # Field name made lowercase.
    descontocondicionado = models.FloatField(db_column='DescontoCondicionado', blank=True, null=True)  # Field name made lowercase.
    basecalculo = models.FloatField(db_column='BaseCalculo', blank=True, null=True)  # Field name made lowercase.
    aliquota = models.FloatField(db_column='Aliquota', blank=True, null=True)  # Field name made lowercase.
    valoriss = models.FloatField(db_column='ValorIss', blank=True, null=True)  # Field name made lowercase.
    valorissretido = models.FloatField(db_column='ValorIssRetido', blank=True, null=True)  # Field name made lowercase.
    valorliquidonfse = models.FloatField(db_column='ValorLiquidoNfse', blank=True, null=True)  # Field name made lowercase.
    itemlistaservico = models.CharField(db_column='ItemListaServico', max_length=10, blank=True, null=True)  # Field name made lowercase.
    codigotributacaomunicipio = models.CharField(db_column='CodigoTributacaoMunicipio', max_length=10, blank=True, null=True)  # Field name made lowercase.
    discriminacao = models.CharField(db_column='Discriminacao', max_length=100, blank=True, null=True)  # Field name made lowercase.
    municipioincidencia = models.CharField(db_column='MunicipioIncidencia', max_length=10, blank=True, null=True)  # Field name made lowercase.
    nomearquivo = models.CharField(db_column='NomeArquivo', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'nfse_nota_fiscal'


class NfseParametros(models.Model):
    inscricaomunicipal = models.CharField(db_column='InscricaoMunicipal', max_length=15, blank=True, null=True)  # Field name made lowercase.
    numerorps = models.IntegerField(db_column='NumeroRPS', blank=True, null=True)  # Field name made lowercase.
    numeronota = models.IntegerField(db_column='NumeroNota', blank=True, null=True)  # Field name made lowercase.
    aliquotaiss = models.FloatField(db_column='AliquotaISS', blank=True, null=True)  # Field name made lowercase.
    lote = models.IntegerField(db_column='Lote', blank=True, null=True)  # Field name made lowercase.
    serie = models.CharField(db_column='Serie', max_length=10, blank=True, null=True)  # Field name made lowercase.
    regimeespecialtributacao = models.IntegerField(db_column='RegimeEspecialTributacao', blank=True, null=True)  # Field name made lowercase.
    naturezaoperacao = models.IntegerField(db_column='NaturezaOperacao', blank=True, null=True)  # Field name made lowercase.
    optantesimplesnacional = models.IntegerField(db_column='OptanteSimplesNacional', blank=True, null=True)  # Field name made lowercase.
    incentivadorcultural = models.IntegerField(db_column='IncentivadorCultural', blank=True, null=True)  # Field name made lowercase.
    exigeiss = models.IntegerField(db_column='ExigeISS', blank=True, null=True)  # Field name made lowercase.
    numeroseriecertificado = models.CharField(db_column='NumeroSerieCertificado', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pathcancelamento = models.CharField(db_column='PathCancelamento', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pathnfse = models.CharField(db_column='PathNFSe', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ambiente = models.IntegerField(db_column='Ambiente', blank=True, null=True)  # Field name made lowercase.
    usuario = models.CharField(db_column='Usuario', max_length=50, blank=True, null=True)  # Field name made lowercase.
    senha = models.CharField(db_column='Senha', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pathlogoempresa = models.CharField(db_column='PathLogoEmpresa', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pathlogoprefeitura = models.CharField(db_column='PathLogoPrefeitura', max_length=255, blank=True, null=True)  # Field name made lowercase.
    prefeitura = models.CharField(db_column='Prefeitura', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pathschemas = models.CharField(db_column='PathSchemas', max_length=255, blank=True, null=True)  # Field name made lowercase.
    emailsmtp = models.CharField(db_column='EmailSmtp', max_length=50, blank=True, null=True)  # Field name made lowercase.
    emailporta = models.IntegerField(db_column='EmailPorta', blank=True, null=True)  # Field name made lowercase.
    emailusuario = models.CharField(db_column='EmailUsuario', max_length=50, blank=True, null=True)  # Field name made lowercase.
    emailsenha = models.CharField(db_column='EmailSenha', max_length=50, blank=True, null=True)  # Field name made lowercase.
    emailassunto = models.CharField(db_column='EmailAssunto', max_length=100, blank=True, null=True)  # Field name made lowercase.
    emailmensagem = models.TextField(db_column='EmailMensagem', blank=True, null=True)  # Field name made lowercase.
    emailconexaosegura = models.IntegerField(db_column='EmailConexaoSegura', blank=True, null=True)  # Field name made lowercase.
    emailtls = models.IntegerField(db_column='EmailTLS', blank=True, null=True)  # Field name made lowercase.
    emailremetente = models.CharField(db_column='EmailRemetente', max_length=255, blank=True, null=True)  # Field name made lowercase.
    emailconfirmaleitura = models.IntegerField(db_column='EmailConfirmaLeitura', blank=True, null=True)  # Field name made lowercase.
    nftemp = models.IntegerField(db_column='NfTemp', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'nfse_parametros'


class NfseServicoFiscal(models.Model):
    numerorps = models.IntegerField(db_column='NumeroRPS', blank=True, null=True)  # Field name made lowercase.
    numeronota = models.IntegerField(db_column='NumeroNota', blank=True, null=True)  # Field name made lowercase.
    emissao = models.DateField(db_column='Emissao', blank=True, null=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=255, blank=True, null=True)  # Field name made lowercase.
    quantidade = models.FloatField(db_column='Quantidade', blank=True, null=True)  # Field name made lowercase.
    valorunitario = models.FloatField(db_column='ValorUnitario', blank=True, null=True)  # Field name made lowercase.
    valortotal = models.FloatField(db_column='ValorTotal', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'nfse_servico_fiscal'


class NfseTabelaNaturezaOperacao(models.Model):
    tributacao = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nfse_tabela_natureza_operacao'


class NfseTabelaRegimeEspecialTributacao(models.Model):
    regime = models.CharField(db_column='Regime', max_length=60, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'nfse_tabela_regime_especial_tributacao'


class Notasentradas(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    tipo = models.IntegerField(blank=True, null=True)
    forcli = models.IntegerField(blank=True, null=True)
    numero = models.IntegerField(db_column='Numero', blank=True, null=True)  # Field name made lowercase.
    naturezaoperacao = models.CharField(db_column='NaturezaOperacao', max_length=60, blank=True, null=True)  # Field name made lowercase.
    modelonf = models.CharField(db_column='ModeloNF', max_length=10, blank=True, null=True)  # Field name made lowercase.
    serie = models.CharField(db_column='Serie', max_length=10, blank=True, null=True)  # Field name made lowercase.
    chavenfe = models.CharField(db_column='ChaveNFe', max_length=44, blank=True, null=True)  # Field name made lowercase.
    fornecedor = models.IntegerField(db_column='Fornecedor', blank=True, null=True)  # Field name made lowercase.
    cfop = models.CharField(db_column='CFOP', max_length=5, blank=True, null=True)  # Field name made lowercase.
    emissao = models.DateField(db_column='Emissao', blank=True, null=True)  # Field name made lowercase.
    desconto = models.FloatField(db_column='Desconto', blank=True, null=True)  # Field name made lowercase.
    repasse = models.FloatField(db_column='Repasse', blank=True, null=True)  # Field name made lowercase.
    baseicms = models.FloatField(blank=True, null=True)
    icms = models.FloatField(db_column='ICMS', blank=True, null=True)  # Field name made lowercase.
    baseicmssubst = models.FloatField(blank=True, null=True)
    icmssubst = models.FloatField(db_column='ICMSSubst', blank=True, null=True)  # Field name made lowercase.
    valorproduto = models.FloatField(db_column='ValorProduto', blank=True, null=True)  # Field name made lowercase.
    ipi = models.FloatField(db_column='IPI', blank=True, null=True)  # Field name made lowercase.
    frete = models.FloatField(db_column='Frete', blank=True, null=True)  # Field name made lowercase.
    freteterceiros = models.FloatField(db_column='FreteTerceiros', blank=True, null=True)  # Field name made lowercase.
    outrasdespesas = models.FloatField(db_column='OutrasDespesas', blank=True, null=True)  # Field name made lowercase.
    seguro = models.FloatField(db_column='Seguro', blank=True, null=True)  # Field name made lowercase.
    totalnf = models.FloatField(db_column='TotalNF', blank=True, null=True)  # Field name made lowercase.
    cadastro = models.DateField(db_column='Cadastro', blank=True, null=True)  # Field name made lowercase.
    conferido = models.IntegerField(db_column='Conferido', blank=True, null=True)  # Field name made lowercase.
    dataconf = models.DateField(db_column='DataConf', blank=True, null=True)  # Field name made lowercase.
    horaconf = models.TimeField(db_column='HoraConf', blank=True, null=True)  # Field name made lowercase.
    usuarioconf = models.IntegerField(db_column='UsuarioConf', blank=True, null=True)  # Field name made lowercase.
    funcionarioconf = models.IntegerField(db_column='FuncionarioConf', blank=True, null=True)  # Field name made lowercase.
    observacaoconf = models.TextField(db_column='ObservacaoConf', blank=True, null=True)  # Field name made lowercase.
    empresa = models.IntegerField(db_column='Empresa', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'notasentradas'


class Notasfiscais(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    numeronota = models.IntegerField(db_column='NumeroNota', blank=True, null=True)  # Field name made lowercase.
    quantnota = models.IntegerField(db_column='QuantNota', blank=True, null=True)  # Field name made lowercase.
    tipo = models.CharField(db_column='Tipo', max_length=1, blank=True, null=True)  # Field name made lowercase.
    natureza = models.CharField(db_column='Natureza', max_length=60, blank=True, null=True)  # Field name made lowercase.
    cfop = models.CharField(db_column='CFOP', max_length=30, blank=True, null=True)  # Field name made lowercase.
    clifor = models.IntegerField(db_column='CliFor', blank=True, null=True)  # Field name made lowercase.
    quen = models.IntegerField(db_column='Quen', blank=True, null=True)  # Field name made lowercase.
    emissao = models.DateField(db_column='Emissao', blank=True, null=True)  # Field name made lowercase.
    saidaentrada = models.DateField(db_column='SaidaEntrada', blank=True, null=True)  # Field name made lowercase.
    horasaida = models.TimeField(db_column='HoraSaida', blank=True, null=True)  # Field name made lowercase.
    duplicata = models.IntegerField(blank=True, null=True)
    dup1 = models.CharField(db_column='Dup1', max_length=20, blank=True, null=True)  # Field name made lowercase.
    dup2 = models.CharField(db_column='Dup2', max_length=20, blank=True, null=True)  # Field name made lowercase.
    dup3 = models.CharField(db_column='Dup3', max_length=20, blank=True, null=True)  # Field name made lowercase.
    dup4 = models.CharField(db_column='Dup4', max_length=20, blank=True, null=True)  # Field name made lowercase.
    dup5 = models.CharField(db_column='Dup5', max_length=20, blank=True, null=True)  # Field name made lowercase.
    dup6 = models.CharField(db_column='Dup6', max_length=20, blank=True, null=True)  # Field name made lowercase.
    dup7 = models.CharField(db_column='Dup7', max_length=20, blank=True, null=True)  # Field name made lowercase.
    dup8 = models.CharField(db_column='Dup8', max_length=20, blank=True, null=True)  # Field name made lowercase.
    dup9 = models.CharField(db_column='Dup9', max_length=20, blank=True, null=True)  # Field name made lowercase.
    dup10 = models.CharField(db_column='Dup10', max_length=20, blank=True, null=True)  # Field name made lowercase.
    dup11 = models.CharField(db_column='Dup11', max_length=20, blank=True, null=True)  # Field name made lowercase.
    dup12 = models.CharField(db_column='Dup12', max_length=20, blank=True, null=True)  # Field name made lowercase.
    venc1 = models.DateField(db_column='Venc1', blank=True, null=True)  # Field name made lowercase.
    venc2 = models.DateField(db_column='Venc2', blank=True, null=True)  # Field name made lowercase.
    venc3 = models.DateField(db_column='Venc3', blank=True, null=True)  # Field name made lowercase.
    venc4 = models.DateField(db_column='Venc4', blank=True, null=True)  # Field name made lowercase.
    venc5 = models.DateField(db_column='Venc5', blank=True, null=True)  # Field name made lowercase.
    venc6 = models.DateField(db_column='Venc6', blank=True, null=True)  # Field name made lowercase.
    venc7 = models.DateField(db_column='Venc7', blank=True, null=True)  # Field name made lowercase.
    venc8 = models.DateField(db_column='Venc8', blank=True, null=True)  # Field name made lowercase.
    venc9 = models.DateField(db_column='Venc9', blank=True, null=True)  # Field name made lowercase.
    venc10 = models.DateField(db_column='Venc10', blank=True, null=True)  # Field name made lowercase.
    venc11 = models.DateField(db_column='Venc11', blank=True, null=True)  # Field name made lowercase.
    venc12 = models.DateField(db_column='Venc12', blank=True, null=True)  # Field name made lowercase.
    val1 = models.FloatField(db_column='Val1', blank=True, null=True)  # Field name made lowercase.
    val2 = models.FloatField(db_column='Val2', blank=True, null=True)  # Field name made lowercase.
    val3 = models.FloatField(db_column='Val3', blank=True, null=True)  # Field name made lowercase.
    val4 = models.FloatField(db_column='Val4', blank=True, null=True)  # Field name made lowercase.
    val5 = models.FloatField(db_column='Val5', blank=True, null=True)  # Field name made lowercase.
    val6 = models.FloatField(db_column='Val6', blank=True, null=True)  # Field name made lowercase.
    val7 = models.FloatField(db_column='Val7', blank=True, null=True)  # Field name made lowercase.
    val8 = models.FloatField(db_column='Val8', blank=True, null=True)  # Field name made lowercase.
    val9 = models.FloatField(db_column='Val9', blank=True, null=True)  # Field name made lowercase.
    val10 = models.FloatField(db_column='Val10', blank=True, null=True)  # Field name made lowercase.
    val11 = models.FloatField(db_column='Val11', blank=True, null=True)  # Field name made lowercase.
    val12 = models.FloatField(db_column='Val12', blank=True, null=True)  # Field name made lowercase.
    valiss = models.FloatField(db_column='ValISS', blank=True, null=True)  # Field name made lowercase.
    valserv = models.FloatField(db_column='ValServ', blank=True, null=True)  # Field name made lowercase.
    descserv = models.FloatField(db_column='DescServ', blank=True, null=True)  # Field name made lowercase.
    totalserv = models.FloatField(db_column='TotalServ', blank=True, null=True)  # Field name made lowercase.
    baseicms = models.FloatField(db_column='BaseICMS', blank=True, null=True)  # Field name made lowercase.
    valoricms = models.FloatField(db_column='ValorICMS', blank=True, null=True)  # Field name made lowercase.
    valprod = models.FloatField(db_column='ValProd', blank=True, null=True)  # Field name made lowercase.
    descprod = models.FloatField(db_column='DescProd', blank=True, null=True)  # Field name made lowercase.
    totalprod = models.FloatField(db_column='TotalProd', blank=True, null=True)  # Field name made lowercase.
    valnota = models.FloatField(db_column='ValNota', blank=True, null=True)  # Field name made lowercase.
    desconto = models.FloatField(blank=True, null=True)
    issqn = models.FloatField(blank=True, null=True)
    freteconta = models.CharField(db_column='FreteConta', max_length=1, blank=True, null=True)  # Field name made lowercase.
    linhad1 = models.CharField(db_column='LinhaD1', max_length=80, blank=True, null=True)  # Field name made lowercase.
    linhad2 = models.CharField(db_column='LinhaD2', max_length=80, blank=True, null=True)  # Field name made lowercase.
    linhad3 = models.CharField(db_column='LinhaD3', max_length=80, blank=True, null=True)  # Field name made lowercase.
    linhad4 = models.CharField(db_column='LinhaD4', max_length=80, blank=True, null=True)  # Field name made lowercase.
    linhad5 = models.CharField(db_column='LinhaD5', max_length=80, blank=True, null=True)  # Field name made lowercase.
    linhad6 = models.CharField(db_column='LinhaD6', max_length=80, blank=True, null=True)  # Field name made lowercase.
    base2 = models.FloatField(db_column='Base2', blank=True, null=True)  # Field name made lowercase.
    valori2 = models.FloatField(db_column='ValorI2', blank=True, null=True)  # Field name made lowercase.
    frete = models.FloatField(db_column='Frete', blank=True, null=True)  # Field name made lowercase.
    seguro = models.FloatField(db_column='Seguro', blank=True, null=True)  # Field name made lowercase.
    despesas = models.FloatField(db_column='Despesas', blank=True, null=True)  # Field name made lowercase.
    ipi = models.FloatField(db_column='IPI', blank=True, null=True)  # Field name made lowercase.
    trans = models.IntegerField(db_column='Trans', blank=True, null=True)  # Field name made lowercase.
    placa = models.CharField(db_column='Placa', max_length=8, blank=True, null=True)  # Field name made lowercase.
    ufplaca = models.CharField(db_column='UFPlaca', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cnplaca = models.CharField(db_column='CNPlaca', max_length=25, blank=True, null=True)  # Field name made lowercase.
    qt = models.CharField(db_column='QT', max_length=15, blank=True, null=True)  # Field name made lowercase.
    especie = models.CharField(db_column='Especie', max_length=15, blank=True, null=True)  # Field name made lowercase.
    marca = models.CharField(db_column='Marca', max_length=15, blank=True, null=True)  # Field name made lowercase.
    numero = models.CharField(db_column='Numero', max_length=15, blank=True, null=True)  # Field name made lowercase.
    peso = models.CharField(db_column='Peso', max_length=15, blank=True, null=True)  # Field name made lowercase.
    liquido = models.CharField(db_column='Liquido', max_length=15, blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(blank=True, null=True)
    data_cancelamento = models.DateField(blank=True, null=True)
    empresa = models.IntegerField(db_column='Empresa', blank=True, null=True)  # Field name made lowercase.
    motivo = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notasfiscais'


class Observacaonf(models.Model):
    codigo = models.AutoField(db_column='Codigo', primary_key=True)  # Field name made lowercase.
    observacao = models.CharField(db_column='Observacao', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cadastro = models.DateField(db_column='Cadastro', blank=True, null=True)  # Field name made lowercase.
    empresa = models.IntegerField(db_column='Empresa', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'observacaonf'


class Oficina(models.Model):
    codigo = models.AutoField(primary_key=True)
    oficina = models.CharField(max_length=40, blank=True, null=True)
    proprietario = models.CharField(max_length=40, blank=True, null=True)
    endereco = models.CharField(max_length=40, blank=True, null=True)
    bairro = models.CharField(max_length=25, blank=True, null=True)
    cep = models.CharField(max_length=9, blank=True, null=True)
    cidade = models.CharField(max_length=40, blank=True, null=True)
    uf = models.CharField(max_length=2, blank=True, null=True)
    fone1 = models.CharField(max_length=13, blank=True, null=True)
    fone2 = models.CharField(max_length=13, blank=True, null=True)
    comissao = models.FloatField(blank=True, null=True)
    comissionado = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oficina'


class Orcamento(models.Model):
    codigo = models.AutoField(db_column='Codigo', primary_key=True)  # Field name made lowercase.
    tipo = models.CharField(max_length=6, blank=True, null=True)
    status = models.IntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    cliente = models.IntegerField(db_column='Cliente', blank=True, null=True)  # Field name made lowercase.
    data = models.DateField(db_column='Data', blank=True, null=True)  # Field name made lowercase.
    hora = models.TimeField(db_column='Hora', blank=True, null=True)  # Field name made lowercase.
    veiculo = models.CharField(db_column='Veiculo', max_length=40, blank=True, null=True)  # Field name made lowercase.
    placa = models.CharField(db_column='Placa', max_length=8, blank=True, null=True)  # Field name made lowercase.
    ano = models.CharField(db_column='Ano', max_length=9, blank=True, null=True)  # Field name made lowercase.
    servicos = models.FloatField(db_column='Servicos', blank=True, null=True)  # Field name made lowercase.
    produtos = models.FloatField(db_column='Produtos', blank=True, null=True)  # Field name made lowercase.
    total = models.FloatField(blank=True, null=True)
    descacre = models.FloatField(blank=True, null=True)
    valortotal = models.FloatField(db_column='ValorTotal', blank=True, null=True)  # Field name made lowercase.
    condicao = models.IntegerField(blank=True, null=True)
    condicao1 = models.CharField(db_column='Condicao1', max_length=3, blank=True, null=True)  # Field name made lowercase.
    titulo1 = models.CharField(db_column='Titulo1', max_length=30, blank=True, null=True)  # Field name made lowercase.
    parcela1 = models.CharField(db_column='Parcela1', max_length=2, blank=True, null=True)  # Field name made lowercase.
    desconto1 = models.CharField(db_column='Desconto1', max_length=10, blank=True, null=True)  # Field name made lowercase.
    valor1 = models.CharField(db_column='Valor1', max_length=10, blank=True, null=True)  # Field name made lowercase.
    total1 = models.CharField(db_column='Total1', max_length=10, blank=True, null=True)  # Field name made lowercase.
    condicao2 = models.CharField(db_column='Condicao2', max_length=3, blank=True, null=True)  # Field name made lowercase.
    titulo2 = models.CharField(db_column='Titulo2', max_length=30, blank=True, null=True)  # Field name made lowercase.
    parcela2 = models.CharField(db_column='Parcela2', max_length=2, blank=True, null=True)  # Field name made lowercase.
    desconto2 = models.CharField(db_column='Desconto2', max_length=10, blank=True, null=True)  # Field name made lowercase.
    valor2 = models.CharField(db_column='Valor2', max_length=10, blank=True, null=True)  # Field name made lowercase.
    total2 = models.CharField(db_column='Total2', max_length=10, blank=True, null=True)  # Field name made lowercase.
    validade = models.DateField(db_column='Validade', blank=True, null=True)  # Field name made lowercase.
    funcionario = models.IntegerField(db_column='Funcionario', blank=True, null=True)  # Field name made lowercase.
    empresa = models.IntegerField(db_column='Empresa', blank=True, null=True)  # Field name made lowercase.
    obs = models.TextField(db_column='Obs', blank=True, null=True)  # Field name made lowercase.
    os = models.IntegerField(db_column='OS', blank=True, null=True)  # Field name made lowercase.
    situacao = models.IntegerField(db_column='Situacao', blank=True, null=True)  # Field name made lowercase.
    portador = models.CharField(max_length=50, blank=True, null=True)
    profissional = models.IntegerField(blank=True, null=True)
    tabela = models.CharField(max_length=1, blank=True, null=True)
    peso = models.FloatField(blank=True, null=True)
    descricaoorcamento = models.TextField(db_column='DescricaoOrcamento', blank=True, null=True)  # Field name made lowercase.
    equipamento = models.CharField(max_length=60, blank=True, null=True)
    modelo = models.CharField(max_length=40, blank=True, null=True)
    marca = models.CharField(max_length=40, blank=True, null=True)
    numeroserie = models.CharField(max_length=30, blank=True, null=True)
    acessorios = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orcamento'


class OrcamentoCondicao(models.Model):
    orcamento = models.IntegerField(blank=True, null=True)
    condicao = models.IntegerField(blank=True, null=True)
    descricao = models.CharField(max_length=50, blank=True, null=True)
    porcentagem = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    descacre = models.FloatField(blank=True, null=True)
    totalgeral = models.FloatField(blank=True, null=True)
    parcelas = models.IntegerField(blank=True, null=True)
    valor_parcela = models.FloatField(blank=True, null=True)
    observacao = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orcamento_condicao'


class OrcamentoProdConsulta(models.Model):
    idd = models.AutoField(primary_key=True)
    id = models.IntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    tipo = models.CharField(max_length=10, blank=True, null=True)
    codigo = models.CharField(max_length=30, blank=True, null=True)
    descricao = models.CharField(max_length=60, blank=True, null=True)
    utilizacao = models.CharField(max_length=60, blank=True, null=True)
    quantidade = models.FloatField(blank=True, null=True)
    unitario = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    grupo = models.IntegerField(db_column='Grupo', blank=True, null=True)  # Field name made lowercase.
    grupodesc = models.CharField(db_column='GrupoDesc', max_length=60, blank=True, null=True)  # Field name made lowercase.
    linha = models.IntegerField(db_column='Linha', blank=True, null=True)  # Field name made lowercase.
    linhadesc = models.CharField(db_column='LinhaDesc', max_length=60, blank=True, null=True)  # Field name made lowercase.
    fabricante = models.IntegerField(db_column='Fabricante', blank=True, null=True)  # Field name made lowercase.
    fabricantedesc = models.CharField(db_column='FabricanteDesc', max_length=60, blank=True, null=True)  # Field name made lowercase.
    empresa = models.IntegerField(db_column='Empresa', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'orcamento_prod_consulta'


class Orcamentocondicao(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    orcamento = models.IntegerField(db_column='Orcamento', blank=True, null=True)  # Field name made lowercase.
    condicao = models.CharField(db_column='Condicao', max_length=30, blank=True, null=True)  # Field name made lowercase.
    parcela = models.CharField(db_column='Parcela', max_length=10, blank=True, null=True)  # Field name made lowercase.
    descacre = models.CharField(db_column='DescAcre', max_length=10, blank=True, null=True)  # Field name made lowercase.
    valor = models.CharField(db_column='Valor', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tipo = models.IntegerField(db_column='Tipo', blank=True, null=True)  # Field name made lowercase.
    empresa = models.IntegerField(db_column='Empresa', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'orcamentocondicao'


class Orcamentoparcelas(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    codigo = models.IntegerField(db_column='Codigo', blank=True, null=True)  # Field name made lowercase.
    emissao = models.DateField(db_column='Emissao', blank=True, null=True)  # Field name made lowercase.
    tipo = models.CharField(db_column='Tipo', max_length=1, blank=True, null=True)  # Field name made lowercase.
    portador = models.IntegerField(db_column='Portador', blank=True, null=True)  # Field name made lowercase.
    cliente = models.IntegerField(db_column='Cliente', blank=True, null=True)  # Field name made lowercase.
    clienteant = models.IntegerField(blank=True, null=True)
    conta = models.IntegerField(db_column='Conta', blank=True, null=True)  # Field name made lowercase.
    condicoes = models.IntegerField(db_column='Condicoes', blank=True, null=True)  # Field name made lowercase.
    vencimento = models.DateField(db_column='Vencimento', blank=True, null=True)  # Field name made lowercase.
    valorprestacao = models.FloatField(db_column='ValorPrestacao', blank=True, null=True)  # Field name made lowercase.
    valordocumento = models.FloatField(db_column='ValorDocumento', blank=True, null=True)  # Field name made lowercase.
    observacao = models.CharField(db_column='Observacao', max_length=100, blank=True, null=True)  # Field name made lowercase.
    situacao = models.CharField(db_column='Situacao', max_length=1, blank=True, null=True)  # Field name made lowercase.
    diferenca = models.FloatField(db_column='Diferenca', blank=True, null=True)  # Field name made lowercase.
    valorpago = models.FloatField(db_column='ValorPago', blank=True, null=True)  # Field name made lowercase.
    datapagto = models.DateField(db_column='DataPagto', blank=True, null=True)  # Field name made lowercase.
    sequencia = models.IntegerField(db_column='Sequencia', blank=True, null=True)  # Field name made lowercase.
    parcelas = models.IntegerField(blank=True, null=True)
    pagocom = models.IntegerField(db_column='PagoCom', blank=True, null=True)  # Field name made lowercase.
    numerobanco = models.CharField(db_column='NumeroBanco', max_length=30, blank=True, null=True)  # Field name made lowercase.
    os = models.IntegerField(db_column='OS', blank=True, null=True)  # Field name made lowercase.
    process = models.DateField(db_column='Process', blank=True, null=True)  # Field name made lowercase.
    esp = models.CharField(db_column='ESP', max_length=2, blank=True, null=True)  # Field name made lowercase.
    empresa = models.IntegerField(db_column='Empresa', blank=True, null=True)  # Field name made lowercase.
    sequencia2 = models.IntegerField(db_column='Sequencia2', blank=True, null=True)  # Field name made lowercase.
    vendedor = models.IntegerField(blank=True, null=True)
    recebimento = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orcamentoparcelas'


class Orcamentoprodutos(models.Model):
    idd = models.AutoField(primary_key=True)
    id = models.IntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    tipo = models.CharField(max_length=10, blank=True, null=True)
    id_produto = models.IntegerField(blank=True, null=True)
    codigo = models.CharField(max_length=30, blank=True, null=True)
    descricao = models.CharField(max_length=60, blank=True, null=True)
    utilizacao = models.CharField(max_length=60, blank=True, null=True)
    quantidade = models.FloatField(blank=True, null=True)
    unitario = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    vendaunitario = models.FloatField(blank=True, null=True)
    quantunidade = models.FloatField(blank=True, null=True)
    peso = models.FloatField(blank=True, null=True)
    precopeso = models.CharField(max_length=1, blank=True, null=True)
    grupo = models.IntegerField(db_column='Grupo', blank=True, null=True)  # Field name made lowercase.
    grupodesc = models.CharField(db_column='GrupoDesc', max_length=60, blank=True, null=True)  # Field name made lowercase.
    linha = models.IntegerField(db_column='Linha', blank=True, null=True)  # Field name made lowercase.
    linhadesc = models.CharField(db_column='LinhaDesc', max_length=60, blank=True, null=True)  # Field name made lowercase.
    fabricante = models.IntegerField(db_column='Fabricante', blank=True, null=True)  # Field name made lowercase.
    fabricantedesc = models.CharField(db_column='FabricanteDesc', max_length=60, blank=True, null=True)  # Field name made lowercase.
    mecanico = models.IntegerField(db_column='Mecanico', blank=True, null=True)  # Field name made lowercase.
    empresa = models.IntegerField(db_column='Empresa', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'orcamentoprodutos'


class Orcconsulta(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    data = models.DateField(db_column='Data', blank=True, null=True)  # Field name made lowercase.
    hora = models.TimeField(db_column='Hora', blank=True, null=True)  # Field name made lowercase.
    totalgeral = models.FloatField(db_column='TotalGeral', blank=True, null=True)  # Field name made lowercase.
    empresa = models.IntegerField(db_column='Empresa', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'orcconsulta'


class Os(models.Model):
    codigo = models.AutoField(db_column='Codigo', primary_key=True)  # Field name made lowercase.
    especie = models.IntegerField(db_column='Especie', blank=True, null=True)  # Field name made lowercase.
    datainicio = models.DateField(db_column='DataInicio', blank=True, null=True)  # Field name made lowercase.
    horainicio = models.TimeField(db_column='HoraInicio', blank=True, null=True)  # Field name made lowercase.
    previsaoentrega = models.DateField(db_column='PrevisaoEntrega', blank=True, null=True)  # Field name made lowercase.
    consultor = models.IntegerField(db_column='Consultor', blank=True, null=True)  # Field name made lowercase.
    oficina = models.IntegerField(db_column='Oficina', blank=True, null=True)  # Field name made lowercase.
    origem = models.IntegerField(blank=True, null=True)
    cliente = models.IntegerField(db_column='Cliente', blank=True, null=True)  # Field name made lowercase.
    hora = models.IntegerField(blank=True, null=True)
    veiculo = models.IntegerField(db_column='Veiculo', blank=True, null=True)  # Field name made lowercase.
    id_produto = models.IntegerField(blank=True, null=True)
    serie = models.CharField(max_length=20, blank=True, null=True)
    diagnostico = models.TextField(db_column='Diagnostico', blank=True, null=True)  # Field name made lowercase.
    observacao = models.TextField(db_column='Observacao', blank=True, null=True)  # Field name made lowercase.
    situacao = models.IntegerField(db_column='Situacao', blank=True, null=True)  # Field name made lowercase.
    datafinaliza = models.DateField(db_column='DataFinaliza', blank=True, null=True)  # Field name made lowercase.
    horafinaliza = models.TimeField(db_column='HoraFinaliza', blank=True, null=True)  # Field name made lowercase.
    liberadopor = models.IntegerField(db_column='LiberadoPor', blank=True, null=True)  # Field name made lowercase.
    motorista = models.CharField(db_column='Motorista', max_length=60, blank=True, null=True)  # Field name made lowercase.
    datafecha = models.DateField(db_column='DataFecha', blank=True, null=True)  # Field name made lowercase.
    horafecha = models.TimeField(db_column='HoraFecha', blank=True, null=True)  # Field name made lowercase.
    produto = models.FloatField(db_column='Produto', blank=True, null=True)  # Field name made lowercase.
    servico = models.FloatField(db_column='Servico', blank=True, null=True)  # Field name made lowercase.
    produtodescacre = models.FloatField(db_column='ProdutoDescAcre', blank=True, null=True)  # Field name made lowercase.
    servicodescacre = models.FloatField(db_column='ServicoDescAcre', blank=True, null=True)  # Field name made lowercase.
    total = models.FloatField(db_column='Total', blank=True, null=True)  # Field name made lowercase.
    descacre = models.FloatField(db_column='DescAcre', blank=True, null=True)  # Field name made lowercase.
    totalgeral = models.FloatField(db_column='TotalGeral', blank=True, null=True)  # Field name made lowercase.
    empresa = models.IntegerField(db_column='Empresa', blank=True, null=True)  # Field name made lowercase.
    usuario = models.IntegerField(db_column='Usuario', blank=True, null=True)  # Field name made lowercase.
    mecanico = models.IntegerField(db_column='Mecanico', blank=True, null=True)  # Field name made lowercase.
    nota = models.IntegerField(blank=True, null=True)
    notaeletronica = models.IntegerField(blank=True, null=True)
    serienf = models.IntegerField(db_column='serieNF', blank=True, null=True)  # Field name made lowercase.
    modelonf = models.IntegerField(db_column='modeloNF', blank=True, null=True)  # Field name made lowercase.
    rps = models.IntegerField(db_column='RPS', blank=True, null=True)  # Field name made lowercase.
    nfse = models.IntegerField(db_column='NFSe', blank=True, null=True)  # Field name made lowercase.
    nfstemp = models.IntegerField(db_column='NFSTemp', blank=True, null=True)  # Field name made lowercase.
    cfe = models.IntegerField(db_column='CFe', blank=True, null=True)  # Field name made lowercase.
    fatura = models.IntegerField(blank=True, null=True)
    equipamento = models.CharField(max_length=60, blank=True, null=True)
    modelo = models.CharField(max_length=40, blank=True, null=True)
    marca = models.CharField(max_length=40, blank=True, null=True)
    numeroserie = models.CharField(max_length=30, blank=True, null=True)
    acessorios = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'os'


class Pagamentos(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    codigo = models.IntegerField(db_column='Codigo', blank=True, null=True)  # Field name made lowercase.
    emissao = models.DateField(db_column='Emissao', blank=True, null=True)  # Field name made lowercase.
    tipo = models.CharField(db_column='Tipo', max_length=1, blank=True, null=True)  # Field name made lowercase.
    portador = models.IntegerField(db_column='Portador', blank=True, null=True)  # Field name made lowercase.
    clifor = models.IntegerField(db_column='CliFor', blank=True, null=True)  # Field name made lowercase.
    cliforant = models.IntegerField(blank=True, null=True)
    contaantiga = models.IntegerField(db_column='Contaantiga', blank=True, null=True)  # Field name made lowercase.
    condicoes = models.IntegerField(db_column='Condicoes', blank=True, null=True)  # Field name made lowercase.
    vencimento = models.DateField(db_column='Vencimento', blank=True, null=True)  # Field name made lowercase.
    valorprestacao = models.FloatField(db_column='ValorPrestacao', blank=True, null=True)  # Field name made lowercase.
    valordocumento = models.FloatField(db_column='ValorDocumento', blank=True, null=True)  # Field name made lowercase.
    observacao = models.CharField(db_column='Observacao', max_length=100, blank=True, null=True)  # Field name made lowercase.
    situacao = models.CharField(db_column='Situacao', max_length=1, blank=True, null=True)  # Field name made lowercase.
    diferenca = models.FloatField(db_column='Diferenca', blank=True, null=True)  # Field name made lowercase.
    valorpago = models.FloatField(db_column='ValorPago', blank=True, null=True)  # Field name made lowercase.
    datapagto = models.DateField(db_column='DataPagto', blank=True, null=True)  # Field name made lowercase.
    sequencia = models.IntegerField(db_column='Sequencia', blank=True, null=True)  # Field name made lowercase.
    pagocom = models.IntegerField(db_column='PagoCom', blank=True, null=True)  # Field name made lowercase.
    duplicata = models.CharField(db_column='Duplicata', max_length=30, blank=True, null=True)  # Field name made lowercase.
    quen = models.IntegerField(db_column='Quen', blank=True, null=True)  # Field name made lowercase.
    process = models.DateField(db_column='Process', blank=True, null=True)  # Field name made lowercase.
    empresa = models.IntegerField(db_column='Empresa', blank=True, null=True)  # Field name made lowercase.
    conta = models.IntegerField(blank=True, null=True)
    contadespesa = models.IntegerField(db_column='ContaDespesa', blank=True, null=True)  # Field name made lowercase.
    centrocusto = models.IntegerField(db_column='CentroCusto', blank=True, null=True)  # Field name made lowercase.
    pagamento = models.IntegerField(blank=True, null=True)
    id_cheque = models.IntegerField(blank=True, null=True)
    numeroaleatorio = models.IntegerField(db_column='NumeroAleatorio', blank=True, null=True)  # Field name made lowercase.
    renegociacao = models.IntegerField(db_column='Renegociacao', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pagamentos'


class PagamentosDetalhe(models.Model):
    id_pagamento = models.IntegerField(blank=True, null=True)
    pago_com = models.CharField(max_length=16, blank=True, null=True)
    id_cheque = models.IntegerField(blank=True, null=True)
    valor_pago = models.FloatField(blank=True, null=True)
    data_pagto = models.DateField(blank=True, null=True)
    usuario = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pagamentos_detalhe'


class PagamentosEvento(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    tipoajuste = models.CharField(db_column='TipoAjuste', max_length=30, blank=True, null=True)  # Field name made lowercase.
    controle = models.IntegerField(db_column='Controle', blank=True, null=True)  # Field name made lowercase.
    dataevento = models.DateField(db_column='DataEvento', blank=True, null=True)  # Field name made lowercase.
    horaevento = models.TimeField(db_column='HoraEvento', blank=True, null=True)  # Field name made lowercase.
    usuarioevento = models.IntegerField(db_column='UsuarioEvento', blank=True, null=True)  # Field name made lowercase.
    maquinaevento = models.CharField(db_column='MaquinaEvento', max_length=60, blank=True, null=True)  # Field name made lowercase.
    idold = models.IntegerField(db_column='IDold', blank=True, null=True)  # Field name made lowercase.
    codigo = models.IntegerField(db_column='Codigo', blank=True, null=True)  # Field name made lowercase.
    emissao = models.DateField(db_column='Emissao', blank=True, null=True)  # Field name made lowercase.
    tipo = models.CharField(db_column='Tipo', max_length=1, blank=True, null=True)  # Field name made lowercase.
    portador = models.IntegerField(db_column='Portador', blank=True, null=True)  # Field name made lowercase.
    clifor = models.IntegerField(db_column='CliFor', blank=True, null=True)  # Field name made lowercase.
    cliforant = models.IntegerField(blank=True, null=True)
    contaantiga = models.IntegerField(db_column='Contaantiga', blank=True, null=True)  # Field name made lowercase.
    condicoes = models.IntegerField(db_column='Condicoes', blank=True, null=True)  # Field name made lowercase.
    vencimento = models.DateField(db_column='Vencimento', blank=True, null=True)  # Field name made lowercase.
    valorprestacao = models.FloatField(db_column='ValorPrestacao', blank=True, null=True)  # Field name made lowercase.
    valordocumento = models.FloatField(db_column='ValorDocumento', blank=True, null=True)  # Field name made lowercase.
    observacao = models.CharField(db_column='Observacao', max_length=100, blank=True, null=True)  # Field name made lowercase.
    situacao = models.CharField(db_column='Situacao', max_length=1, blank=True, null=True)  # Field name made lowercase.
    diferenca = models.FloatField(db_column='Diferenca', blank=True, null=True)  # Field name made lowercase.
    valorpago = models.FloatField(db_column='ValorPago', blank=True, null=True)  # Field name made lowercase.
    datapagto = models.DateField(db_column='DataPagto', blank=True, null=True)  # Field name made lowercase.
    sequencia = models.IntegerField(db_column='Sequencia', blank=True, null=True)  # Field name made lowercase.
    pagocom = models.IntegerField(db_column='PagoCom', blank=True, null=True)  # Field name made lowercase.
    duplicata = models.CharField(db_column='Duplicata', max_length=30, blank=True, null=True)  # Field name made lowercase.
    quen = models.IntegerField(db_column='Quen', blank=True, null=True)  # Field name made lowercase.
    process = models.DateField(db_column='Process', blank=True, null=True)  # Field name made lowercase.
    empresa = models.IntegerField(db_column='Empresa', blank=True, null=True)  # Field name made lowercase.
    conta = models.IntegerField(blank=True, null=True)
    contadespesa = models.IntegerField(db_column='ContaDespesa', blank=True, null=True)  # Field name made lowercase.
    centrocusto = models.IntegerField(db_column='CentroCusto', blank=True, null=True)  # Field name made lowercase.
    pagamento = models.IntegerField(blank=True, null=True)
    id_cheque = models.IntegerField(blank=True, null=True)
    numeroaleatorio = models.IntegerField(db_column='NumeroAleatorio', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pagamentos_evento'


class PagamentosId(models.Model):
    data = models.DateField(blank=True, null=True)
    valor = models.FloatField(blank=True, null=True)
    descacre = models.FloatField(blank=True, null=True)
    valorpago = models.FloatField(blank=True, null=True)
    usuario = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    numeroaleatorio = models.IntegerField(blank=True, null=True)
    data_cancelamento = models.DateField(blank=True, null=True)
    hora_cancelamento = models.TimeField(blank=True, null=True)
    usuario_cancelamento = models.IntegerField(blank=True, null=True)
    maquina_cancelamento = models.CharField(max_length=50, blank=True, null=True)
    empresa = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pagamentos_id'


class PagamentosRenegociacao(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    data = models.DateField(db_column='Data', blank=True, null=True)  # Field name made lowercase.
    hora = models.TimeField(db_column='Hora', blank=True, null=True)  # Field name made lowercase.
    clifor = models.IntegerField(db_column='CliFor', blank=True, null=True)  # Field name made lowercase.
    usuario = models.IntegerField(db_column='Usuario', blank=True, null=True)  # Field name made lowercase.
    total = models.FloatField(db_column='Total', blank=True, null=True)  # Field name made lowercase.
    descacre = models.FloatField(db_column='DescAcre', blank=True, null=True)  # Field name made lowercase.
    totalfinal = models.FloatField(db_column='TotalFinal', blank=True, null=True)  # Field name made lowercase.
    maquina = models.CharField(db_column='Maquina', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pagamentos_renegociacao'


class Parametros(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    senhabaixareceber = models.CharField(db_column='SenhaBaixaReceber', max_length=30, blank=True, null=True)  # Field name made lowercase.
    senhaeditareceber = models.CharField(db_column='SenhaEditaReceber', max_length=30, blank=True, null=True)  # Field name made lowercase.
    printrecibo = models.CharField(db_column='PrintRecibo', max_length=30, blank=True, null=True)  # Field name made lowercase.
    senhaprintrecibo = models.CharField(db_column='SenhaPrintRecibo', max_length=30, blank=True, null=True)  # Field name made lowercase.
    senhaposicaor = models.CharField(db_column='SenhaPosicaoR', max_length=30, blank=True, null=True)  # Field name made lowercase.
    senhabordero = models.CharField(db_column='SenhaBordero', max_length=30, blank=True, null=True)  # Field name made lowercase.
    senhaosr = models.CharField(db_column='SenhaOSR', max_length=30, blank=True, null=True)  # Field name made lowercase.
    senhaposicaop = models.CharField(db_column='SenhaPosicaoP', max_length=30, blank=True, null=True)  # Field name made lowercase.
    senhaeditapagar = models.CharField(db_column='SenhaEditaPagar', max_length=30, blank=True, null=True)  # Field name made lowercase.
    senhabaixapagar = models.CharField(db_column='SenhaBaixaPagar', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fechaose = models.CharField(db_column='FechaOsE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    numeronota = models.IntegerField(db_column='NumeroNota', blank=True, null=True)  # Field name made lowercase.
    fatura = models.IntegerField(db_column='Fatura', blank=True, null=True)  # Field name made lowercase.
    iss = models.FloatField(db_column='ISS', blank=True, null=True)  # Field name made lowercase.
    orcamento = models.IntegerField(db_column='Orcamento', blank=True, null=True)  # Field name made lowercase.
    printrequisicao = models.CharField(db_column='PrintRequisicao', max_length=50, blank=True, null=True)  # Field name made lowercase.
    printpneu = models.CharField(db_column='PrintPneu', max_length=30, blank=True, null=True)  # Field name made lowercase.
    printinventario = models.CharField(db_column='PrintInventario', max_length=30, blank=True, null=True)  # Field name made lowercase.
    printmovimento = models.CharField(db_column='PrintMovimento', max_length=30, blank=True, null=True)  # Field name made lowercase.
    senhaedvalos = models.CharField(db_column='SenhaEdValOs', max_length=30, blank=True, null=True)  # Field name made lowercase.
    senhaeddesos = models.CharField(db_column='SenhaEdDesOs', max_length=30, blank=True, null=True)  # Field name made lowercase.
    senhaesvalos = models.CharField(db_column='SenhaEsValOs', max_length=30, blank=True, null=True)  # Field name made lowercase.
    senhaesdesos = models.CharField(db_column='SenhaEsDesOs', max_length=30, blank=True, null=True)  # Field name made lowercase.
    numerobalcao = models.IntegerField(db_column='NumeroBalcao', blank=True, null=True)  # Field name made lowercase.
    conscli = models.IntegerField(db_column='ConsCli', blank=True, null=True)  # Field name made lowercase.
    consfor = models.IntegerField(db_column='ConsFor', blank=True, null=True)  # Field name made lowercase.
    conspro = models.IntegerField(db_column='ConsPro', blank=True, null=True)  # Field name made lowercase.
    ultcodigop = models.IntegerField(db_column='UltCodigoP', blank=True, null=True)  # Field name made lowercase.
    codigopro = models.IntegerField(db_column='CodigoPro', blank=True, null=True)  # Field name made lowercase.
    arredonda = models.IntegerField(db_column='Arredonda', blank=True, null=True)  # Field name made lowercase.
    printcarta = models.CharField(db_column='PrintCarta', max_length=30, blank=True, null=True)  # Field name made lowercase.
    itemlista = models.CharField(db_column='ItemLista', max_length=10, blank=True, null=True)  # Field name made lowercase.
    cfps = models.CharField(db_column='CFPS', max_length=10, blank=True, null=True)  # Field name made lowercase.
    maquina = models.CharField(db_column='Maquina', max_length=50, blank=True, null=True)  # Field name made lowercase.
    empresa = models.IntegerField(db_column='Empresa', blank=True, null=True)  # Field name made lowercase.
    printdemais = models.CharField(db_column='PrintDemais', max_length=50, blank=True, null=True)  # Field name made lowercase.
    estatistica = models.IntegerField(db_column='Estatistica', blank=True, null=True)  # Field name made lowercase.
    textoaniversario = models.CharField(db_column='TextoAniversario', max_length=150, blank=True, null=True)  # Field name made lowercase.
    dias = models.IntegerField(blank=True, null=True)
    backup = models.DateField(db_column='Backup', blank=True, null=True)  # Field name made lowercase.
    mcf = models.IntegerField(db_column='mCF', blank=True, null=True)  # Field name made lowercase.
    mgem = models.IntegerField(db_column='mGEM', blank=True, null=True)  # Field name made lowercase.
    mmanifesto = models.IntegerField(db_column='mManifesto', blank=True, null=True)  # Field name made lowercase.
    mexpedicao = models.IntegerField(db_column='mExpedicao', blank=True, null=True)  # Field name made lowercase.
    codigobaixaparcial = models.IntegerField(db_column='CodigoBaixaParcial', blank=True, null=True)  # Field name made lowercase.
    baixaparcial = models.IntegerField(blank=True, null=True)
    data_baixaparcial = models.IntegerField(blank=True, null=True)
    alteraprecovenda = models.CharField(max_length=3, blank=True, null=True)
    id_kit = models.IntegerField(blank=True, null=True)
    codigo_automatico = models.CharField(max_length=5, blank=True, null=True)
    numerorecebe = models.IntegerField(blank=True, null=True)
    duplicata = models.IntegerField(blank=True, null=True)
    carta_cobranca = models.IntegerField(blank=True, null=True)
    credito = models.IntegerField(blank=True, null=True)
    separacao = models.IntegerField(blank=True, null=True)
    desconto_recebimento = models.FloatField(blank=True, null=True)
    desconto_recebimento_gerencial = models.FloatField(blank=True, null=True)
    desconto_vendas = models.FloatField(blank=True, null=True)
    desconto_vendas_gerencial = models.FloatField(blank=True, null=True)
    baixa_minimo = models.CharField(max_length=3, blank=True, null=True)
    maximo_vendas = models.FloatField(blank=True, null=True)
    checa_tabela_venda = models.IntegerField(blank=True, null=True)
    usar_ordem_devolucao = models.IntegerField(blank=True, null=True)
    lote_cheque = models.IntegerField(blank=True, null=True)
    modelo_notafiscal = models.IntegerField(blank=True, null=True)
    msg1_nf = models.CharField(max_length=200, blank=True, null=True)
    msg2_nf = models.CharField(max_length=200, blank=True, null=True)
    msg3_nf = models.CharField(max_length=200, blank=True, null=True)
    msg4_nf = models.CharField(max_length=200, blank=True, null=True)
    msg5_nf = models.CharField(max_length=200, blank=True, null=True)
    msg6_nf = models.CharField(max_length=200, blank=True, null=True)
    dias_restricao_credito = models.IntegerField(blank=True, null=True)
    tipo_venda = models.IntegerField(blank=True, null=True)
    imprimir_draft = models.IntegerField(blank=True, null=True)
    atualizacao_bd = models.DateField(blank=True, null=True)
    versao_software = models.CharField(max_length=10, blank=True, null=True)
    data_versao_software = models.DateField(blank=True, null=True)
    altera_preco_entrada_mercadoria = models.CharField(max_length=3, blank=True, null=True)
    fone_atualizado = models.CharField(max_length=3, blank=True, null=True)
    limite_dias_recebimento_cheque = models.IntegerField(blank=True, null=True)
    limite_dias_atraso_desconto = models.IntegerField(blank=True, null=True)
    limite_venda_cliente_monitorado = models.FloatField(blank=True, null=True)
    agrupa_produtos_nf = models.IntegerField(blank=True, null=True)
    cliente_venda_atacado = models.IntegerField(blank=True, null=True)
    modelo_tabela_similar = models.IntegerField(blank=True, null=True)
    maquinas = models.IntegerField(blank=True, null=True)
    compor_cheque_limite_cliente = models.IntegerField(blank=True, null=True)
    dias_antes_data_cheque = models.IntegerField(blank=True, null=True)
    inf_conta_baixa_banco = models.IntegerField(blank=True, null=True)
    credito_restrito_cliente_novo = models.IntegerField(blank=True, null=True, db_comment='0 = false / 1 - true')
    consvendaprodcli = models.IntegerField(db_column='ConsVendaProdCli', blank=True, null=True, db_comment='Consulta de vendas do produto para o cliente')  # Field name made lowercase.
    checacustomedioentradanf = models.IntegerField(db_column='ChecaCustoMedioEntradaNF', blank=True, null=True)  # Field name made lowercase.
    pdvmodovenda = models.IntegerField(db_column='PdvModoVenda', blank=True, null=True, db_comment='0 = normal / 1 = alterar val unit do produto')  # Field name made lowercase.
    pdvmodorecebimento = models.IntegerField(db_column='PdvModoRecebimento', blank=True, null=True, db_comment='0-Por Titulo 1-Por Produto')  # Field name made lowercase.
    caixageral = models.IntegerField(db_column='CaixaGeral', blank=True, null=True, db_comment='0 = false / 1 = true')  # Field name made lowercase.
    promissoriaordemservico = models.IntegerField(db_column='PromissoriaOrdemServico', blank=True, null=True)  # Field name made lowercase.
    vercustotelavenda = models.IntegerField(db_column='VerCustoTelaVenda', blank=True, null=True)  # Field name made lowercase.
    ativastf = models.IntegerField(db_column='AtivaSTF', blank=True, null=True)  # Field name made lowercase.
    fatorpeso = models.FloatField(db_column='FatorPeso', blank=True, null=True)  # Field name made lowercase.
    usartabeladescontocliente = models.IntegerField(db_column='UsarTabelaDescontoCliente', blank=True, null=True)  # Field name made lowercase.
    informarenderecoexpedicao = models.IntegerField(db_column='InformarEnderecoExpedicao', blank=True, null=True)  # Field name made lowercase.
    baixarvendavista = models.IntegerField(db_column='BaixarVendaVista', blank=True, null=True)  # Field name made lowercase.
    imprimirdebitonorecibo = models.IntegerField(db_column='ImprimirDebitoNoRecibo', blank=True, null=True)  # Field name made lowercase.
    ultimonsu = models.IntegerField(db_column='UltimoNSU', blank=True, null=True)  # Field name made lowercase.
    caminhobalanca = models.CharField(db_column='CaminhoBalanca', max_length=255, blank=True, null=True)  # Field name made lowercase.
    modelobalanca = models.IntegerField(db_column='ModeloBalanca', blank=True, null=True)  # Field name made lowercase.
    identificaclientepdv = models.IntegerField(db_column='IdentificaClientePDV', blank=True, null=True)  # Field name made lowercase.
    alertaabrevendapdv = models.IntegerField(db_column='AlertaAbreVendaPDV', blank=True, null=True)  # Field name made lowercase.
    ativacomandapdv = models.IntegerField(db_column='AtivaComandaPDV', blank=True, null=True)  # Field name made lowercase.
    infendcomandapdv = models.IntegerField(db_column='InfEndComandaPDV', blank=True, null=True)  # Field name made lowercase.
    usarexpedicao = models.IntegerField(db_column='UsarExpedicao', blank=True, null=True)  # Field name made lowercase.
    aceitavendaalteracao = models.IntegerField(db_column='AceitaVendaAlteracao', blank=True, null=True)  # Field name made lowercase.
    imprimirdescduaslinhas = models.IntegerField(db_column='ImprimirDescDuasLinhas', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'parametros'


class Pdv(models.Model):
    codigo = models.AutoField(db_column='Codigo', primary_key=True)  # Field name made lowercase.
    cliente = models.IntegerField(db_column='Cliente', blank=True, null=True)  # Field name made lowercase.
    vendedor = models.IntegerField(db_column='Vendedor', blank=True, null=True)  # Field name made lowercase.
    portador = models.CharField(db_column='Portador', max_length=60, blank=True, null=True)  # Field name made lowercase.
    situacao = models.IntegerField(db_column='Situacao', blank=True, null=True)  # Field name made lowercase.
    data = models.DateField(db_column='Data', blank=True, null=True)  # Field name made lowercase.
    hora = models.TimeField(db_column='Hora', blank=True, null=True)  # Field name made lowercase.
    subtotal = models.FloatField(db_column='SubTotal', blank=True, null=True)  # Field name made lowercase.
    desconto = models.FloatField(db_column='Desconto', blank=True, null=True)  # Field name made lowercase.
    total = models.FloatField(db_column='Total', blank=True, null=True)  # Field name made lowercase.
    porcento = models.FloatField(db_column='Porcento', blank=True, null=True)  # Field name made lowercase.
    empresa = models.IntegerField(db_column='Empresa', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pdv'


class PdvParametros(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    maquina = models.CharField(db_column='Maquina', max_length=30, blank=True, null=True)  # Field name made lowercase.
    nomemaquina = models.CharField(db_column='NomeMaquina', max_length=30, blank=True, null=True)  # Field name made lowercase.
    id_caixa = models.IntegerField(db_column='ID_Caixa', blank=True, null=True)  # Field name made lowercase.
    habilitarsat = models.IntegerField(db_column='HabilitarSat', blank=True, null=True)  # Field name made lowercase.
    codigoconsumidor = models.IntegerField(db_column='CodigoConsumidor', blank=True, null=True)  # Field name made lowercase.
    alteraprecovenda = models.IntegerField(db_column='AlteraPrecoVenda', blank=True, null=True)  # Field name made lowercase.
    codificacaobalanca = models.CharField(db_column='CodificacaoBalanca', max_length=14, blank=True, null=True)  # Field name made lowercase.
    codigobalancakilo = models.IntegerField(db_column='CodigoBalancaKilo', blank=True, null=True)  # Field name made lowercase.
    logopdv = models.CharField(db_column='LogoPDV', max_length=250, blank=True, null=True)  # Field name made lowercase.
    perguntaimprimir = models.IntegerField(db_column='PerguntaImprimir', blank=True, null=True)  # Field name made lowercase.
    datalogado = models.DateTimeField(db_column='DataLogado', blank=True, null=True)  # Field name made lowercase.
    horalogado = models.TimeField(db_column='HoraLogado', blank=True, null=True)  # Field name made lowercase.
    versaopdv = models.CharField(db_column='VersaoPDV', max_length=10, blank=True, null=True)  # Field name made lowercase.
    balmodelo = models.IntegerField(db_column='BalModelo', blank=True, null=True)  # Field name made lowercase.
    balporta = models.CharField(db_column='BalPorta', max_length=8, blank=True, null=True)  # Field name made lowercase.
    balbaudrate = models.IntegerField(db_column='BalBaudRate', blank=True, null=True)  # Field name made lowercase.
    baldatabits = models.IntegerField(db_column='BalDataBits', blank=True, null=True)  # Field name made lowercase.
    balparity = models.IntegerField(db_column='BalParity', blank=True, null=True)  # Field name made lowercase.
    balstopbits = models.IntegerField(db_column='BalStopBits', blank=True, null=True)  # Field name made lowercase.
    balhandshake = models.IntegerField(db_column='BalHandshake', blank=True, null=True)  # Field name made lowercase.
    baltimeout = models.IntegerField(db_column='BalTimeOut', blank=True, null=True)  # Field name made lowercase.
    balarqlog = models.CharField(db_column='BalArqLog', max_length=100, blank=True, null=True)  # Field name made lowercase.
    balmonitorar = models.IntegerField(db_column='BalMonitorar', blank=True, null=True)  # Field name made lowercase.
    balativa = models.IntegerField(db_column='BalAtiva', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pdv_parametros'


class PdvVendaCancelada(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    pdv = models.IntegerField(db_column='PDV', blank=True, null=True)  # Field name made lowercase.
    caixa = models.IntegerField(db_column='Caixa', blank=True, null=True)  # Field name made lowercase.
    nos = models.IntegerField(db_column='NOS', blank=True, null=True)  # Field name made lowercase.
    cliente = models.IntegerField(blank=True, null=True)
    tipo = models.CharField(max_length=5, blank=True, null=True)
    codigobarra = models.CharField(db_column='CodigoBarra', max_length=30, blank=True, null=True)  # Field name made lowercase.
    codigo = models.CharField(db_column='Codigo', max_length=30, blank=True, null=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=100, blank=True, null=True)  # Field name made lowercase.
    aplicacao = models.CharField(db_column='Aplicacao', max_length=40, blank=True, null=True)  # Field name made lowercase.
    quantidade = models.FloatField(db_column='Quantidade', blank=True, null=True)  # Field name made lowercase.
    unitario = models.FloatField(db_column='Unitario', blank=True, null=True)  # Field name made lowercase.
    total = models.FloatField(db_column='Total', blank=True, null=True)  # Field name made lowercase.
    descacre = models.FloatField(db_column='DescAcre', blank=True, null=True)  # Field name made lowercase.
    vendaunitario = models.FloatField(blank=True, null=True)
    vendatotal = models.FloatField(blank=True, null=True)
    unidade = models.CharField(max_length=2, blank=True, null=True)
    funcionario = models.IntegerField(db_column='Funcionario', blank=True, null=True)  # Field name made lowercase.
    datavenda = models.DateField(db_column='DataVenda', blank=True, null=True)  # Field name made lowercase.
    data = models.DateField(db_column='Data', blank=True, null=True)  # Field name made lowercase.
    hora = models.TimeField(db_column='Hora', blank=True, null=True)  # Field name made lowercase.
    custo = models.FloatField(db_column='Custo', blank=True, null=True)  # Field name made lowercase.
    medio = models.FloatField(blank=True, null=True)
    venda = models.FloatField(db_column='Venda', blank=True, null=True)  # Field name made lowercase.
    usuario = models.IntegerField(db_column='Usuario', blank=True, null=True)  # Field name made lowercase.
    grupo = models.IntegerField(db_column='Grupo', blank=True, null=True)  # Field name made lowercase.
    grupodesc = models.CharField(db_column='GrupoDesc', max_length=60, blank=True, null=True)  # Field name made lowercase.
    linha = models.IntegerField(db_column='Linha', blank=True, null=True)  # Field name made lowercase.
    linhadesc = models.CharField(db_column='LinhaDesc', max_length=60, blank=True, null=True)  # Field name made lowercase.
    fabricante = models.IntegerField(db_column='Fabricante', blank=True, null=True)  # Field name made lowercase.
    fabricantedesc = models.CharField(db_column='FabricanteDesc', max_length=60, blank=True, null=True)  # Field name made lowercase.
    reduzido = models.CharField(max_length=30, blank=True, null=True)
    id_kit = models.IntegerField(blank=True, null=True)
    pedido = models.IntegerField(blank=True, null=True)
    profissional = models.IntegerField(blank=True, null=True)
    empresa = models.IntegerField(db_column='Empresa', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pdv_venda_cancelada'


class Pdvpagto(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    forma = models.CharField(db_column='Forma', max_length=3, blank=True, null=True)  # Field name made lowercase.
    vencimento = models.DateField(db_column='Vencimento', blank=True, null=True)  # Field name made lowercase.
    valor = models.FloatField(db_column='Valor', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pdvpagto'


class Pdvprod(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nbalcao = models.IntegerField(db_column='NBalcao', blank=True, null=True)  # Field name made lowercase.
    codigo = models.CharField(db_column='Codigo', max_length=30, blank=True, null=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=100, blank=True, null=True)  # Field name made lowercase.
    quantidade = models.FloatField(db_column='Quantidade', blank=True, null=True)  # Field name made lowercase.
    preco = models.FloatField(db_column='Preco', blank=True, null=True)  # Field name made lowercase.
    desconto = models.FloatField(db_column='Desconto', blank=True, null=True)  # Field name made lowercase.
    unitario = models.FloatField(db_column='Unitario', blank=True, null=True)  # Field name made lowercase.
    total = models.FloatField(db_column='Total', blank=True, null=True)  # Field name made lowercase.
    data = models.DateField(db_column='Data', blank=True, null=True)  # Field name made lowercase.
    hora = models.TimeField(db_column='Hora', blank=True, null=True)  # Field name made lowercase.
    vendedor = models.IntegerField(db_column='Vendedor', blank=True, null=True)  # Field name made lowercase.
    portador = models.CharField(db_column='Portador', max_length=60, blank=True, null=True)  # Field name made lowercase.
    situacao = models.IntegerField(db_column='Situacao', blank=True, null=True)  # Field name made lowercase.
    grupo = models.IntegerField(db_column='Grupo', blank=True, null=True)  # Field name made lowercase.
    grupodesc = models.CharField(db_column='GrupoDesc', max_length=60, blank=True, null=True)  # Field name made lowercase.
    linha = models.IntegerField(db_column='Linha', blank=True, null=True)  # Field name made lowercase.
    linhadesc = models.CharField(db_column='LinhaDesc', max_length=60, blank=True, null=True)  # Field name made lowercase.
    fabricante = models.IntegerField(db_column='Fabricante', blank=True, null=True)  # Field name made lowercase.
    fabricantedesc = models.CharField(db_column='FabricanteDesc', max_length=60, blank=True, null=True)  # Field name made lowercase.
    empresa = models.IntegerField(db_column='Empresa', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pdvprod'


class Pdvreq(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    req = models.IntegerField(db_column='Req', blank=True, null=True)  # Field name made lowercase.
    cliente = models.IntegerField(db_column='Cliente', blank=True, null=True)  # Field name made lowercase.
    vendedor = models.CharField(db_column='Vendedor', max_length=70, blank=True, null=True)  # Field name made lowercase.
    portador = models.CharField(db_column='Portador', max_length=60, blank=True, null=True)  # Field name made lowercase.
    data = models.DateField(db_column='Data', blank=True, null=True)  # Field name made lowercase.
    hora = models.TimeField(db_column='Hora', blank=True, null=True)  # Field name made lowercase.
    codigo = models.CharField(db_column='Codigo', max_length=30, blank=True, null=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=100, blank=True, null=True)  # Field name made lowercase.
    quantidade = models.FloatField(db_column='Quantidade', blank=True, null=True)  # Field name made lowercase.
    preco = models.FloatField(db_column='Preco', blank=True, null=True)  # Field name made lowercase.
    desconto = models.FloatField(db_column='Desconto', blank=True, null=True)  # Field name made lowercase.
    unitario = models.FloatField(db_column='Unitario', blank=True, null=True)  # Field name made lowercase.
    total = models.FloatField(db_column='Total', blank=True, null=True)  # Field name made lowercase.
    totalgeral = models.FloatField(db_column='TotalGeral', blank=True, null=True)  # Field name made lowercase.
    descacre = models.FloatField(db_column='DescAcre', blank=True, null=True)  # Field name made lowercase.
    bruto = models.FloatField(db_column='Bruto', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pdvreq'


class Pedidos(models.Model):
    codigo = models.AutoField(db_column='Codigo', primary_key=True)  # Field name made lowercase.
    fornecedor = models.IntegerField(db_column='Fornecedor', blank=True, null=True)  # Field name made lowercase.
    process = models.DateField(db_column='Process', blank=True, null=True)  # Field name made lowercase.
    hora = models.TimeField(db_column='Hora', blank=True, null=True)  # Field name made lowercase.
    empresa = models.IntegerField(db_column='Empresa', blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status', blank=True, null=True, db_comment='0-aberto 1-finalizado')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pedidos'


class Pedidosdetalhe(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status', blank=True, null=True, db_comment='0-aberto 1-finalizado')  # Field name made lowercase.
    pedido = models.IntegerField(db_column='Pedido', blank=True, null=True)  # Field name made lowercase.
    codigo = models.CharField(db_column='Codigo', max_length=30, blank=True, null=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=100, blank=True, null=True)  # Field name made lowercase.
    utilizacao = models.CharField(db_column='Utilizacao', max_length=100, blank=True, null=True)  # Field name made lowercase.
    fabricante = models.IntegerField(db_column='Fabricante', blank=True, null=True)  # Field name made lowercase.
    quantidade = models.FloatField(db_column='Quantidade', blank=True, null=True)  # Field name made lowercase.
    codigoforn = models.CharField(db_column='CodigoForn', max_length=30, blank=True, null=True)  # Field name made lowercase.
    custo = models.FloatField(db_column='Custo', blank=True, null=True)  # Field name made lowercase.
    total = models.FloatField(db_column='Total', blank=True, null=True)  # Field name made lowercase.
    data = models.DateField(db_column='Data', blank=True, null=True)  # Field name made lowercase.
    hora = models.TimeField(db_column='Hora', blank=True, null=True)  # Field name made lowercase.
    empresa = models.IntegerField(db_column='Empresa', blank=True, null=True)  # Field name made lowercase.
    estoque = models.FloatField(db_column='Estoque', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pedidosdetalhe'


class Planocontas(models.Model):
    codigo = models.AutoField(db_column='Codigo', primary_key=True)  # Field name made lowercase.
    conta = models.CharField(db_column='Conta', max_length=80, blank=True, null=True)  # Field name made lowercase.
    linha = models.IntegerField(db_column='Linha', blank=True, null=True)  # Field name made lowercase.
    valido = models.IntegerField(db_column='Valido', blank=True, null=True)  # Field name made lowercase.
    empresa = models.IntegerField(db_column='Empresa', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'planocontas'


class Prodnfe(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    tipo = models.IntegerField(db_column='Tipo', blank=True, null=True)  # Field name made lowercase.
    forcli = models.IntegerField(db_column='Forcli', blank=True, null=True)  # Field name made lowercase.
    nf = models.IntegerField(db_column='NF', blank=True, null=True)  # Field name made lowercase.
    fornecedor = models.IntegerField(db_column='Fornecedor', blank=True, null=True)  # Field name made lowercase.
    codigo = models.CharField(db_column='Codigo', max_length=30, blank=True, null=True)  # Field name made lowercase.
    codigofornecedor = models.CharField(db_column='CodigoFornecedor', max_length=60, blank=True, null=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=60, blank=True, null=True)  # Field name made lowercase.
    cean = models.CharField(db_column='cEAN', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ncm = models.CharField(db_column='NCM', max_length=8, blank=True, null=True)  # Field name made lowercase.
    cfop = models.CharField(db_column='CFOP', max_length=5, blank=True, null=True)  # Field name made lowercase.
    csticms = models.CharField(db_column='CSTICMS', max_length=5, blank=True, null=True)  # Field name made lowercase.
    cstpis = models.CharField(db_column='CSTPIS', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cstcofins = models.CharField(db_column='CSTCOFINS', max_length=2, blank=True, null=True)  # Field name made lowercase.
    quantidade = models.FloatField(db_column='Quantidade', blank=True, null=True)  # Field name made lowercase.
    unitario = models.FloatField(db_column='Unitario', blank=True, null=True)  # Field name made lowercase.
    valorproduto = models.FloatField(db_column='ValorProduto', blank=True, null=True)  # Field name made lowercase.
    customedio = models.FloatField(db_column='CustoMedio', blank=True, null=True)  # Field name made lowercase.
    markup = models.FloatField(db_column='Markup', blank=True, null=True)  # Field name made lowercase.
    frete = models.FloatField(db_column='Frete', blank=True, null=True)  # Field name made lowercase.
    freteterceiros = models.FloatField(db_column='FreteTerceiros', blank=True, null=True)  # Field name made lowercase.
    seguro = models.FloatField(db_column='Seguro', blank=True, null=True)  # Field name made lowercase.
    desconto = models.FloatField(db_column='Desconto', blank=True, null=True)  # Field name made lowercase.
    outros = models.FloatField(db_column='Outros', blank=True, null=True)  # Field name made lowercase.
    icmsst = models.FloatField(db_column='ICMSST', blank=True, null=True)  # Field name made lowercase.
    ipi = models.FloatField(db_column='IPI', blank=True, null=True)  # Field name made lowercase.
    total = models.FloatField(db_column='Total', blank=True, null=True)  # Field name made lowercase.
    custoanterior = models.FloatField(db_column='CustoAnterior', blank=True, null=True)  # Field name made lowercase.
    precovenda = models.FloatField(db_column='PrecoVenda', blank=True, null=True)  # Field name made lowercase.
    grupo = models.IntegerField(db_column='Grupo', blank=True, null=True)  # Field name made lowercase.
    grupodesc = models.CharField(db_column='GrupoDesc', max_length=60, blank=True, null=True)  # Field name made lowercase.
    linha = models.IntegerField(db_column='Linha', blank=True, null=True)  # Field name made lowercase.
    linhadesc = models.CharField(db_column='LinhaDesc', max_length=60, blank=True, null=True)  # Field name made lowercase.
    fabricante = models.IntegerField(db_column='Fabricante', blank=True, null=True)  # Field name made lowercase.
    fabricantedesc = models.CharField(db_column='FabricanteDesc', max_length=60, blank=True, null=True)  # Field name made lowercase.
    process = models.DateField(db_column='Process', blank=True, null=True)  # Field name made lowercase.
    hora = models.TimeField(db_column='Hora', blank=True, null=True)  # Field name made lowercase.
    emissao = models.DateField(db_column='Emissao', blank=True, null=True)  # Field name made lowercase.
    empresa = models.IntegerField(db_column='Empresa', blank=True, null=True)  # Field name made lowercase.
    usuario = models.IntegerField(db_column='Usuario', blank=True, null=True)  # Field name made lowercase.
    estoqueant = models.FloatField(blank=True, null=True)
    falha = models.CharField(max_length=40, blank=True, null=True)
    contagem = models.FloatField(db_column='Contagem', blank=True, null=True)  # Field name made lowercase.
    idlote = models.IntegerField(db_column='IDLote', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'prodnfe'


class Prodreq(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    cliente = models.IntegerField(db_column='Cliente', blank=True, null=True)  # Field name made lowercase.
    codigo = models.CharField(db_column='Codigo', max_length=30, blank=True, null=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=100, blank=True, null=True)  # Field name made lowercase.
    aplicacao = models.CharField(db_column='Aplicacao', max_length=40, blank=True, null=True)  # Field name made lowercase.
    quantidade = models.FloatField(db_column='Quantidade', blank=True, null=True)  # Field name made lowercase.
    unitario = models.FloatField(db_column='Unitario', blank=True, null=True)  # Field name made lowercase.
    total = models.FloatField(db_column='Total', blank=True, null=True)  # Field name made lowercase.
    unidade = models.CharField(db_column='Unidade', max_length=2, blank=True, null=True)  # Field name made lowercase.
    quantunidade = models.FloatField(db_column='QuantUnidade', blank=True, null=True)  # Field name made lowercase.
    peso = models.FloatField(db_column='Peso', blank=True, null=True)  # Field name made lowercase.
    precopeso = models.CharField(db_column='PrecoPeso', max_length=1, blank=True, null=True)  # Field name made lowercase.
    devolvido = models.CharField(db_column='Devolvido', max_length=1, blank=True, null=True)  # Field name made lowercase.
    funcionario = models.IntegerField(db_column='Funcionario', blank=True, null=True)  # Field name made lowercase.
    data = models.DateField(db_column='Data', blank=True, null=True)  # Field name made lowercase.
    hora = models.TimeField(db_column='Hora', blank=True, null=True)  # Field name made lowercase.
    custo = models.FloatField(db_column='Custo', blank=True, null=True)  # Field name made lowercase.
    medio = models.FloatField(db_column='Medio', blank=True, null=True)  # Field name made lowercase.
    venda = models.FloatField(db_column='Venda', blank=True, null=True)  # Field name made lowercase.
    usuario = models.IntegerField(db_column='Usuario', blank=True, null=True)  # Field name made lowercase.
    grupo = models.IntegerField(db_column='Grupo', blank=True, null=True)  # Field name made lowercase.
    grupodesc = models.CharField(db_column='GrupoDesc', max_length=60, blank=True, null=True)  # Field name made lowercase.
    linha = models.IntegerField(db_column='Linha', blank=True, null=True)  # Field name made lowercase.
    linhadesc = models.CharField(db_column='LinhaDesc', max_length=60, blank=True, null=True)  # Field name made lowercase.
    fabricante = models.IntegerField(db_column='Fabricante', blank=True, null=True)  # Field name made lowercase.
    fabricantedesc = models.CharField(db_column='FabricanteDesc', max_length=60, blank=True, null=True)  # Field name made lowercase.
    reduzido = models.CharField(db_column='Reduzido', max_length=30, blank=True, null=True)  # Field name made lowercase.
    id_listadetalhe = models.IntegerField(db_column='ID_ListaDetalhe', blank=True, null=True)  # Field name made lowercase.
    pedido = models.IntegerField(db_column='Pedido', blank=True, null=True)  # Field name made lowercase.
    observacao = models.CharField(db_column='Observacao', max_length=50, blank=True, null=True)  # Field name made lowercase.
    empresa = models.IntegerField(db_column='Empresa', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'prodreq'


class ProducaoControle(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    situacao = models.IntegerField(db_column='Situacao', blank=True, null=True, db_comment='0-Em Aberto, 1-Em Andamento, 2-Finalizada')  # Field name made lowercase.
    codprod = models.CharField(db_column='CODPROD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    coduniversal = models.CharField(db_column='CODUNIVERSAL', max_length=20, blank=True, null=True)  # Field name made lowercase.
    proddesc = models.CharField(db_column='PRODDESC', max_length=200, blank=True, null=True)  # Field name made lowercase.
    usuariocriacao = models.IntegerField(db_column='UsuarioCriacao', blank=True, null=True)  # Field name made lowercase.
    datacriacao = models.DateTimeField(db_column='DataCriacao', blank=True, null=True)  # Field name made lowercase.
    usuariofinalizacao = models.IntegerField(db_column='UsuarioFinalizacao', blank=True, null=True)  # Field name made lowercase.
    dataproducao = models.DateTimeField(db_column='DataProducao', blank=True, null=True)  # Field name made lowercase.
    basedecalculoformula = models.FloatField(db_column='BaseDeCalculoFormula', blank=True, null=True)  # Field name made lowercase.
    qtd_produzida = models.FloatField(db_column='QTD_PRODUZIDA', blank=True, null=True)  # Field name made lowercase.
    unidade = models.CharField(db_column='UNIDADE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    qtd_produzida_gr = models.FloatField(db_column='QTD_PRODUZIDA_GR', blank=True, null=True)  # Field name made lowercase.
    qtd_produzida_ml = models.FloatField(db_column='QTD_PRODUZIDA_ML', blank=True, null=True)  # Field name made lowercase.
    custo = models.FloatField(db_column='CUSTO', blank=True, null=True)  # Field name made lowercase.
    observacao = models.TextField(db_column='OBSERVACAO', blank=True, null=True)  # Field name made lowercase.
    obsformula = models.TextField(db_column='ObsFormula', blank=True, null=True)  # Field name made lowercase.
    numeroaleatorio = models.IntegerField(db_column='NUMEROALEATORIO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'producao_controle'


class ProducaoItens(models.Model):
    codproducao = models.IntegerField(db_column='CODPRODUCAO', blank=True, null=True)  # Field name made lowercase.
    data_producao = models.DateTimeField(db_column='Data_producao', blank=True, null=True)  # Field name made lowercase.
    codprod = models.CharField(db_column='CODPROD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    lote = models.CharField(db_column='LOTE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    validade = models.DateField(db_column='VALIDADE', blank=True, null=True)  # Field name made lowercase.
    qtd_gr_receita = models.FloatField(db_column='QTD_GR_RECEITA', blank=True, null=True)  # Field name made lowercase.
    qtd_gr_ajuste = models.FloatField(db_column='QTD_GR_AJUSTE', blank=True, null=True)  # Field name made lowercase.
    qtd_gr_final = models.FloatField(db_column='QTD_GR_FINAL', blank=True, null=True)  # Field name made lowercase.
    qtd_ml = models.FloatField(db_column='QTD_ML', blank=True, null=True)  # Field name made lowercase.
    qtdunestoqueformula = models.FloatField(db_column='QtdUnEstoqueFormula', blank=True, null=True)  # Field name made lowercase.
    qtdunestoqueajuste = models.FloatField(db_column='QtdUnEstoqueAjuste', blank=True, null=True)  # Field name made lowercase.
    qtd_un_estoque = models.FloatField(db_column='QTD_UN_ESTOQUE', blank=True, null=True)  # Field name made lowercase.
    unidade = models.CharField(db_column='Unidade', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'producao_itens'


class Produtos(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    codigo = models.CharField(db_column='Codigo', max_length=30, blank=True, null=True)  # Field name made lowercase.
    codigofabrica = models.CharField(db_column='CodigoFabrica', max_length=30, blank=True, null=True)  # Field name made lowercase.
    codant = models.IntegerField(blank=True, null=True)
    tipo = models.IntegerField(db_column='Tipo', blank=True, null=True)  # Field name made lowercase.
    situacao = models.IntegerField(db_column='Situacao', blank=True, null=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=100, blank=True, null=True)  # Field name made lowercase.
    utilizacao = models.CharField(db_column='Utilizacao', max_length=250, blank=True, null=True)  # Field name made lowercase.
    utilizacaolonga = models.TextField(db_column='UtilizacaoLonga', blank=True, null=True)  # Field name made lowercase.
    outros = models.CharField(db_column='Outros', max_length=100, blank=True, null=True)  # Field name made lowercase.
    grupo = models.IntegerField(db_column='Grupo', blank=True, null=True)  # Field name made lowercase.
    grupoant = models.IntegerField(db_column='GrupoAnt', blank=True, null=True)  # Field name made lowercase.
    grupodesc = models.CharField(db_column='GrupoDesc', max_length=60, blank=True, null=True)  # Field name made lowercase.
    linha = models.IntegerField(db_column='Linha', blank=True, null=True)  # Field name made lowercase.
    linhaant = models.IntegerField(blank=True, null=True)
    linhadesc = models.CharField(db_column='LinhaDesc', max_length=60, blank=True, null=True)  # Field name made lowercase.
    fabricante = models.IntegerField(db_column='Fabricante', blank=True, null=True)  # Field name made lowercase.
    fabricanteant = models.IntegerField(blank=True, null=True)
    fabricantedesc = models.CharField(db_column='FabricanteDesc', max_length=60, blank=True, null=True)  # Field name made lowercase.
    estoque = models.FloatField(db_column='Estoque', blank=True, null=True)  # Field name made lowercase.
    indisponivel = models.FloatField(blank=True, null=True)
    minimo = models.FloatField(db_column='Minimo', blank=True, null=True)  # Field name made lowercase.
    maximo = models.FloatField(db_column='Maximo', blank=True, null=True)  # Field name made lowercase.
    unidade = models.CharField(db_column='Unidade', max_length=2, blank=True, null=True)  # Field name made lowercase.
    espessura = models.FloatField(db_column='Espessura', blank=True, null=True)  # Field name made lowercase.
    pesounidade = models.FloatField(db_column='PesoUnidade', blank=True, null=True)  # Field name made lowercase.
    precopeso = models.IntegerField(db_column='PrecoPeso', blank=True, null=True)  # Field name made lowercase.
    calcularpeso = models.IntegerField(db_column='CalcularPeso', blank=True, null=True)  # Field name made lowercase.
    curva = models.CharField(max_length=1, blank=True, null=True)
    venda = models.FloatField(db_column='Venda', blank=True, null=True)  # Field name made lowercase.
    vendaant = models.FloatField(db_column='VendaAnt', blank=True, null=True)  # Field name made lowercase.
    tabela = models.FloatField(db_column='Tabela', blank=True, null=True)  # Field name made lowercase.
    atacado = models.FloatField(db_column='Atacado', blank=True, null=True)  # Field name made lowercase.
    localizacao = models.CharField(db_column='Localizacao', max_length=60, blank=True, null=True)  # Field name made lowercase.
    codigobarra = models.CharField(db_column='CodigoBarra', max_length=30, blank=True, null=True)  # Field name made lowercase.
    codigobarra2 = models.CharField(db_column='CodigoBarra2', max_length=30, blank=True, null=True)  # Field name made lowercase.
    codigobarra3 = models.CharField(db_column='CodigoBarra3', max_length=30, blank=True, null=True)  # Field name made lowercase.
    exportarbalanca = models.IntegerField(db_column='ExportarBalanca', blank=True, null=True)  # Field name made lowercase.
    validadebalanca = models.IntegerField(db_column='ValidadeBalanca', blank=True, null=True)  # Field name made lowercase.
    penultimavenda = models.DateField(db_column='PenultimaVenda', blank=True, null=True)  # Field name made lowercase.
    ultimavenda = models.DateField(db_column='UltimaVenda', blank=True, null=True)  # Field name made lowercase.
    ultimoaumento = models.DateField(db_column='UltimoAumento', blank=True, null=True)  # Field name made lowercase.
    ultimacompra = models.DateField(db_column='UltimaCompra', blank=True, null=True)  # Field name made lowercase.
    ultimacontagem = models.DateField(db_column='UltimaContagem', blank=True, null=True)  # Field name made lowercase.
    classtr = models.IntegerField(db_column='ClassTr', blank=True, null=True)  # Field name made lowercase.
    classtrdesc = models.CharField(db_column='ClassTrDesc', max_length=3, blank=True, null=True)  # Field name made lowercase.
    csticmsorigem = models.CharField(db_column='CstICMSOrigem', max_length=1, blank=True, null=True)  # Field name made lowercase.
    csticms = models.CharField(db_column='CstICMS', max_length=2, blank=True, null=True)  # Field name made lowercase.
    icms = models.FloatField(blank=True, null=True)
    predbcicms = models.FloatField(db_column='pRedBcICMS', blank=True, null=True)  # Field name made lowercase.
    obsnf = models.IntegerField(db_column='ObsNf', blank=True, null=True)  # Field name made lowercase.
    obsnfdesc = models.CharField(db_column='ObsNfDesc', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ipi = models.FloatField(db_column='IPI', blank=True, null=True)  # Field name made lowercase.
    cstipi = models.IntegerField(db_column='CstIPI', blank=True, null=True)  # Field name made lowercase.
    pis = models.FloatField(db_column='PIS', blank=True, null=True)  # Field name made lowercase.
    cstpis = models.IntegerField(db_column='CstPIS', blank=True, null=True)  # Field name made lowercase.
    cofins = models.FloatField(db_column='Cofins', blank=True, null=True)  # Field name made lowercase.
    cstcofins = models.IntegerField(db_column='CstCofins', blank=True, null=True)  # Field name made lowercase.
    idsimilar = models.IntegerField(db_column='IDSimilar', blank=True, null=True)  # Field name made lowercase.
    pglp = models.FloatField(db_column='pGLP', blank=True, null=True)  # Field name made lowercase.
    pgnn = models.FloatField(db_column='pGNn', blank=True, null=True)  # Field name made lowercase.
    pgni = models.FloatField(db_column='pGNi', blank=True, null=True)  # Field name made lowercase.
    vpart = models.FloatField(db_column='vPart', blank=True, null=True)  # Field name made lowercase.
    kgunglp = models.FloatField(db_column='KgUnGLP', blank=True, null=True)  # Field name made lowercase.
    converg1 = models.CharField(db_column='Converg1', max_length=30, blank=True, null=True)  # Field name made lowercase.
    converg2 = models.CharField(db_column='Converg2', max_length=30, blank=True, null=True)  # Field name made lowercase.
    converg3 = models.CharField(db_column='Converg3', max_length=30, blank=True, null=True)  # Field name made lowercase.
    janeiro = models.FloatField(db_column='Janeiro', blank=True, null=True)  # Field name made lowercase.
    fevereiro = models.FloatField(db_column='Fevereiro', blank=True, null=True)  # Field name made lowercase.
    marco = models.FloatField(db_column='Marco', blank=True, null=True)  # Field name made lowercase.
    abril = models.FloatField(db_column='Abril', blank=True, null=True)  # Field name made lowercase.
    maio = models.FloatField(db_column='Maio', blank=True, null=True)  # Field name made lowercase.
    junho = models.FloatField(db_column='Junho', blank=True, null=True)  # Field name made lowercase.
    julho = models.FloatField(db_column='Julho', blank=True, null=True)  # Field name made lowercase.
    agosto = models.FloatField(db_column='Agosto', blank=True, null=True)  # Field name made lowercase.
    setembro = models.FloatField(db_column='Setembro', blank=True, null=True)  # Field name made lowercase.
    outubro = models.FloatField(db_column='Outubro', blank=True, null=True)  # Field name made lowercase.
    novembro = models.FloatField(db_column='Novembro', blank=True, null=True)  # Field name made lowercase.
    dezembro = models.FloatField(db_column='Dezembro', blank=True, null=True)  # Field name made lowercase.
    custo = models.FloatField(db_column='Custo', blank=True, null=True)  # Field name made lowercase.
    medio = models.FloatField(db_column='Medio', blank=True, null=True)  # Field name made lowercase.
    markup = models.FloatField(db_column='Markup', blank=True, null=True)  # Field name made lowercase.
    margem = models.FloatField(db_column='Margem', blank=True, null=True)  # Field name made lowercase.
    promocao = models.FloatField(db_column='Promocao', blank=True, null=True)  # Field name made lowercase.
    inicio = models.DateField(db_column='Inicio', blank=True, null=True)  # Field name made lowercase.
    termino = models.DateField(db_column='Termino', blank=True, null=True)  # Field name made lowercase.
    original = models.CharField(db_column='Original', max_length=60, blank=True, null=True)  # Field name made lowercase.
    redoriginal = models.CharField(db_column='RedOriginal', max_length=60, blank=True, null=True)  # Field name made lowercase.
    barros = models.IntegerField(blank=True, null=True)
    print = models.IntegerField(db_column='Print', blank=True, null=True)  # Field name made lowercase.
    compra = models.FloatField(db_column='Compra', blank=True, null=True)  # Field name made lowercase.
    comprar = models.IntegerField(db_column='Comprar', blank=True, null=True)  # Field name made lowercase.
    reduzido = models.CharField(db_column='Reduzido', max_length=30, blank=True, null=True)  # Field name made lowercase.
    redcodigofabrica = models.CharField(db_column='RedCodigoFabrica', max_length=30, blank=True, null=True)  # Field name made lowercase.
    redconverg1 = models.CharField(max_length=30, blank=True, null=True)
    redconverg2 = models.CharField(max_length=30, blank=True, null=True)
    redconverg3 = models.CharField(max_length=30, blank=True, null=True)
    cadastro = models.DateField(db_column='Cadastro', blank=True, null=True)  # Field name made lowercase.
    observacao = models.TextField(db_column='Observacao', blank=True, null=True)  # Field name made lowercase.
    foto = models.CharField(db_column='Foto', max_length=200, blank=True, null=True)  # Field name made lowercase.
    empresa = models.IntegerField(db_column='Empresa', blank=True, null=True)  # Field name made lowercase.
    etiqueta = models.IntegerField(db_column='Etiqueta', blank=True, null=True)  # Field name made lowercase.
    lista = models.IntegerField(db_column='Lista', blank=True, null=True)  # Field name made lowercase.
    alteraos = models.IntegerField(db_column='AlteraOS', blank=True, null=True)  # Field name made lowercase.
    alteravenda = models.IntegerField(db_column='AlteraVenda', blank=True, null=True)  # Field name made lowercase.
    alteraorcamento = models.IntegerField(db_column='AlteraOrcamento', blank=True, null=True)  # Field name made lowercase.
    alteracustovenda = models.IntegerField(db_column='AlteraCustoVenda', blank=True, null=True)  # Field name made lowercase.
    controlado = models.IntegerField(db_column='Controlado', blank=True, null=True)  # Field name made lowercase.
    ativo = models.IntegerField(db_column='Ativo', blank=True, null=True)  # Field name made lowercase.
    stf = models.FloatField(db_column='Stf', blank=True, null=True)  # Field name made lowercase.
    dataf = models.DateField(db_column='DataF', blank=True, null=True)  # Field name made lowercase.
    preindice = models.CharField(max_length=3, blank=True, null=True)
    preatac = models.FloatField(blank=True, null=True)
    prevar = models.FloatField(blank=True, null=True)
    premec = models.FloatField(blank=True, null=True)
    ncms = models.CharField(max_length=8, blank=True, null=True)
    cest = models.CharField(db_column='Cest', max_length=7, blank=True, null=True)  # Field name made lowercase.
    iva = models.FloatField(blank=True, null=True)
    icms_intra = models.FloatField(blank=True, null=True)
    c_janeiro = models.FloatField(blank=True, null=True)
    c_fevereiro = models.FloatField(blank=True, null=True)
    c_marco = models.FloatField(blank=True, null=True)
    c_abril = models.FloatField(blank=True, null=True)
    c_maio = models.FloatField(blank=True, null=True)
    c_junho = models.FloatField(blank=True, null=True)
    c_julho = models.FloatField(blank=True, null=True)
    c_agosto = models.FloatField(blank=True, null=True)
    c_setembro = models.FloatField(blank=True, null=True)
    c_outubro = models.FloatField(blank=True, null=True)
    c_novembro = models.FloatField(blank=True, null=True)
    c_dezembro = models.FloatField(blank=True, null=True)
    brinde = models.IntegerField(blank=True, null=True)
    pontos_cartao = models.FloatField(blank=True, null=True)
    brinde_ativo = models.IntegerField(blank=True, null=True)
    controle_lote_estoque = models.IntegerField(blank=True, null=True, db_comment='0-false 1-true')
    vendaembalagem = models.IntegerField(db_column='VendaEmbalagem', blank=True, null=True)  # Field name made lowercase.
    quantidadeembalagem = models.FloatField(db_column='QuantidadeEmbalagem', blank=True, null=True)  # Field name made lowercase.
    insumoembalagem = models.IntegerField(db_column='InsumoEmbalagem', blank=True, null=True)  # Field name made lowercase.
    vendadigital = models.IntegerField(db_column='VendaDigital', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'produtos'


class ProdutosKit(models.Model):
    id_produto = models.IntegerField(blank=True, null=True)
    codigo_kit = models.CharField(max_length=30, blank=True, null=True)
    codigo_prod = models.CharField(max_length=30, blank=True, null=True)
    quantidade = models.FloatField(blank=True, null=True)
    empresa = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'produtos_kit'


class ProdutosLote(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    produto = models.CharField(db_column='Produto', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lote = models.CharField(db_column='Lote', max_length=20, blank=True, null=True)  # Field name made lowercase.
    estoque = models.FloatField(db_column='Estoque', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'produtos_lote'


class ProdutosProducao(models.Model):
    id = models.IntegerField(primary_key=True)
    id_produto = models.IntegerField(blank=True, null=True)
    codigo_kit = models.CharField(max_length=30, blank=True, null=True)
    codigo_prod = models.CharField(max_length=30, blank=True, null=True)
    quantidade = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'produtos_producao'


class ProdutosSimilar(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    referencia = models.CharField(db_column='Referencia', max_length=30, blank=True, null=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=60, blank=True, null=True)  # Field name made lowercase.
    aplicacao = models.CharField(db_column='Aplicacao', max_length=250, blank=True, null=True)  # Field name made lowercase.
    cadastro = models.DateField(db_column='Cadastro', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'produtos_similar'


class Produtosbalcao(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    balcao = models.IntegerField(db_column='Balcao', blank=True, null=True)  # Field name made lowercase.
    codigo = models.CharField(db_column='Codigo', max_length=30, blank=True, null=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=100, blank=True, null=True)  # Field name made lowercase.
    quantidade = models.FloatField(db_column='Quantidade', blank=True, null=True)  # Field name made lowercase.
    unitario = models.FloatField(db_column='Unitario', blank=True, null=True)  # Field name made lowercase.
    total = models.FloatField(db_column='Total', blank=True, null=True)  # Field name made lowercase.
    descacre = models.FloatField(db_column='DescAcre', blank=True, null=True)  # Field name made lowercase.
    data = models.DateField(db_column='Data', blank=True, null=True)  # Field name made lowercase.
    hora = models.TimeField(db_column='Hora', blank=True, null=True)  # Field name made lowercase.
    situacao = models.IntegerField(db_column='Situacao', blank=True, null=True)  # Field name made lowercase.
    custo = models.FloatField(db_column='Custo', blank=True, null=True)  # Field name made lowercase.
    grupo = models.IntegerField(db_column='Grupo', blank=True, null=True)  # Field name made lowercase.
    grupodesc = models.CharField(db_column='GrupoDesc', max_length=60, blank=True, null=True)  # Field name made lowercase.
    linha = models.IntegerField(db_column='Linha', blank=True, null=True)  # Field name made lowercase.
    linhadesc = models.CharField(db_column='LinhaDesc', max_length=60, blank=True, null=True)  # Field name made lowercase.
    fabricante = models.IntegerField(db_column='Fabricante', blank=True, null=True)  # Field name made lowercase.
    fabricantedesc = models.CharField(db_column='FabricanteDesc', max_length=60, blank=True, null=True)  # Field name made lowercase.
    empresa = models.IntegerField(db_column='Empresa', blank=True, null=True)  # Field name made lowercase.
    mecanico = models.IntegerField(db_column='Mecanico', blank=True, null=True)  # Field name made lowercase.
    vendedor = models.IntegerField(db_column='Vendedor', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'produtosbalcao'


class Produtoscond(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nos = models.IntegerField(db_column='NOS', blank=True, null=True)  # Field name made lowercase.
    cliente = models.IntegerField(blank=True, null=True)
    codigo = models.CharField(db_column='Codigo', max_length=30, blank=True, null=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=100, blank=True, null=True)  # Field name made lowercase.
    aplicacao = models.CharField(db_column='Aplicacao', max_length=40, blank=True, null=True)  # Field name made lowercase.
    quantidade = models.FloatField(db_column='Quantidade', blank=True, null=True)  # Field name made lowercase.
    unitario = models.FloatField(db_column='Unitario', blank=True, null=True)  # Field name made lowercase.
    total = models.FloatField(db_column='Total', blank=True, null=True)  # Field name made lowercase.
    descacre = models.FloatField(db_column='DescAcre', blank=True, null=True)  # Field name made lowercase.
    vendaunitario = models.FloatField(blank=True, null=True)
    vendatotal = models.FloatField(blank=True, null=True)
    unidade = models.CharField(max_length=2, blank=True, null=True)
    fechamento = models.IntegerField(blank=True, null=True)
    datafechamento = models.DateField(blank=True, null=True)
    nota = models.IntegerField(blank=True, null=True)
    devolvido = models.CharField(max_length=1, blank=True, null=True)
    datadevolucao = models.DateField(db_column='DataDevolucao', blank=True, null=True)  # Field name made lowercase.
    horadevolucao = models.TimeField(db_column='HoraDevolucao', blank=True, null=True)  # Field name made lowercase.
    funcionario = models.IntegerField(db_column='Funcionario', blank=True, null=True)  # Field name made lowercase.
    data = models.DateField(db_column='Data', blank=True, null=True)  # Field name made lowercase.
    hora = models.TimeField(db_column='Hora', blank=True, null=True)  # Field name made lowercase.
    custo = models.FloatField(db_column='Custo', blank=True, null=True)  # Field name made lowercase.
    medio = models.FloatField(blank=True, null=True)
    venda = models.FloatField(db_column='Venda', blank=True, null=True)  # Field name made lowercase.
    usuario = models.IntegerField(db_column='Usuario', blank=True, null=True)  # Field name made lowercase.
    grupo = models.IntegerField(db_column='Grupo', blank=True, null=True)  # Field name made lowercase.
    grupodesc = models.CharField(db_column='GrupoDesc', max_length=60, blank=True, null=True)  # Field name made lowercase.
    linha = models.IntegerField(db_column='Linha', blank=True, null=True)  # Field name made lowercase.
    linhadesc = models.CharField(db_column='LinhaDesc', max_length=60, blank=True, null=True)  # Field name made lowercase.
    fabricante = models.IntegerField(db_column='Fabricante', blank=True, null=True)  # Field name made lowercase.
    fabricantedesc = models.CharField(db_column='FabricanteDesc', max_length=60, blank=True, null=True)  # Field name made lowercase.
    reduzido = models.CharField(max_length=30, blank=True, null=True)
    id_kit = models.IntegerField(blank=True, null=True)
    empresa = models.IntegerField(db_column='Empresa', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'produtoscond'


class Produtosfiscais(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    numeroid = models.IntegerField(db_column='NumeroID', blank=True, null=True)  # Field name made lowercase.
    numeronota = models.IntegerField(db_column='NumeroNota', blank=True, null=True)  # Field name made lowercase.
    emissao = models.DateField(db_column='Emissao', blank=True, null=True)  # Field name made lowercase.
    codigo = models.CharField(db_column='Codigo', max_length=30, blank=True, null=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=80, blank=True, null=True)  # Field name made lowercase.
    cfop = models.CharField(max_length=6, blank=True, null=True)
    ncms = models.CharField(max_length=8, blank=True, null=True)
    sittrib = models.CharField(db_column='SitTrib', max_length=3, blank=True, null=True)  # Field name made lowercase.
    cstpis = models.CharField(db_column='CstPis', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cstcofins = models.CharField(db_column='CstCofins', max_length=2, blank=True, null=True)  # Field name made lowercase.
    unidade = models.CharField(db_column='Unidade', max_length=2, blank=True, null=True)  # Field name made lowercase.
    quantidade = models.FloatField(db_column='Quantidade', blank=True, null=True)  # Field name made lowercase.
    unitario = models.FloatField(db_column='Unitario', blank=True, null=True)  # Field name made lowercase.
    total = models.FloatField(db_column='Total', blank=True, null=True)  # Field name made lowercase.
    aliquota = models.FloatField(db_column='Aliquota', blank=True, null=True)  # Field name made lowercase.
    observacao = models.CharField(db_column='Observacao', max_length=80, blank=True, null=True)  # Field name made lowercase.
    empresa = models.IntegerField(db_column='Empresa', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'produtosfiscais'


class Produtosgarantia(models.Model):
    id_garantia = models.IntegerField(blank=True, null=True)
    tipo = models.CharField(max_length=8, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    obs = models.CharField(max_length=200, blank=True, null=True)
    data = models.DateField(blank=True, null=True)
    codigo = models.CharField(max_length=25, blank=True, null=True)
    descricao = models.CharField(max_length=50, blank=True, null=True)
    aplicacao = models.CharField(max_length=50, blank=True, null=True)
    quantidade = models.FloatField(blank=True, null=True)
    unitario = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    forncompra = models.IntegerField(blank=True, null=True)
    nfcompra = models.IntegerField(blank=True, null=True)
    datanfcompra = models.DateField(blank=True, null=True)
    custocompra = models.FloatField(blank=True, null=True)
    fornenvio = models.IntegerField(blank=True, null=True)
    nfenvio = models.IntegerField(blank=True, null=True)
    datanfenvio = models.DateField(blank=True, null=True)
    custoenvio = models.FloatField(blank=True, null=True)
    fornretorno = models.IntegerField(blank=True, null=True)
    nfretorno = models.IntegerField(blank=True, null=True)
    datanfretorno = models.DateField(blank=True, null=True)
    custoretorno = models.FloatField(blank=True, null=True)
    obsretorno = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'produtosgarantia'


class Produtosorc(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    numero = models.IntegerField(db_column='Numero', blank=True, null=True)  # Field name made lowercase.
    codigo = models.CharField(db_column='Codigo', max_length=30, blank=True, null=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=60, blank=True, null=True)  # Field name made lowercase.
    quantidade = models.FloatField(db_column='Quantidade', blank=True, null=True)  # Field name made lowercase.
    unitario = models.FloatField(db_column='Unitario', blank=True, null=True)  # Field name made lowercase.
    total = models.FloatField(db_column='Total', blank=True, null=True)  # Field name made lowercase.
    grupo = models.IntegerField(db_column='Grupo', blank=True, null=True)  # Field name made lowercase.
    grupodesc = models.CharField(db_column='GrupoDesc', max_length=60, blank=True, null=True)  # Field name made lowercase.
    linha = models.IntegerField(db_column='Linha', blank=True, null=True)  # Field name made lowercase.
    linhadesc = models.CharField(db_column='LinhaDesc', max_length=60, blank=True, null=True)  # Field name made lowercase.
    fabricante = models.IntegerField(db_column='Fabricante', blank=True, null=True)  # Field name made lowercase.
    fabricantedesc = models.CharField(db_column='FabricanteDesc', max_length=60, blank=True, null=True)  # Field name made lowercase.
    empresa = models.IntegerField(db_column='Empresa', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'produtosorc'


class Produtosorcamento(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    orcamento = models.IntegerField(db_column='Orcamento', blank=True, null=True)  # Field name made lowercase.
    codigo = models.CharField(db_column='Codigo', max_length=30, blank=True, null=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=100, blank=True, null=True)  # Field name made lowercase.
    quantidade = models.FloatField(db_column='Quantidade', blank=True, null=True)  # Field name made lowercase.
    unitario = models.FloatField(db_column='Unitario', blank=True, null=True)  # Field name made lowercase.
    total = models.FloatField(db_column='Total', blank=True, null=True)  # Field name made lowercase.
    descacre = models.FloatField(db_column='DescAcre', blank=True, null=True)  # Field name made lowercase.
    data = models.DateField(db_column='Data', blank=True, null=True)  # Field name made lowercase.
    hora = models.TimeField(db_column='Hora', blank=True, null=True)  # Field name made lowercase.
    grupo = models.IntegerField(db_column='Grupo', blank=True, null=True)  # Field name made lowercase.
    grupodesc = models.CharField(db_column='GrupoDesc', max_length=60, blank=True, null=True)  # Field name made lowercase.
    linha = models.IntegerField(db_column='Linha', blank=True, null=True)  # Field name made lowercase.
    linhadesc = models.CharField(db_column='LinhaDesc', max_length=60, blank=True, null=True)  # Field name made lowercase.
    fabricante = models.IntegerField(db_column='Fabricante', blank=True, null=True)  # Field name made lowercase.
    fabricantedesc = models.CharField(db_column='FabricanteDesc', max_length=60, blank=True, null=True)  # Field name made lowercase.
    empresa = models.IntegerField(db_column='Empresa', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'produtosorcamento'


class Produtosos(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nos = models.IntegerField(db_column='NOS', blank=True, null=True)  # Field name made lowercase.
    cliente = models.IntegerField(blank=True, null=True)
    garantia = models.IntegerField(db_column='Garantia', blank=True, null=True)  # Field name made lowercase.
    codigobarra = models.CharField(db_column='CodigoBarra', max_length=30, blank=True, null=True)  # Field name made lowercase.
    codigo = models.CharField(db_column='Codigo', max_length=30, blank=True, null=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=100, blank=True, null=True)  # Field name made lowercase.
    aplicacao = models.CharField(max_length=40, blank=True, null=True)
    quantidade = models.FloatField(db_column='Quantidade', blank=True, null=True)  # Field name made lowercase.
    unitario = models.FloatField(db_column='Unitario', blank=True, null=True)  # Field name made lowercase.
    total = models.FloatField(db_column='Total', blank=True, null=True)  # Field name made lowercase.
    descacre = models.FloatField(db_column='DescAcre', blank=True, null=True)  # Field name made lowercase.
    vendaunitario = models.FloatField(blank=True, null=True)
    vendatotal = models.FloatField(blank=True, null=True)
    funcionario = models.IntegerField(db_column='Funcionario', blank=True, null=True)  # Field name made lowercase.
    consultor = models.IntegerField(db_column='Consultor', blank=True, null=True)  # Field name made lowercase.
    data = models.DateField(db_column='Data', blank=True, null=True)  # Field name made lowercase.
    hora = models.TimeField(db_column='Hora', blank=True, null=True)  # Field name made lowercase.
    custo = models.FloatField(db_column='Custo', blank=True, null=True)  # Field name made lowercase.
    medio = models.FloatField(blank=True, null=True)
    venda = models.FloatField(db_column='Venda', blank=True, null=True)  # Field name made lowercase.
    usuario = models.IntegerField(db_column='Usuario', blank=True, null=True)  # Field name made lowercase.
    grupo = models.IntegerField(db_column='Grupo', blank=True, null=True)  # Field name made lowercase.
    grupodesc = models.CharField(db_column='GrupoDesc', max_length=60, blank=True, null=True)  # Field name made lowercase.
    linha = models.IntegerField(db_column='Linha', blank=True, null=True)  # Field name made lowercase.
    linhadesc = models.CharField(db_column='LinhaDesc', max_length=60, blank=True, null=True)  # Field name made lowercase.
    fabricante = models.IntegerField(db_column='Fabricante', blank=True, null=True)  # Field name made lowercase.
    fabricantedesc = models.CharField(db_column='FabricanteDesc', max_length=60, blank=True, null=True)  # Field name made lowercase.
    empresa = models.IntegerField(db_column='Empresa', blank=True, null=True)  # Field name made lowercase.
    mecanico = models.IntegerField(blank=True, null=True)
    nftemp = models.IntegerField(blank=True, null=True)
    nota = models.IntegerField(blank=True, null=True)
    notaeletronica = models.IntegerField(blank=True, null=True)
    serie = models.IntegerField(blank=True, null=True)
    modelo = models.IntegerField(blank=True, null=True)
    cfetemp = models.IntegerField(blank=True, null=True)
    cfe = models.IntegerField(blank=True, null=True)
    fatura = models.IntegerField(blank=True, null=True)
    numeropedidocompra = models.CharField(db_column='NumeroPedidoCompra', max_length=15, blank=True, null=True)  # Field name made lowercase.
    numeroitempedidocompra = models.IntegerField(db_column='NumeroItemPedidoCompra', blank=True, null=True)  # Field name made lowercase.
    seleciona = models.CharField(db_column='Seleciona', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'produtosos'


class Produtosreq(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    pdv = models.IntegerField(db_column='PDV', blank=True, null=True)  # Field name made lowercase.
    caixa = models.IntegerField(db_column='Caixa', blank=True, null=True)  # Field name made lowercase.
    nos = models.IntegerField(db_column='NOS', blank=True, null=True)  # Field name made lowercase.
    cliente = models.IntegerField(blank=True, null=True)
    tipo = models.CharField(max_length=5, blank=True, null=True)
    codigobarra = models.CharField(db_column='CodigoBarra', max_length=30, blank=True, null=True)  # Field name made lowercase.
    codigo = models.CharField(db_column='Codigo', max_length=30, blank=True, null=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=100, blank=True, null=True)  # Field name made lowercase.
    aplicacao = models.CharField(db_column='Aplicacao', max_length=40, blank=True, null=True)  # Field name made lowercase.
    quantidade = models.FloatField(db_column='Quantidade', blank=True, null=True)  # Field name made lowercase.
    unitario = models.FloatField(db_column='Unitario', blank=True, null=True)  # Field name made lowercase.
    total = models.FloatField(db_column='Total', blank=True, null=True)  # Field name made lowercase.
    descacre = models.FloatField(db_column='DescAcre', blank=True, null=True)  # Field name made lowercase.
    vendaunitario = models.FloatField(blank=True, null=True)
    vendatotal = models.FloatField(blank=True, null=True)
    ncm = models.CharField(db_column='NCM', max_length=8, blank=True, null=True)  # Field name made lowercase.
    csticms = models.CharField(db_column='CstICMS', max_length=3, blank=True, null=True)  # Field name made lowercase.
    localizacao = models.CharField(max_length=60, blank=True, null=True)
    unidade = models.CharField(max_length=2, blank=True, null=True)
    quantunidade = models.FloatField(blank=True, null=True)
    peso = models.FloatField(blank=True, null=True)
    precopeso = models.CharField(max_length=1, blank=True, null=True)
    fechamento = models.IntegerField(blank=True, null=True)
    datafechamento = models.DateField(blank=True, null=True)
    agrupamento = models.IntegerField(blank=True, null=True)
    dataagrupamento = models.DateTimeField(blank=True, null=True)
    usuarioagrupamento = models.IntegerField(blank=True, null=True)
    nftemp = models.IntegerField(blank=True, null=True)
    nota = models.IntegerField(blank=True, null=True)
    notaeletronica = models.IntegerField(blank=True, null=True)
    serie = models.IntegerField(blank=True, null=True)
    modelo = models.IntegerField(blank=True, null=True)
    cfetemp = models.IntegerField(blank=True, null=True)
    cupom = models.IntegerField(blank=True, null=True)
    cfe = models.IntegerField(blank=True, null=True)
    nfstemp = models.IntegerField(blank=True, null=True)
    rps = models.IntegerField(blank=True, null=True)
    nfse = models.IntegerField(blank=True, null=True)
    devolvido = models.CharField(max_length=1, blank=True, null=True)
    tipodev = models.IntegerField(blank=True, null=True, db_comment='0-Alt, 1-Canc 2-Dev')
    quantdev = models.FloatField(blank=True, null=True)
    usuariodev = models.IntegerField(blank=True, null=True)
    funcdev = models.IntegerField(blank=True, null=True)
    datadev = models.DateField(blank=True, null=True)
    horadev = models.TimeField(blank=True, null=True)
    id_dev = models.IntegerField(blank=True, null=True)
    id_prod_dev = models.IntegerField(blank=True, null=True)
    id_devolucao = models.IntegerField(blank=True, null=True)
    usuconfdev = models.IntegerField(db_column='UsuConfDev', blank=True, null=True)  # Field name made lowercase.
    dataconfdev = models.DateField(db_column='DataConfDev', blank=True, null=True)  # Field name made lowercase.
    funcionario = models.IntegerField(db_column='Funcionario', blank=True, null=True)  # Field name made lowercase.
    datavenda = models.DateField(db_column='DataVenda', blank=True, null=True)  # Field name made lowercase.
    data = models.DateField(db_column='Data', blank=True, null=True)  # Field name made lowercase.
    hora = models.TimeField(db_column='Hora', blank=True, null=True)  # Field name made lowercase.
    custo = models.FloatField(db_column='Custo', blank=True, null=True)  # Field name made lowercase.
    medio = models.FloatField(blank=True, null=True)
    venda = models.FloatField(db_column='Venda', blank=True, null=True)  # Field name made lowercase.
    usuario = models.IntegerField(db_column='Usuario', blank=True, null=True)  # Field name made lowercase.
    grupo = models.IntegerField(db_column='Grupo', blank=True, null=True)  # Field name made lowercase.
    grupodesc = models.CharField(db_column='GrupoDesc', max_length=60, blank=True, null=True)  # Field name made lowercase.
    linha = models.IntegerField(db_column='Linha', blank=True, null=True)  # Field name made lowercase.
    linhadesc = models.CharField(db_column='LinhaDesc', max_length=60, blank=True, null=True)  # Field name made lowercase.
    fabricante = models.IntegerField(db_column='Fabricante', blank=True, null=True)  # Field name made lowercase.
    fabricantedesc = models.CharField(db_column='FabricanteDesc', max_length=60, blank=True, null=True)  # Field name made lowercase.
    reduzido = models.CharField(max_length=30, blank=True, null=True)
    id_kit = models.IntegerField(blank=True, null=True)
    entrega = models.CharField(max_length=1, blank=True, null=True)
    entregue = models.CharField(max_length=1, blank=True, null=True)
    pedido = models.IntegerField(blank=True, null=True)
    profissional = models.IntegerField(blank=True, null=True)
    oficina = models.IntegerField(blank=True, null=True)
    idlote = models.IntegerField(blank=True, null=True)
    numeropedidocompra = models.CharField(db_column='NumeroPedidoCompra', max_length=15, blank=True, null=True)  # Field name made lowercase.
    numeroitempedidocompra = models.IntegerField(db_column='NumeroItemPedidoCompra', blank=True, null=True)  # Field name made lowercase.
    seleciona = models.CharField(db_column='Seleciona', max_length=1, blank=True, null=True)  # Field name made lowercase.
    contagem = models.FloatField(db_column='Contagem', blank=True, null=True)  # Field name made lowercase.
    empresa = models.IntegerField(db_column='Empresa', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'produtosreq'


class Produtostransf(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nos = models.IntegerField(db_column='NOS', blank=True, null=True)  # Field name made lowercase.
    cliente = models.IntegerField(blank=True, null=True)
    tipo = models.CharField(max_length=5, blank=True, null=True)
    codigo = models.CharField(db_column='Codigo', max_length=30, blank=True, null=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=100, blank=True, null=True)  # Field name made lowercase.
    aplicacao = models.CharField(db_column='Aplicacao', max_length=40, blank=True, null=True)  # Field name made lowercase.
    quantidade = models.FloatField(db_column='Quantidade', blank=True, null=True)  # Field name made lowercase.
    unitario = models.FloatField(db_column='Unitario', blank=True, null=True)  # Field name made lowercase.
    total = models.FloatField(db_column='Total', blank=True, null=True)  # Field name made lowercase.
    descacre = models.FloatField(db_column='DescAcre', blank=True, null=True)  # Field name made lowercase.
    vendaunitario = models.FloatField(blank=True, null=True)
    vendatotal = models.FloatField(blank=True, null=True)
    unidade = models.CharField(max_length=2, blank=True, null=True)
    fechamento = models.IntegerField(blank=True, null=True)
    datafechamento = models.DateField(blank=True, null=True)
    nftemp = models.IntegerField(blank=True, null=True)
    nota = models.IntegerField(blank=True, null=True)
    notaeletronica = models.IntegerField(blank=True, null=True)
    serie = models.IntegerField(blank=True, null=True)
    modelo = models.IntegerField(blank=True, null=True)
    cupom = models.IntegerField(blank=True, null=True)
    devolvido = models.CharField(max_length=1, blank=True, null=True)
    quantdev = models.FloatField(blank=True, null=True)
    funcdev = models.IntegerField(blank=True, null=True)
    datadev = models.DateField(blank=True, null=True)
    id_dev = models.IntegerField(blank=True, null=True)
    id_prod_dev = models.IntegerField(blank=True, null=True)
    funcionario = models.IntegerField(db_column='Funcionario', blank=True, null=True)  # Field name made lowercase.
    data = models.DateField(db_column='Data', blank=True, null=True)  # Field name made lowercase.
    hora = models.TimeField(db_column='Hora', blank=True, null=True)  # Field name made lowercase.
    custo = models.FloatField(db_column='Custo', blank=True, null=True)  # Field name made lowercase.
    medio = models.FloatField(blank=True, null=True)
    venda = models.FloatField(db_column='Venda', blank=True, null=True)  # Field name made lowercase.
    usuario = models.IntegerField(db_column='Usuario', blank=True, null=True)  # Field name made lowercase.
    grupo = models.IntegerField(db_column='Grupo', blank=True, null=True)  # Field name made lowercase.
    grupodesc = models.CharField(db_column='GrupoDesc', max_length=60, blank=True, null=True)  # Field name made lowercase.
    linha = models.IntegerField(db_column='Linha', blank=True, null=True)  # Field name made lowercase.
    linhadesc = models.CharField(db_column='LinhaDesc', max_length=60, blank=True, null=True)  # Field name made lowercase.
    fabricante = models.IntegerField(db_column='Fabricante', blank=True, null=True)  # Field name made lowercase.
    fabricantedesc = models.CharField(db_column='FabricanteDesc', max_length=60, blank=True, null=True)  # Field name made lowercase.
    reduzido = models.CharField(max_length=30, blank=True, null=True)
    id_kit = models.IntegerField(blank=True, null=True)
    entrega = models.CharField(max_length=1, blank=True, null=True)
    pedido = models.IntegerField(blank=True, null=True)
    profissional = models.IntegerField(blank=True, null=True)
    empresa = models.IntegerField(db_column='Empresa', blank=True, null=True)  # Field name made lowercase.
    numeropedidocompra = models.CharField(db_column='NumeroPedidoCompra', max_length=15, blank=True, null=True)  # Field name made lowercase.
    numeroitempedidocompra = models.IntegerField(db_column='NumeroItemPedidoCompra', blank=True, null=True)  # Field name made lowercase.
    seleciona = models.CharField(db_column='Seleciona', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'produtostransf'


class Profissional(models.Model):
    codigo = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50, blank=True, null=True)
    apelido = models.CharField(max_length=50, blank=True, null=True)
    nascimento = models.DateField(blank=True, null=True)
    profissao = models.CharField(max_length=30, blank=True, null=True)
    endereco = models.CharField(max_length=50, blank=True, null=True)
    bairro = models.CharField(max_length=30, blank=True, null=True)
    cep = models.CharField(max_length=9, blank=True, null=True)
    cpf = models.CharField(max_length=14, blank=True, null=True)
    rg = models.CharField(max_length=25, blank=True, null=True)
    fone1 = models.CharField(max_length=14, blank=True, null=True)
    fone2 = models.CharField(max_length=14, blank=True, null=True)
    pontos = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'profissional'


class Protesto(models.Model):
    empresa = models.IntegerField(blank=True, null=True)
    cliente = models.IntegerField(blank=True, null=True)
    data_inclusao = models.DateField(blank=True, null=True)
    data_saida = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'protesto'


class Recebimentos(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    pdv = models.IntegerField(db_column='PDV', blank=True, null=True)  # Field name made lowercase.
    caixa = models.IntegerField(db_column='Caixa', blank=True, null=True)  # Field name made lowercase.
    codigo = models.IntegerField(db_column='Codigo', blank=True, null=True)  # Field name made lowercase.
    emissao = models.DateField(db_column='Emissao', blank=True, null=True)  # Field name made lowercase.
    tipo = models.CharField(db_column='Tipo', max_length=1, blank=True, null=True)  # Field name made lowercase.
    portador = models.IntegerField(db_column='Portador', blank=True, null=True)  # Field name made lowercase.
    cliente = models.IntegerField(db_column='Cliente', blank=True, null=True)  # Field name made lowercase.
    clienteant = models.IntegerField(blank=True, null=True)
    conta = models.IntegerField(db_column='Conta', blank=True, null=True)  # Field name made lowercase.
    condicoes = models.IntegerField(db_column='Condicoes', blank=True, null=True)  # Field name made lowercase.
    vencimento = models.DateField(db_column='Vencimento', blank=True, null=True)  # Field name made lowercase.
    valorprestacao = models.FloatField(db_column='ValorPrestacao', blank=True, null=True)  # Field name made lowercase.
    valordocumento = models.FloatField(db_column='ValorDocumento', blank=True, null=True)  # Field name made lowercase.
    valordiferenca = models.FloatField(db_column='ValorDiferenca', blank=True, null=True)  # Field name made lowercase.
    observacao = models.CharField(db_column='Observacao', max_length=100, blank=True, null=True)  # Field name made lowercase.
    situacao = models.CharField(db_column='Situacao', max_length=1, blank=True, null=True)  # Field name made lowercase.
    boleto = models.CharField(db_column='Boleto', max_length=1, blank=True, null=True)  # Field name made lowercase.
    id_boleto = models.IntegerField(db_column='Id_boleto', blank=True, null=True)  # Field name made lowercase.
    descontado = models.CharField(db_column='Descontado', max_length=1, blank=True, null=True)  # Field name made lowercase.
    lote = models.IntegerField(db_column='Lote', blank=True, null=True)  # Field name made lowercase.
    diferenca = models.FloatField(db_column='Diferenca', blank=True, null=True)  # Field name made lowercase.
    valorpago = models.FloatField(db_column='ValorPago', blank=True, null=True)  # Field name made lowercase.
    datapagto = models.DateField(db_column='DataPagto', blank=True, null=True)  # Field name made lowercase.
    usuario_baixa = models.IntegerField(db_column='Usuario_baixa', blank=True, null=True)  # Field name made lowercase.
    sequencia = models.IntegerField(db_column='Sequencia', blank=True, null=True)  # Field name made lowercase.
    parcelas = models.IntegerField(blank=True, null=True)
    usuarioreabertura = models.IntegerField(db_column='UsuarioReabertura', blank=True, null=True)  # Field name made lowercase.
    datareabertura = models.DateField(db_column='DataReabertura', blank=True, null=True)  # Field name made lowercase.
    pagocom = models.IntegerField(db_column='PagoCom', blank=True, null=True)  # Field name made lowercase.
    numerobanco = models.CharField(db_column='NumeroBanco', max_length=30, blank=True, null=True)  # Field name made lowercase.
    os = models.IntegerField(db_column='OS', blank=True, null=True)  # Field name made lowercase.
    process = models.DateField(db_column='Process', blank=True, null=True)  # Field name made lowercase.
    esp = models.CharField(db_column='ESP', max_length=2, blank=True, null=True)  # Field name made lowercase.
    empresa = models.IntegerField(db_column='Empresa', blank=True, null=True)  # Field name made lowercase.
    sequencia2 = models.IntegerField(db_column='Sequencia2', blank=True, null=True)  # Field name made lowercase.
    vendedor = models.IntegerField(blank=True, null=True)
    recebimento = models.IntegerField(blank=True, null=True)
    baixaparcial = models.IntegerField(db_column='BaixaParcial', blank=True, null=True)  # Field name made lowercase.
    saldobaixaparcial = models.FloatField(db_column='SaldoBaixaParcial', blank=True, null=True)  # Field name made lowercase.
    desconto = models.FloatField(blank=True, null=True)
    notaeletronica = models.IntegerField(blank=True, null=True)
    serie = models.IntegerField(blank=True, null=True)
    modelo = models.IntegerField(blank=True, null=True)
    documentofiscal = models.CharField(db_column='DocumentoFiscal', max_length=3, blank=True, null=True)  # Field name made lowercase.
    numerodocumento = models.IntegerField(db_column='NumeroDocumento', blank=True, null=True)  # Field name made lowercase.
    perdido = models.IntegerField(db_column='Perdido', blank=True, null=True, db_comment='0-false 1-true')  # Field name made lowercase.
    dataperdido = models.DateField(db_column='DataPerdido', blank=True, null=True)  # Field name made lowercase.
    obsperdido = models.CharField(db_column='ObsPerdido', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'recebimentos'


class RecebimentosAjuste(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    tipoajuste = models.CharField(db_column='TipoAjuste', max_length=30, blank=True, null=True)  # Field name made lowercase.
    controle = models.IntegerField(db_column='Controle', blank=True, null=True)  # Field name made lowercase.
    dataevento = models.DateField(db_column='DataEvento', blank=True, null=True)  # Field name made lowercase.
    horaevento = models.TimeField(db_column='HoraEvento', blank=True, null=True)  # Field name made lowercase.
    usuarioevento = models.IntegerField(db_column='UsuarioEvento', blank=True, null=True)  # Field name made lowercase.
    maquinaevento = models.CharField(db_column='MaquinaEvento', max_length=60, blank=True, null=True)  # Field name made lowercase.
    idold = models.IntegerField(db_column='IDOld', blank=True, null=True)  # Field name made lowercase.
    pdv = models.IntegerField(db_column='PDV', blank=True, null=True)  # Field name made lowercase.
    caixa = models.IntegerField(db_column='Caixa', blank=True, null=True)  # Field name made lowercase.
    codigo = models.IntegerField(db_column='Codigo', blank=True, null=True)  # Field name made lowercase.
    emissao = models.DateField(db_column='Emissao', blank=True, null=True)  # Field name made lowercase.
    tipo = models.CharField(db_column='Tipo', max_length=1, blank=True, null=True)  # Field name made lowercase.
    portador = models.IntegerField(db_column='Portador', blank=True, null=True)  # Field name made lowercase.
    cliente = models.IntegerField(db_column='Cliente', blank=True, null=True)  # Field name made lowercase.
    clienteant = models.IntegerField(blank=True, null=True)
    conta = models.IntegerField(db_column='Conta', blank=True, null=True)  # Field name made lowercase.
    condicoes = models.IntegerField(db_column='Condicoes', blank=True, null=True)  # Field name made lowercase.
    vencimento = models.DateField(db_column='Vencimento', blank=True, null=True)  # Field name made lowercase.
    valorprestacao = models.FloatField(db_column='ValorPrestacao', blank=True, null=True)  # Field name made lowercase.
    valordocumento = models.FloatField(db_column='ValorDocumento', blank=True, null=True)  # Field name made lowercase.
    valordiferenca = models.FloatField(db_column='ValorDiferenca', blank=True, null=True)  # Field name made lowercase.
    observacao = models.CharField(db_column='Observacao', max_length=100, blank=True, null=True)  # Field name made lowercase.
    situacao = models.CharField(db_column='Situacao', max_length=1, blank=True, null=True)  # Field name made lowercase.
    boleto = models.CharField(db_column='Boleto', max_length=1, blank=True, null=True)  # Field name made lowercase.
    id_boleto = models.IntegerField(db_column='Id_boleto', blank=True, null=True)  # Field name made lowercase.
    descontado = models.CharField(db_column='Descontado', max_length=1, blank=True, null=True)  # Field name made lowercase.
    lote = models.IntegerField(db_column='Lote', blank=True, null=True)  # Field name made lowercase.
    diferenca = models.FloatField(db_column='Diferenca', blank=True, null=True)  # Field name made lowercase.
    valorpago = models.FloatField(db_column='ValorPago', blank=True, null=True)  # Field name made lowercase.
    datapagto = models.DateField(db_column='DataPagto', blank=True, null=True)  # Field name made lowercase.
    usuario_baixa = models.IntegerField(db_column='Usuario_baixa', blank=True, null=True)  # Field name made lowercase.
    sequencia = models.IntegerField(db_column='Sequencia', blank=True, null=True)  # Field name made lowercase.
    parcelas = models.IntegerField(blank=True, null=True)
    usuarioreabertura = models.IntegerField(db_column='UsuarioReabertura', blank=True, null=True)  # Field name made lowercase.
    datareabertura = models.DateField(db_column='DataReabertura', blank=True, null=True)  # Field name made lowercase.
    pagocom = models.IntegerField(db_column='PagoCom', blank=True, null=True)  # Field name made lowercase.
    numerobanco = models.CharField(db_column='NumeroBanco', max_length=30, blank=True, null=True)  # Field name made lowercase.
    os = models.IntegerField(db_column='OS', blank=True, null=True)  # Field name made lowercase.
    process = models.DateField(db_column='Process', blank=True, null=True)  # Field name made lowercase.
    esp = models.CharField(db_column='ESP', max_length=2, blank=True, null=True)  # Field name made lowercase.
    empresa = models.IntegerField(db_column='Empresa', blank=True, null=True)  # Field name made lowercase.
    sequencia2 = models.IntegerField(db_column='Sequencia2', blank=True, null=True)  # Field name made lowercase.
    vendedor = models.IntegerField(blank=True, null=True)
    recebimento = models.IntegerField(blank=True, null=True)
    baixaparcial = models.IntegerField(db_column='BaixaParcial', blank=True, null=True)  # Field name made lowercase.
    saldobaixaparcial = models.FloatField(db_column='SaldoBaixaParcial', blank=True, null=True)  # Field name made lowercase.
    desconto = models.FloatField(blank=True, null=True)
    notaeletronica = models.IntegerField(blank=True, null=True)
    serie = models.IntegerField(blank=True, null=True)
    modelo = models.IntegerField(blank=True, null=True)
    documentofiscal = models.CharField(db_column='DocumentoFiscal', max_length=3, blank=True, null=True)  # Field name made lowercase.
    numerodocumento = models.IntegerField(db_column='NumeroDocumento', blank=True, null=True)  # Field name made lowercase.
    perdido = models.IntegerField(db_column='Perdido', blank=True, null=True, db_comment='0-false 1-true')  # Field name made lowercase.
    dataperdido = models.DateField(db_column='DataPerdido', blank=True, null=True)  # Field name made lowercase.
    obsperdido = models.CharField(db_column='ObsPerdido', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'recebimentos_ajuste'


class RecebimentosDetalhe(models.Model):
    id_recebimento = models.IntegerField(blank=True, null=True)
    pago_com = models.CharField(max_length=16, blank=True, null=True)
    valor_pago = models.FloatField(blank=True, null=True)
    data_pagto = models.DateField(blank=True, null=True)
    funcionario = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    lote = models.IntegerField(blank=True, null=True)
    cartao_id = models.IntegerField(blank=True, null=True)
    cartao_nome = models.CharField(max_length=50, blank=True, null=True)
    cartao_doc = models.CharField(max_length=15, blank=True, null=True)
    cartao_parcela = models.IntegerField(blank=True, null=True)
    conta_id = models.IntegerField(blank=True, null=True)
    conta_corrente = models.CharField(max_length=20, blank=True, null=True)
    conta_nome = models.CharField(max_length=50, blank=True, null=True)
    conta_data_baixa = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'recebimentos_detalhe'


class RecebimentosRenegociacao(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    data = models.DateField(db_column='Data', blank=True, null=True)  # Field name made lowercase.
    hora = models.TimeField(db_column='Hora', blank=True, null=True)  # Field name made lowercase.
    cliente = models.IntegerField(db_column='Cliente', blank=True, null=True)  # Field name made lowercase.
    usuario = models.IntegerField(db_column='Usuario', blank=True, null=True)  # Field name made lowercase.
    total = models.FloatField(db_column='Total', blank=True, null=True)  # Field name made lowercase.
    descacre = models.FloatField(db_column='DescAcre', blank=True, null=True)  # Field name made lowercase.
    totalfinal = models.FloatField(db_column='TotalFinal', blank=True, null=True)  # Field name made lowercase.
    maquina = models.CharField(db_column='Maquina', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'recebimentos_renegociacao'


class Recebprod(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    pdv = models.IntegerField(db_column='PDV', blank=True, null=True)  # Field name made lowercase.
    caixa = models.IntegerField(db_column='Caixa', blank=True, null=True)  # Field name made lowercase.
    pedido = models.BigIntegerField(db_column='Pedido', blank=True, null=True)  # Field name made lowercase.
    cliente = models.IntegerField(db_column='Cliente', blank=True, null=True)  # Field name made lowercase.
    codigobarra = models.CharField(db_column='CodigoBarra', max_length=30, blank=True, null=True)  # Field name made lowercase.
    codigo = models.CharField(db_column='Codigo', max_length=30, blank=True, null=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=100, blank=True, null=True)  # Field name made lowercase.
    aplicacao = models.CharField(db_column='Aplicacao', max_length=40, blank=True, null=True)  # Field name made lowercase.
    quantidade = models.FloatField(db_column='Quantidade', blank=True, null=True)  # Field name made lowercase.
    unitario = models.FloatField(db_column='Unitario', blank=True, null=True)  # Field name made lowercase.
    total = models.FloatField(db_column='Total', blank=True, null=True)  # Field name made lowercase.
    descacre = models.FloatField(db_column='DescAcre', blank=True, null=True)  # Field name made lowercase.
    vendaunitario = models.FloatField(db_column='VendaUnitario', blank=True, null=True)  # Field name made lowercase.
    vendatotal = models.FloatField(db_column='VendaTotal', blank=True, null=True)  # Field name made lowercase.
    unidade = models.CharField(db_column='Unidade', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cfe = models.IntegerField(db_column='CFe', blank=True, null=True)  # Field name made lowercase.
    funcionario = models.IntegerField(db_column='Funcionario', blank=True, null=True)  # Field name made lowercase.
    usuario = models.IntegerField(db_column='Usuario', blank=True, null=True)  # Field name made lowercase.
    data = models.DateField(db_column='Data', blank=True, null=True)  # Field name made lowercase.
    hora = models.TimeField(db_column='Hora', blank=True, null=True)  # Field name made lowercase.
    empresa = models.IntegerField(db_column='Empresa', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'recebprod'


class Recebprodpago(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    idold = models.BigIntegerField(db_column='IDOld', blank=True, null=True)  # Field name made lowercase.
    pdv = models.IntegerField(db_column='PDV', blank=True, null=True)  # Field name made lowercase.
    caixa = models.IntegerField(db_column='Caixa', blank=True, null=True)  # Field name made lowercase.
    pdvbaixa = models.IntegerField(db_column='PDVBaixa', blank=True, null=True)  # Field name made lowercase.
    caixabaixa = models.IntegerField(db_column='CaixaBaixa', blank=True, null=True)  # Field name made lowercase.
    pedido = models.BigIntegerField(db_column='Pedido', blank=True, null=True)  # Field name made lowercase.
    cliente = models.IntegerField(db_column='Cliente', blank=True, null=True)  # Field name made lowercase.
    codigobarra = models.CharField(db_column='CodigoBarra', max_length=30, blank=True, null=True)  # Field name made lowercase.
    codigo = models.CharField(db_column='Codigo', max_length=30, blank=True, null=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=100, blank=True, null=True)  # Field name made lowercase.
    aplicacao = models.CharField(db_column='Aplicacao', max_length=40, blank=True, null=True)  # Field name made lowercase.
    quantidade = models.FloatField(db_column='Quantidade', blank=True, null=True)  # Field name made lowercase.
    unitario = models.FloatField(db_column='Unitario', blank=True, null=True)  # Field name made lowercase.
    total = models.FloatField(db_column='Total', blank=True, null=True)  # Field name made lowercase.
    descacre = models.FloatField(db_column='DescAcre', blank=True, null=True)  # Field name made lowercase.
    datapagto = models.DateField(db_column='DataPagto', blank=True, null=True)  # Field name made lowercase.
    valorpago = models.FloatField(db_column='ValorPago', blank=True, null=True)  # Field name made lowercase.
    usuariobaixa = models.IntegerField(db_column='UsuarioBaixa', blank=True, null=True)  # Field name made lowercase.
    recebimento = models.IntegerField(db_column='Recebimento', blank=True, null=True)  # Field name made lowercase.
    idrecebimento = models.IntegerField(db_column='IDRecebimento', blank=True, null=True)  # Field name made lowercase.
    vendaunitario = models.FloatField(db_column='VendaUnitario', blank=True, null=True)  # Field name made lowercase.
    vendatotal = models.FloatField(db_column='VendaTotal', blank=True, null=True)  # Field name made lowercase.
    unidade = models.CharField(db_column='Unidade', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cfe = models.IntegerField(db_column='CFe', blank=True, null=True)  # Field name made lowercase.
    funcionario = models.IntegerField(db_column='Funcionario', blank=True, null=True)  # Field name made lowercase.
    usuario = models.IntegerField(db_column='Usuario', blank=True, null=True)  # Field name made lowercase.
    data = models.DateField(db_column='Data', blank=True, null=True)  # Field name made lowercase.
    hora = models.TimeField(db_column='Hora', blank=True, null=True)  # Field name made lowercase.
    empresa = models.IntegerField(db_column='Empresa', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'recebprodpago'


class Regiao(models.Model):
    codigo = models.AutoField(db_column='Codigo', primary_key=True)  # Field name made lowercase.
    regiao = models.CharField(db_column='Regiao', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cadastro = models.DateField(db_column='Cadastro', blank=True, null=True)  # Field name made lowercase.
    empresa = models.IntegerField(db_column='Empresa', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'regiao'


class Registro(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    maquina = models.CharField(max_length=100, blank=True, null=True)
    nome_maquina = models.CharField(max_length=100, blank=True, null=True)
    chv = models.CharField(max_length=100, blank=True, null=True)
    val = models.CharField(max_length=100, blank=True, null=True)
    versao_software = models.CharField(max_length=100, blank=True, null=True)
    data_versao_software = models.DateField(blank=True, null=True)
    ativa = models.CharField(max_length=1, blank=True, null=True)
    host = models.CharField(db_column='Host', max_length=50, blank=True, null=True)  # Field name made lowercase.
    adress = models.CharField(db_column='Adress', max_length=50, blank=True, null=True)  # Field name made lowercase.
    hard = models.CharField(db_column='Hard', max_length=50, blank=True, null=True)  # Field name made lowercase.
    espira = models.CharField(db_column='Espira', max_length=40, blank=True, null=True)  # Field name made lowercase.
    data = models.CharField(db_column='Data', max_length=40, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'registro'


class Relattemp(models.Model):
    campo1 = models.IntegerField(blank=True, null=True)
    campo2 = models.CharField(max_length=10, blank=True, null=True)
    campo3 = models.CharField(max_length=10, blank=True, null=True)
    campo4 = models.IntegerField(blank=True, null=True)
    campo5 = models.IntegerField(blank=True, null=True)
    campo6 = models.CharField(max_length=60, blank=True, null=True)
    campo7 = models.CharField(max_length=40, blank=True, null=True)
    campo8 = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'relattemp'


class Relatvendatemp(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    campo1 = models.CharField(db_column='Campo1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    campo2 = models.CharField(db_column='Campo2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    campo3 = models.CharField(db_column='Campo3', max_length=100, blank=True, null=True)  # Field name made lowercase.
    empresa = models.IntegerField(db_column='Empresa', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'relatvendatemp'


class Requisicao(models.Model):
    codigo = models.AutoField(primary_key=True)
    numeroaleatorio = models.IntegerField(blank=True, null=True)
    cliente = models.IntegerField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    descacre = models.FloatField(blank=True, null=True)
    totalgeral = models.FloatField(blank=True, null=True)
    vendedor = models.IntegerField(blank=True, null=True)
    data = models.DateField(blank=True, null=True)
    hora = models.TimeField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    data_cancelamento = models.DateField(blank=True, null=True)
    hora_cancelamento = models.TimeField(blank=True, null=True)
    usuario_cancelamento = models.IntegerField(blank=True, null=True)
    maquina_cancelamento = models.CharField(max_length=40, blank=True, null=True)
    portador = models.CharField(max_length=30, blank=True, null=True)
    observacao = models.CharField(max_length=50, blank=True, null=True)
    condicao = models.CharField(max_length=30, blank=True, null=True)
    oficina = models.IntegerField(blank=True, null=True)
    fechamento = models.IntegerField(blank=True, null=True)
    datafechamento = models.DateField(blank=True, null=True)
    agrupamento = models.IntegerField(blank=True, null=True)
    data_agrupamento = models.DateTimeField(blank=True, null=True)
    usuario_agrupamento = models.IntegerField(blank=True, null=True)
    maquina_agrupamento = models.CharField(max_length=100, blank=True, null=True)
    nota = models.IntegerField(blank=True, null=True)
    notaeletronica = models.IntegerField(blank=True, null=True)
    serie = models.IntegerField(blank=True, null=True)
    modelo = models.IntegerField(blank=True, null=True)
    peso = models.FloatField(blank=True, null=True)
    conferido = models.IntegerField(db_column='Conferido', blank=True, null=True)  # Field name made lowercase.
    dataconf = models.DateField(db_column='DataConf', blank=True, null=True)  # Field name made lowercase.
    horaconf = models.TimeField(db_column='HoraConf', blank=True, null=True)  # Field name made lowercase.
    usuarioconf = models.IntegerField(db_column='UsuarioConf', blank=True, null=True)  # Field name made lowercase.
    funcionarioconf = models.IntegerField(db_column='FuncionarioConf', blank=True, null=True)  # Field name made lowercase.
    observacaoconf = models.TextField(db_column='ObservacaoConf', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'requisicao'


class Requisicaofecha(models.Model):
    codigo = models.AutoField(primary_key=True)
    pdv = models.IntegerField(blank=True, null=True)
    caixa = models.IntegerField(blank=True, null=True)
    cliente = models.IntegerField(blank=True, null=True)
    tipo = models.CharField(max_length=5, blank=True, null=True)
    data = models.DateField(blank=True, null=True)
    hora = models.TimeField(blank=True, null=True)
    requisicao = models.IntegerField(blank=True, null=True)
    condicao = models.IntegerField(blank=True, null=True)
    frete = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    descacre = models.FloatField(blank=True, null=True)
    totalgeral = models.FloatField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    vendavista = models.FloatField(blank=True, null=True)
    vendaprazo = models.FloatField(blank=True, null=True)
    data_cancelamento = models.DateField(blank=True, null=True)
    hora_cancelamento = models.TimeField(blank=True, null=True)
    usuario_cancelamento = models.IntegerField(blank=True, null=True)
    maquina_cancelamento = models.CharField(max_length=40, blank=True, null=True)
    nota = models.IntegerField(blank=True, null=True)
    notaeletronica = models.IntegerField(blank=True, null=True)
    serie = models.IntegerField(blank=True, null=True)
    modelo = models.IntegerField(blank=True, null=True)
    chavenfe = models.CharField(max_length=44, blank=True, null=True)
    cupom = models.IntegerField(blank=True, null=True)
    cfe = models.IntegerField(blank=True, null=True)
    chavecfe = models.CharField(max_length=44, blank=True, null=True)
    seriecfe = models.CharField(max_length=20, blank=True, null=True)
    rps = models.IntegerField(blank=True, null=True)
    nfse = models.IntegerField(blank=True, null=True)
    nfstemp = models.IntegerField(blank=True, null=True)
    vendedor = models.IntegerField(blank=True, null=True)
    portador = models.CharField(max_length=40, blank=True, null=True)
    observacao = models.CharField(max_length=50, blank=True, null=True)
    oficina = models.IntegerField(blank=True, null=True)
    transportadora = models.IntegerField(blank=True, null=True)
    profissional = models.IntegerField(blank=True, null=True)
    agrupamento = models.IntegerField(blank=True, null=True)
    agrupado = models.IntegerField(blank=True, null=True)
    numeroaleatorio = models.IntegerField(blank=True, null=True)
    servico = models.FloatField(blank=True, null=True)
    descserv = models.FloatField(blank=True, null=True)
    totalserv = models.FloatField(blank=True, null=True)
    comissao = models.FloatField(blank=True, null=True)
    grantotal = models.FloatField(blank=True, null=True)
    tabela = models.CharField(max_length=1, blank=True, null=True)
    peso = models.FloatField(blank=True, null=True)
    entregue = models.IntegerField(blank=True, null=True)
    funcionario_entrega = models.IntegerField(blank=True, null=True)
    data_entrega = models.DateField(blank=True, null=True)
    venda_a_vista = models.IntegerField(blank=True, null=True)
    usuario_venda_a_vista = models.IntegerField(blank=True, null=True)
    conferido = models.IntegerField(db_column='Conferido', blank=True, null=True)  # Field name made lowercase.
    dataconf = models.DateField(db_column='DataConf', blank=True, null=True)  # Field name made lowercase.
    horaconf = models.TimeField(db_column='HoraConf', blank=True, null=True)  # Field name made lowercase.
    usuarioconf = models.IntegerField(db_column='UsuarioConf', blank=True, null=True)  # Field name made lowercase.
    funcionarioconf = models.IntegerField(db_column='FuncionarioConf', blank=True, null=True)  # Field name made lowercase.
    observacaoconf = models.TextField(db_column='ObservacaoConf', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'requisicaofecha'


class Requisicaotransf(models.Model):
    codigo = models.AutoField(primary_key=True)
    cliente = models.IntegerField(blank=True, null=True)
    tipo = models.CharField(max_length=5, blank=True, null=True)
    data = models.DateField(blank=True, null=True)
    hora = models.TimeField(blank=True, null=True)
    requisicao = models.IntegerField(blank=True, null=True)
    condicao = models.IntegerField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    descacre = models.FloatField(blank=True, null=True)
    totalgeral = models.FloatField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    nota = models.IntegerField(blank=True, null=True)
    notaeletronica = models.IntegerField(blank=True, null=True)
    serie = models.IntegerField(blank=True, null=True)
    modelo = models.IntegerField(blank=True, null=True)
    cupom = models.IntegerField(blank=True, null=True)
    vendedor = models.IntegerField(blank=True, null=True)
    portador = models.CharField(max_length=40, blank=True, null=True)
    observacao = models.CharField(max_length=50, blank=True, null=True)
    oficina = models.IntegerField(blank=True, null=True)
    transportadora = models.IntegerField(blank=True, null=True)
    profissional = models.IntegerField(blank=True, null=True)
    agrupamento = models.IntegerField(blank=True, null=True)
    servico = models.FloatField(blank=True, null=True)
    descserv = models.FloatField(blank=True, null=True)
    totalserv = models.FloatField(blank=True, null=True)
    comissao = models.FloatField(blank=True, null=True)
    grantotal = models.FloatField(blank=True, null=True)
    tabela = models.CharField(max_length=1, blank=True, null=True)
    peso = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'requisicaotransf'


class Saldo(models.Model):
    saldo = models.FloatField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'saldo'


class SaldoCaixa(models.Model):
    saldo = models.FloatField(primary_key=True)
    dinheiro_f = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'saldo_caixa'


class SatCartaoCredito(models.Model):
    codigo = models.CharField(db_column='Codigo', primary_key=True, max_length=3)  # Field name made lowercase.
    empresa = models.CharField(db_column='Empresa', max_length=60, blank=True, null=True)  # Field name made lowercase.
    cnpj = models.CharField(db_column='CNPJ', max_length=18, blank=True, null=True)  # Field name made lowercase.
    ativo = models.IntegerField(db_column='Ativo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sat_cartao_credito'


class SatCfe(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    cfe = models.IntegerField(db_column='CFe', blank=True, null=True)  # Field name made lowercase.
    chave = models.CharField(db_column='Chave', max_length=47, blank=True, null=True)  # Field name made lowercase.
    numeroserie = models.IntegerField(db_column='NumeroSerie', blank=True, null=True)  # Field name made lowercase.
    numerosessao = models.IntegerField(db_column='NumeroSessao', blank=True, null=True)  # Field name made lowercase.
    notaeletronica = models.IntegerField(db_column='NotaEletronica', blank=True, null=True)  # Field name made lowercase.
    serie = models.IntegerField(db_column='Serie', blank=True, null=True)  # Field name made lowercase.
    modelo = models.IntegerField(db_column='Modelo', blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    data = models.DateField(db_column='Data', blank=True, null=True)  # Field name made lowercase.
    hora = models.TimeField(db_column='Hora', blank=True, null=True)  # Field name made lowercase.
    informarcliente = models.IntegerField(db_column='InformarCliente', blank=True, null=True)  # Field name made lowercase.
    cliente = models.IntegerField(db_column='Cliente', blank=True, null=True)  # Field name made lowercase.
    cpf = models.CharField(db_column='CPF', max_length=14, blank=True, null=True)  # Field name made lowercase.
    vendedor = models.IntegerField(db_column='Vendedor', blank=True, null=True)  # Field name made lowercase.
    produtos = models.FloatField(db_column='Produtos', blank=True, null=True)  # Field name made lowercase.
    desconto = models.FloatField(db_column='Desconto', blank=True, null=True)  # Field name made lowercase.
    outrasdespesas = models.FloatField(db_column='OutrasDespesas', blank=True, null=True)  # Field name made lowercase.
    icms = models.FloatField(db_column='ICMS', blank=True, null=True)  # Field name made lowercase.
    pis = models.FloatField(db_column='Pis', blank=True, null=True)  # Field name made lowercase.
    cofins = models.FloatField(db_column='Cofins', blank=True, null=True)  # Field name made lowercase.
    total = models.FloatField(db_column='Total', blank=True, null=True)  # Field name made lowercase.
    descacre = models.FloatField(db_column='DescAcre', blank=True, null=True)  # Field name made lowercase.
    totalgeral = models.FloatField(db_column='TotalGeral', blank=True, null=True)  # Field name made lowercase.
    xml = models.TextField(db_column='XML', blank=True, null=True)  # Field name made lowercase.
    xmlcancelamento = models.TextField(db_column='XMLCancelamento', blank=True, null=True)  # Field name made lowercase.
    nfe = models.IntegerField(db_column='NFe', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sat_cfe'


class SatMeioPagamento(models.Model):
    codigo = models.CharField(db_column='Codigo', primary_key=True, max_length=2)  # Field name made lowercase.
    meiopagamento = models.CharField(db_column='MeioPagamento', max_length=25, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sat_meio_pagamento'


class SatPagamento(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_cfe = models.IntegerField(db_column='ID_CFe', blank=True, null=True)  # Field name made lowercase.
    cfe = models.IntegerField(db_column='CFe', blank=True, null=True)  # Field name made lowercase.
    id_pedido = models.IntegerField(db_column='ID_Pedido', blank=True, null=True)  # Field name made lowercase.
    codigomp = models.CharField(db_column='CodigoMP', max_length=2, blank=True, null=True)  # Field name made lowercase.
    nomemp = models.CharField(db_column='NomeMP', max_length=25, blank=True, null=True)  # Field name made lowercase.
    valor = models.FloatField(db_column='Valor', blank=True, null=True)  # Field name made lowercase.
    codigocartao = models.CharField(db_column='CodigoCartao', max_length=3, blank=True, null=True)  # Field name made lowercase.
    nomecartao = models.CharField(db_column='NomeCartao', max_length=60, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sat_pagamento'


class SatProduto(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_cfe = models.IntegerField(db_column='ID_CFe', blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    cupom = models.IntegerField(db_column='Cupom', blank=True, null=True)  # Field name made lowercase.
    marca = models.CharField(db_column='Marca', max_length=20, blank=True, null=True)  # Field name made lowercase.
    modelo = models.CharField(db_column='Modelo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    numeroserie = models.CharField(db_column='NumeroSerie', max_length=20, blank=True, null=True)  # Field name made lowercase.
    data = models.DateField(db_column='Data', blank=True, null=True)  # Field name made lowercase.
    cliente = models.IntegerField(db_column='Cliente', blank=True, null=True)  # Field name made lowercase.
    codigo = models.CharField(db_column='Codigo', max_length=40, blank=True, null=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=60, blank=True, null=True)  # Field name made lowercase.
    codigobarra = models.CharField(db_column='CodigoBarra', max_length=14, blank=True, null=True)  # Field name made lowercase.
    ncm = models.CharField(db_column='NCM', max_length=8, blank=True, null=True)  # Field name made lowercase.
    cest = models.CharField(db_column='Cest', max_length=7, blank=True, null=True)  # Field name made lowercase.
    cfop = models.CharField(db_column='CFOP', max_length=4, blank=True, null=True)  # Field name made lowercase.
    anpsimp = models.CharField(db_column='AnpSimp', max_length=9, blank=True, null=True)  # Field name made lowercase.
    descricaoanp = models.CharField(db_column='DescricaoAnp', max_length=100, blank=True, null=True)  # Field name made lowercase.
    unidade = models.CharField(db_column='Unidade', max_length=2, blank=True, null=True)  # Field name made lowercase.
    monofasico = models.IntegerField(db_column='Monofasico', blank=True, null=True)  # Field name made lowercase.
    quantidade = models.FloatField(db_column='Quantidade', blank=True, null=True)  # Field name made lowercase.
    unitario = models.FloatField(db_column='Unitario', blank=True, null=True)  # Field name made lowercase.
    total = models.FloatField(db_column='Total', blank=True, null=True)  # Field name made lowercase.
    desconto = models.FloatField(db_column='Desconto', blank=True, null=True)  # Field name made lowercase.
    acrescimo = models.FloatField(db_column='Acrescimo', blank=True, null=True)  # Field name made lowercase.
    valortributos = models.FloatField(db_column='ValorTributos', blank=True, null=True)  # Field name made lowercase.
    tributofederal = models.FloatField(db_column='TributoFederal', blank=True, null=True)  # Field name made lowercase.
    tributoestadual = models.FloatField(db_column='TributoEstadual', blank=True, null=True)  # Field name made lowercase.
    tributomunicipal = models.FloatField(db_column='TributoMunicipal', blank=True, null=True)  # Field name made lowercase.
    icmsorigem = models.CharField(db_column='IcmsOrigem', max_length=1, blank=True, null=True)  # Field name made lowercase.
    icmscst = models.CharField(db_column='IcmsCst', max_length=3, blank=True, null=True)  # Field name made lowercase.
    icmsbasecalculo = models.FloatField(db_column='IcmsBaseCalculo', blank=True, null=True)  # Field name made lowercase.
    icmsaliquota = models.FloatField(db_column='IcmsAliquota', blank=True, null=True)  # Field name made lowercase.
    icmsvalor = models.FloatField(db_column='IcmsValor', blank=True, null=True)  # Field name made lowercase.
    piscst = models.CharField(db_column='PisCst', max_length=2, blank=True, null=True)  # Field name made lowercase.
    pisbasecalculo = models.FloatField(db_column='PisBaseCalculo', blank=True, null=True)  # Field name made lowercase.
    pisaliquota = models.FloatField(db_column='PisAliquota', blank=True, null=True)  # Field name made lowercase.
    pisvalor = models.FloatField(db_column='PisValor', blank=True, null=True)  # Field name made lowercase.
    cofinscst = models.CharField(db_column='CofinsCst', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cofinsbasecalculo = models.FloatField(db_column='CofinsBaseCalculo', blank=True, null=True)  # Field name made lowercase.
    cofinsaliquota = models.FloatField(db_column='CofinsAliquota', blank=True, null=True)  # Field name made lowercase.
    cofinsvalor = models.FloatField(db_column='CofinsValor', blank=True, null=True)  # Field name made lowercase.
    vendaunitario = models.FloatField(db_column='VendaUnitario', blank=True, null=True)  # Field name made lowercase.
    vendatotal = models.FloatField(db_column='VendaTotal', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sat_produto'


class Separacao(models.Model):
    id = models.IntegerField(blank=True, null=True)
    data = models.DateField(blank=True, null=True)
    hora = models.TimeField(blank=True, null=True)
    os = models.IntegerField(blank=True, null=True)
    id_prod = models.IntegerField(blank=True, null=True)
    codigo = models.CharField(max_length=30, blank=True, null=True)
    descricao = models.CharField(max_length=50, blank=True, null=True)
    quantidade = models.FloatField(blank=True, null=True)
    localizacao = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'separacao'


class Servicos(models.Model):
    codigo = models.AutoField(db_column='Codigo', primary_key=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=60, blank=True, null=True)  # Field name made lowercase.
    preco = models.FloatField(db_column='Preco', blank=True, null=True)  # Field name made lowercase.
    comissionado = models.IntegerField(blank=True, null=True)
    ultimavenda = models.DateField(db_column='UltimaVenda', blank=True, null=True)  # Field name made lowercase.
    ultimoaumento = models.DateField(db_column='UltimoAumento', blank=True, null=True)  # Field name made lowercase.
    janeiro = models.FloatField(db_column='Janeiro', blank=True, null=True)  # Field name made lowercase.
    fevereiro = models.FloatField(db_column='Fevereiro', blank=True, null=True)  # Field name made lowercase.
    marco = models.FloatField(db_column='Marco', blank=True, null=True)  # Field name made lowercase.
    abril = models.FloatField(db_column='Abril', blank=True, null=True)  # Field name made lowercase.
    maio = models.FloatField(db_column='Maio', blank=True, null=True)  # Field name made lowercase.
    junho = models.FloatField(db_column='Junho', blank=True, null=True)  # Field name made lowercase.
    julho = models.FloatField(db_column='Julho', blank=True, null=True)  # Field name made lowercase.
    agosto = models.FloatField(db_column='Agosto', blank=True, null=True)  # Field name made lowercase.
    setembro = models.FloatField(db_column='Setembro', blank=True, null=True)  # Field name made lowercase.
    outubro = models.FloatField(db_column='Outubro', blank=True, null=True)  # Field name made lowercase.
    novembro = models.FloatField(db_column='Novembro', blank=True, null=True)  # Field name made lowercase.
    dezembro = models.FloatField(db_column='Dezembro', blank=True, null=True)  # Field name made lowercase.
    observacao = models.TextField(db_column='Observacao', blank=True, null=True)  # Field name made lowercase.
    cadastro = models.DateField(db_column='Cadastro', blank=True, null=True)  # Field name made lowercase.
    empresa = models.IntegerField(db_column='Empresa', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'servicos'


class Servicosfiscais(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    numeroid = models.IntegerField(db_column='NumeroID', blank=True, null=True)  # Field name made lowercase.
    numeronota = models.IntegerField(db_column='NumeroNota', blank=True, null=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=80, blank=True, null=True)  # Field name made lowercase.
    unidade = models.CharField(db_column='Unidade', max_length=2, blank=True, null=True)  # Field name made lowercase.
    quantidade = models.FloatField(db_column='Quantidade', blank=True, null=True)  # Field name made lowercase.
    unitario = models.FloatField(db_column='Unitario', blank=True, null=True)  # Field name made lowercase.
    total = models.FloatField(db_column='Total', blank=True, null=True)  # Field name made lowercase.
    empresa = models.IntegerField(db_column='Empresa', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'servicosfiscais'


class Servicosorc(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    numero = models.IntegerField(db_column='Numero', blank=True, null=True)  # Field name made lowercase.
    codigo = models.IntegerField(db_column='Codigo', blank=True, null=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=60, blank=True, null=True)  # Field name made lowercase.
    quantidade = models.FloatField(db_column='Quantidade', blank=True, null=True)  # Field name made lowercase.
    unitario = models.FloatField(db_column='Unitario', blank=True, null=True)  # Field name made lowercase.
    total = models.FloatField(db_column='Total', blank=True, null=True)  # Field name made lowercase.
    empresa = models.IntegerField(db_column='Empresa', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'servicosorc'


class Servicosos(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nos = models.IntegerField(db_column='NOS', blank=True, null=True)  # Field name made lowercase.
    cliente = models.IntegerField(db_column='Cliente', blank=True, null=True)  # Field name made lowercase.
    garantia = models.IntegerField(db_column='Garantia', blank=True, null=True)  # Field name made lowercase.
    codigo = models.IntegerField(db_column='Codigo', blank=True, null=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=150, blank=True, null=True)  # Field name made lowercase.
    quantidade = models.FloatField(db_column='Quantidade', blank=True, null=True)  # Field name made lowercase.
    unitario = models.FloatField(db_column='Unitario', blank=True, null=True)  # Field name made lowercase.
    total = models.FloatField(db_column='Total', blank=True, null=True)  # Field name made lowercase.
    descacre = models.FloatField(db_column='DescAcre', blank=True, null=True)  # Field name made lowercase.
    vendaunitario = models.FloatField(db_column='VendaUnitario', blank=True, null=True)  # Field name made lowercase.
    vendatotal = models.FloatField(db_column='VendaTotal', blank=True, null=True)  # Field name made lowercase.
    funcionario = models.IntegerField(db_column='Funcionario', blank=True, null=True)  # Field name made lowercase.
    consultor = models.IntegerField(db_column='Consultor', blank=True, null=True)  # Field name made lowercase.
    data = models.DateField(db_column='Data', blank=True, null=True)  # Field name made lowercase.
    hora = models.TimeField(db_column='Hora', blank=True, null=True)  # Field name made lowercase.
    usuario = models.IntegerField(db_column='Usuario', blank=True, null=True)  # Field name made lowercase.
    empresa = models.IntegerField(db_column='Empresa', blank=True, null=True)  # Field name made lowercase.
    mecanico = models.IntegerField(blank=True, null=True)
    datafinalizacao = models.DateField(db_column='DataFinalizacao', blank=True, null=True)  # Field name made lowercase.
    horafinalizacao = models.TimeField(db_column='HoraFinalizacao', blank=True, null=True)  # Field name made lowercase.
    nftemp = models.IntegerField(blank=True, null=True)
    nota = models.IntegerField(blank=True, null=True)
    notaeletronica = models.IntegerField(blank=True, null=True)
    rps = models.IntegerField(blank=True, null=True)
    nfse = models.IntegerField(blank=True, null=True)
    nfstemp = models.IntegerField(blank=True, null=True)
    fatura = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'servicosos'


class Subconta(models.Model):
    codigo = models.AutoField(db_column='Codigo', primary_key=True)  # Field name made lowercase.
    conta = models.IntegerField(db_column='Conta', blank=True, null=True)  # Field name made lowercase.
    contadesc = models.CharField(db_column='ContaDesc', max_length=60, blank=True, null=True)  # Field name made lowercase.
    subconta = models.CharField(db_column='SubConta', max_length=60, blank=True, null=True)  # Field name made lowercase.
    empresa = models.IntegerField(blank=True, null=True)
    despesa = models.CharField(max_length=12, blank=True, null=True)
    custo = models.CharField(max_length=8, blank=True, null=True)
    imposto = models.IntegerField(blank=True, null=True)
    compra = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'subconta'


class Subcontatemp(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    campo1 = models.CharField(db_column='Campo1', max_length=60, blank=True, null=True)  # Field name made lowercase.
    campo2 = models.CharField(db_column='Campo2', max_length=60, blank=True, null=True)  # Field name made lowercase.
    campo3 = models.CharField(db_column='Campo3', max_length=60, blank=True, null=True)  # Field name made lowercase.
    campo4 = models.CharField(db_column='Campo4', max_length=60, blank=True, null=True)  # Field name made lowercase.
    campo5 = models.CharField(db_column='Campo5', max_length=60, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'subcontatemp'


class Sugestao(models.Model):
    data = models.DateField(blank=True, null=True)
    funcionario = models.IntegerField(blank=True, null=True)
    setor = models.IntegerField(blank=True, null=True)
    sugestao = models.TextField(blank=True, null=True)
    resposta = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sugestao'


class SugestaoSetor(models.Model):
    codigo = models.AutoField(db_column='Codigo', primary_key=True)  # Field name made lowercase.
    setor = models.CharField(db_column='Setor', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cadastro = models.DateField(db_column='Cadastro', blank=True, null=True)  # Field name made lowercase.
    empresa = models.IntegerField(db_column='Empresa', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sugestao_setor'


class System(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    codigo = models.IntegerField(db_column='Codigo', blank=True, null=True)  # Field name made lowercase.
    idyandeh = models.IntegerField(db_column='IDYandeh', blank=True, null=True)  # Field name made lowercase.
    empresa = models.CharField(db_column='Empresa', max_length=60, blank=True, null=True)  # Field name made lowercase.
    razao = models.CharField(db_column='Razao', max_length=60, blank=True, null=True)  # Field name made lowercase.
    proprietario = models.CharField(max_length=60, blank=True, null=True)
    cgc = models.CharField(db_column='CGC', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ie = models.CharField(db_column='IE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    end = models.CharField(db_column='End', max_length=60, blank=True, null=True)  # Field name made lowercase.
    endereco = models.CharField(db_column='Endereco', max_length=60, blank=True, null=True)  # Field name made lowercase.
    numero = models.CharField(db_column='Numero', max_length=35, blank=True, null=True)  # Field name made lowercase.
    bairro = models.CharField(db_column='Bairro', max_length=60, blank=True, null=True)  # Field name made lowercase.
    cep = models.CharField(db_column='Cep', max_length=9, blank=True, null=True)  # Field name made lowercase.
    cidade = models.CharField(db_column='Cidade', max_length=60, blank=True, null=True)  # Field name made lowercase.
    codigocidade = models.IntegerField(db_column='CodigoCidade', blank=True, null=True)  # Field name made lowercase.
    uf = models.CharField(db_column='UF', max_length=2, blank=True, null=True)  # Field name made lowercase.
    codigoestado = models.IntegerField(db_column='CodigoEstado', blank=True, null=True)  # Field name made lowercase.
    fone = models.CharField(db_column='Fone', max_length=13, blank=True, null=True)  # Field name made lowercase.
    fax = models.CharField(db_column='Fax', max_length=13, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=60, blank=True, null=True)  # Field name made lowercase.
    home = models.CharField(db_column='Home', max_length=60, blank=True, null=True)  # Field name made lowercase.
    cadastro = models.DateField(db_column='Cadastro', blank=True, null=True)  # Field name made lowercase.
    padrao = models.IntegerField(db_column='Padrao', blank=True, null=True)  # Field name made lowercase.
    image = models.CharField(db_column='Image', max_length=250, blank=True, null=True)  # Field name made lowercase.
    tipocliente = models.IntegerField(blank=True, null=True)
    regime_tributario = models.IntegerField(db_column='Regime_Tributario', blank=True, null=True)  # Field name made lowercase.
    tipo_estabelecimento = models.IntegerField(db_column='Tipo_Estabelecimento', blank=True, null=True)  # Field name made lowercase.
    direito_credito_icms = models.IntegerField(db_column='Direito_Credito_Icms', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'system'


class TabelaAtividadeFederal(models.Model):
    codigo = models.CharField(db_column='Codigo', primary_key=True, max_length=8)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tabela_atividade_federal'


class TabelaCest(models.Model):
    cest = models.CharField(db_column='CEST', max_length=7)  # Field name made lowercase.
    ncm = models.CharField(db_column='NCM', max_length=8, blank=True, null=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='DESCRICAO', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tabela_cest'


class TabelaCfop(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    cfop = models.IntegerField(db_column='CFOP', blank=True, null=True)  # Field name made lowercase.
    descricao = models.TextField(db_column='DESCRICAO', blank=True, null=True)  # Field name made lowercase.
    aplicacao = models.TextField(db_column='APLICACAO', blank=True, null=True)  # Field name made lowercase.
    nivel = models.IntegerField(db_column='Nivel', blank=True, null=True)  # Field name made lowercase.
    intervalo = models.IntegerField(db_column='Intervalo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tabela_cfop'


class TabelaCnae(models.Model):
    cnae = models.IntegerField(db_column='CNAE', primary_key=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tabela_cnae'


class TabelaDeCor(models.Model):
    codigo = models.AutoField(primary_key=True)
    cor = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tabela_de_cor'


class TabelaDesconto(models.Model):
    a = models.FloatField(db_column='A', blank=True, null=True)  # Field name made lowercase.
    b = models.FloatField(db_column='B', blank=True, null=True)  # Field name made lowercase.
    c = models.FloatField(db_column='C', blank=True, null=True)  # Field name made lowercase.
    d = models.FloatField(db_column='D', blank=True, null=True)  # Field name made lowercase.
    e = models.FloatField(db_column='E', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tabela_desconto'


class TabelaFundoCombatePobreza(models.Model):
    estado = models.CharField(db_column='Estado', primary_key=True, max_length=2)  # Field name made lowercase.
    percentual = models.FloatField(db_column='Percentual', blank=True, null=True)  # Field name made lowercase.
    lei = models.CharField(db_column='Lei', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tabela_fundo_combate_pobreza'


class TabelaGrupo(models.Model):
    grupo = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tabela_grupo'


class TabelaOlhoNoImposto(models.Model):
    codigo = models.CharField(max_length=8)
    ex = models.CharField(max_length=8, blank=True, null=True)
    tabela = models.IntegerField(blank=True, null=True)
    aliqnac = models.FloatField(db_column='aliqNac', blank=True, null=True)  # Field name made lowercase.
    aliqimp = models.FloatField(db_column='aliqImp', blank=True, null=True)  # Field name made lowercase.
    aliqestadual = models.FloatField(db_column='aliqEstadual', blank=True, null=True)  # Field name made lowercase.
    aliqmunicipal = models.FloatField(db_column='aliqMunicipal', blank=True, null=True)  # Field name made lowercase.
    vigenciainicio = models.DateField(db_column='vigenciaInicio', blank=True, null=True)  # Field name made lowercase.
    vigenciafim = models.DateField(db_column='vigenciaFim', blank=True, null=True)  # Field name made lowercase.
    chave = models.CharField(max_length=6, blank=True, null=True)
    versao = models.CharField(max_length=6, blank=True, null=True)
    fonte = models.CharField(max_length=34, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tabela_olho_no_imposto'


class Tempbc(models.Model):
    requisicao = models.IntegerField(db_column='Requisicao', blank=True, null=True)  # Field name made lowercase.
    codigo = models.CharField(db_column='Codigo', max_length=30, blank=True, null=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=100, blank=True, null=True)  # Field name made lowercase.
    quantidade = models.FloatField(db_column='Quantidade', blank=True, null=True)  # Field name made lowercase.
    unitario = models.FloatField(db_column='Unitario', blank=True, null=True)  # Field name made lowercase.
    total = models.FloatField(db_column='Total', blank=True, null=True)  # Field name made lowercase.
    data = models.DateField(db_column='Data', blank=True, null=True)  # Field name made lowercase.
    hora = models.TimeField(db_column='Hora', blank=True, null=True)  # Field name made lowercase.
    empresa = models.IntegerField(db_column='Empresa', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tempbc'


class Tempo(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    tempo = models.IntegerField(db_column='Tempo', blank=True, null=True)  # Field name made lowercase.
    maquina = models.CharField(db_column='Maquina', max_length=30, blank=True, null=True)  # Field name made lowercase.
    empresa = models.IntegerField(db_column='Empresa', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tempo'


class Tempuser(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    usuario = models.IntegerField(db_column='Usuario', blank=True, null=True)  # Field name made lowercase.
    maquina = models.CharField(db_column='Maquina', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ip = models.CharField(db_column='IP', max_length=30, blank=True, null=True)  # Field name made lowercase.
    empresa = models.IntegerField(db_column='Empresa', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tempuser'


class TintasBases(models.Model):
    codprod = models.CharField(db_column='CODPROD', max_length=12, blank=True, null=True)  # Field name made lowercase.
    codbase = models.CharField(db_column='CODBASE', max_length=7, blank=True, null=True)  # Field name made lowercase.
    peso_esp = models.FloatField(db_column='PESO_ESP', blank=True, null=True)  # Field name made lowercase.
    mixing = models.CharField(db_column='MIXING', max_length=40, blank=True, null=True)  # Field name made lowercase.
    embal = models.CharField(db_column='EMBAL', max_length=2, blank=True, null=True)  # Field name made lowercase.
    acao = models.CharField(db_column='ACAO', max_length=255, blank=True, null=True)  # Field name made lowercase.
    estoque = models.FloatField(db_column='ESTOQUE', blank=True, null=True)  # Field name made lowercase.
    icms = models.FloatField(db_column='ICMS', blank=True, null=True)  # Field name made lowercase.
    ipi = models.FloatField(db_column='IPI', blank=True, null=True)  # Field name made lowercase.
    frete = models.FloatField(db_column='FRETE', blank=True, null=True)  # Field name made lowercase.
    desconto = models.FloatField(db_column='DESCONTO', blank=True, null=True)  # Field name made lowercase.
    mva = models.FloatField(db_column='MVA', blank=True, null=True)  # Field name made lowercase.
    icms_subst = models.FloatField(db_column='ICMS_SUBST', blank=True, null=True)  # Field name made lowercase.
    grupo = models.CharField(db_column='GRUPO', max_length=4, blank=True, null=True)  # Field name made lowercase.
    preco_prod = models.FloatField(db_column='PRECO_PROD', blank=True, null=True, db_comment='Preço com Imposto')  # Field name made lowercase.
    qtd_embal_ml = models.FloatField(db_column='QTD_EMBAL_ML', blank=True, null=True)  # Field name made lowercase.
    preco_imp_ml = models.FloatField(db_column='PRECO_IMP_ML', blank=True, null=True, db_comment='Preço com Imposto /')  # Field name made lowercase.
    preco_imp_gr = models.FloatField(db_column='PRECO_IMP_GR', blank=True, null=True, db_comment='Preço com Imposto / (')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tintas_bases'


class TintasEmbalagens(models.Model):
    codemb = models.CharField(db_column='CODEMB', max_length=13, blank=True, null=True)  # Field name made lowercase.
    descemb = models.CharField(db_column='DESCEMB', max_length=8, blank=True, null=True)  # Field name made lowercase.
    disp_formula = models.IntegerField(db_column='DISP_FORMULA', blank=True, null=True)  # Field name made lowercase.
    embal = models.CharField(db_column='EMBAL', max_length=2, blank=True, null=True)  # Field name made lowercase.
    grupo = models.CharField(db_column='GRUPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    quant = models.FloatField(db_column='QUANT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tintas_embalagens'


class TintasFormulas(models.Model):
    codprod = models.CharField(db_column='CODPROD', max_length=12, blank=True, null=True)  # Field name made lowercase.
    condil = models.CharField(db_column='CONDIL', max_length=11, blank=True, null=True)  # Field name made lowercase.
    quant = models.CharField(db_column='QUANT', max_length=15, blank=True, null=True)  # Field name made lowercase.
    base = models.CharField(db_column='BASE', max_length=7, blank=True, null=True)  # Field name made lowercase.
    peso_gr = models.FloatField(db_column='PESO_GR', blank=True, null=True)  # Field name made lowercase.
    versao = models.IntegerField(db_column='VERSAO', blank=True, null=True)  # Field name made lowercase.
    data_atu = models.DateTimeField(db_column='DATA_ATU', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tintas_formulas'


class TintasInfgrupo(models.Model):
    grupo = models.CharField(db_column='GRUPO', max_length=1, blank=True, null=True)  # Field name made lowercase.
    linha = models.CharField(db_column='LINHA', max_length=3, blank=True, null=True)  # Field name made lowercase.
    marca = models.CharField(db_column='MARCA', max_length=10, blank=True, null=True)  # Field name made lowercase.
    quantemb = models.FloatField(db_column='QUANTEMB', blank=True, null=True)  # Field name made lowercase.
    validade = models.IntegerField(db_column='VALIDADE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tintas_infgrupo'


class TintasInfsgrupo(models.Model):
    aspecto = models.CharField(db_column='ASPECTO', max_length=10, blank=True, null=True)  # Field name made lowercase.
    sgrupo = models.IntegerField(db_column='SGRUPO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tintas_infsgrupo'


class TintasMedidas(models.Model):
    quant = models.CharField(db_column='QUANT', max_length=15, blank=True, null=True)  # Field name made lowercase.
    fator = models.FloatField(db_column='FATOR', blank=True, null=True)  # Field name made lowercase.
    grqtd = models.CharField(db_column='GRQTD', max_length=3, blank=True, null=True)  # Field name made lowercase.
    condil = models.CharField(db_column='CONDIL', max_length=11, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tintas_medidas'


class TintasMontadoras(models.Model):
    cod_mont = models.CharField(db_column='Cod_Mont', max_length=3, blank=True, null=True)  # Field name made lowercase.
    montadora = models.CharField(db_column='Montadora', max_length=25, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tintas_montadoras'


class TintasParametros(models.Model):
    produtomolde = models.IntegerField(db_column='ProdutoMolde', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tintas_parametros'


class TintasPrecoform(models.Model):
    codfor = models.CharField(db_column='CODFOR', max_length=12, blank=True, null=True)  # Field name made lowercase.
    condil = models.CharField(db_column='CONDIL', max_length=11, blank=True, null=True)  # Field name made lowercase.
    data_atu = models.DateTimeField(db_column='DATA_ATU', blank=True, null=True)  # Field name made lowercase.
    versao = models.IntegerField(db_column='VERSAO', blank=True, null=True)  # Field name made lowercase.
    preco = models.FloatField(db_column='PRECO', blank=True, null=True)  # Field name made lowercase.
    medida = models.CharField(db_column='MEDIDA', max_length=14, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tintas_precoform'


class TintasProdutos(models.Model):
    codprod = models.CharField(db_column='CODPROD', max_length=13, blank=True, null=True)  # Field name made lowercase.
    desc_ptb = models.CharField(db_column='DESC_PTB', max_length=40, blank=True, null=True)  # Field name made lowercase.
    ano = models.CharField(db_column='ANO', max_length=9, blank=True, null=True)  # Field name made lowercase.
    coduniv = models.CharField(db_column='CODUNIV', max_length=20, blank=True, null=True)  # Field name made lowercase.
    anuancia = models.CharField(db_column='ANUANCIA', max_length=5, blank=True, null=True)  # Field name made lowercase.
    cor_pai = models.CharField(db_column='COR_PAI', max_length=5, blank=True, null=True)  # Field name made lowercase.
    nacionalidade = models.CharField(db_column='NACIONALIDADE', max_length=1, blank=True, null=True)  # Field name made lowercase.
    cd_mont = models.CharField(db_column='CD_MONT', max_length=3, blank=True, null=True)  # Field name made lowercase.
    obscon = models.CharField(db_column='OBSCON', max_length=5, blank=True, null=True)  # Field name made lowercase.
    obsprod = models.CharField(db_column='OBSPROD', max_length=255, blank=True, null=True)  # Field name made lowercase.
    grupo = models.CharField(db_column='GRUPO', max_length=4, blank=True, null=True)  # Field name made lowercase.
    sgrupo = models.CharField(db_column='SGRUPO', max_length=4, blank=True, null=True)  # Field name made lowercase.
    personalizado = models.IntegerField(db_column='PERSONALIZADO', blank=True, null=True)  # Field name made lowercase.
    desc_ing = models.CharField(db_column='DESC_ING', max_length=40, blank=True, null=True)  # Field name made lowercase.
    desc_esp = models.CharField(db_column='DESC_ESP', max_length=40, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tintas_produtos'


class Transportadores(models.Model):
    codigo = models.AutoField(db_column='Codigo', primary_key=True)  # Field name made lowercase.
    tipo = models.IntegerField(db_column='Tipo', blank=True, null=True)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=60, blank=True, null=True)  # Field name made lowercase.
    endereco = models.CharField(db_column='Endereco', max_length=60, blank=True, null=True)  # Field name made lowercase.
    bairro = models.CharField(db_column='Bairro', max_length=60, blank=True, null=True)  # Field name made lowercase.
    cep = models.CharField(db_column='Cep', max_length=9, blank=True, null=True)  # Field name made lowercase.
    fone = models.CharField(db_column='Fone', max_length=13, blank=True, null=True)  # Field name made lowercase.
    fax = models.CharField(db_column='Fax', max_length=13, blank=True, null=True)  # Field name made lowercase.
    observacao = models.TextField(db_column='Observacao', blank=True, null=True)  # Field name made lowercase.
    cnpj = models.CharField(db_column='CNPJ', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ie = models.CharField(db_column='IE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    cadastro = models.DateField(db_column='Cadastro', blank=True, null=True)  # Field name made lowercase.
    empresa = models.IntegerField(db_column='Empresa', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'transportadores'


class Unidades(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    unidade = models.CharField(db_column='Unidade', max_length=2, blank=True, null=True)  # Field name made lowercase.
    empresa = models.IntegerField(db_column='Empresa', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'unidades'


class Usuarios(models.Model):
    codigo = models.AutoField(db_column='Codigo', primary_key=True)  # Field name made lowercase.
    usuario = models.CharField(db_column='Usuario', max_length=80, blank=True, null=True)  # Field name made lowercase.
    login = models.CharField(db_column='Login', max_length=80, blank=True, null=True)  # Field name made lowercase.
    senha = models.CharField(db_column='Senha', max_length=80, blank=True, null=True)  # Field name made lowercase.
    ativo = models.IntegerField(db_column='Ativo', blank=True, null=True)  # Field name made lowercase.
    checarsenha = models.IntegerField(db_column='ChecarSenha', blank=True, null=True)  # Field name made lowercase.
    mes = models.IntegerField(db_column='Mes', blank=True, null=True)  # Field name made lowercase.
    permissao = models.TextField(db_column='Permissao', blank=True, null=True)  # Field name made lowercase.
    permissaof = models.TextField(db_column='PermissaoF', blank=True, null=True)  # Field name made lowercase.
    empresa = models.IntegerField(db_column='Empresa', blank=True, null=True)  # Field name made lowercase.
    funcionario = models.IntegerField(db_column='Funcionario', blank=True, null=True)  # Field name made lowercase.
    token = models.TextField(db_column='Token', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'usuarios'


class Veiculos(models.Model):
    codigo = models.AutoField(db_column='Codigo', primary_key=True)  # Field name made lowercase.
    veiculo = models.CharField(db_column='Veiculo', max_length=60, blank=True, null=True)  # Field name made lowercase.
    placa = models.CharField(db_column='Placa', max_length=8, blank=True, null=True)  # Field name made lowercase.
    cor = models.CharField(db_column='Cor', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ano = models.CharField(db_column='Ano', max_length=9, blank=True, null=True)  # Field name made lowercase.
    anomodelo = models.IntegerField(db_column='AnoModelo', blank=True, null=True)  # Field name made lowercase.
    cidade = models.CharField(db_column='Cidade', max_length=60, blank=True, null=True)  # Field name made lowercase.
    modelo = models.CharField(db_column='Modelo', max_length=30, blank=True, null=True)  # Field name made lowercase.
    marca = models.IntegerField(db_column='Marca', blank=True, null=True)  # Field name made lowercase.
    montadora = models.CharField(max_length=40, blank=True, null=True)
    combustivel = models.IntegerField(db_column='Combustivel', blank=True, null=True)  # Field name made lowercase.
    combust = models.CharField(max_length=30, blank=True, null=True)
    motor = models.CharField(db_column='Motor', max_length=30, blank=True, null=True)  # Field name made lowercase.
    km = models.IntegerField(db_column='KM', blank=True, null=True)  # Field name made lowercase.
    hora = models.IntegerField(blank=True, null=True)
    chassi = models.CharField(db_column='Chassi', max_length=30, blank=True, null=True)  # Field name made lowercase.
    cliente = models.IntegerField(db_column='Cliente', blank=True, null=True)  # Field name made lowercase.
    cadastro = models.DateField(db_column='Cadastro', blank=True, null=True)  # Field name made lowercase.
    nos = models.IntegerField(db_column='NOS', blank=True, null=True)  # Field name made lowercase.
    cidcli = models.CharField(max_length=60, blank=True, null=True)
    empresa = models.IntegerField(db_column='Empresa', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'veiculos'


class Veiculoscliente(models.Model):
    codigo = models.AutoField(db_column='Codigo', primary_key=True)  # Field name made lowercase.
    cliente = models.IntegerField(db_column='Cliente', blank=True, null=True)  # Field name made lowercase.
    veiculo = models.CharField(db_column='Veiculo', max_length=60, blank=True, null=True)  # Field name made lowercase.
    placa = models.CharField(db_column='Placa', max_length=8, blank=True, null=True)  # Field name made lowercase.
    cor = models.CharField(db_column='Cor', max_length=60, blank=True, null=True)  # Field name made lowercase.
    ano = models.IntegerField(db_column='Ano', blank=True, null=True)  # Field name made lowercase.
    anomodelo = models.IntegerField(db_column='AnoModelo', blank=True, null=True)  # Field name made lowercase.
    cidade = models.CharField(db_column='Cidade', max_length=60, blank=True, null=True)  # Field name made lowercase.
    modelo = models.CharField(db_column='Modelo', max_length=60, blank=True, null=True)  # Field name made lowercase.
    marca = models.IntegerField(db_column='Marca', blank=True, null=True)  # Field name made lowercase.
    combustivel = models.IntegerField(db_column='Combustivel', blank=True, null=True)  # Field name made lowercase.
    motor = models.CharField(db_column='Motor', max_length=30, blank=True, null=True)  # Field name made lowercase.
    chassi = models.CharField(db_column='Chassi', max_length=30, blank=True, null=True)  # Field name made lowercase.
    empresa = models.IntegerField(db_column='Empresa', blank=True, null=True)  # Field name made lowercase.
    cadastro = models.DateField(db_column='Cadastro', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'veiculoscliente'


class Vendas(models.Model):
    codigo = models.AutoField(primary_key=True)
    cliente = models.IntegerField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    vendedor = models.IntegerField(blank=True, null=True)
    data = models.DateField(blank=True, null=True)
    hora = models.TimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vendas'
