import pytest


from environment import emulator

if __name__ == "__main__":
    test_device = emulator.iPhone_12_Pro

    pytest.main(["-v", "/"])
