# Quickstart: Setup with uv

This project uses [uv](https://github.com/astral-sh/uv) for Python dependency management.

## Steps to get started

1. **Install uv** (if not already installed):
	```sh
	curl -Ls https://astral.sh/uv/install.sh | sh
	```

2. **Clone repo and Sync dependencies:**
	```sh
    git clone https://github.com/sudarshan-koirala/strands-agents-tutorial.git
    cd strands-agents-tutorial
	uv sync
	```

3. **Run your scripts:**
	```sh
	uv run python3 multi-agent-example/teachers_assistant.py
	```

