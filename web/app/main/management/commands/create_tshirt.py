import logging
from django.core.management.base import BaseCommand, CommandError

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = """Create a decorated tshirt"""

    def add_arguments(self, parser):
        parser.add_argument('color', type=str)
        parser.add_argument('decorator', type=str)

    def handle(self, *args, **options):
        color = options["color"]
        decorator = options["decorator"]
        logger.debug("generating tshirt in color `%s` with `%s`" % (color, decorator))

        print("\nDone!\n")
