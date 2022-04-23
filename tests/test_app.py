import hello_world


def test_get_root() -> None:
    assert hello_world.get_root() == {"message": "Hello, World!"}
