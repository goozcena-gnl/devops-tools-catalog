from scripts.check_links import classify_status, repository_coordinates


def test_link_status_classification_is_non_binary() -> None:
    assert classify_status(204, []) == "valid"
    assert classify_status(200, [301]) == "permanent-redirect"
    assert classify_status(200, [302]) == "valid-redirect"
    assert classify_status(401, []) == "authentication-required"
    assert classify_status(403, []) == "restricted-or-bot-blocked"
    assert classify_status(429, []) == "rate-limited"
    assert classify_status(404, []) == "manual-verification-required"


def test_github_repository_coordinates_ignore_organization_pages() -> None:
    assert repository_coordinates("https://github.com/org/repository") == (
        "org",
        "repository",
    )
    assert repository_coordinates("https://github.com/org") is None
    assert repository_coordinates("https://github.com/features/actions") is None
