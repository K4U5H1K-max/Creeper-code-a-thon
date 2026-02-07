# Multi-Round Interview Backend

A Python Flask backend for conducting AI-powered multi-round interviews using Groq API.

## Features

✅ **Multi-Round Interview System**
- Round 1: Screening (4 questions) - 60% pass threshold
- Round 2: Technical (5 questions) - 65% pass threshold
- Round 3: Scenario/Problem-Solving (3 questions) - 70% pass threshold

✅ **Different AI Models per Round**
- Each round uses a specialized Groq model
- Ensures varied interview experience

✅ **Smart Evaluation System**
- Real-time response quality assessment
- AI feedback analysis
- Weighted scoring across rounds

✅ **Final Assessment**
- Batch assignment (A+, A, B+, B, C, D)
- Confidence score
- Hiring recommendation

## Architecture

```
backend/
├── app.py              # Main Flask application
├── models.py           # Pydantic data models
├── groq_service.py     # Groq API integration
├── evaluator.py        # Evaluation logic
├── prompts.py          # System prompts for each round
├── requirements.txt    # Python dependencies
└── .env               # Environment variables
```

## Setup Instructions

### 1. Prerequisites

- Python 3.8 or higher
- Groq API key

### 2. Installation

```bash
# Navigate to backend directory
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Configuration

Create a `.env` file in the backend directory:

```bash
# Copy the example file
cp .env.example .env
```

Edit `.env` and add your Groq API key:

```env
GROQ_API_KEY=your_actual_groq_api_key_here
PORT=5000
FLASK_ENV=development
```

### 4. Run the Server

```bash
python app.py
```

The server will start on `http://localhost:5000`

## API Endpoints

### 1. Health Check
```http
GET /health
```

**Response:**
```json
{
  "status": "healthy",
  "service": "interview-backend"
}
```

### 2. Start Interview
```http
POST /api/start-interview
Content-Type: application/json

{
  "job_role": "Software Engineer",
  "candidate_name": "John Doe"
}
```

**Response:**
```json
{
  "session_id": "uuid",
  "job_role": "Software Engineer",
  "current_round": 1,
  "round_name": "Screening Round",
  "greeting": "AI greeting and first question...",
  "total_questions": 4
}
```

### 3. Send Chat Message
```http
POST /api/chat
Content-Type: application/json

{
  "session_id": "uuid",
  "message": "Your answer here..."
}
```

**Response:**
```json
{
  "session_id": "uuid",
  "ai_message": "AI feedback and next question...",
  "current_round": 1,
  "current_question": 2,
  "total_questions": 4,
  "round_complete": false,
  "round_passed": null,
  "interview_complete": false
}
```

**When Round Completes:**
```json
{
  "session_id": "uuid",
  "ai_message": "Feedback and next round introduction...",
  "current_round": 2,
  "current_question": 0,
  "total_questions": 5,
  "round_complete": true,
  "round_passed": true,
  "round_feedback": "Good performance. Score: 72.5%..."
}
```

**When Interview Completes:**
```json
{
  "session_id": "uuid",
  "ai_message": "Final congratulations message...",
  "current_round": 3,
  "current_question": 3,
  "total_questions": 3,
  "round_complete": true,
  "round_passed": true,
  "interview_complete": true,
  "final_evaluation": {
    "overall_score": 78.5,
    "confidence_score": 82.3,
    "batch": "B+",
    "recommendation": "HIRE",
    "summary": "Candidate showed good competency...",
    "round_breakdown": {
      "1": 72.5,
      "2": 80.2,
      "3": 76.8
    }
  }
}
```

### 4. Get Session Status
```http
GET /api/session/{session_id}
```

### 5. Get Conversation History
```http
GET /api/session/{session_id}/history
```

## Interview Flow

