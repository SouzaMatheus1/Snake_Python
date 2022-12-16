BIBLIOTECA_RANDOM=$(pip freeze | grep random)
BIBLIOTECA_PYGAME=$(pip freeze | grep pygame)
APT_PIP=$(sudo apt list | grep python3-pip)

clear
if ['' = '$APT_PIP']; then
    sudo apt install python3-pip

    echo "\n--------------------------------"
    echo "pip successfully installed! "
else 
    echo "pip already installed!"
fi

if ['' = '$BIBLIOTECA_RANDOM']; then
    pip install random

    echo "\n--------------------------------"
    echo "Random library successfully installed! "
else 
    echo "Random library already installed!"
fi

if ['' = '$BIBLIOTECA_PYGAME']; then
    pip install pygame

    echo "\n--------------------------------"
    echo "Pygame library successfully installed! "
else 
    echo "Pygame library already installed!"
fi

pip install pyinstaller

 echo "\n--------------------------------"
 echo "Starting game..."

python3 snake.py