PYTHON = python3
PYTHON_VENV = venv
PYINSTALLER = $(PYTHON_VENV)/bin/pyinstaller
SRC_DIR = .
DIST_DIR = dist
CONFIG_DIR = $${HOME}/.config/pinboard
REQUIREMENTS_FILE = requirements.txt

EXECUTABLE_NAME = pinboard

all: create_venv install_dependencies create_config_dir build_executable

create_venv:
	$(PYTHON) -m venv $(PYTHON_VENV)
	@echo "Venv created"

install_dependencies:
	$(PYTHON_VENV)/bin/pip install -r $(REQUIREMENTS_FILE)
	@echo "Dependencies installed."

create_config_dir:
	mkdir -p $(CONFIG_DIR)
	@echo ".config/pinboard created"

build_executable:
	$(PYINSTALLER) --onefile --hidden-import=PIL._tkinter_finder $(SRC_DIR)/main.py --distpath $(DIST_DIR) --name $(EXECUTABLE_NAME)
	@echo "Building done."

clean:
	rm -rf $(DIST_DIR)
	rm -rf build
	rm -rf $(EXECUTABLE_NAME).spec
	rm -rf $(PYTHON_VENV)
	@echo "Cleaned up."

uninstall: clean
	rm -rf $(CONFIG_DIR)
	@echo "Uninstalled"

.PHONY: create_venv install_dependencies create_config_dir build_executable clean uninstall