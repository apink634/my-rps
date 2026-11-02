"""A real browser plays and replays a round with the real game rules."""

# pytest injects fixtures by name; the test name documents the journey.
# pylint: disable=redefined-outer-name,missing-function-docstring

import pytest
from playwright.sync_api import Page, expect

import app as web

pytestmark = pytest.mark.e2e


def test_player_can_play_and_replay_a_round(page: Page, live_server, monkeypatch):
    monkeypatch.setattr(web.random, "choice", lambda _moves: "paper")
    page.goto(live_server)

    page.get_by_role("button", name="Rock", exact=True).click()
    expect(page.locator('[data-outcome="lose"]')).to_be_visible()
    expect(page.get_by_role("heading", name="Computer wins")).to_be_visible()
    expect(page.get_by_label("This round’s choices")).to_contain_text("Rock")
    expect(page.get_by_label("This round’s choices")).to_contain_text("Paper")

    page.get_by_role("button", name="Scissors", exact=True).click()
    expect(page.locator('[data-outcome="win"]')).to_be_visible()
    expect(page.get_by_role("heading", name="You win!")).to_be_visible()
    expect(page.get_by_label("This round’s choices")).to_contain_text("Scissors")
    expect(page.get_by_label("This round’s choices")).to_contain_text("Paper")
