from hypothesis import settings

# 100 examples by default; `uv run pytest --hypothesis-profile=thorough` runs 10,000
settings.register_profile("dev", max_examples=100)
settings.register_profile("thorough", max_examples=10_000, deadline=None)
settings.load_profile("dev")
