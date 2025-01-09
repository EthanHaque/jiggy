from unittest.mock import MagicMock, patch

import pytest

from jiggy.extensions.minecraft import (
    MinecraftCog,
    minecraft_username_is_valid,
    sanitize_minecraft_username,
    send_tmux_command,
)


@pytest.mark.parametrize(
    ("username", "expected"),
    [
        ("validUser", True),
        ("12345", True),
        ("user_name", True),
        ("us", False),  # Too short
        ("a" * 17, False),  # Too long
        ("invalid!", False),  # Special characters
    ],
)
def test_minecraft_username_is_valid(username, expected):
    assert minecraft_username_is_valid(username) == expected


@pytest.mark.parametrize(
    ("username", "expected"),
    [
        ("validUser", "validUser"),
        ("user!name", "username"),  # Removes disallowed characters
        ("a" * 20, "a" * 16),  # Trims to 16 characters
        ("", ""),  # Empty username
    ],
)
def test_sanitize_minecraft_username(username, expected):
    assert sanitize_minecraft_username(username) == expected


@patch("jiggy.extensions.minecraft.subprocess.run")
def test_send_tmux_command(mock_run):
    send_tmux_command("minecraft", "whitelist add validUser")
    mock_run.assert_called_once_with(
        ["tmux", "send-keys", "-t", "minecraft:0", "whitelist add validUser", "ENTER"],
        check=True,
    )


def test_get_whitelist_embed():
    bot = MagicMock()
    cog = MinecraftCog(bot)

    with patch(
        "jiggy.extensions.minecraft.os.getenv",
        side_effect=lambda k, _=None: "1.16.5"
        if k == "SERVER_MINECRAFT_VERSION"
        else "127.0.0.1",
    ):
        embed = cog.get_whitelist_embed("validUser")

    assert embed.title == "You're Whitelisted"
    assert "validUser" in embed.description
    assert embed.description.endswith("IP: 127.0.0.1")
    assert embed.thumbnail.url == "https://mc-heads.net/avatar/validUser"
