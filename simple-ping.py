import os
from utils import PingLibrary


def simple_ping():
    print("=" * 100)
    host = input("IP/Host: ")
    package_qty = input("Quantidade de pacotes(0/nada padrão 4 pacotes):  ")
    if package_qty == "" or package_qty == "0":
        package_qty = "4"
    cmd = _ping_cmd()
    if cmd != "":
        cmd = cmd.replace("{package_qty}", package_qty).replace("{host}", host)
        os.system(cmd)
    else:
        print("Erro: seu sistema operacional não tem o comando ping atribuido nas configuracoes. "
              "Reveja o arquivo json e tente novamente.")

    print("=" * 100)


def _ping_cmd():
    command = PingLibrary()
    return command.get_ping_command()


if __name__ == "__main__":
    simple_ping()