from app.services import ai

# Test AI service directly
try:
    print("Testing AI service...")
    response = ai.get_chat_response([{"role": "user", "content": "Hello"}])
    print(f"✅ AI Response: {response}")
except Exception as e:
    print(f"❌ AI Error: {e}")
    import traceback
    traceback.print_exc()
