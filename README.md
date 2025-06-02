# resolver

## Backend Python Environment Setup

After cloning this repository, you need to set up a Python virtual environment for the backend. The `venv` directory is not tracked in git and must be created on each machine.

### Steps to set up the backend environment:

1. **Navigate to the backend directory:**
   ```bash
   cd backend
   ```
2. **Create a virtual environment:**
   ```bash
   python3 -m venv venv
   ```
3. **Activate the virtual environment:**
   ```bash
   source venv/bin/activate
   ```
4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

> **Note:**
> - Always activate the virtual environment before running backend Python scripts.
> - If you update dependencies, remember to update `requirements.txt` and commit those changes.
> - The `venv` directory should be listed in `.gitignore` and never committed to the repository.

---

## Frontend (React/Next.js) Environment Setup

After cloning this repository, you need to install frontend dependencies for the React/Next.js app. The `node_modules` directory is not tracked in git and must be created on each machine.

### Steps to set up the frontend environment:

1. **Navigate to the frontend directory:**
   ```bash
   cd frontend
   ```
2. **Install dependencies:**
   ```bash
   npm install
   ```
   or if you use yarn:
   ```bash
   yarn install
   ```
3. **Run the development server:**
   ```bash
   npm run dev
   ```
   or with yarn:
   ```bash
   yarn dev
   ```

> **Note:**
> - The `node_modules` directory should be listed in `.gitignore` and never committed to the repository.
> - If you add or update dependencies, remember to update `package.json`/`yarn.lock` and commit those changes.

