import google.generativeai as genai
import argparse
import sys
import os
from dotenv import load_dotenv, set_key
from rich.console import Console
from rich.syntax import Syntax

# Load environment variables
load_dotenv()
console = Console()

# Check for API key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

def set_api_key(api_key):
    """Saves the API key to .env file"""
    with open(".env", "a") as env_file:
        env_file.write(f"\nGEMINI_API_KEY={api_key}\n")
    set_key(".env", "GEMINI_API_KEY", api_key)
    console.print("[green]API Key has been set successfully![/green]")

def configure_api():
    """Checks API key and configures Gemini"""
    global GEMINI_API_KEY
    if not GEMINI_API_KEY:
        console.print("[yellow]API Key not found! Please set it using: codegen set-key YOUR_API_KEY[/yellow]")
        sys.exit(1)
    genai.configure(api_key=GEMINI_API_KEY)

def generate_code(prompt, language="python", model="gemini-2.0-pro"):
    """Generates code using Google Gemini API"""
    configure_api()
    try:
        model = genai.GenerativeModel(model)
        response = model.generate_content(f"Generate {language} code for: {prompt}")
        return response.text
    except Exception as e:
        console.print(f"[red]Error generating code: {e}[/red]")
        sys.exit(1)

def ask_question(question, model="gemini-2.0-pro"):
    """Asks a coding-related question to the AI."""
    configure_api()
    try:
        model = genai.GenerativeModel(model)
        response = model.generate_content(f"Answer this programming question: {question}")
        return response.text
    except Exception as e:
        console.print(f"[red]Error getting response: {e}[/red]")
        sys.exit(1)

def interactive_mode():
    """Runs the CLI tool in interactive mode."""
    configure_api()
    console.print("[cyan]AI Code Generator CLI - Interactive Mode (type 'exit' to quit)[/cyan]")
    while True:
        user_input = input("\nEnter your prompt: ")
        if user_input.lower() == "exit":
            console.print("[green]Exiting...[/green]")
            break
        language = input("Enter language (default: Python): ") or "python"
        code = generate_code(user_input, language)
        console.print(Syntax(code, language, theme="monokai", line_numbers=True))

def start_cli():
    """Starts the CLI interface."""
    while True:
        console.print("\n[bold cyan]Welcome to AI Code Generator CLI[/bold cyan]")
        console.print("[green]Choose an option:[/green]")
        console.print("1. Generate Code")
        console.print("2. Ask a Question")
        console.print("3. Interactive Mode")
        console.print("4. Exit")
        
        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            prompt = input("Enter your prompt for code generation: ")
            language = input("Enter the programming language (default: Python): ") or "python"
            code = generate_code(prompt, language)
            console.print(Syntax(code, language, theme="monokai", line_numbers=True))

        elif choice == "2":
            question = input("Enter your question: ")
            response = ask_question(question)
            console.print("\n[bold]AI Response:[/bold]\n")
            console.print(response)

        elif choice == "3":
            interactive_mode()

        elif choice == "4":
            console.print("[green]Exiting...[/green]")
            sys.exit(0)

        else:
            console.print("[red]Invalid choice! Please enter a number between 1-4.[/red]")

def main():
    parser = argparse.ArgumentParser(description="AI-powered CLI Code Generator (Gemini API)")
    subparsers = parser.add_subparsers(dest="command")

    # Command: set-key
    key_parser = subparsers.add_parser("set-key", help="Set your Gemini API key")
    key_parser.add_argument("api_key", type=str, help="Your Gemini API Key")

    # Command: start CLI
    subparsers.add_parser("start", help="Start the CLI menu")

    # Command: generate
    gen_parser = subparsers.add_parser("generate", help="Generate code from a prompt")
    gen_parser.add_argument("prompt", type=str, help="Describe the code you need")
    gen_parser.add_argument("-l", "--language", type=str, default="python", help="Programming language (default: Python)")

    # Command: ask
    ask_parser = subparsers.add_parser("ask", help="Ask a coding-related question")
    ask_parser.add_argument("question", type=str, help="Ask a programming-related question")

    # Command: interactive mode
    subparsers.add_parser("interactive", help="Run the CLI in interactive mode")

    args = parser.parse_args()

    if args.command == "set-key":
        set_api_key(args.api_key)
    elif args.command == "start":
        start_cli()
    elif args.command == "generate":
        code = generate_code(args.prompt, args.language)
        console.print("\n[bold]Generated Code:[/bold]\n")
        console.print(Syntax(code, args.language, theme="monokai", line_numbers=True))
    elif args.command == "ask":
        response = ask_question(args.question)
        console.print("\n[bold]AI Response:[/bold]\n")
        console.print(response)
    elif args.command == "interactive":
        interactive_mode()
    else:
        parser.print_help()
        sys.exit(1)

if __name__ == "__main__":
    main()
