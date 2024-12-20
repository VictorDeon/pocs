import httpx


def main(timeout: float = 5.0) -> None:
    with httpx.Client(
        base_url="https://httpbin.org",
        headers={"trace_id": "abcd1234"},
        timeout=timeout
    ) as client:
        for i in range(10):
            response = client.post('/post', json={"code": i})
            print(f"{i}) {response.status_code} {response.json()}")


if __name__ == '__main__':
    main()
