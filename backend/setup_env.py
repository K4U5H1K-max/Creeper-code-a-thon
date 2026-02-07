"""
Setup helper script for the interview backend.
Run this to configure your .env file interactively.
"""

import os
import sys

def setup_env():
    """Interactive setup for .env file."""
    print("\n" + "="*60)
    print("  Multi-Round Interview Backend - Setup")
    print("="*60 + "\n")
    
    # Check if .env already exists
    env_file = ".env"
    if os.path.exists(env_file):
        response = input(".env file already exists. Overwrite? (y/n): ")
        if response.lower() != 'y':
            print("Setup cancelled.")
            return
    
    print("Let's configure your environment variables.\n")
    
    # Get Groq API key
    print("1. Groq API Key")
    print("   Get your API key from: https://console.groq.com/keys")
    api_key = input("   Enter your Groq API key: ").strip()
    
    if not api_key:
        print("❌ Error: API key is required!")
        sys.exit(1)
    
    # Get port
    print("\n2. Port Configuration")
    port = input("   Enter port number (default: 5000): ").strip() or "5000"
    
    # Get environment
    print("\n3. Environment")
    print("   development - enables debug mode")
    print("   production  - disables debug mode")
    env = input("   Enter environment (default: development): ").strip() or "development"
    
    # Create .env file
    env_content = f"""GROQ_API_KEY={api_key}
PORT={port}
FLASK_ENV={env}
"""
    
    with open(env_file, 'w') as f:
        f.write(env_content)
    
    print("\n" + "="*60)
    print("✅ Setup complete!")
    print("="*60)
    print(f"\n.env file created with:")
    print(f"  - Groq API Key: {api_key[:20]}...")
    print(f"  - Port: {port}")
    print(f"  - Environment: {env}")
    print("\nNext steps:")
    print("  1. Install dependencies: pip install -r requirements.txt")
    print("  2. Run the server: python app.py")
    print("  3. Test the API: python test_api.py\n")

def verify_dependencies():
    """Check if required packages are installed."""
    print("\nChecking dependencies...")
    
    required = ['flask', 'flask_cors', 'groq', 'dotenv', 'pydantic']
    missing = []
    
    for package in required:
        try:
            __import__(package)
            print(f"  ✅ {package}")
        except ImportError:
            missing.append(package)
            print(f"  ❌ {package} - not installed")
    
    if missing:
        print("\n⚠️  Missing dependencies detected!")
        print("   Run: pip install -r requirements.txt\n")
        return False
    else:
        print("\n✅ All dependencies installed!\n")
        return True

if __name__ == "__main__":
    try:
        setup_env()
        
        # Ask if user wants to verify dependencies
        response = input("Would you like to verify dependencies? (y/n): ")
        if response.lower() == 'y':
            verify_dependencies()
            
    except KeyboardInterrupt:
        print("\n\nSetup cancelled by user.")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Error during setup: {e}")
        sys.exit(1)
