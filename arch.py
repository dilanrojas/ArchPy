# Imports
import os
import sys
import time
from keybindings import keybindings
from paquetes import lista_paquetes

# Limpiar la pantalla
def clean():
    os.system("clear")
clean()

# time.sleep
def wait():
    time.sleep(0.5)

# Espaciador
def spacer():
    print("")

# ¡Completado!
def done():
    clean()
    spacer()
    print(" ¡Completado!")
    wait()
    clean()

# Saliendo...
def exiting():
    clean()
    spacer()
    print(" Saliendo.")
    wait()
    clean()
    spacer()
    print(" Saliendo..")
    wait()
    clean()
    spacer()
    print(" Saliendo...")
    wait()
    clean()
    sys.exit()

# Bienvenida
def welcome():
    clean()
    spacer()
    print(" Bienvenido a mi script de instalación.")
    print(" Con este script podrás utilizar mis configuraciones del sistema.")
    spacer()
    print(" ¿Quieres continuar?")
    print(" 1. Sí")
    print(" 2. No")
    spacer()
    run_or_not = int(input(" --> "))
    if run_or_not == 1:
        done()
    else:
        exiting()

# Despedida
def byebye():
    clean()
    spacer()
    print(" ¡Reinicia el equipo para completar la configuración!")
    wait()
    print(" Aquí te dejo una lista con los atajos de teclado")
    spacer()
    keybindings()
    spacer()
    print(" Puedes consultar esta lista cuando desees ejecutando el archivo 'keybindings.py'")

# Clonando repositorio...
def clone():
    clean()
    spacer()
    print(" Clonando repositorio.")
    wait()
    clean()
    spacer()
    print(" Clonando repositorio..")
    wait()
    clean()
    spacer()
    print(" Clonando repositorio...")
    wait()
    clean()
    os.system(" git clone https://github.com/dilanrojas/dotfiles.git && cp -r dotfiles/.config ~/ && cp -r dotfiles/.local ~/ && chmod +x ~/.config/qtile/autostart.sh")
    clean()

# Bienvenida
welcome()
print(" Instalando paquetes.")
clean()
print(" Instalando paquetes..")
clean()
print(" Instalando paquetes...")
wait()
os.system("sudo pacman -S --noconfirm " + lista_paquetes)
os.system("xdg-user-dirs-update")
os.system("sudo systemctl enable lightdm")
clean()

# Instalación de AUR Helper
os.system("git clone https://aur.archlinux.org/yay-git.git && mv yay-git/PKGBUILD . && makepkg -si --noconfirm")
clean()

# Instala fork de Picom (Compositor de ventanas)
os.system("yay -S picom-jonaburg-git --noconfirm")

# Instalación de las fuentes necesarias
os.system("yay -S nerd-fonts-jetbrains-mono nerd-fonts-ubuntu-mono --noconfirm")

# Clonar mi repositorio
clone()

# Cambiar la shell
os.system("sudo usermod --shell /usr/bin/fish $USER")
os.system("sudo usermod --shell /usr/bin/fish root")

# Tema personalizado de LightDM
os.system("sudo pacman -S lightdm-webkit2-greeter --noconfirm")
os.system("yay -S lightdm-webkit-theme-aether --noconfirm")

# Tema personalizado de NeoVim (NvChad)
os.system("git clone https://github.com/NvChad/NvChad ~/.config/nvim --depth 1 && nvim +'hi NormalFloat guibg=#1e222a' +PackerSync")
clean()

# Despedida
byebye()
