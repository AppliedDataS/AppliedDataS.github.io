
export PATH="/opt/homebrew/bin:$PATH"
# source  /Users/sophie/conda/bin/activate
source .venv/bin/activate
python -m pip install -U pip

pip install tensorflow-macos
pip install tensorflow-metal
pip3 install numpy  
pip3 install pandas  
pip3 install matplotlib  
pip3 install scikit-learn  
pip3 install scipy  
pip3 install plotly  
pip3 install networkx  
pip3 install keras
pip install torchvision torch
pip install graphviz
pip install networkx
pip install matplotlib
pip install numpy
brew install lualatex
# python -m pip install opencv-python
# export GRAPHVIZ_DIR="/opt/homebrew/Cellar/graphviz/8.0.1"
# pip install pygraphviz --global-option=build_ext --global-option="-I$GRAPHVIZ_DIR/include" --global-option="-L$GRAPHVIZ_DIR/lib"