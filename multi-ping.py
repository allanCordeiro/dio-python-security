import os
import argparse
import time
from utils import PingLibrary


def multi_ping(hosts_file):
    hosts = _get_hosts(hosts_file)
    if isinstance(hosts, list):
        cmd = _ping_cmd()
        if cmd != "":
            cmd = cmd.replace("{package_qty}", "4").replace("{host}", "")
            for host in hosts:
                print(f"*** Início Ping para {host} ***")
                os.system(f"{cmd} {host}")
                print(f"*** Fim Ping para {host} ***")
                time.sleep(2)
        else:
            print("Erro: seu sistema operacional não tem o comando ping atribuido nas configuracoes. "
                  "Reveja o arquivo json e tente novamente.")
    else:
        print("Erro: arquivo de hosts para ping nao encontrado.")


def _get_hosts(file_name:str):
    try:
        with open(file_name, "r") as file:
            item = []
            for line in file.read().splitlines():
                item.append(line)
            return item
    except Exception as error:
        return error


def _ping_cmd():
    command = PingLibrary()
    return command.get_ping_command()


if __name__ == "__main__":
    print("=" * 100)
    parser = argparse.ArgumentParser("description='Parameters'")
    parser.add_argument('--filename',
                        '-f',
                        required=False,
                        help="Nome do arquivo hosts. Caso omitido, sera utilizado root/files/hosts.txt")
    args = parser.parse_args()
    host_file = "files/hosts.txt"
    if args.filename is not None:
        host_file = args.filename

    multi_ping(host_file)
    print("=" * 100)


