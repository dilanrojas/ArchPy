# Imports
import os
import sys
import time
from keybindings import keybindings

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

# Cargando
def loading():
    clean()
    spacer()
    print(" Cargando.")
    wait()
    clean()
    spacer()
    print(" Cargando..")
    wait()
    clean()
    spacer()
    print(" Cargando...")
    wait()
    clean()
    spacer()
    print(" Cargando.")
    wait()
    clean()
    spacer()
    print(" Cargando..")
    wait()
    clean()
    spacer()
    print(" Cargando...")
    wait()
    clean()

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

# Omitiendo...
def skip():
    clean()
    spacer()
    print(" Omitiendo.")
    wait()
    clean()
    spacer()
    print(" Omitiendo..")
    wait()
    clean()
    spacer()
    print(" Omitiendo...")
    wait()
    clean()

# Bienvenida
def welcome():
    clean()
    spacer()
    print(" Bienvenido a mi script de instalación.")
    print(" Con este script podrás configurar el sistema a tu gusto y utilizar mis configuraciones.")
    spacer()
    print(" ¿Quieres continuar?")
    print(" 1. Sí")
    print(" 2. No")
    spacer()
    run_or_not = int(input(" --> "))
    if run_or_not == 1:
        loading()
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
    print("Puedes consultar esta lista cuando desees ejecutando el archivo 'keybindings.py'")

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
    os.system(" git clone https://github.com/dilanrojas/dotfiles.git && cp -r dotfiles/.config ~/ && cp -r dotfiles/.local ~/")
    clean()

# Bienvenida
welcome()

# Lista de paquetes
lista_paquetes_1 = " xorg xorg-server lightdm lightdm-gtk-greeter qtile alacritty fish starship pcmanfm rofi nitrogen scrot redshift file-roller gvfs glib2 gvfs-mtp udiskie network-manager-applet cbatticon pulseaudio pavucontrol pamixer alsa-utils brightnessctl gedit eog arandr xdg-user-dirs ntfs-3g lxappearance vlc dunst nano neovim lsd bat lxsession xscreensaver volumeicon gnome-themes-extra gtk-engine-murrine python-colorama"
spacer()
print(" ¿Instalar los siguientes paquetes?")
spacer()
print(lista_paquetes_1)
spacer()
print(" 1. Sí")
print(" 2. No")
spacer()

# Respuesta de paquetes #1
r1 = int(input(" --> "))

if r1 == 1:
    os.system("sudo pacman -S --noconfirm " + lista_paquetes_1)
    # Generar carpetas de usuario
    os.system("xdg-user-dirs-update")
    # Habilita el servicio LightDM
    os.system("sudo systemctl enable lightdm")
    done()
elif r1 == 2:
    exiting()
    
# Instalación de AUR Helper
spacer()
print(" ¿Cuál 'AUR Helper' prefieres?")
spacer()
print(" 1. Yay")
print(" 2. Paru")
spacer()

# AUR Helper
aur_helper = int(input(" --> "))

if aur_helper == 1:
    spacer()
    os.system("git clone https://aur.archlinux.org/yay-git.git && mv yay-git/PKGBUILD . && makepkg -si --noconfirm")
    done()

elif aur_helper == 2:
    spacer()
    os.system("git clone https://aur.archlinux.org/paru-git.git && mv paru-git/PKGBUILD . && makepkg -si --noconfirm")
    done()

# Instala fork de Picom (Compositor de ventanas)
spacer()
print(" ¿Quiéres instalar el compositor de ventanas Picom-Jonaburg?")
spacer()
print(" 1. Sí")
print(" 2. No")
spacer()

# Respuesta de paquetes #2
r2 = int(input(" --> "))

if r2 == 1:
    spacer()
    if aur_helper == 1:
        os.system("yay -S picom-jonaburg-git --noconfirm")
        done()
    elif aur_helper == 2:
        os.system("paru -S picom-jonaburg-git --noconfirm")
        done()
elif r2 == 2:
    skip()

# Instalación de las fuentes necesarias

# Lista de fuentes
lista_fuentes = " nerd-fonts-jetbrains-mono nerd-fonts-ubuntu-mono"

print(" Las siguientes fuentes son necearias:")
print("" + lista_fuentes)
spacer()
print(" 1. Instalar")
print(" 2. No instalar (No recomendado)")
spacer()

# Respuesta de paquetes #3
r3 = int(input(" --> "))

if r3 == 1:
    spacer()
    if aur_helper == 1:
        os.system("yay -S nerd-fonts-jetbrains-mono nerd-fonts-ubuntu-mono --noconfirm")
    elif aur_helper == 2:
        os.system("paru -S nerd-fonts-jetbrains-mono nerd-fonts-ubuntu-mono --noconfirm")
    done()
elif r3 == 2:
    skip()

# Clonar mi repositorio
clone()

# Cambiar la shell
spacer()
print(" ¿Quieres utilizar Fish como Shell?")
spacer()
print(" 1. Sí")
print(" 2. No")
spacer()

# Repuesta de paquetes #4
r4 = int(input(" --> "))

if r4 == 1:
    spacer()
    os.system("sudo usermod --shell /usr/bin/fish $USER")
    os.system("sudo usermod --shell /usr/bin/fish root")
    done()
if r4 == 2:
    skip()

# Instala tema de LightDM
spacer()
print(" ¿Quieres instalar un tema personalizado de LightDM?")
spacer()
print(" 1. Sí")
print(" 2. No")
spacer()

# Respuseta de paquetes #5
r5 = int(input(" --> "))

if r5 == 1:
    spacer()
    os.system("sudo pacman -S lightdm-webkit2-greeter --noconfirm")
    if aur_helper == 1:
        os.system("yay -S lightdm-webkit-theme-aether --noconfirm")
    elif aur_helper == 2:
        os.system("paru -S lightdm-webkit-theme-aether --noconfirm")
    done()
elif r5 == 2:
    skip()

# Instala tema de NeoVim
spacer()
print(" ¿Quieres instalar un tema personalizado de NeoVim?")
spacer()
print(" 1. Sí")
print(" 2. No")
spacer()

# Respuesta de paquetes #6
r6 = int(input(" --> "))

if r6 == 1:
    spacer()
    os.system("git clone https://github.com/NvChad/NvChad ~/.config/nvim --depth 1 && nvim +'hi NormalFloat guibg=#1e222a' +PackerSync")
    done()
elif r6 == 2:
    skip()

# Despedida
byebye()
