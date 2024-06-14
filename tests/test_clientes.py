import pytest

@pytest.mark.asyncio
async def test_post_cliente(async_client):
    response = await async_client.post("/api/v1/clientes/", json={"nome": "Test Cliente", "email": "test@cliente.com", "telefone": "123456789"})
    assert response.status_code == 201
    assert response.json()["nome"] == "Test Cliente"

@pytest.mark.asyncio
async def test_get_clientes(async_client):
    response = await async_client.get("/api/v1/clientes/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

@pytest.mark.asyncio
async def test_get_cliente(async_client):
    post_response = await async_client.post("/api/v1/clientes/", json={"nome": "Test Cliente", "email": "test@cliente.com", "telefone": "123456789"})
    cliente_id = post_response.json()["id"]
    get_response = await async_client.get(f"/api/v1/clientes/{cliente_id}")
    assert get_response.status_code == 200
    assert get_response.json()["nome"] == "Test Cliente"
