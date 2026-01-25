# Simple Cart (backend + Streamlit frontend)

This workspace contains a small Python cart system (`cart_system.py`) and a simple Streamlit frontend (`cart_app.py`).

Features

- Programmatic helpers in `cart_system.py`: `add_item`, `update_item`, `remove_item`, `view_cart` (also CLI compatible)
- A quick interactive UI using Streamlit in `cart_app.py` (English UI)

Run the Streamlit app

```bash
# From the project directory
streamlit run cart_app.py
```

Run the CLI

```bash
python cart_system.py
```

Run tests (requires pytest)

```bash
python -m pytest -q
```

Notes

- `requirements.txt` already lists `streamlit`.
- The frontend stores the cart in `st.session_state` so it persists while the app runs.

Happy coding! 🛒
