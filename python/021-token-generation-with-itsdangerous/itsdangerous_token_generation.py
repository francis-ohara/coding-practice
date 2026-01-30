from itsdangerous import URLSafeTimedSerializer

secret_key = "my-app-secret-key"

serializer = URLSafeTimedSerializer(secret_key=secret_key)
token = serializer.dumps("francisohara", salt="test-salt-1")

# token = Base64Encoded 'francisohara' + . + Signature (hash(data, secret_key, salt))
print(f"Generated token: {token}")  

original_string = serializer.loads(token, salt="test-salt-1")
print(f"Original string: {original_string}")