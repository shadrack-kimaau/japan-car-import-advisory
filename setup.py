import os

def create_project_structure():
    # Define the structure: { 'directory': ['file1', 'file2'] }
    structure = {
        "japan-car-import": [
            "requirements.txt"
        ],
        "japan-car-import/scrapers": [
            "scraper_base.py",
            "scraper_beforward.py",
            "scraper_carfromjapan.py",
            "scraper_sbtjapan.py",
            "scraper_japanesecartrade.py",
            "run_all_scrapers.py"
        ],
        "japan-car-import/database": [
            "schema.sql",
            "db_manager.py",
            "data_cleaner.py"
        ],
        "japan-car-import/ml_model": [
            "train_model.py",
            "predict.py",
            "model_eval.py"
        ],
        "japan-car-import/api": [
            "app.py"
        ],
        "japan-car-import/dashboard": [
            "index.html"
        ],
        "japan-car-import/data/raw": [],
        "japan-car-import/data/cleaned": [],
        "japan-car-import/data": [
            "sample_data.csv"
        ],
        "japan-car-import/docs": [
            "import_cost_formula.md"
        ]
    }

    print("🏗️ Creating project structure...")

    for folder, files in structure.items():
        # Create the directory if it doesn't exist
        os.makedirs(folder, exist_ok=True)
        
        # Create each file in the directory
        for file in files:
            file_path = os.path.join(folder, file)
            if not os.path.exists(file_path):
                with open(file_path, 'w') as f:
                    # Optional: Add a small header to files based on extension
                    if file.endswith('.py'):
                        f.write(f"# {file}\n\nimport os\n")
                    elif file.endswith('.md'):
                        f.write(f"# {file.replace('.md', '').replace('_', ' ').title()}\n")
                print(f"Created: {file_path}")
            else:
                print(f"Skipping (already exists): {file_path}")

    print("\n Setup complete! Happy scraping.")

if __name__ == "__main__":
    create_project_structure()