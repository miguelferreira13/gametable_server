import os

def main():
    port = os.getenv('PORT', 8080)
    os.system(f'python -m uvicorn app.main:app  --reload --host 0.0.0.0 --port {port}')

if __name__ == "__main__":
    main()