from dotenv import load_dotenv
import os
from typing import Any

def get_var(key: {"widget_name": "string_entry"} = "") -> [{"name": "value", "type": str}]:
	load_dotenv(os.getenv("PWD")) # NOTE: is this correct? with emptry values it doesn't work in Nodezator, wonder where it would be searching...
	return os.getenv(key)

main_callable = get_var
