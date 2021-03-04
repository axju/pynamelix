import argparse
import logging

from check_pypi_name import check_pypi_name

from pynamelix import __version__
from pynamelix.utils import get_names

logger = logging.getLogger(__name__)


def set_logger(verbose):
    levels = [logging.WARNING, logging.INFO, logging.DEBUG]
    level = levels[min(len(levels) - 1, verbose)]
    logging.basicConfig(level=level, format="%(asctime)s %(levelname)s %(message)s")


def main(argv=None):
    parser = argparse.ArgumentParser(prog='pynamelix')
    parser.add_argument('-V', '--version', action='version', version=__version__)
    parser.add_argument('-v', '--verbose', action='count', default=0)
    parser.add_argument('-p', '--pypi', action='store_true')
    parser.add_argument('-s', '--styles',
                        choices=['multiword', 'brandable', 'language', 'wordmix',
                                 'spelling', 'dictionary', 'rhyme', 'person'],
                        default='brandable')
    parser.add_argument('-l', '--lengths', choices=['short', 'medium', 'long'], default='short')
    parser.add_argument('keywords', nargs='+')

    args = parser.parse_args(argv)
    set_logger(args.verbose)

    index = 1
    for name in get_names(args.keywords, args.styles, args.lengths):
        logger.debug('check %s', name)
        if (not args.pypi) or (args.pypi and not check_pypi_name(name, 'pypi.org')):
            print(index, name)
            index += 1


if __name__ == '__main__':
    main()
