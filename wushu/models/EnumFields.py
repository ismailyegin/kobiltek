import enum


class EnumFields(enum.Enum):
    class LEVELTYPE(enum.Enum):
        VISA = 1
        GRADE = 2
        BELT = 3

    class BRANCH(enum.Enum):
        TAOLU = 1
        SANDA = 2
        WUSHU = 3

    class COMPSTATUS(enum.Enum):
        PREREGISTRATIONOPEN = 1
        PREREGISTRATIONCLOSED = 2
        COMPLETED = 3

    class COMPTYPE(enum.Enum):
        NATIONAL = 1
        INTERNATIONAL = 2
