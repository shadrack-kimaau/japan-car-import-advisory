import os
import shutil

def update_current_workspace():
    structure = {
        ".": [
            ".gitignore",
            ".env.example",
            "requirements.txt",
            "README.md",
            "Dockerfile",
            "docker-compose.yml",
            "Makefile",
        ],
        "config": [
            "__init__.py",
            "settings.py",
        ],
        "database": [
            "__init__.py",
            "schema.sql",
            "db_manager.py",
            "data_cleaner.py",
        ],
        "scripts": [
            "generate_sample_data.py",
        ],
        "scrapers": [
            "__init__.py",
            "scraper_base.py",
            "scraper_beforward.py",
            "scraper_sbtjapan.py",
            "scraper_carfromjapan.py",
            "scraper_japanesecartrade.py",
            "scraper_aaajapan.py",
            "run_all_scrapers.py",
        ],
        "ml_model": [
            "__init__.py",
            "train_model.py",
            "predict.py",
            "model_eval.py",
        ],
        "ml_model/artifacts": [],
        "api": [
            "__init__.py",
            "import_calculator.py",
            "app.py",
            "celery_worker.py",
        ],
        "dashboard": [
            "index.html",
        ],
        "tests": [
            "__init__.py",
            "test_import_calculator.py",
            "test_data_cleaner.py",
            "test_ml_model.py",
            "test_scrapers.py",
        ],
        "docs": [
            "import_cost_formula.md",
        ],
        ".github/workflows": [
            "ci.yml",
        ],
        "data/raw": [],
        "data/cleaned": [],
        "logs": [],
    }

    print(" Cleaning up unnecessary nested folders...")
    if os.path.exists("japan-car-import"):
        shutil.rmtree("japan-car-import")
        print("  Deleted redundant 'japan-car-import' folder.")

    print("\n  Updating current workspace structure...")

    for folder, files in structure.items():
        # Create folder (unless it's the root '.')
        if folder != ".":
            os.makedirs(folder, exist_ok=True)
        
        for file in files:
            file_path = os.path.join(folder, file) if folder != "." else file
            
            if not os.path.exists(file_path):
                with open(file_path, "w") as f:
                    # Basic header for python files
                    if file.endswith(".py"):
                        f.write(f"# {file}\n")
                print(f"  Created  {file_path}")
            else:
                print(f"  Verified {file_path}")

    print("\n Success! Your workspace is now updated.")
    print("You can now delete this script file if you wish.")

if __name__ == "__main__":
    update_current_workspace()