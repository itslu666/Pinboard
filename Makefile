PYTHON = python3
PYINSTALLER = pyinstaller
SRC_DIR = src
DIST_DIR = dist
CONFIG_DIR = .config/pinboard

EXECUTABLE_NAME = pinboard

all: create_config_dir build_executable

create_config_dir:
	@mkdir -p $(CONFIG_DIR)
	@echo ".config/pinboard created"

build_executable:
	$(PYINSTALLER) --onefile $(SRC_DIR)/main.py --distpath $(DIST_DIR) --name $(EXECUTABLE_NAME)
	@echo "Building done."

clean:
	rm -rf $(DIST_DIR)
	rm -rf build
	rm -rf $(EXECUTABLE_NAME).spec
	@echo "Cleaned up."

uninstall:
	rm -rf $(CONFIG_DIR)
	@echo ".config dir removed"

.PHONY: all create_config_dir build_executable clean uninstall