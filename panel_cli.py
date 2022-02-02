import argparse
from src.dolar_value import DolarValue

class CommandLineInterface:
  # Versão do CLI
  CLI_VERSION = "panelCLI 1.0.0"

  # Criar o CLI
  parser = argparse.ArgumentParser(
    prog="panelCLI",
    description="Automação de ferramentas",
    epilog="Desenvolvido por: @isaelsantos0",
    usage="%(prog)s [options]" 
  )
  parser.version = CLI_VERSION 

  parser.add_argument("-v", "--version", action="version", version=CLI_VERSION)
  parser.add_argument("-t", "--teste", action="store_true", help="executa o teste de conexão")
  parser.add_argument("-pd", "--pricedolar", action="store_true", help="Cotação do dolar")

  # CLI Widget
  doll = DolarValue()

  arg_parser = parser.parse_args()
  if arg_parser:
    if arg_parser.teste:
      print("teste")
    if arg_parser.pricedolar:
      print(doll.coin)
      print(f'>>> {doll.date}')
      print(f'>>> Current Value: R$ {doll.bid}')
      print(f'>>> Max: R$ {doll.maxvalue} / Min: R$ {doll.minvalue}')