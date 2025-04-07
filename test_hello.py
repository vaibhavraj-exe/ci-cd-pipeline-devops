# test_hello.py
import hello

def test_main(capsys):
    hello.main()
    captured = capsys.readouterr()
    assert "Hello, World!" in captured.out
