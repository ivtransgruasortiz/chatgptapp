import os
import utils.constants as cons
import utils.functions
import openai
import typer
from rich import print
from rich.table import Table


def chatgptiv():
    api_key = os.getenv("api_key")
    openai.api_key = api_key

    print("[bold green]ChatGPT API en Python[/bold green]")

    table = Table("Comando", "Descripción")
    table.add_row("exit", "Salir de la aplicación")
    table.add_row("new", "Crear una nueva conversación")

    while True:
        prompt = input("\nIntroduce una pregunta a chatGPT: ")
        if prompt == "exit":
            break
        completion = openai.Completion.create(model="text-davinci-003",
                                              prompt=prompt,
                                              max_tokens=2048)
        print(completion.choices[0].text)


def chatgptiv2():
    api_key = os.getenv("api_key")
    openai.api_key = api_key

    print("[bold green]ChatGPT API en Python[/bold green]")

    table = Table("Comando", "Descripción")
    table.add_row("exit", "Salir de la aplicación")
    table.add_row("new", "Crear una nueva conversación")

    messages = [{"role": "system",
                "content": "Eres un asistente muy útil."}]
    while True:
        content = input("Sobre qué quieres hablar?")
        if content == "exit":
            break

        messages.append({"role": "user",
                         "content": content})

        response = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                                messages=messages)

        response_content = response.choices[0].message.content

        messages.append({"role": "assistant",
                         "content": response_content})
        print(response_content)


if __name__ == "__main__":
    # chatgptiv()
    chatgptiv2()
