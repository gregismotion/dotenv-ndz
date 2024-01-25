from dotenv import load_dotenv
import os
from typing import Any

def get_var(key: {"widget_name": "string_entry", "type": str} = "", override: {"widget_name": "check_button", "type": bool} = True) -> [{"name": "value", "type": str}]:
	# NOTE: is this correct? with empty values it doesn't work in Nodezator, wonder where it would be searching...
	load_dotenv(os.path.join(os.getenv('PWD'), ".env"), override=override) 
	return os.getenv(key)

main_callable = get_var
