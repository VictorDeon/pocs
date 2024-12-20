import httpx


def main(timeout: float = 5.0) -> None:
    for i in range(10):
        response = httpx.post(
            'https://httpbin.org/post',
            headers={"trace_id": "abcd1234"},
            timeout=timeout,
            json={"code": i}
        )
        print(f"{i}) {response.status_code} {response.json()}")


if __name__ == '__main__':
    main()
