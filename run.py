from app import create_app
from pathlib import Path
from dotenv import load_dotenv


load_dotenv(Path(Path(__file__).parent, '.env'))

if __name__ == "__main__":
    
    app = create_app()

    app.run()