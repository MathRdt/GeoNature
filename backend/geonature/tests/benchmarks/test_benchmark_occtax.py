import logging
import pytest
from geonature.tests.benchmarks import *
from geonature.tests.test_pr_occhab import stations

from .benchmark_generator import BenchmarkTest, CLater

from .utils import activate_profiling_sql

logging.basicConfig()
logger = logging.getLogger("logger-name")
logger.setLevel(logging.DEBUG)

from .utils import CLIENT_GET, CLIENT_POST


@pytest.mark.benchmark(group="occtax")
@pytest.mark.usefixtures("client_class", "temporary_transaction", "activate_profiling_sql")
class TestBenchmarkOcctax:

    test_list_releves_restricted = BenchmarkTest(
        CLIENT_GET,
        [CLater("""url_for("pr_occtax.getReleves")""")],
        dict(user_profile="user_restricted_occhab", fixtures=[]),
    )()
    test_list_releves_unrestricted = BenchmarkTest(
        CLIENT_GET,
        [CLater("""url_for("pr_occtax.getReleves")""")],
        dict(user_profile="admin_user", fixtures=[]),
    )()
