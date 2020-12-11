#!/usr/bin/python3

from subprocess import run, check_output
from time import sleep
from os import listdir
import pathlib

# ==================== DEFINES ==================== #

# Limpa a tela
def clear():
    run(['clear'])


# Mensagem de saudação
def greet_update():
    clear()
    txt = " Atualizando Repositórios "
    f_txt = txt.center(80, '=')
    print('\n' + f_txt + '\n')


# Mensagem em erro de subprocess
def sp_error():
    clear()
    txt = " Subprocess Error "
    f_txt = txt.center(80, '=')
    print('\n' + f_txt + '\n')


# Mensagem de erro de timeout
def to_error():
    clear()
    txt = " Timeout Expired "
    f_txt = txt.center(80, '=')
    print('\n' + f_txt + '\n')


# Mensagem de erro de timeout
def brother_msg():
    clear()
    txt = " Instalando Impressora Brother "
    f_txt = txt.center(85, '=')
    print('\n' + f_txt + '\n')


# Atualiza repositórios e Programas
def update_all():
    clear()
    greet_update()
    
    try:
        run(['sudo', 'apt-get', 'update', '-y'])
        run(['sudo', 'apt-get', 'upgrade', '-y'])
        run(['sudo', 'apt-get', 'full-upgrade', '-y'])
    
    except SubprocessError:
        sp_error()
    
    except TimeoutExpired:
        to_error()
    
    finally:
        clear()


# Checa se o diretório é o correto
def check_dir():
    actual_path = str(pathlib.Path(__file__).parent.absolute())
    if actual_path.endswith('Downloads'):
        return 0
    
    else:
        return 1


# Instala impressoras Brother e HP
def install_printers(model):
    if model == 1:
        brother_msg()
        run(['wget', '--quiet', 'https://download.brother.com/welcome/dlf006893/linux-brprinter-installer-2.2.2-1.gz'])
        run(['gunzip', 'linux-brprinter-installer-2.2.2-1.gz'])
        run(['sudo', 'bash', 'linux-brprinter-installer-2.2.2-1', 'DCP-L2540DW'])
    
    elif model == 2:
        
        while True:
            print(str(" Selecione a Sessão: ").center(80, '='))
            sessao = int(input("\n1 - Atendimento\n2 - Análise\n3 - Cancelar\n"))
            
            if sessao == 1:
                run(['sudo', 'apt-get', 'install', '--assume-yes', 'libcups2', 'cups', 'libcups2-dev', 'cups-bsd', 'cups-client', 'libcupsimage2-dev', 'libdbus-1-dev', 'build-essential', 'ghostscript', 'openssl', 'libjpeg62-dev', 'libsnmp-dev', 'libtool', 'libusb-1.0-0-dev', 'wget', 'python-imaging', 'policykit-1', 'policykit-1-gnome', 'python-qt4', 'python-qt4-dbus', 'python-dbus', 'python-gobject', 'python-dev', 'python-notify', 'python', 'python-reportlab', 'libsane', 'libsane-dev', 'sane-utils', 'xsane'])
                run(['sudo', 'hp-setup', '10.194.62.245'])
                break
            
            elif sessao == 2:
                run(['sudo', 'apt-get', 'install', '--assume-yes', 'libcups2', 'cups', 'libcups2-dev', 'cups-bsd', 'cups-client', 'libcupsimage2-dev', 'libdbus-1-dev', 'build-essential', 'ghostscript', 'openssl', 'libjpeg62-dev', 'libsnmp-dev', 'libtool', 'libusb-1.0-0-dev', 'wget', 'python-imaging', 'policykit-1', 'policykit-1-gnome', 'python-qt4', 'python-qt4-dbus', 'python-dbus', 'python-gobject', 'python-dev', 'python-notify', 'python', 'python-reportlab', 'libsane', 'libsane-dev', 'sane-utils', 'xsane'])
                run(['sudo', 'hp-setup', '10.194.62.244'])
                break
            
            elif sessao == 3:
                break
            
            else:
                True


# Limpa os arquivos baixados
def clear_dir():
    files = listdir()
    
    for file in files:
        if file.startswith('wget'):
            run(['rm', '-f', file])
            run(['rm', '-rf', file])

        elif file.startswith('linux'):
            run(['rm', '-f', file])
            run(['rm', '-rf', file])
        
        elif file.startswith('hplip'):
            run(['rm', '-f', file])
            run(['rmdir', '-rf', file])

        elif file.startswith('brscan'):
	        run(['rm', '-f', file])
	        run(['rm', '-rf', file])

        elif file.startswith('uninstaller'):
            run(['rm', '-f', file])
            run(['rm', '-rf', file])

        elif file.startswith('dcpl'):
            run(['rm', '-f', file])
            run(['rm', '-rf', file])


# Desabilita o cups-browsed
def stop_cups():
    print(str(" Desabilitando Impressoras da rede ").center(80, '='))
    run(['sudo', 'service', 'cups-browsed', 'stop'])
    run(['sudo', 'systemctl', 'disable', 'cups-browsed'])
    clear()


# ================== END DEFINES ================== #

if __name__ == '__main__':
    dir = check_dir()
    
    if dir == 0:
        update_all()
        stop_cups()
        
        while True:
            print(str(" Você deseja instalar uma impressora? (S* / N) ").center(80, '='))
            resp = input().upper()
            
            if resp == 'S' or resp == '':
                print(str(" Selecione o Modelo: ").center(80, '='))
                model = int(input("\n1 - Brother\n2 - HP\n"))
                install_printers(model)
                clear_dir()
                clear()
                break
            
            else:
                break
    else:
        clear()
        print(str(" Change directory to Downloads! ").center(80, '='))
