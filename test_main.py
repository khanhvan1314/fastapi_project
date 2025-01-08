from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

# Test 1: Kiểm tra API root trả về đúng message
def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

# Test 2: Kiểm tra phiên bản API
def test_get_version():
    response = client.get("/get_version")
    assert response.status_code == 200
    assert response.json() == {"version": "1.0.0"}

# Test 3: Kiểm tra số nguyên tố (prime) - số nguyên tố
def test_check_prime_with_prime_number():
    response = client.get("/check_prime/7")
    assert response.status_code == 200
    assert response.json() == {"result": True}

# Test 4: Kiểm tra số nguyên tố (prime) - số không phải nguyên tố
def test_check_prime_with_non_prime_number():
    response = client.get("/check_prime/10")
    assert response.status_code == 200
    assert response.json() == {"result": False}

# Test 5: Kiểm tra số nguyên tố (prime) - số âm
def test_check_prime_with_negative_number():
    response = client.get("/check_prime/-5")
    assert response.status_code == 200
    assert response.json() == {"result": False}

# Test 6: Kiểm tra API với tham số lớn
def test_large_prime_number():
    response = client.get("/check_prime/999983")
    assert response.status_code == 200
    assert response.json() == {"result": True}

# Test 7: Kiểm tra số 1 (không phải nguyên tố)
def test_prime_with_one():
    response = client.get("/check_prime/1")
    assert response.status_code == 200
    assert response.json() == {"result": False}

# Test 8: Kiểm tra số 2 (số nguyên tố nhỏ nhất)
def test_prime_with_two():
    response = client.get("/check_prime/2")
    assert response.status_code == 200
    assert response.json() == {"result": True}

# Test 9: Kiểm tra input không hợp lệ
def test_invalid_input():
    response = client.get("/check_prime/abc")
    assert response.status_code == 422  # 422: Unprocessable Entity

# Test 10: Kiểm tra đường dẫn không tồn tại
def test_invalid_path():
    response = client.get("/invalid_path")
    assert response.status_code == 404
