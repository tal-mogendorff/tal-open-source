from typing_extensions import Annotated

import typer

from kubiya_sdk.tools import function_tool


@function_tool(
    description="Prints pandas {name}!",
    requirements=["pandas==2.2.3"],
)
def test_123(
    name: str,
    boolean_val: bool,  # This will validate that the input is a boolean
    optional_str: Annotated[
        str, typer.Argument()
    ] = "sheeesh",  # This is how to add a default value
):
    import pandas as pd

    print(f"Hello {name}! {boolean_val} {optional_str}")
    df = pd.DataFrame(
        {"name": [name], "boolean_val": [boolean_val], "test": [optional_str]}
    )

    print(df)
    
    
@function_tool(
    description="Print JSONPlace holder Users",
    requirements=['requests==2.32.3'],
)
def get_users(
     start_of_name: Annotated[
        str, typer.Argument()
    ] = None,
):
    import requests

    response = requests.get("https://jsonplaceholder.typicode.com/users")
    users = response.json()

    for user in users:
        if start_of_name and not user["name"].startswith(start_of_name):
            continue
        print(user["name"])
        print(user["email"])
        print(user["address"]["city"])
        print()
