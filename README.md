# AI Code Generator CLI

A powerful command-line tool that generates code snippets and answers coding-related questions using the Google Gemini API.

## Features

- Generate code in various programming languages based on user prompts.
- Ask coding-related questions and receive AI-generated responses.
- Interactive mode for a chat-like experience.
- Set and manage API keys and default AI models.

## Installation

### Prerequisites

Ensure you have the following installed:
- Python 3.7+
- `pip` (Python package manager)

### Setup

1. Clone the repository:
   ```sh
   git clone https://github.com/iamcosmo/AI-CodeGen-CLi.git
   cd ai-codegen-cli
   ```

2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

3. Set your Google Gemini API key:
   ```sh
   python codegen.py set-key YOUR_GEMINI_API_KEY
   ```
   <!-- Optionally, specify a default model:
   ```sh
   python codegen.py set-key YOUR_GEMINI_API_KEY --model gemini-2.0-pro
   ``` -->

## Usage

Run the CLI tool using:
```sh
codegen start
```

### Available Commands

| Command | Description |
|---------|-------------|
| `set-key` | Set the API key and (optionally) the default AI model. |
<!-- | `set-model` | Update the default AI model. | -->
| `generate` | Generate code from a user prompt. |
| `ask` | Ask a coding-related question. |
| `interactive` | Run the CLI in interactive mode. |
| `start` | Start the CLI menu. |

### Examples

**Start the CLI:**
```sh
codegen start

Welcome to AI Code Generator CLI
Choose an option:
1. Generate Code
2. Ask a Question
3. Interactive Mode
4. Exit
Enter your choice (1-4):
```

**Generate Code:**
```sh
python codegen.py generate "A Python script that reverses a string" --language python
```

**Ask a Question:**
```sh
python codegen.py ask "What is the difference between list and tuple in Python?"
```

**Interactive Mode:**
```sh
python codegen.py interactive
```

## Configuration

The tool stores API keys and model preferences in a `.env` file.
- You can manually edit `.env` to update configurations.
- To reset settings, delete `.env` and rerun `set-key`.

## Contributing

1. Fork the repository.
2. Create a new branch (`feature-branch`).
3. Commit your changes.
4. Push to your branch and create a pull request.

## License

This project is licensed under the MIT License. See `LICENSE` for details.

## Author

Developed by [Your Name](https://github.com/iamcosmo).

---
🚀 **Now you’re all set! Start generating code effortlessly!**

