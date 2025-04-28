"""
This file contains tests for running the Phpactor Language Server.
"""

import pytest
from multilspy import LanguageServer
from multilspy.multilspy_config import Language
from tests.test_utils import create_test_context
from pathlib import PurePath

pytest_plugins = ("pytest_asyncio",)


@pytest.mark.asyncio
async def test_multilspy_php():
    """
    Test the working of multilspy with a PHP repository.
    """
    code_language = Language.PHP
    params = {
        "code_language": code_language,
        "repo_url": "https://github.com/phpactor/phpactor/",
        "repo_commit": "bfc8a7040bed145a35fb9afee0ddd645297b9ed9",
    }
    print("Creating test context...")
    with create_test_context(params) as context:
        print("Creating context...")
        lsp = LanguageServer.create(
            context.config, context.logger, context.source_directory
        )
        print("Starting server...")

        async with lsp.start_server():
            print("Starting test...")
            result = await lsp.request_document_symbols(
                str(
                    PurePath(
                        "lib/Extension/LanguageServerIndexer/Handler/WorkspaceSymbolHandler.php"
                    )
                ),
            )

            assert isinstance(result, tuple)
            assert len(result) == 2

            symbols = result[0]
            for symbol in symbols:
                del symbol["kind"]

            assert symbols == [
                {
                    "name": "WorkspaceSymbolHandler",
                    "range": {
                        "start": {"line": 12, "character": 0},
                        "end": {"line": 43, "character": 1},
                    },
                    "selectionRange": {
                        "start": {"line": 12, "character": 6},
                        "end": {"line": 12, "character": 28},
                    },
                },
                {
                    "name": "provider",
                    "range": {
                        "start": {"line": 14, "character": 36},
                        "end": {"line": 14, "character": 45},
                    },
                    "selectionRange": {
                        "start": {"line": 14, "character": 36},
                        "end": {"line": 14, "character": 45},
                    },
                },
                {
                    "name": "__construct",
                    "range": {
                        "start": {"line": 16, "character": 4},
                        "end": {"line": 19, "character": 5},
                    },
                    "selectionRange": {
                        "start": {"line": 16, "character": 20},
                        "end": {"line": 16, "character": 31},
                    },
                },
                {
                    "name": "methods",
                    "range": {
                        "start": {"line": 21, "character": 4},
                        "end": {"line": 26, "character": 5},
                    },
                    "selectionRange": {
                        "start": {"line": 21, "character": 20},
                        "end": {"line": 21, "character": 27},
                    },
                },
                {
                    "name": "symbol",
                    "range": {
                        "start": {"line": 31, "character": 4},
                        "end": {"line": 37, "character": 5},
                    },
                    "selectionRange": {
                        "start": {"line": 31, "character": 20},
                        "end": {"line": 31, "character": 26},
                    },
                },
                {
                    "name": "registerCapabiltiies",
                    "range": {
                        "start": {"line": 39, "character": 4},
                        "end": {"line": 42, "character": 5},
                    },
                    "selectionRange": {
                        "start": {"line": 39, "character": 20},
                        "end": {"line": 39, "character": 40},
                    },
                },
            ]