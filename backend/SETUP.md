# Quick Setup Guide

## Get Started in 3 Steps

### Step 1: Install Dependencies

```bash
cd backend
python -m venv venv

# Activate virtual environment
venv\Scripts\activate    # Windows
# source venv/bin/activate  # Mac/Linux

pip install -r requirements.txt
```

### Step 2: Configure API Key

1. Copy the example environment file:
```bash
copy .env.example .env    # Windows
# cp .env.example .env    # Mac/Linux
```

2. Edit `.env` and replace with your actual Groq API key:
```env
GROQ_API_KEY=gsk_your_actual_groq_api_key_here
PORT=5000
FLASK_ENV=development
```

**Get your Groq API key:** https://console.groq.com/keys

### Step 3: Run the Server

```bash
python app.py
```

You should see:
```
* Running on http://0.0.0.0:5000
* Debug mode: on
```

## Test the Backend

Open a new terminal and test:

```bash
# Windows PowerShell
curl.exe http://localhost:5000/health

# Mac/Linux
curl http://localhost:5000/health
```

Expected response:
```json
{"status": "healthy", "service": "interview-backend"}
```

## Connect Frontend

Update your frontend to point to the backend:

```javascript
const API_BASE_URL = 'http://localhost:5000/api';
```

## Common Issues

### Virtual Environment Not Activating
**Windows:**
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
venv\Scripts\activate
```

### Port Already in Use
Change port in `.env`:
```env
PORT=5001
```

### Module Not Found
```bash
pip install -r requirements.txt
```

## Next Steps

1. ✅ Backend is running
2. Start your frontend: `cd .. && npm run dev`
3. Open browser to frontend URL
4. Start an interview!

## API Endpoints

Backend provides these endpoints:

- `POST /api/start-interview` - Start new interview
- `POST /api/chat` - Send message
- `GET /api/session/{id}` - Get session status
- `GET /api/session/{id}/history` - Get conversation history

See [README.md](README.md) for full API documentation.
