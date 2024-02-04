TEST_DIR := test

.PHONY: all init env test build
all: test

init:
	@pipenv install --ignore-pipefile

env:
	@pipenv shell

test:
	@if [ ! -d $(TEST_DIR) ]; then \
        mkdir -p $(TEST_DIR); \
        echo "Directory $(TEST_DIR) created."; \
    fi
	@python3 2600_bitma.py -i data/test_img.png -t 200 -o test/output_file.txt -s test/converted_img.png -v

build:
	@pyinstaller --onefile 2600_bitma.py