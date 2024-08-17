from pathlib import Path
import sys

current_file = Path(__file__)
sys.path.insert(0, str(current_file.parent))

# 加载插件
pytest_plugins = ['myplugin']
