from main import ubc

def test_ubc():

    inp = [
        [1, 2, 3],
        ["a", "b", "c", "d"],
        ["🤡"],
        ["あ", "え"]
    ]

    result = ubc((), *inp)

    assert result == [
        (1, "a", "🤡", "あ"),
        (1, "a", "🤡", "え"),
        (1, "b", "🤡", "あ"),
        (1, "b", "🤡", "え"),
        (1, "c", "🤡", "あ"),
        (1, "c", "🤡", "え"),
        (1, "d", "🤡", "あ"),
        (1, "d", "🤡", "え"),
        (2, "a", "🤡", "あ"),
        (2, "a", "🤡", "え"),
        (2, "b", "🤡", "あ"),
        (2, "b", "🤡", "え"),
        (2, "c", "🤡", "あ"),
        (2, "c", "🤡", "え"),
        (2, "d", "🤡", "あ"),
        (2, "d", "🤡", "え"),
        (3, "a", "🤡", "あ"),
        (3, "a", "🤡", "え"),
        (3, "b", "🤡", "あ"),
        (3, "b", "🤡", "え"),
        (3, "c", "🤡", "あ"),
        (3, "c", "🤡", "え"),
        (3, "d", "🤡", "あ"),
        (3, "d", "🤡", "え"),
    ]