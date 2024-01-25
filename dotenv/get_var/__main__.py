from dotenv import load_dotenv
import os
from typing import Any

def get_var(key: {"widget_name": "string_entry"} = "") -> [{"name": "value", "type": str}]:
	load_dotenv()
	return os.getenv(key)

main_callable = get_var
