import os
import json

def test_answers_file_exists():
    assert os.path.exists("answers.json"), "answers.json does not exist!"

def test_answers_not_empty():
    with open("answers.json", "r") as f:
        answers = json.load(f)
    assert len(answers) > 0, "answers.json is empty!"

def test_answers_structure():
    with open("answers.json", "r") as f:
        answers = json.load(f)
    for i, ans in enumerate(answers):
        assert "question" in ans, f"Answer {i} missing 'question'"
        assert "answer" in ans, f"Answer {i} missing 'answer'"
        assert "sources" in ans, f" Answer {i} missing 'sources'"
        assert isinstance(ans["sources"], list), f" Answer {i} 'sources' is not a list"

if __name__ == "__main__":

    test_answers_file_exists()
    test_answers_not_empty()
    test_answers_structure()
    print("All tests passed")
