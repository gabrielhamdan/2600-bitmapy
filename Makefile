TEST_DIR := test
DATA_DIR := data
IMG_FILE := bitmapy_splash.png
THRSHLD := 100
OUTPUT_FILE_PATH := hex_logo.txt
CONVERTED_IMG_PATH := converted_logo.png

.PHONY: all init env test build
all: test

init:
	@pipenv install --ignore-pipefile

env:
	@pipenv shell

test:
	@if [ ! -d $(TEST_DIR) ]; then \
        mkdir -p $(TEST_DIR); \
        echo "> Directory $(TEST_DIR) created."; \
    fi
	@python3 2600_bitma.py -i $(DATA_DIR)/$(IMG_FILE) -t $(THRSHLD) -I -o $(TEST_DIR)/$(OUTPUT_FILE_PATH) -s $(TEST_DIR)/$(CONVERTED_IMG_PATH) -b -v

build:
	@pyinstaller --onefile 2600_bitma.py