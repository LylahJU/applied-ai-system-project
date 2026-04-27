from ai_agent import generate_ai_hint

def test_ai_hint_structure():
    result = generate_ai_hint([], 1, 100)
    assert "hint" in result
    assert "confidence" in result

def test_confidence_increases():
    r1 = generate_ai_hint([], 1, 100)
    r2 = generate_ai_hint([10, 20, 30], 1, 100)
    assert r2["confidence"] >= r1["confidence"]