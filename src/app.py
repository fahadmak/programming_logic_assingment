# ---- app.py ----
# This file contains the entry point to your tasks
# and the logic to manage it

from src.helper import select
from src.accounts import login_prompt

if __name__ == "__main__":
    login_prompt()
    select()


