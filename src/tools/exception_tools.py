from typing import Callable, TypeVar
from logging import Logger


ARGT = TypeVar("ARGT")
RT = TypeVar("RT")
def safe_call(logger: Logger, fnc: Callable[[ARGT], RT]) -> Callable[[ARGT], RT | None]:
    def _safe_call(*arg):
        try:
            return fnc(*arg)
        except Exception as ex:
            logger.error(ex, stack_info=True, exc_info=True)
        return None
    return _safe_call