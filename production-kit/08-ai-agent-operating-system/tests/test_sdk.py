"""
Wild Story Lab OS
Module 08 - Testing
test_sdk.py
"""

from __future__ import annotations

import unittest

from runtime.sdk.client import Client


class TestSDK(unittest.TestCase):

    def test_client_registration(self):
        client = Client()
        service = object()

        client.connect("demo", service)

        self.assertIn("demo", client.available())
        self.assertIs(client.service("demo"), service)


if __name__ == "__main__":
    unittest.main()
