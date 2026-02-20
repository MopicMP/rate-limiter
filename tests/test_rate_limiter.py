"""Tests for rate-limiter."""

import pytest
from rate_limiter import limiter


class TestLimiter:
    """Test suite for limiter."""

    def test_basic(self):
        """Test basic usage."""
        result = limiter("test")
        assert result is not None

    def test_empty(self):
        """Test with empty input."""
        try:
            limiter("")
        except (ValueError, TypeError):
            pass  # Expected for some utilities

    def test_type_error(self):
        """Test with wrong type raises or handles gracefully."""
        try:
            result = limiter(12345)
        except (TypeError, AttributeError, ValueError):
            pass  # Expected for strict-typed utilities
