import asyncio
import sys
import os

# Add the app directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'app'))

from app.services.database import DatabaseService
from app.utils.auth import create_access_token, verify_token
from app.models.user import User

async def test_session_retrieval():
    """Test that session retrieval from database works correctly."""
    print("Testing session retrieval fix...")
    
    # Initialize database service
    db_service = DatabaseService()
    
    try:
        # Test database connection
        health = await db_service.health_check()
        print(f"Database health check: {'✓ PASS' if health else '✗ FAIL'}")
        
        if not health:
            print("Database is not available. Please ensure the database is running.")
            return False
        
        # Create a test user
        test_email = "test_session@example.com"
        test_password = "TestPassword123!"
        
        # Check if user already exists, if so delete it
        existing_user = await db_service.get_user_by_email(test_email)
        if existing_user:
            print(f"Cleaning up existing test user...")
            # Note: We don't have a delete_user method, so we'll just use the existing user
            user = existing_user
        else:
            print("Creating test user...")
            user = await db_service.create_user(email=test_email, password=User.hash_password(test_password))
        
        print(f"Test user created/found: ID={user.id}, Email={user.email}")
        
        # Create a test session
        print("Creating test session...")
        import uuid
        session_id = str(uuid.uuid4())
        session = await db_service.create_session(session_id, user.id)
        print(f"Test session created: ID={session.id}, User ID={session.user_id}")
        
        # Create a token with the session ID
        print("Creating access token...")
        token = create_access_token(session_id)
        print(f"Token created: {token.access_token[:20]}...")
        
        # Verify the token returns the correct session ID
        print("Verifying token...")
        verified_session_id = verify_token(token.access_token)
        print(f"Token verification result: {verified_session_id}")
        
        if verified_session_id != session_id:
            print(f"✗ FAIL: Token verification returned {verified_session_id}, expected {session_id}")
            return False
        
        print("✓ PASS: Token verification successful")
        
        # Test session retrieval from database
        print("Testing session retrieval from database...")
        retrieved_session = await db_service.get_session(session_id)
        
        if retrieved_session is None:
            print("✗ FAIL: Session not found in database")
            return False
        
        print(f"✓ PASS: Session retrieved from database: ID={retrieved_session.id}, User ID={retrieved_session.user_id}")
        
        # Test that the session belongs to the correct user
        if retrieved_session.user_id != user.id:
            print(f"✗ FAIL: Session user_id {retrieved_session.user_id} doesn't match expected user_id {user.id}")
            return False
        
        print("✓ PASS: Session belongs to correct user")
        
        # Clean up - delete the test session
        print("Cleaning up test session...")
        deleted = await db_service.delete_session(session_id)
        if deleted:
            print("✓ PASS: Test session deleted successfully")
        else:
            print("✗ FAIL: Failed to delete test session")
        
        print("\n🎉 All tests passed! Session retrieval from database is working correctly.")
        return True
        
    except Exception as e:
        print(f"✗ FAIL: Test failed with error: {str(e)}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    result = asyncio.run(test_session_retrieval())
    sys.exit(0 if result else 1)