def get_user_data(user_id):
    # Example of DynamoDB logic
    # In practice, you'd fetch from DynamoDB, but here's a mock
    if user_id == "valid_user":
        return {"user_id": user_id, "preferences": {"work_from_home": {"brightness": 100}}}
    return None