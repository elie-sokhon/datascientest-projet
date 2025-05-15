def test_login_logout_list_users(client):
    # 1. Test login
    response = client.post("/login", json={"pseudonym": "testuser"})
    assert response.status_code == 200
    data = response.get_json()
    assert data["pseudonym"] == "testuser"
    assert data["is_connected"] is True

    # 2. Test duplicate login
    response = client.post("/login", json={"pseudonym": "testuser"})
    assert response.status_code == 400

    # 3. Test list users
    response = client.get("/users")
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) == 1
    assert data[0]["pseudonym"] == "testuser"

    # 4. Test logout
    response = client.post("/logout", json={"pseudonym": "testuser"})
    assert response.status_code == 200

    # 5. Test logout again → should fail
    response = client.post("/logout", json={"pseudonym": "testuser"})
    assert response.status_code == 400