```
┌─────────────────────┐
│  Start Interview    │
│  (job_role input)   │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│   Round 1: Screen   │
│   (4 questions)     │
│   Pass: ≥60%        │
└──────────┬──────────┘
           │
           ├─ Pass ──►┌─────────────────────┐
           │          │  Round 2: Technical │
           │          │  (5 questions)      │
           │          │  Pass: ≥65%         │
           │          └──────────┬──────────┘
           │                     │
           │                     ├─ Pass ──►┌─────────────────────┐
           │                     │          │  Round 3: Scenario  │
           │                     │          │  (3 questions)      │
           │                     │          │  Pass: ≥70%         │
           │                     │          └──────────┬──────────┘
           │                     │                     │
           │                     │                     ├─ Pass ──►┌──────────────────┐
           │                     │                     │          │ Final Evaluation │
           │                     │                     │          │ • Batch          │
           │                     │                     │          │ • Confidence     │
           │                     │                     │          │ • Recommendation │
           │                     │                     │          └──────────────────┘
           │                     │                     │
           └─ Fail ──────────────┴─ Fail ──────────────┴─ Fail ──► [Interview Ends]
```

## Evaluation System

### Question Scoring
- Length analysis (10-300 words optimal)
- Coherence check (sentence structure)
- Relevance detection (technical terms, experience indicators)
- AI feedback sentiment analysis

### Round Scoring
- Weighted average of all question scores
- Round 2 (Technical): Later questions weighted higher
- Round 1 & 3: Equal weights

### Final Evaluation
- Round 1 (Screening): 20% weight
- Round 2 (Technical): 45% weight
- Round 3 (Scenario): 35% weight

### Batch Assignment
- **A+**: 90-100% - Exceptional candidate
- **A**: 80-89% - Strong hire
- **B+**: 70-79% - Good candidate
- **B**: 60-69% - Consider for junior roles
- **C**: 50-59% - Needs development
- **D**: 0-49% - Not recommended

## System Prompts

Each round has a carefully crafted system prompt that:
- Defines the interviewer's role and expertise
- Sets question count requirements (4, 5, 3)
- Establishes evaluation criteria
- Provides question progression guidelines
- Identifies red flags to watch for

See `prompts.py` for full prompt details.

## Groq Models Used

- **Round 1**: `llama-3.3-70b-versatile` - Versatile for screening
- **Round 2**: `llama-3.3-70b-versatile` - Technical expertise
- **Round 3**: `llama-3.3-70b-versatile` - Complex scenario handling

## Development Notes

### Session Management
Currently uses in-memory storage (`active_sessions` dict). For production:
- Use Redis for session storage
- Add session expiration
- Implement session persistence

### Error Handling
- All API calls wrapped in try-except
- Groq API errors caught and returned as HTTP 500
- Session validation on every request

### CORS
Enabled for frontend integration. Configure origins in production.

## Testing

Test the backend with curl:

```bash
# Health check
curl http://localhost:5000/health

# Start interview
curl -X POST http://localhost:5000/api/start-interview \
  -H "Content-Type: application/json" \
  -d '{"job_role": "Software Engineer", "candidate_name": "Test User"}'

# Send message
curl -X POST http://localhost:5000/api/chat \
  -H "Content-Type: application/json" \
  -d '{"session_id": "your-session-id", "message": "I have 5 years of experience..."}'
```

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `GROQ_API_KEY` | Your Groq API key | Required |
| `PORT` | Server port | 5000 |
| `FLASK_ENV` | Environment mode | development |

## Troubleshooting

### "GROQ_API_KEY not found"
- Ensure `.env` file exists in backend directory
- Check that `.env` contains `GROQ_API_KEY=your_key`
- Verify the key is valid

### "Session not found"
- Session IDs expire when server restarts
- Use the session_id from `/api/start-interview` response
- Implement persistent storage for production

### Import Errors
- Ensure virtual environment is activated
- Reinstall dependencies: `pip install -r requirements.txt`

## License

MIT
