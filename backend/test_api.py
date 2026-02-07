"""
Test script for the interview backend API.
Run this to verify the backend is working correctly.
"""

import requests
import json
import time

BASE_URL = "http://localhost:5000"

def test_health():
    """Test health check endpoint."""
    print("\n" + "="*60)
    print("Testing Health Check...")
    print("="*60)
    
    response = requests.get(f"{BASE_URL}/health")
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"
    print("✅ Health check passed!")

def test_start_interview():
    """Test starting a new interview."""
    print("\n" + "="*60)
    print("Testing Start Interview...")
    print("="*60)
    
    data = {
        "job_role": "Software Engineer",
        "candidate_name": "Test User"
    }
    
    response = requests.post(f"{BASE_URL}/api/start-interview", json=data)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    
    assert response.status_code == 200
    result = response.json()
    assert "session_id" in result
    assert result["job_role"] == "Software Engineer"
    assert result["current_round"] == 1
    
    print("✅ Start interview passed!")
    return result["session_id"]

def test_chat(session_id):
    """Test sending chat messages."""
    print("\n" + "="*60)
    print("Testing Chat Messages...")
    print("="*60)
    
    messages = [
        "I have 5 years of experience in software development, working primarily with Python and JavaScript.",
        "I'm motivated by solving complex problems and building scalable systems that impact users.",
        "I understand that a Software Engineer designs, develops, and maintains software applications using best practices.",
        "I'm available to start immediately and expect a competitive salary and growth opportunities."
    ]
    
    for i, message in enumerate(messages, 1):
        print(f"\n--- Message {i} ---")
        print(f"Sending: {message[:50]}...")
        
        data = {
            "session_id": session_id,
            "message": message
        }
        
        response = requests.post(f"{BASE_URL}/api/chat", json=data)
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200:
            result = response.json()
            print(f"Current Round: {result['current_round']}")
            print(f"Current Question: {result['current_question']}/{result['total_questions']}")
            print(f"Round Complete: {result['round_complete']}")
            print(f"\nAI Response: {result['ai_message'][:200]}...")
            
            if result.get('round_complete'):
                print(f"\n🎉 Round {result['current_round']} Complete!")
                if result.get('round_passed'):
                    print(f"✅ Passed!")
                else:
                    print(f"❌ Failed")
                if result.get('round_feedback'):
                    print(f"Feedback: {result['round_feedback']}")
            
            if result.get('interview_complete'):
                print("\n" + "="*60)
                print("Interview Complete!")
                print("="*60)
                if result.get('final_evaluation'):
                    eval = result['final_evaluation']
                    print(f"\nFinal Evaluation:")
                    print(f"  Overall Score: {eval['overall_score']}%")
                    print(f"  Confidence: {eval['confidence_score']}%")
                    print(f"  Batch: {eval['batch']}")
                    print(f"  Recommendation: {eval['recommendation']}")
                    print(f"\n  {eval['summary']}")
                return True
        else:
            print(f"Error: {response.json()}")
        
        time.sleep(1)  # Rate limiting
    
    print("✅ Chat test passed!")
    return False

def test_get_session(session_id):
    """Test getting session status."""
    print("\n" + "="*60)
    print("Testing Get Session...")
    print("="*60)
    
    response = requests.get(f"{BASE_URL}/api/session/{session_id}")
    print(f"Status Code: {response.status_code}")
    
    if response.status_code == 200:
        result = response.json()
        print(f"Session ID: {result['session_id']}")
        print(f"Job Role: {result['job_role']}")
        print(f"Current Round: {result['current_round']}")
        print(f"Status: {result['status']}")
        print("✅ Get session passed!")
    else:
        print(f"Error: {response.json()}")

def test_get_history(session_id):
    """Test getting conversation history."""
    print("\n" + "="*60)
    print("Testing Get History...")
    print("="*60)
    
    response = requests.get(f"{BASE_URL}/api/session/{session_id}/history")
    print(f"Status Code: {response.status_code}")
    
    if response.status_code == 200:
        result = response.json()
        print(f"Total Messages: {len(result['history'])}")
        print("✅ Get history passed!")
    else:
        print(f"Error: {response.json()}")

def run_all_tests():
    """Run all tests."""
    print("\n" + "="*60)
    print("🚀 Starting Backend API Tests")
    print("="*60)
    
    try:
        # Test 1: Health check
        test_health()
        
        # Test 2: Start interview
        session_id = test_start_interview()
        
        # Test 3: Chat messages
        interview_complete = test_chat(session_id)
        
        # Test 4: Get session
        test_get_session(session_id)
        
        # Test 5: Get history
        test_get_history(session_id)
        
        print("\n" + "="*60)
        print("✅ All Tests Passed!")
        print("="*60)
        
    except requests.exceptions.ConnectionError:
        print("\n❌ Error: Could not connect to backend.")
        print("Make sure the backend is running on http://localhost:5000")
        print("Run: python app.py")
        
    except AssertionError as e:
        print(f"\n❌ Test Failed: {e}")
        
    except Exception as e:
        print(f"\n❌ Unexpected Error: {e}")

if __name__ == "__main__":
    run_all_tests()
