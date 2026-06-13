# Binge N Fiesta - Backend

Minimal instructions to run the FastAPI backend locally.

Prerequisites
- Python 3.10+
- MongoDB running and reachable

Setup
1. Create a virtual environment and activate it

```bash
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\Activate.ps1 on Windows
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Copy `.env.example` to `.env` and update values

4. Run the app

```bash
uvicorn main:app --reload
```

API
- Theatre routes: `/theatre` (list/new/update/delete)
- Slots routes: `/slots` (list/new/update/delete)
- Bookings routes: `/bookings` (list/new/update/delete)

Tests
1. Run the test suite with pytest:

```bash
pytest -q
```

# BingeNFiesta WebApp Backend

## How to setup

Note:
* Python 3.12 is being used to develop. Make sure you install the same for consistency.

### 1. Installing UV

`pip install uv`

### 2. Using UV to setup the virtualenv and install packages

`uv sync`
