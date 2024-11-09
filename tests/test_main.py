import os
import pytest
import random
import datetime
from PIL import Image
from pathlib import Path
from app.user import User
from _pytest.monkeypatch import MonkeyPatch


# -----------------------------------------------------------------------------
@pytest.fixture
def user() -> User:
    return User(80386, "Zoubida", 42)


# -----------------------------------------------------------------------------
def test_user_greet(user: User) -> None:
    assert user.greet() == "Hello, my name is Zoubida and I am 42 years old."


# -----------------------------------------------------------------------------
def test_password_default(monkeypatch: MonkeyPatch) -> None:
    # Simulate the lack of env variable PASSWORD
    monkeypatch.delenv("PASSWORD", raising=False)
    default_password = "CPE1704TKS"
    my_password = os.getenv("PASSWORD", default_password)
    assert my_password == default_password


# -----------------------------------------------------------------------------
def test_image_creation(monkeypatch: MonkeyPatch, tmp_path: Path) -> None:

    monkeypatch.chdir(tmp_path)

    # create the "img" directory and the png
    img_path = tmp_path / "img"
    img_path.mkdir(parents=True, exist_ok=True)

    color = random.choice(["blue", "red", "orange", "green"])
    image = Image.new("RGB", (100, 100), color=color)
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    image_file = img_path / f"{timestamp}_dummy_artifact.png"
    image.save(image_file)

    # Check the .png and its content
    assert image_file.exists()
    with Image.open(image_file) as img:
        assert img.size == (100, 100)
        assert img.mode == "RGB"
